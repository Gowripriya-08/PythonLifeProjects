# # from pypdf import PdfReader
# # from gtts import gTTS

# # reader = PdfReader("questions.pdf")

# # page = reader.pages[0]

# # text = page.extract_text()

# # print(text)   # Check whether PDF text was extracted

# # tts = gTTS(text, lang="en")

# # tts.save("questions.mp3")

# # print("MP3 created successfully!")

# from pypdf import PdfReader

# reader = PdfReader("questions.pdf")

# page = reader.pages[0]

# text = page.extract_text()

# print(text)
from pypdf import PdfReader
from gtts import gTTS

reader = PdfReader("questions.pdf")

page = reader.pages[0]

text = page.extract_text()

print(text)

print("Converting to audio...")

tts = gTTS(text, lang="en")

tts.save("questions.mp3")

print("MP3 created successfully!")