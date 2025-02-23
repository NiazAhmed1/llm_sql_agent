from langchain_community.utilities import SQLDatabase
from langchain_community.llms import Ollama
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain.agents import create_sql_agent
from langchain.agents.agent_types import AgentType
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.chains import LLMChain
import os


def setup_sql_agent(db_file: str):
    db_uri=f"sqlite:///{db_file}"
    db=SQLDatabase.from_uri(db_uri)
    
    llm = Ollama(
        model="mistral:latest",
        temperature=0.1
    )
    toolkit=SQLDatabaseToolkit(db=db,llm=llm)
    agent=create_sql_agent(
        llm=llm,
        toolkit=toolkit,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )
    
    explanation_prompt=PromptTemplate(
        input_variables=["query","results"],
        template="""Given this SQL query :
        {query}
        and these resuts:
        {result}
        provide a clear, concise explanation of what these result mean in natural language.
        focus on the key insights and pattern in the data.
        """
    )
    
    explanation_chain=LLMChain(
        llm=llm,
        prompt=explanation_prompt,
        output_parser=StrOutputParser()
    )
    
    # return llm,db,toolkit,agent,explanation_chain
    return agent,db

def query_database(agent,question):
    
    try:
        result=agent.run(question)
        return result
    except Exception as e:
        return f"Error occured: {str(e)}"
    

def get_db_schema(db):
    return db.get_table_info()



if __name__ =="__main__":
    
    agent, db = setup_sql_agent("chinook.db")
    

    print("Database Schema:")
    print(get_db_schema(db))
    
    # Example questions you can ask about the chinook database
    questions = [
        "How many employees are there?",
        "What is the most popular music genre by number of tracks?",
        "Find the most expensive track in the database",
        "Show the number of tracks available in each genre",
        "List all the albums by artists with the word ‘black’ in their name",
        " Find the name and length (in seconds) of all tracks that have lengthbetween 50 and 70 seconds."
    ]
    
    #Run example questions
    for question in questions:
        print(f"\nQuestion: {question}")
        print("Answer:", query_database(agent, question))
    
