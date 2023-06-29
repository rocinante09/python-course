from PIL import Image
import os
import sys


def create_output_dir(image_root, dir):
    converted_folder = os.path.join(image_root, dir)
    try:
        os.mkdir(converted_folder)
    except FileExistsError as err:
        pass
    else:
        raise err
    finally:
        return converted_folder

def get_pokemon_file_list(image_root, pokemon_file):
    file_name = os.path.join(image_root, pokemon_file)
    with open(file_name, 'r') as my_file:
        text = my_file.read()
        pokemon_list = text.split(',')
    return pokemon_list

pokemon_file = sys.argv[1]
image_root = sys.argv[2]

print(pokemon_file, image_root)
# pokemon_file = 'pokemon.csv'
# image_root = './images'
print(os.path.join(image_root, pokemon_file))
converted_folder = create_output_dir(image_root, 'converted')

pokemon_list = get_pokemon_file_list(image_root, pokemon_file)

for file in pokemon_list:
    file = file.strip()
    img = Image.open(os.path.join(image_root,file + '.jpg'))
    name = file
    print(name)
    img.save(os.path.join(converted_folder, name + '.png'), 'png')