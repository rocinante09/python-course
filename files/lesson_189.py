from translate import Translator

print('hello')
try:
    with open('./test.txt', mode='r') as my_file:
        text = my_file.read()
        print(f'text - {text}')
    with open('./test.txt', mode='w+') as my_file:
        translator = Translator(to_lang="jpn")
        translation = translator.translate(text)
        print(translation)
        my_file.write(translation)
except FileNotFoundError as err:
    print("can't find the file")
    raise err
except IOError as err:
    print("IO Error")
    raise err


