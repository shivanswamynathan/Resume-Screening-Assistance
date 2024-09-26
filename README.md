# Resume-Screening-Assistance
Resume Screening Assistance Chatbot is an AI-powered conversational assistant designed to help recruiters and HR professionals streamline the resume screening process through natural language interactions. The chatbot leverages Generative AI (GenAI) models from HuggingFace to provide insightful and interactive conversations, helping users parse resumes, rank candidates, and assist with initial candidate screening questions.

# Project Overview
This project integrates advanced natural language models from HuggingFace with a resume screening system. The chatbot can handle recruiter queries regarding job applications, automatically parse resumes for relevant information, compare qualifications against job descriptions, and generate personalized candidate recommendations. It reduces manual effort and enhances efficiency by using conversational AI to automate and assist with the early stages of recruitment.

# Key Features
1. Conversational AI: The chatbot allows recruiters to interact naturally through chat, asking about job candidates, qualifications, and resume parsing.
2. Resume Parsing: Automatically extracts key information from resumes, such as experience, skills, education, and certifications.
3. Job Matching: The chatbot compares parsed resume data with job descriptions to assess candidate suitability.
4. Candidate Ranking: Provides ranking and scoring for candidates based on predefined criteria like skills, experience, and education.

# Requirements
langchain==0.0.350
streamlit==1.29.0
openai==1.5.0
tiktoken==0.5.2
python-dotenv==1.0.0
unstructured==0.11.5
pinecone-client==2.2.4
pypdf==3.17.2
sentence-transformers==2.2.2

# Technologies Used
1. Technologies UsedHuggingFace Transformers: Uses pre-trained language models like GPT, T5, or BERT from HuggingFace to power natural conversations and NLP tasks.
2. Python: The main language used for backend chatbot logic and integration.
3. streamlit:For containerizing the application and ensuring a consistent development environment.
