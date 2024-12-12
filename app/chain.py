# from langchain_community.chat_models import ChatOllama
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate 

llm = ChatOllama(model="EEVE-Korean-10.8B:latest")

# 프롬프트 설정
prompt = ChatPromptTemplate.from_template('{topic} 에 대해 간략히 설명해 줘.')

# LangChain 표현식 언어 체인 구문 사용 
chain = prompt | llm | StrOutputParser()