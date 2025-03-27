from crewai_tools import FileWriterTool

# Read extracted text
with open("ai_text.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Initialize File Writer
file_writer_tool = FileWriterTool()

# Write content to file
result = file_writer_tool._run(filename='ai.txt', content=text, directory='', overwrite=True)
print(result)
