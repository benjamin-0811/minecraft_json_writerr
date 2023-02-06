import os
# import random
from typing import List
from dataclasses import dataclass


is_testing = False
current_id = "minecraft"


@dataclass
class Templates:
    ROOT = os.path.abspath(os.curdir) + "\\templates"
    BLOCK_MODEL = ROOT + "\\block_model"
    ITEM_MODEL = ROOT + "\\item_model"
    BLOCKSTATE = ROOT + "\\blockstate"
    RECIPE = ROOT + "\\recipe"
    LOOT_TABLE = ROOT + "\\loot_table"


@dataclass
class Results:
    ROOT = os.path.abspath(os.curdir) + "\\results"
    BLOCK_MODEL = ROOT + "\\block_model"
    ITEM_MODEL = ROOT + "\\item_model"
    BLOCKSTATE = ROOT + "\\blockstate"
    RECIPE = ROOT + "\\recipe"
    LOOT_TABLE = ROOT + "\\loot_table"


def get_file_content_as_string(path):
    """
    - Get File Content As String.
    :param path: location of the file
    :return: content of the file as a string value
    """
    f = open(path)
    text = f.read()
    f.close()
    return text


def is_block_model_dir(name):
    accept_names = [Templates.BLOCK_MODEL.lower(), "block_model", "blockmodel",
                    "block_m", "blockm", "block", "b_m", "bm"]
    return name.lower() in accept_names


def is_item_model_dir(name):
    accept_names = [Templates.ITEM_MODEL.lower(), "item_model", "itemmodel",
                    "item_m", "itemm", "item", "i_m", "im", "i"]
    return name.lower() in accept_names


def is_blockstate_dir(name):
    accept_names = [Templates.BLOCKSTATE.lower(), "block_state", "blockstate",
                    "block_s", "blocks", "state", "b_s", "bs", "b"]
    return name.lower() in accept_names


def is_recipe_dir(name):
    accept_names = [Templates.RECIPE.lower(), "crafting_recipe", "crafting_recipe",
                    "crafting_r", "craftingr", "c_r", "cr", "recipe", "rec", "r"]
    return name.lower() in accept_names


def is_loot_table_dir(name):
    accept_names = [Templates.LOOT_TABLE.lower(), "loot_table", "loottable",
                    "loot_t", "loott", "l_t", "lt", "loot", "l", "table", "t"]
    return name.lower() in accept_names


def get_content_of_template_file(file_name, directory="root", subdir=None):
    """
    - Get Content Of Template File.
    :param file_name: name of the file
    :param directory: location of the file
    :param subdir: subdirectory under templates
    :return: content of the file as a string value
    """
    if is_block_model_dir(directory):
        abspath = Templates.BLOCK_MODEL
    elif is_item_model_dir(directory):
        abspath = Templates.ITEM_MODEL
    elif is_blockstate_dir(directory):
        abspath = Templates.BLOCKSTATE
    elif is_recipe_dir(directory):
        abspath = Templates.RECIPE
    elif is_loot_table_dir(directory):
        abspath = Templates.LOOT_TABLE
    else:
        abspath = Templates.ROOT
        if subdir is not None:
            abspath = abspath + "\\" + subdir
    return get_content_of_template_file(abspath + "\\" + file_name + ".json")


def write_file(file_path, content):
    f = open(file_path, "w")
    f.write(content)
    f.close()


def texpath(name, namespace="minecraft", directory="block"):
    return None if name is None else "%s:%s/%s" % (namespace, directory, name)


def item_list(names: List[str], namespace="minecraft"):
    for i in range(len(names)):
        if names[i].find(":") != -1:
            names[i] = item(names[i], namespace)
    return names


def item(name, namespace="minecraft"):
    return "%s:%s" % (namespace, name)


def write(name, text, result_dir):
    """
    - write a file
    - just prints the text if the program is in testing mode
    :param name: name of the file
    :param text: file content
    :param result_dir: directory where the file will be saved
    """
    if is_testing:
        print(name, "\n", text, sep="", flush=True)
        input()
    else:
        write_file("%s\\%s.json" % (result_dir, name), text)


def right_angle(angle):
    if angle < 0:
        angle = angle + (int(angle * -1 / 360) + 1) * 360
    elif angle >= 360:
        angle = angle - int(angle / 360) * 360
    x = angle % 90
    angle = angle - x if x < 45 else angle + 90 - x
    return angle


def range_or_number(x=None, y=None, range_type=None):
    if range_type is None:
        return x
    text = {"type": range_type}
    if range_type == "minecraft:uniform":
        innatd(text, "max", y)
        innatd(text, "min", x)
    elif range_type == "minecraft:binomial":
        innatd(text, "n", x)
        innatd(text, "p", y)
    else:
        innatd(text, "x", x)
        innatd(text, "y", y)
    return text


def if_not_none_add_to_dict(dictionary, key, value):
    """
    - If Not None Add To Dict
    - sets tuple to list
    """
    if value is None:
        return
    if isinstance(value, tuple):
        dictionary[key] = list(value)
    else:
        dictionary[key] = value


def make_list(x):
    if x is None:
        return None
    elif isinstance(x, (str, int, float, dict)):
        return [x]
    # if isinstance(x, dict):
    #     t = []
    #     for i in x.keys():
    #         t.append({i: x[i]})
    #     return t
    elif isinstance(x, (tuple, list, dict)) and len(x) == 0:
        return None
    else:
        return list(x)


Temp = Templates
Res = Results
gcfas = get_file_content_as_string
ibmd = is_block_model_dir
iimd = is_item_model_dir
ibsd = is_blockstate_dir
ird = is_recipe_dir
iltd = is_loot_table_dir
gcotf = get_content_of_template_file
wf = write_file
ra = right_angle
ron = range_or_number
innatd = if_not_none_add_to_dict
ml = make_list


def test():
    """
    Tests the functions to read text from a file by creating a test file, writing to the file,
    then reading it and lastly, deleting it.
    """
    # file_name = "\\test_" + "%08d" % random.randrange(0, 100000000)
    # full_path = Templates.ROOT + file_name
    # file_name_with_suffix = file_name + ".json"
    # full_path_with_suffix = full_path + ".json"
    # f = open(full_path_with_suffix, "w")
    # f.write("{\n  \"parent\": \"cube_all\",\n  \"texture\": \"stone\"\n}")
    # f.close()
    # print(full_path_with_suffix)
    # print(gcotf(file_name))
    # os.remove(full_path_with_suffix)


if __name__ == "__main__":
    test()
