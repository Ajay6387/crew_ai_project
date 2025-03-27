from crewai_tools import ScrapeWebsiteTool

# Initialize the tool
tool = ScrapeWebsiteTool(website_url='https://en.wikipedia.org/wiki/Artificial_intelligence')

# Extract text
text = tool.run()
print(text)

# Save extracted text to use in other scripts
with open("ai_text.txt", "w", encoding="utf-8") as file:
    file.write(text)
