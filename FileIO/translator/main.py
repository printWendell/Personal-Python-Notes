from translate import Translator
translator= Translator(to_lang="es")
# translation = translator.translate("This is a pen.")
# print(translation)

try: 
    with open('test.txt', mode="r") as my_file: 
        text = my_file.read()
        translation = translator.translate(text)
        print(f"{text} translates to '{translation}' in Spanish")
except FileNotFoundError as err: 
    print('File not found')
    raise err