# CHAT-GPT语音对话程序

## 1.安装

确保你所处的操作系统已安装ffmpeg、python版本大于或等于3.8

[ffmpeg安装教程](https://zhuanlan.zhihu.com/p/623994780)

然后cd到工程目录下

安装所需依赖：

```bash
pip install -r requirements.txt --ignore-installed
```

## 2.配置科大讯飞API与CHAT-GPT的API

a.去[科大讯飞开放平台官网](https://www.xfyun.cn/)主策并申请语音识别的API并免费领取在线文字转语音和语音转文字次数后,获取到**APP_ID、API_KEY**与**SECRET_KEY**并将其依次填写到**api.txt的前三行**

b.去[chatgpt_api](https://platform.openai.com/account/api-keys)生成api并将其填写到api.txt的最后一行

例如：

```bash
APP_ID:123456789
API_KEY:xxxxxxxxxxxxxxxxxxx
SECRET_KEY:xxxxxxxxxxxxxxx
GPT_API:sk-xxxxxx
```

## 3.开始使用

打开终端输入如下指令即可开始使用

```
python main.py
```

根据提示可以录入声音，chatgpt将会作出相应的回应并以语音形式播放。
