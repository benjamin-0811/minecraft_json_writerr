import helper as h
import json as j
import model_objects as o


def write(name, parent, ambient_occlusion=True, keys=None, values=None):
    h.write(name, j.dumps(o.cim(parent, ambient_occlusion, keys, values), indent=2), h.Results.ITEM_MODEL)


def item(name, textures=None):
    """
    - textures = name
    - enter a list of textures for multiple layers
    """
    textures = textures or name
    if isinstance(textures, list):
        keys = []
        for i in range(len(textures)):
            keys.append("layer%d" % i)
    else:
        keys = "layer0"
    write(name, "generated", True, keys, textures)


def item_parent(name, item_model=None, particle=None):
    """
    - item_model = name
    - examples: spawn_egg, banner
    - particle: bed, shulker_box
    """
    key = None if particle is None else "particle"
    h.write(name, j.dumps(o.cim(item_model or name, True, key, particle), indent=2), h.Results.ITEM_MODEL)


def block_parent(name, block_model=None):
    """
    - block_model = name
    """
    h.write(name, j.dumps(o.cbm(block_model or name), indent=2), h.Results.ITEM_MODEL)


def handheld(name, textures=None, rod=False):
    """
    - textures = name
    - examples: sword, tools, bamboo, blaze_rod, stick, bone
    - rod: fishing_rods
    """
    textures = textures or name
    if isinstance(textures, list):
        keys = []
        for i in range(len(textures)):
            keys.append("layer%d" % i)
    else:
        keys = "layer0"
    write(name, "handheld_rod" if rod else "handheld", True, keys, textures)


if __name__ == "__main__":
    h.is_testing = True
    use_all_params = input("Testing Item Model Creation\nFull parameters? [Y] / [N]\n")
    if use_all_params == "Y":
        item("xx", ["yy", "zz", "uu", "vv"])
        item_parent("xx", "yy", "zz")
        block_parent("xx", "yy")
        handheld("xx", ["yy", "zz", "uu", "vv"], True)
    elif use_all_params == "N":
        item("xx")
        item_parent("xx")
        block_parent("xx")
        handheld("xx")
    h.is_testing = False
