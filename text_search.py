import os
from crewai_tools import TXTSearchTool
import os
from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# Raise an error if the API key is not set
if not OPENAI_API_KEY:
    raise ValueError("⚠️ OpenAI API Key is missing! Add it to the .env file.")

# Set API Key
# os.environ['OPENAI_API_KEY'] = 'OPENAI_API_KEY'

# Initialize search tool
tool = TXTSearchTool(txt='ai.txt')

# Search Example
context = tool.run('What is natural language processing?')
print(context)
