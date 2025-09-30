from googletrans import Translator

text = "I don't get why we don't have a unified language for the whole world"
translator = Translator()

filipino_translation = translator.translate(text, dest='tl')
print(filipino_translation.text)