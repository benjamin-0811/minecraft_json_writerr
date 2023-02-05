import helper as h


def copy_name(conditions=None):
    text = {}
    h.innatd(text, "conditions", h.ml(conditions))
    text["function"] = "minecraft:copy_name"
    text["source"] = "block_entity"
    return text


def explosion_decay(conditions=None):
    text = {}
    h.innatd(text, "conditions", h.ml(conditions))
    text["function"] = "minecraft:explosion_decay"
    return text


def set_count(x=None, y=None, range_type=None, add=False, conditions=None):
    text = {"add": add}
    h.innatd(text, "conditions", h.ml(conditions))
    text["count"] = h.range_or_number(x, y, range_type)
    text["function"] = "minecraft:set_count"
    return text


def uniform_count(x=None, y=None, add=False, conditions=None):
    return set_count(x, y, "minecraft:uniform", add, conditions)


def binomial_count(x=None, y=None, add=False, conditions=None):
    return set_count(x, y, "minecraft:binomial", add, conditions)


def constant_count(count, add=False, conditions=None):
    return set_count(count, None, None, add, h.ml(conditions))


def fortune(bonus_multiplier=1, conditions=None):
    text = {}
    h.innatd(text, "conditions", h.ml(conditions))
    text["enchantment"] = "minecraft:fortune"
    text["formula"] = "minecraft:uniform_bonus_count"
    text["function"] = "minecraft:apply_bonus"
    text["parameters"] = {"bonusMultiplier": bonus_multiplier}
    return text


def limit_count(minimum=None, maximum=None, conditions=None):
    text = {}
    h.innatd(text, "conditions", h.ml(conditions))
    text["function"] = "minecraft:limit_count"
    limit = {}
    h.innatd(limit, "min", minimum)
    h.innatd(limit, "max", maximum)
    text["limit"] = limit
    return text


def ore_fortune(conditions=None):
    text = {}
    h.innatd(text, "conditions", h.ml(conditions))
    text["enchantment"] = "minecraft:fortune"
    text["formula"] = "minecraft:ore_drops"
    text["function"] = "minecraft:apply_bonus"
    return text


def nbt_op(op, source, target):
    return {"op": op, "source": source, "target": target}


def copy_nbt(ops, conditions=None):
    """
    use nbt_op(op, source, target) for *ops
    """
    text = {}
    h.innatd(text, "conditions", h.ml(conditions))
    text["function"] = "minecraft:copy_nbt"
    text["ops"] = h.ml(ops)
    text["source"] = "block_entity"
    return text


def binomial_with_bonus_count(extra, probability, conditions=None):
    text = {}
    h.innatd(text, "conditions", h.ml(conditions))
    text["enchantment"] = "minecraft:fortune"
    text["formula"] = "minecraft:binomial_with_bonus_count"
    text["function"] = "minecraft:apply_bonus"
    text["parameters"] = {"extra": extra, "probability": probability}
    return text


def copy_state(block, properties, conditions=None):
    text = {"block": block}
    h.innatd(text, "conditions", h.ml(conditions))
    text["function"] = "minecraft:copy_state"
    text["properties"] = h.ml(properties)
    return text


def copy_content(container, conditions=None):
    """
    copy contents of a storage block
    examples: shulker boxes
    """
    text = {"type": container}
    h.innatd(text, "conditions", h.ml(conditions))
    text["entries"] = [{"type": "minecraft:dynamic", "name": "minecraft:contents"}]
    text["function"] = "minecraft:set_contents"
    return text


def looting_enchant(x, y, range_type, limit, conditions=None):
    text = {}
    h.innatd(text, "conditions", h.ml(conditions))
    text["count"] = h.range_or_number(x, y, range_type)
    text["function"] = "minecraft:looting_enchant"
    h.innatd(text, "limit", limit)
    return text


def furnace_smelt(conditions):
    return {"conditions": h.ml(conditions), "function": "minecraft:furnace_smelt"}


def set_potion(effect, conditions=None):
    text = {}
    h.innatd(text, "conditions", h.ml(conditions))
    text["function"] = "minecraft:set_potion"
    text["id"] = effect
    return text


def enchant_randomly(enchantments, conditions=None):
    text = {}
    h.innatd(text, "conditions", h.ml(conditions))
    text = {"function": "minecraft:enchant_randomly"}
    h.innatd(text, "enchantments", h.ml(enchantments))
    return text


def set_damage(x, y, range_type, add=False, conditions=None):
    text = {"add": add}
    h.innatd(text, "conditions", h.ml(conditions))
    text["damage"] = h.range_or_number(x, y, range_type)
    text = {"function": "minecraft:set_damage"}
    return text


def enchant_with_levels(x, y, range_type, treasure=True, conditions=None):
    text = {}
    h.innatd(text, "conditions", h.ml(conditions))
    text["function"] = "minecraft:enchant_with_levels"
    text["levels"] = h.range_or_number(x, y, range_type)
    if treasure:
        text["treasure"] = True
    return text


def stew_effect(effect, x, y, range_type):
    return {"type": effect, "duration": h.range_or_number(x, y, range_type)}


def set_stew_effects(effects, conditions=None):
    """
    use stew_effect(effect, x, y, range_type) for *effects
    """
    text = {}
    h.innatd(text, "conditions", h.ml(conditions))
    return {"effects": h.ml(effects), "function": "minecraft:set_stew_effect"}


def set_instruments(instruments, conditions=None):
    text = {}
    h.innatd(text, "conditions", h.ml(conditions))
    return {"function": "minecraft:set_instrument", "options": h.ml(instruments)}


def exploration_map(decoration="red_x", skip_existing_chunks=False, zoom=1, conditions=None):
    text = {}
    h.innatd(text, "conditions", h.ml(conditions))
    return {"decoration": decoration, "function": "minecraft:exploration_map",
            "skip_existing_chunks": skip_existing_chunks, "zoom": zoom}


def translate(name):
    return {"translate": name}


def set_name(name, conditions=None):
    """
    use string or translate(name) for name
    """
    text = {}
    h.innatd(text, "conditions", h.ml(conditions))
    return {"function": "minecraft:set_name", "name": name}


cn = copy_name
ed = explosion_decay
sc = set_count
uc = uniform_count
bc = binomial_count
const = constant_count
ftn = fortune
lc = limit_count
oftn = ore_fortune
nbto = nbt_op
cnbt = copy_nbt
bwbc = binomial_with_bonus_count
cs = copy_state
cc = copy_content
le = looting_enchant
fs = furnace_smelt
sp = set_potion
er = enchant_randomly
sd = set_damage
ewl = enchant_with_levels
ste = stew_effect
sse = set_stew_effects
si = set_instruments
em = exploration_map
tr = translate
sn = set_name
