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

 # class XMLParse(object):
 #     """提供提取消息格式中的密文及生成回复消息格式的接口"""
 #     # xml消息模板
 #     AES_TEXT_RESPONSE_TEMPLATE = """<xml>
 #        <Encrypt><![CDATA[%(msg_encrypt)s]]></Encrypt>
 #        <MsgSignature><![CDATA[%(msg_signaturet)s]]></MsgSignature>
 #        <TimeStamp>%(timestamp)s</TimeStamp>
 #        <Nonce><![CDATA[%(nonce)s]]></Nonce>
 #        </xml>"""
