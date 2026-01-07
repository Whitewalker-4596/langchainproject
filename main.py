from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama 
import os


def main():
    print("Hello from langchainproject!")
    load_dotenv()
    print("OPEN_API_KEY:", os.getenv("OPEN_API_KEY"))
    print(os.environ.get("OPEN_API_KEY"))
    info = """
    Elon Reeve Musk (/ˈiːlɒn/ EE-lon; born June 28, 1971) is a businessman and entrepreneur known for his leadership of Tesla, SpaceX, Twitter, and xAI.
    Musk has been the wealthiest person in the world since 2021; 
    as of December 2025, Forbes estimates his net worth to be around US$717 billion.
    Born into a wealthy family in Pretoria, South Africa, Musk emigrated in 1989 to Canada; 
    he has Canadian citizenship since his mother was born there. 
    He received bachelor's degrees in 1997 from the University of Pennsylvania in Philadelphia, United States, before moving to California to pursue business ventures.
    In 1995, Musk co-founded the software company Zip2. Following its sale in 1999, he co-founded X.com, an online payment company that later merged to form PayPal, which was acquired by eBay in 2002.
    Musk also became an American citizen in 2002.
    """

    summary_template = """
    given the information {info} about a person.
    1,write a short summary about their life in less than 30 words.
    2,write two intresting facts about them.
    """
    summary_prompt_template = PromptTemplate(
        input_variables=["info"],
        template = summary_template
    )
    # llm = ChatOpenAI(model_name="gpt-5", temperature=0)
    # llm = ChatOllama(model="gemma3:270m", temperature=0)
    llm = ChatOllama(model="gpt-oss:20b", temperature=0)
    # llm = ChatOllama(model="gemma3:1b", temperature=0)
    
    print(type(summary_prompt_template))
    chain = summary_prompt_template | llm
    response = chain.invoke({"info":info})
    print(response.content)
    #the above gives runnable chain 
    

if __name__ == "__main__":
    main()
