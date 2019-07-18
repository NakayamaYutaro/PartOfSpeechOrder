import sys

class write_to_txt:
    def insert_text(self,text_name,text_content):
        path_w = text_name 
       
        with open(path_w,mode='a') as f:
            f.write(text_content+"\n") 
