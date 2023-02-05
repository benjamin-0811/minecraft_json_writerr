import helper as h


def snbm(name):
    return h.texpath(name, h.current_id, "block")


def smbm(name):
    return h.texpath(name, "minecraft", "block")


def snim(name):
    return h.texpath(name, h.current_id, "item")


def smim(name):
    return h.texpath(name, "minecraft", "item")


def model(parent, ambient_occlusion=True, textures=None):
    text = {}
    if parent:
        text["parent"] = parent
    if not ambient_occlusion:
        text["ambient_occlusion"] = False
    if textures:
        text["textures"] = textures
    return text


def create_model(parent, ambient_occlusion=True, textures=None):
    return model(parent, ambient_occlusion, textures)


def create_block_model(parent, ambient_occlusion=True, keys=None, values=None):
    if isinstance(values, list):
        values_c = values.copy()
        for i in range(len(values_c)):
            values_c[i] = snbm(values_c[i])
    else:
        values_c = snbm(values)
    return create_model(smbm(parent), ambient_occlusion, create_textures(keys, values_c))


def create_item_model(parent, ambient_occlusion=True, keys=None, values=None):
    if isinstance(values, list):
        for i in range(len(values)):
            values[i] = snim(values[i])
    else:
        values = snim(values)
    return create_model(smim(parent), ambient_occlusion, create_textures(keys, values))


def create_textures(keys, values):
    keys = h.ml(keys)
    values = h.ml(values)
    if keys is None or values is None:
        return None
    klen = len(keys)
    vlen = len(values)
    if klen != vlen or klen < 1:
        return None
    text = {}
    for i in range(klen):
        text[keys[i]] = values[i]
    return text


mo = model
cm = create_model
cbm = create_block_model
cim = create_item_model
ct = create_textures
