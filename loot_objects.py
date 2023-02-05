import helper as h


def loot_table(table_type, pools=None, functions=None):
    text = {"type": table_type}
    h.innatd(text, "functions", h.ml(functions))
    h.innatd(text, "pools", h.ml(pools))
    return text


def block_loot_table(pools=None, functions=None):
    return loot_table("minecraft:block", pools, functions)


def chest_loot_table(pools=None, functions=None):
    return loot_table("minecraft:chest", pools, functions)


def entity_loot_table(pools=None, functions=None):
    return loot_table("minecraft:entity", pools, functions)


def gift_loot_table(pools=None, functions=None):
    return loot_table("minecraft:gift", pools, functions)


def fishing_loot_table(pools=None, functions=None):
    return loot_table("minecraft:fishing", pools, functions)


def bartering_loot_table(pools=None, functions=None):
    return loot_table("minecraft:barter", pools, functions)


def pool(entries, bonus_rolls=0.0, rolls=1.0, conditions=None, functions=None):
    text = {"bonus_rolls": bonus_rolls}
    h.innatd(text, "conditions", h.ml(conditions))
    text["entries"] = h.ml(entries)
    h.innatd(text, "functions", h.ml(functions))
    text["rolls"] = rolls
    return text


def default_pool(entries):
    return pool(h.ml(entries), 0.0, 1.0, None, None)


def entry(name, entry_type="minecraft:item", conditions=None, functions=None, weight=None, quality=None):
    text = {"type": entry_type}
    h.innatd(text, "conditions", h.ml(conditions))
    h.innatd(text, "functions", h.ml(functions))
    text["name"] = name
    h.innatd(text, "quality", quality)
    h.innatd(text, "weight", weight)
    return text


def item_entry(name, conditions=None, functions=None, weight=None, quality=None):
    return entry(name, "minecraft:item", h.ml(conditions), h.ml(functions), weight, quality)


def tag_entry(name, conditions=None, functions=None, weight=None, expand=False, quality=None):
    text = {"type": "minecraft:tag", "expand": expand}
    h.innatd(text, "conditions", h.ml(conditions))
    h.innatd(text, "functions", h.ml(functions))
    text["name"] = name
    h.innatd(text, "quality", quality)
    h.innatd(text, "weight", weight)
    return text


def loot_table_entry(name, conditions=None, functions=None, weight=None, quality=None):
    return entry(name, "minecraft:loot_table", h.ml(conditions), h.ml(functions), weight, quality)


def dynamic_entry(name, conditions=None, functions=None, weight=None, quality=None):
    return entry(name, "minecraft:dynamic", h.ml(conditions), h.ml(functions), weight, quality)


def empty_entry(conditions=None, functions=None, weight=None, quality=None):
    text = {"type": "minecraft:empty"}
    h.innatd(text, "conditions", h.ml(conditions))
    h.innatd(text, "functions", h.ml(functions))
    h.innatd(text, "quality", quality)
    h.innatd(text, "weight", weight)
    return text


def multiple_entries(entries, conditions=None, entry_type="minecraft:alternatives"):
    text = {"type": entry_type, "children": h.ml(entries)}
    h.innatd(text, "conditions", h.ml(conditions))
    return text


def group_entries(entries, conditions=None):
    return multiple_entries(entries, conditions, "minecraft:group")


def alternative_entries(entries, conditions=None):
    return multiple_entries(entries, conditions, "minecraft:alternatives")


def sequence_entries(entries, conditions=None):
    return multiple_entries(entries, conditions, "minecraft:sequence")


lt = loot_table
blt = block_loot_table
clt = chest_loot_table
elt = entity_loot_table
glt = gift_loot_table
flt = fishing_loot_table
plt = piglin_loot_table = bartering_loot_table
pl = pool
dp = default_pool
en = entry
ie = item_entry
te = tag_entry
lte = loot_table_entry
ee = empty_entry
me = multiple_entries
ge = group_entries
ae = alternative_entries
se = sequence_entries
