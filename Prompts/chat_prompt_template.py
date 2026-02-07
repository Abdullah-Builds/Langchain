from langchain_core.prompts import ChatPromptTemplate

template = ChatPromptTemplate([
    ('system','You are a helpeful {domain} expert'),
    ('human', "you have to explain {topic} in simple terms")
])

prompts = template.invoke({'domain':"cricket",'topic' : "Dusra"})
print(prompts)