import os
import openai

openai_api_key=os.getenv("OPENAI_API_KEY");
openai.api_key = openai_api_key
#print(openai.Model.list())

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", 
                                          messages=[{"role": "user", "content": "Hello world"}])
print(completion.choices[0].message.content)
