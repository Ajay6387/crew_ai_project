import os
from crewai_tools import TXTSearchTool
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Retrieve OpenAI API Key from .env
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Raise an error if the API key is missing
if not OPENAI_API_KEY:
    raise ValueError("⚠️ OpenAI API Key is missing! Add it to the .env file.")

# Set API Key (optional, if needed explicitly)
os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY

# Check if the file exists before initializing TXTSearchTool
file_path = r"ai.txt"
if not os.path.exists(file_path):
    raise FileNotFoundError(f"⚠️ The file '{file_path}' does not exist. Please provide a valid text file.")

# Initialize search tool
tool = TXTSearchTool(txt=file_path)

# Search Example
context = tool.run('What is natural language processing?')

# Print the search result
print(context)
