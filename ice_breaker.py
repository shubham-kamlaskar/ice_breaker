import os
from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

if __name__ == "__main__":
    print("Working on langchain")
    print(os.environ["OPENAI_API_KEY"])