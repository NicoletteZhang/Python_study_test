#-*- coding:utf-8 -*-
#
from flask import Flask,request
# from WXBizMsgCrypt import WXBizMsgCrypt
from WXBizMsgCrypt_py3 import WXBizMsgCrypt
import xml.etree.cElementTree as ET
import sys

app = Flask(__name__)
app.route('/',methods=['GET','POST'])

def index():
    #以下为开发者在服务器配置中填写的相应信息
    sToken = 'weixin'#根据自己设置的信息填写
    sEncodingAESKey = 'E7zXIxxxxxxxxxxxxxxx'#根据自己设置的信息填写
    sCorpID = 'wxxxxxxxxx'#根据自己设置的信息填写
    wxcpt=WXBizMsgCrypt(sToken,sEncodingAESKey,sCorpID)
    #获取url验证时微信发送的相关参数
    #get方法
    sVerifyMsgSig=request.args.get("signature")
    sVerifyTimeStamp=request.args.get('timestamp')
    sVerifyNonce=request.args.get('nonce')
    sVerifyEchoStr=request.args.get('echostr')
    print(request.args)
    print("sVerifyMsgSig",sVerifyMsgSig)
    print("sVerifyTimeStamp",sVerifyTimeStamp)
    print("sVerifyNonce",sVerifyNonce )
    print("sVerifyEchoStr",sVerifyEchoStr )
    #验证url
    if request.method == 'GET':
        return sVerifyEchoStr
    #接收客户端消息
    if request.method == 'POST':
        sReqData = request.data
        print(request.args)
        print("request.data:",request.data)
        #解析接收的内容，XML格式
        xml_tree = ET.fromstring(sReqData)
        content = xml_tree.find("Content").text
        ToUserName=xml_tree.find("ToUserName").text
        FromUserName=xml_tree.find("FromUserName").text
        CreateTime=xml_tree.find("CreateTime").text
        MsgType=xml_tree.find("MsgType").text
        MsgId=xml_tree.find("MsgId").text
    #被动响应消息，将微信端发送的消息返回给微信端
    response='''<xml><ToUserName><![CDATA['''+FromUserName+''']]></ToUserName>\n
            <FromUserName><![CDATA['''+ToUserName+''']]></FromUserName>\n
            <CreateTime>'''+CreateTime+'''</CreateTime>\n
            <MsgType><![CDATA['''+MsgType+''']]></MsgType>\n
            <Content><![CDATA['''+content+''']]></Content>\n
            <MsgId>'''+MsgId+'''</MsgId>\n</xml>'''
    return response

if __name__ == '__main__':
    app.run(host='128.24.6.122', port=80, debug=False)#根据自己设置的信息填写