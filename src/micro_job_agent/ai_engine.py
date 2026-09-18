""" 
Groq Extraction Code
---------------------------
We wil take raw, messy text string extracted by PDF parser and send it to Groq. 
We'll use a highly optimized system prompt to force AI model to behave like a data extraction machine, 
returning clean list of technical keywords. 
"""

import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from micro_job_agent.parser import extract_text_from_pdf

# Load the environment keys from the local .env file
load_dotenv()

def extract_keywords_with_ai(resume_text: str) -> str:
    """Sends raw resume text to Groq to extract clean technical keywords."""
    
    # 1. Initialize the flagship, universally accessible Groq model
    llm = ChatGroq(
        model="openai/gpt-oss-120b",
        temperature=0.1,  # Low temperature forces the AI to be precise and factual
    )
    
    # 2. Design a strict prompt template that forces the AI to only return keywords
    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            "You are an expert AI resume parsing engine. Your job is to extract technical keywords "
            "from the provided resume text. Output ONLY a comma-separated list of the top technical skills, "
            "languages, frameworks, and databases found. Do not include introductory text, conversational text, "
            "or explanations. \n\nExample Output: Python, Django, PostgreSQL, Git, Docker"
        ),
        ("human", "Extract the keywords from this resume text:\n\n{text}")
    ])
    
    # 3. Chain the prompt together with the language model
    chain = prompt | llm
    
    try:
        # Execute the chain
        response = chain.invoke({"text": resume_text})
        return response.content.strip()
    except Exception as e:
        return f"Error communicating with Groq: {str(e)}"



# Direct script execution test
if __name__ == "__main__":
    print("Booting up the Micro AI Engine...")
    
    # 1. Grab the text using our Phase 2 tool
    test_pdf = "sample_resume.pdf"
    print(f"Reading {test_pdf}...")
    raw_text = extract_text_from_pdf(test_pdf)
    
    # 2. Pass the text to Groq
    print("Sending text to Groq for keyword extraction...")
    keywords = extract_keywords_with_ai(raw_text)
    
    print("\n--- AI Extracted Technical Keywords ---")
    print(keywords)
    print("---------------------------------------")







