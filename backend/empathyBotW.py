from transformers import pipeline
from transformers import (
    AutoTokenizer,
    AutoModel,
    AutoModelForSeq2SeqLM,
    AutoModelForCausalLM
)
import pickle

class EmpathyResponse:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("microsoft/GODEL-v1_1-base-seq2seq")
        self.model = AutoModelForSeq2SeqLM.from_pretrained("microsoft/GODEL-v1_1-base-seq2seq")
        self.history = ['hi']

    def generate(self,instruction, knowledge, dialog, top_p, min_length, max_length):
        if knowledge != '':
            knowledge = '[KNOWLEDGE] ' + knowledge
        dialog = ' EOS '.join(dialog)
        query = f"{instruction} [CONTEXT] {dialog} {knowledge}"

        input_ids = self.tokenizer(f"{query}", return_tensors="pt").input_ids
        outputs = self.model.generate(input_ids, min_length=int(
            min_length), max_length=int(max_length), top_p=top_p, do_sample=True)
        output = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return output


    def predict(self,query):
        dialog = [
            query
        ]
        instruction = 'given a conversation, you need to give the next empathetic response.'
        # instruction = raw_instruction + self.history
        min_length = 8
        max_length = 64
        top_p = 0.9
        knowledge = ''.join(self.history)
        self.history.append(query)
        response = self.generate(instruction, knowledge, dialog,
                            top_p, min_length, max_length)
        

        print("conversation history: ",self.history)
        # return response

        print("This is the AI's response: ",response)
        # send_ai_response = input("Do you want to submit it?(Y/n):")
        # if(send_ai_response == 'Y' or send_ai_response == 'y'):
        #     self.history.append(response)
        #     return response
        # else:
        #     crowd_response = input("crowd choice: ")
        #     self.history.append(crowd_response)
        #     return crowd_response
        return response

    
