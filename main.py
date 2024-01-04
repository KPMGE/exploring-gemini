import pathlib
import textwrap
import os

import google.generativeai as genai

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)


def show_available_genai_models():
    print("Available models:")
    for m in genai.list_models():
      if 'generateContent' in m.supported_generation_methods:
        print(m.name)


def main():
    show_available_genai_models()


if __name__ == '__main__': 
    main()
