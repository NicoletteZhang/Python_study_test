    #!/usr/bin/env python
# -*- encoding:utf-8 -*-

"""
    python3对公众平台发送给公众账号的消息加解密代码.支持中文.
"""
# ------------------------------------------------------------------------

import base64
import string
import random
import hashlib
import time
import struct

import binascii
from Crypto.Cipher import AES
import xml.etree.cElementTree as ET
import socket

import ierror

""" AES加解密用 pycrypto """


class FormatException(Exception):
    pass


def throw_exception(message, exception_class=FormatException):
    """my define raise exception function"""
    raise exception_class(message)


class SHA1:
    """计算公众平台的消息签名接口"""

    def getSHA1(self, token, timestamp, nonce, encrypt):
        """用SHA1算法生成安全签名
        @param token:  票据
        @param timestamp: 时间戳
        @param encrypt: 密文
        @param nonce: 随机字符串
        @return: 安全签名
        """
        try:
            token = token.decode()
            sortlist = [token, timestamp, nonce, encrypt]
            sortlist.sort()
            sha = hashlib.sha1()
            sha.update("".join(sortlist).encode("utf8"))
            return ierror.WXBizMsgCrypt_OK, sha.hexdigest()
        except Exception as e:
            print(e)
            return ierror.WXBizMsgCrypt_ComputeSignature_Error, None

    def extract(self, xmltext):
        """提取出xml数据包中的加密消息
        @param xmltext: 待提取的xml字符串
        @return: 提取出的加密消息字符串
        """
        try:
            xml_tree = ET.fromstring(xmltext)
            encrypt = xml_tree.find("Encrypt")
            touser_name = xml_tree.find("ToUserName")
            return ierror.WXBizMsgCrypt_OK, encrypt.text, touser_name.text
        except Exception as e:
            print(e)
            return ierror.WXBizMsgCrypt_ParseXml_Error, None, None

    def generate(self, encrypt, signature, timestamp, nonce):
        """生成xml消息
        @param encrypt: 加密后的消息密文
        @param signature: 安全签名
        @param timestamp: 时间戳
        @param nonce: 随机字符串
        @return: 生成的xml字符串
        """
        resp_dict = {
            'msg_encrypt': encrypt,
            'msg_signaturet': signature,
            'timestamp': timestamp,
            'nonce': nonce,
        }
        resp_xml = self.AES_TEXT_RESPONSE_TEMPLATE % resp_dict
        return resp_xml

    class PKCS7Encoder(object):
        """提供基于PKCS7算法的加解密接口"""

        block_size = 32

        def encode(self, text):
            """ 对需要加密的明文进行填充补位
            @param text: 需要进行填充补位操作的明文
            @return: 补齐明文字符串
            """
            text_length = len(text)
            # 计算需要填充的位数
            amount_to_pad = self.block_size - (text_length % self.block_size)
            if amount_to_pad == 0:
                amount_to_pad = self.block_size
            # 获得补位所用的字符
            pad = chr(amount_to_pad).encode()
            return text + pad * amount_to_pad

        def decode(self, decrypted):
            """删除解密后明文的补位字符
            @param decrypted: 解密后的明文
            @return: 删除补位字符后的明文
            """
            pad = ord(decrypted[-1])
            if pad < 1 or pad > 32:
                pad = 0
            return decrypted[:-pad]

    class Prpcrypt(object):
        """提供接收和推送给公众平台消息的加解密接口"""

        def __init__(self, key):
            # self.key = base64.b64decode(key+"=")
            self.key = key
            # 设置加解密模式为AES的CBC模式
            self.mode = AES.MODE_CBC

        def encrypt(self, text, appid):
            """对明文进行加密
            @param text: 需要加密的明文
            @return: 加密得到的字符串
            """
            # 16位随机字符串添加到明文开头
            len_str = struct.pack("I", socket.htonl(len(text.encode())))
            # text = self.get_random_str() + binascii.b2a_hex(len_str).decode() + text + appid
            text = self.get_random_str() + len_str + text.encode() + appid
            # 使用自定义的填充方式对明文进行补位填充
            pkcs7 = PKCS7Encoder()
            text = pkcs7.encode(text)
            # 加密
            cryptor = AES.new(self.key, self.mode, self.key[:16])
            try:
                ciphertext = cryptor.encrypt(text)
                # 使用BASE64对加密后的字符串进行编码
                return ierror.WXBizMsgCrypt_OK, base64.b64encode(ciphertext).decode('utf8')
            except Exception as e:
                return ierror.WXBizMsgCrypt_EncryptAES_Error, None

        def decrypt(self, text, appid):
            """对解密后的明文进行补位删除
            @param text: 密文
            @return: 删除填充补位后的明文
            """
            try:
                cryptor = AES.new(self.key, self.mode, self.key[:16])
                # 使用BASE64对密文进行解码，然后AES-CBC解密
                plain_text = cryptor.decrypt(base64.b64decode(text))
            except Exception as e:
                print(e)
                return ierror.WXBizMsgCrypt_DecryptAES_Error, None
            try:
                # pad = ord(plain_text[-1])
                pad = plain_text[-1]
                # 去掉补位字符串
                # pkcs7 = PKCS7Encoder()
                # plain_text = pkcs7.encode(plain_text)
                # 去除16位随机字符串
                content = plain_text[16:-pad]
                xml_len = socket.ntohl(struct.unpack("I", content[: 4])[0])
                xml_content = content[4: xml_len + 4]
                from_appid = content[xml_len + 4:]
            except Exception as e:
                return ierror.WXBizMsgCrypt_IllegalBuffer, None
            if from_appid != appid:
                return ierror.WXBizMsgCrypt_ValidateAppid_Error, None
            return 0, xml_content.decode()
