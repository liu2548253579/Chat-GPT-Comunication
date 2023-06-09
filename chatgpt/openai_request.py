import requests
import json

class OpenAI_Request(object):

    def __init__(self,key,model_name,request_address):
        super().__init__()
        self.headers = {"Authorization":f"Bearer {key}","Content-Type": "application/json"}
        self.model__name = model_name
        self.request_address = request_address

    def post_request(self,message):

        data = {
            "model": self.model__name,
            "messages":  message
        }
        data = json.dumps(data)

        response = requests.post(self.request_address, headers=self.headers, data=data)

        return response


if __name__ == '__main__':
    keys = "OpenAI API keys"
    model_name = "gpt-3.5-turbo"
    request_address = "https://api.openai.com/v1/chat/completions"
    requestor = OpenAI_Request(keys,model_name,request_address)

    while 1:
        input_s = input('user input: ')
        res = requestor.post_request(input_s)

        response = res.json()['choices'][0]['message']['content']

        if  response:
            requestor.context_handler.append_cur_to_context(response,tag=1)

        print(f"chatGPT: {response}")



def get_chatgpt_api ():
    with open('api.txt', 'r') as f:
        lines = f.readlines()
    return lines[3].split(':')[1].strip()

config_dict = dict(

    Acess_config = dict(
    # authorization = "Your OpenAI API keys",        
        authorization = get_chatgpt_api (),
    ),

    Model_config = dict(
        model_name = "gpt-3.5-turbo",
        request_address = "https://api.openai.com/v1/chat/completions",
    ),

    Context_manage_config = dict(
        max_context = 3200,
        del_config = dict(
        distance_weights=0.05,
        length_weights=0.4,
        role_weights=1,
        sys_role_ratio=3,
        del_ratio = 0.4,
        max_keep_turns=30)
    )
)

