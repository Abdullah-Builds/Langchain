from langchain_core.prompts import MessagesPlaceholder,ChatPromptTemplate

# chat template
template = ChatPromptTemplate([
    ('system','You are a {domain} expert'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human', "Explain the {topic} in simple terms"),
])

#Load The Chat History
chat_history = []

with open('chat_history.txt') as f :
      chat_history.extend(f.readlines())

#Invoke the template

prompt = template.invoke({"domain" : "cricket","chat_history" : chat_history,"topic": "dusra"})
print(prompt)