from chatgpt.openai_request import OpenAI_Request,config_dict
from tools.cfg_wrapper import load_config
from tools.context import ContextHandler
from tools.tokennizer import Tokennizer
from ifly.record_voice import record
from ifly.audio_play import play
from ifly.ifly_t2a import text_to_audio
from ifly.ifly_a2t import audio_to_text,clear_text

file = 'user_voice.wav'           # 语音录制，识别文件
synth_file = "answer_audio.mp3"    # 语音合成文件


def communicate_with_gpt(keys,model_name,request_address,context_handler,tokenizer,log_time=False,context_max=3200):

    requestor = OpenAI_Request(keys, model_name,request_address)
    
    while True:
        record(file)                # 录制音频 
        txt_str = audio_to_text(file)               # 语音识别
        print(txt_str)                              # 打印识别结果
        input_s = txt_str                           # 输入语句

        if input_s == "clear":
            context_handler.clear()
            print('start a new session')
            continue
        else:
            inputs_length = tokenizer.num_tokens_from_string(input_s)
            context_handler.append_cur_to_context(input_s,inputs_length)
        res = requestor.post_request(context_handler.context)
        if res.status_code == 200:
            response = res.json()['choices'][0]['message']['content']
            # cut \n for show
            response = response.lstrip("\n")
            completion_length = res.json()['usage']['completion_tokens']
            total_length = res.json()['usage']['total_tokens']
            print(f"\nchatgpt : {response}")
            ret = text_to_audio(synth_file,response)    # 语音合成
            if ret == 1:
                play(synth_file)                        # 播放合成结果
                clear_text()                            # 清空识别结果
            context_handler.append_cur_to_context(response,completion_length,tag=1)
            if total_length > context_max:
                context_handler.cut_context(total_length,tokenizer)




if __name__ == '__main__':

    # 加载配置
    config = load_config(config_dict)
    keys = config.Acess_config.authorization
    model_name = config.Model_config.model_name
    request_address = config.Model_config.request_address

    # load context
    context_manage_config = config.Context_manage_config
    del_config = context_manage_config.del_config
    max_context = context_manage_config.max_context
    context = ContextHandler(max_context=max_context,context_del_config=del_config)

    # load tokenizer
    tokenizer = Tokennizer(model_name)

    # for test
    communicate_with_gpt(keys,model_name,request_address,context,tokenizer)