import helper as h


def block_state_property(block, attribute, value):
    return {"block": block, "condition": "minecraft:block_state_property", "properties": {attribute: value}}


def silk_touch():
    return {"condition": "minecraft:match_tool", "predicate": {"enchantments": [
        {"enchantment": "minecraft:silk_touch", "levels": {"min": 1}}]}}


def survives_explosion():
    return {"condition": "minecraft:survives_explosion"}


def alternative(conditions):
    return {"condition": "minecraft:alternative", "terms": h.ml(conditions)}


def match_tool(tools):
    return {"condition": "minecraft:match_tool", "predicate": {"items": h.ml(tools)}}


def shears():
    return match_tool("minecraft:shears")


def fortune(chances):
    return {"chances": h.ml(chances), "condition": "minecraft:table_bonus", "enchantment": "minecraft:fortune"}


def inverted(condition):
    return {"condition": "minecraft:inverted", "term": condition}


def random_chance(chance):
    return {"chance": chance, "condition": "minecraft:random_chance"}


def blockstate_at_location(attribute, value, blocks, offset_x=None, offset_y=None, offset_z=None):
    text = {"condition": "minecraft:location_check"}
    h.innatd(text, "offsetX", offset_x)
    h.innatd(text, "offsetY", offset_y)
    h.innatd(text, "offsetZ", offset_z)
    text["predicate"] = {"block": {"blocks": h.ml(blocks), "state": {attribute: value}}}
    return text


def empty_entity_properties():
    return {"condition": "minecraft:entity_properties", "entity": "this", "predicate": {}}


def killed_by_player():
    return {"condition": "minecraft:killed_by_player"}


def entity_on_fire():
    return {"condition": "minecraft:entity_properties", "entity": "this", "predicate": {"flags": {"is_on_fire": True}}}


def random_chance_with_looting(chance, looting_multiplier):
    return {"chance": chance, "condition": "minecraft:random_chance_with_looting",
            "looting_multiplier": looting_multiplier}


def a_killed_by_b(entity):
    return {"condition": "minecraft:entity_properties", "entity": "killer", "predicate": {"type": entity}}


def damage_source_entity(entity):
    return {"condition": "minecraft:damage_source_properties", "predicate": {"source_entity": {"type": entity}}}


def damage_by_lightning():
    return {"condition": "minecraft:damage_source_properties", "predicate": {"is_lightning": True}}


def biome_at_location(biome):
    return {"condition": "minecraft:location_check", "predicate": {"biome": biome}}


def type_specific_entity_properties(entity_type, attribute, value):
    return {"condition": "minecraft:entity_properties", "entity": "this", "predicate": {"type_specific": {
        "type": entity_type, attribute: value}}}


def weather_check(raining=False, thundering=False):
    if not (raining or thundering):
        return None
    text = {"condition": "minecraft:weather_check"}
    h.innatd(text, "raining", raining)
    h.innatd(text, "thundering", thundering)
    return text


def time_check(x=None, y=None, range_type=None, period=None):
    text = {"condition": "minecraft:time_check", "value": h.range_or_number(x, y, range_type)}
    h.innatd(text, "period", period)
    return text


def reference(name):
    return {"condition": "minecraft:time_check", "name": name}


# alias
bsp = block_state_property
st = silk_touch
se = survives_explosion
alt = alternative
mt = match_tool
sh = shears
ftn = fortune
inv = inverted
rc = random_chance
bal = blockstate_at_location
eep = empty_entity_properties
kbp = killed_by_player
eof = entity_on_fire
rcwl = random_chance_with_looting
akbb = a_killed_by_b
dse = damage_source_entity
dbl = damage_by_lightning
bat = biome_at_location
tsep = type_specific_entity_properties
wc = weather_check
tc = time_check
ref = reference
