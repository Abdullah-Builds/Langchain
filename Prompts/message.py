import os
from openai import OpenAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage,AIMessage,HumanMessage
load_dotenv()

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.environ["HUGGINGFACEHUB_API_TOKEN"],
)

# we can also use prompt template as a specialized prompt with every msg 
# from langchain_core.prompts import PromptTemplate, we have to use this for it

chat_history = [
  SystemMessage(content="You are a helper"),
  AIMessage(content="You have to help")  
]

while True:
    user_input = input ("User : ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input == "exit" :
        break

    completion = client.chat.completions.create(
         model="openai/gpt-oss-20b:groq",
         messages=[
        {
            "role": "user",
            "content": user_input
        }
        ],
     )
    response = completion.choices[0].message.content
    chat_history.append(AIMessage(content=user_input))
    print(completion.choices[0].message.content)

print("ChatHistory \n",chat_history)