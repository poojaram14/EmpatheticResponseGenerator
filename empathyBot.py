from transformers import pipeline
from transformers import (
    AutoTokenizer,
    AutoModel,
    AutoModelForSeq2SeqLM,
    AutoModelForCausalLM
)
import pandas as pd

# class EmpathyResponse:
#     def __init__(self):
#         self.model_pipeline = pipeline("text2text-generation", model = "benjaminbeilharz/dialoGPT-small-empatheticdialogues-generation")
    
#     def predict(self, query):
#         return self.model_pipeline(query)

class EmpathyResponse:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("microsoft/GODEL-v1_1-base-seq2seq")
        self.model = AutoModelForSeq2SeqLM.from_pretrained("microsoft/GODEL-v1_1-base-seq2seq") 
        self.model_t5 = pipeline("text2text-generation", model="benjaminbeilharz/t5-empatheticdialogues")

        
        self.history = ['hi']
        # mi_raw = pd.read_csv("MI_data\dataset.csv")
        # mi_cleaned = mi_raw[['topic','interlocutor','utterance_text']]
        # mi_cleaned_just_therapist_responses = mi_cleaned.loc[mi_cleaned['interlocutor'] == 'therapist']
        # self.knowledge = mi_raw.utterance_text[0:100].to_string()


    def generate(self,instruction, knowledge, dialog, top_p, min_length, max_length):
        if knowledge != '':
            knowledge = '[KNOWLEDGE] ' + knowledge
        dialog = ' EOS '.join(dialog)
        query = f"{instruction} [CONTEXT] {dialog} {knowledge}"

        alt_output = self.model_t5(query)[0]["generated_text"]
        
        input_ids = self.tokenizer(f"{query}", return_tensors="pt").input_ids
        outputs = self.model.generate(input_ids, min_length=int(
            min_length), max_length=int(max_length), top_p=top_p, do_sample=True)
        output = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return output,alt_output


    def predict(self,query):
        # dialog = [
        #     query
        # ]
        instruction = 'given a dialog context, you need to response empathically.'
        # instruction = raw_instruction + self.history
        min_length = 4
        max_length = 24
        top_p = 0.9
        knowledge = ""
        self.history.append(query)
        if len(self.history) > 2 and len(self.history) < 4:
            dialog = self.history[-2:]
        elif len(self.history) >= 4:
            dialog = self.history[-4:] 
        else:
            dialog = [query]

        response,alt_response = self.generate(instruction, knowledge, dialog,
                            top_p, min_length, max_length)
        
        
        
        print("conversation history: ",self.history)
        # return response

        print("This is the AI's first suggestion: ",response)
        print("This is the AI's second suggestion: ",alt_response)

        # send_ai_response = input("Do you want to submit it?(Y/n):")
        # if(send_ai_response == 'Y' or send_ai_response == 'y'):
        #     self.history.append(response)
        #     return response
        # else:
        #     crowd_response = input("crowd choice: ")
        #     self.history.append(crowd_response)
        #     return crowd_response

        send_ai_response = input("To use the first or second sugeestion, press 1 for the first, or 2 for the second, or type your own response: ")
        if(send_ai_response == '1' or send_ai_response == 1):
            self.history.append(response)
            return response
        elif(send_ai_response == '2' or send_ai_response == 2):
            self.history.append(alt_response)
            return alt_response
        else:
            self.history.append(send_ai_response)
            return send_ai_response
