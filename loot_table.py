import helper as h
import json as j
import loot_objects as o
import loot_conditions as c
import loot_functions as f

res_block = h.Results.LOOT_TABLE + "\\blocks"
res_entity = h.Results.LOOT_TABLE + "\\entities"
res_chest = h.Results.LOOT_TABLE + "\\chests"
res_village = res_chest + "\\village"
res_gameplay = h.Results.LOOT_TABLE + "\\gameplay"
res_fishing = res_gameplay + "\\fishing"
res_hero = res_gameplay + "\\hero_of_the_village"


def insni(maybe_none, x):
    """
    - If None Set Minecraft Item
    - example: "minecraft:item/<x>"
    :param maybe_none: value 1 (can be None)
    :param x: value 2 (should not be None)
    :return: "minecraft:item/<x>" if maybe_none is None, maybe_none anytime else
    """
    return h.none_to_x(maybe_none, h.item(x, h.current_id))


def insmi(maybe_none, x):
    """
    - If None Set Minecraft Item
    - example: "minecraft:item/<x>"
    :param maybe_none: value 1 (can be None)
    :param x: value 2 (should not be None)
    :return: "minecraft:item/<x>" if maybe_none is None, maybe_none anytime else
    """
    return h.none_to_x(maybe_none, h.item(x, "minecraft"))


def write(name, text, result_dir=h.Results.LOOT_TABLE):
    h.write(name, j.dumps(text, indent=2), result_dir)


def cube(name, item=None, survive_explosion=True):
    """
    - any block that drops itself as an item
    - item == None --> name
    - must_survive_explosion: conduit, dragon_egg, dragon_head, any skull/head
    :param name: name of the block
    :param item: item
    :param survive_explosion: determines if the block must survive an explosion
    """
    write(name, o.blt(o.pl(o.en(insni(item, name)), conditions=c.se() if survive_explosion else None)), res_block)


def slab(name, block=None, item=None):
    """
    - any slab
    - block == None --> <name>_slab
    - item == None --> <name>_slab
    :param name: name of the slab (without "_slab")
    :param block: name of the slab
    :param item: item
    """
    name = "%s_slab" % name
    functions = (f.const(2.0, False, c.bsp(insni(block, name), "type", "double")), f.ed())
    table = o.blt(o.dp(o.ie(insni(item, name), functions=functions)))
    write(name, table, res_block)


def door(name, block=None, item=None):
    """
    - any door
    - block == None --> <name>_door
    - item == None --> <name>_door
    :param name: name of the door (without "_door")
    :param block: name of the door
    :param item: item
    """
    name = "%s_door" % name
    table = o.blt(o.dp(o.ie(insni(item, name), conditions=(c.bsp(insni(block, name), "half", "lower")))))
    write(name, table, res_block)


def leaves(name, leaf=None, sapling=None, stick=None, fruit=None, custom_stick=False, custom_fruit=False):
    """
    - any leaf block
    - leaf == None --> leaf = <name>_leaves
    - sapling == None --> sapling = <name>_sapling
    - stick == None - if custom_stick --> <name>_stick , else --> "minecraft:stick"
    - fruit == None - if custom_fruit --> <name>_fruit , else --> "minecraft:apple"
    :param name: name of the leaves (without "_leaves")
    :param leaf: leaves item
    :param sapling: sapling item
    :param stick: stick item
    :param fruit: fruit item
    :param custom_stick: determines if the leaves get a custom stick
    :param custom_fruit: determines if the leaves get a custom fruit
    """
    e00 = o.ie(insni(leaf, "%s_leaves" % name), [c.alt([c.sh(), c.st()])])
    e01 = o.ie(insni(sapling, "%s_sapling" % name), [c.se(), c.ftn([0.05, 0.0625, 0.083333336, 0.1])])
    n1 = insni(stick, "%s_stick" % name) if custom_stick else "minecraft:stick"
    c1 = [c.ftn([0.02, 0.022222223, 0.025, 0.033333335, 0.1])]
    f1 = [f.sc(1.0, 2.0, "minecraft:uniform", False), f.ed()]
    p1 = o.pl([o.ie(n1, c1, f1)], 0.0, 1.0, c.inv(c.alt([c.sh(), c.st()])))
    pools = [o.dp([o.ae([e00, e01])]), p1]
    if fruit is not None:
        ce2 = [c.se(), c.ftn([0.005, 0.0055555557, 0.00625, 0.008333334, 0.025])]
        e2 = o.ie(insni(fruit, "%s_fruit" % name) if custom_fruit else "minecraft:apple", ce2)
        pools.append(o.pl([e2], 0.0, 1.0, c.inv(c.alt([c.sh(), c.st()]))))
    write("%s_leaves" % name, o.blt(pools), res_block)


def empty_block(name):
    """
    - any block that drops nothing
    :param name: name of the block
    """
    write(name, o.blt(), res_block)


def silk_touch(name, with_silk_touch=None, without_silk_touch=None, minimum=None, maximum=None,
               limit_min=None, limit_max=None, chances=None, ore_bonus=False, uniform_bonus=False):
    """
    - any block that drops something with silk touch and something else without
    - only_one (minimum = maximum = limit_min = limit_max = 0)
    - constant_amount (minimum = x, maximum = limit_min = limit_max = 0)
    - min_max (minimum = x, maximum = y, limit_min = limit_max = 0)
    - limits (minimum = x, maximum = y, limit_min = a, limit_max = b)
    :param name: name of the block
    :param with_silk_touch: item that drops with silk touch
    :param without_silk_touch: item that drops without silk touch
    :param minimum: min amount of items that drop when not using silk touch
    :param maximum: max amount of items that drop when not using silk touch
    :param limit_min: lower limit of items that drop
    :param limit_max: upper limit of items that drop
    :param chances: chances for fortune level 0, 1, 2, 3...
    :param ore_bonus: bonus
    :param uniform_bonus: bonus
    """
    with_silk_touch = insni(with_silk_touch, name)
    without_silk_touch = insni(without_silk_touch, name)
    functions = []
    if minimum is not None:
        functions.append(f.sc(minimum) if maximum is None else f.uc(minimum, maximum))
    if ore_bonus:
        functions.append(f.oftn())
    if uniform_bonus:
        functions.append(f.ftn())
    if limit_min is not None or limit_max is not None:
        functions.append(f.lc(limit_min, limit_max))
    if chances is not None:
        entry = o.ae([o.ie(without_silk_touch, c.ftn(chances), functions), o.ie(with_silk_touch)], c.se())
    else:
        functions.append(f.ed())
        entry = o.ie(without_silk_touch, functions=functions)
    write(name, o.blt(o.dp(o.ae([o.ie(with_silk_touch, c.st()), entry]))), res_block)


def only_silk_touch(name, item=None):
    """
    - any block that only drops something with silk touch
    glass
    """
    write(name, o.blt(o.pl(o.ie(insni(item, name)), conditions=c.st())), res_block)


def ore(name, block=None, item=None, minimum=None, maximum=None, uniform_bonus=False):
    """
    - any ore
    :param name: name of the ore (without "_ore")
    :param block: ore item
    :param item: item
    :param minimum: min amount of items that drop when not using silk touch
    :param maximum: max amount of items that drop when not using silk touch
    :param uniform_bonus: redstone-like fortune calculation
    """
    silk_touch("%s_ore" % name, insni(block, "%s_ore" % name), insni(item, name), minimum, maximum,
               ore_bonus=not uniform_bonus, uniform_bonus=uniform_bonus)


def tile_entity(name, item=None, survive_explosion=True):
    """
    - any tile entity that can have a custom name
    :param name:
    :param item:
    :param survive_explosion:
    """
    table = o.blt(o.pl(o.ie(insni(item, name), functions=f.cn()), conditions=c.se() if survive_explosion else None))
    write(name, table, res_block)


def one_part(name, block=None, item=None, key=None, value=None):
    """
    - any multi-block structure where only one part drops the entire thing as an item
    :param name: name of the block
    :param block: name of the block
    :param item: name of the item
    :param key: name of the state important to the loot table
    :param value: value of the state important to the loot table
    """
    table = o.blt(o.pl(o.ie(insni(item, name), c.bsp(insni(block, name), key, value)), conditions=c.se()))
    write(name, table, res_block)


def multiple_items(name, items, survive_explosion=True):
    """
    - any block that drops multiple items at once
    :param name: name of the block
    :param items: list of items that the block drops
    :param survive_explosion: determines if the block must survive an explosion
    """
    item_list = h.ml(items)
    pools = []
    for i in range(len(item_list)):
        pools.append(o.pl(o.ie(item_list[i]), conditions=c.se() if survive_explosion else None))
    write(name, o.blt(pools), res_block)


def like_grass(name, grass=None, seeds=None, seed_chance=0.125, double=None, is_double=False):
    """
    - any block that drops items like grass
    - drops grass when using shears
    - either drops seeds or nothing when not using shears
    - grass == None --> grass = name
    - seeds == None --> seeds = "minecraft:wheat_seeds"
    - double == None --> double = tall_<name>
    :param name: name of the block
    :param grass: name of the block item
    :param seeds: name of the item
    :param seed_chance: chance to drop seeds
    :param double: name of the 2-block item
    :param is_double: determines if the block is 2 blocks tall
    """
    grass = insni(grass, name)
    seeds = insmi(seeds, "wheat_seeds")
    if is_double:
        double = insni(double, "tall_%s" % name)
        entry = o.ae([o.ie(grass, c.sh(), f.sc(2.0)), o.ie(seeds, [c.se(), c.rc(seed_chance)])])
        p0 = o.pl(entry, conditions=[c.bsp(double, "half", "lower"), c.bal("half", "upper", double, offset_y=1)])
        p1 = o.pl(entry, conditions=[c.bsp(double, "half", "upper"), c.bal("half", "lower", double, offset_y=-1)])
        write(name, o.blt([p0, p1]), res_block)
    else:
        table = o.blt(o.dp(o.ae([o.ie(grass, c.sh()), o.ie(seeds, c.rc(seed_chance), [f.ftn(2), f.ed()])])))
        write(name, table, res_block)


def cereal(name, block=None, fruit=None, seeds=None, age=7, extra=3, probability=0.5714286):
    block = insni(block, name)
    fruit = insni(fruit, name)
    seeds = insni(seeds, "%s_seeds" % name)
    p0 = o.dp(o.ae([o.ie(fruit, c.bsp(block, "age", str(age))), o.ie(seeds)]))
    p1 = o.pl(o.ie(seeds, functions=f.bwbc(extra, probability)), conditions=c.bsp(block, "age", str(age)))
    write(name, o.blt([p0, p1], f.ed()), res_block)


def root_vegetable(name, block=None, fruit=None, alt_fruit=None, age=7,
                   extra=3, probability=0.5714286, alt_fruit_chance=0.02):
    block = insni(block, name)
    fruit = insni(fruit, name)
    p0 = o.dp(o.ie(fruit))
    p1 = o.pl(o.ie(fruit, functions=f.bwbc(extra, probability)), conditions=c.bsp(block, "age", str(age)))
    pools = [p0, p1]
    if alt_fruit is not None:
        pools.append(o.pl(o.ie(alt_fruit, c.rc(alt_fruit_chance)), conditions=c.bsp(block, "age", str(age))))
    write(name, o.blt(pools, f.ed()), res_block)


def stem(name, block=None, seeds=None, age=7, n_list=None, p_list=None):
    block = insni(block, "%s_stem" % name)
    seeds = insni(seeds, "%s_seeds" % name)
    length = age + 1
    if isinstance(n_list, float):
        n_list = [n_list] * length
    elif n_list is None or (isinstance(n_list, list) and len(n_list) < length):
        n_list = [3.0] * length
    if isinstance(p_list, float):
        p_list = [round(p_list * (i + 1), 8) for i in range(length)]
    elif p_list is None or (isinstance(p_list, list) and len(p_list) < length):
        p_list = [round(2 / 30 * (i + 1), 8) for i in range(length)]
    functions = []
    for i in range(length):
        functions.append(f.bc(n_list[i], p_list[i], False, c.bsp(block, "age", i)))
    write("%s_stem" % name, o.blt(o.pl(o.ie(seeds, functions=functions), functions=f.ed())), res_block)
    table = o.blt(o.pl(o.ie(seeds, functions=f.bc(n_list[age], p_list[age], False)), functions=f.ed()))
    write("attached_%s_stem" % name, table, res_block)


def pod_fruit(name, block=None, item=None, age=2, x=3.0, y=None):
    cf0 = c.bsp(insni(block, name), "age", str(age))
    f0 = f.set_count(x, y, "uniform_count" if y is not None else None, False, cf0)
    table = o.blt(o.dp(o.ie(insni(item, "%s_beans" % name), functions=[f0, f.ed()])))
    write(name, table, res_block)


def fruit_bush(name, block=None, item=None, plural_item=True, amm=None):
    """
    :param name: name of the berry (without "_bush")
    :param block: bush block
    :param item: berry item
    :param plural_item: Are there multiple berries in one item?
    :param amm: list of age, minimum, maximum triplets
    """
    block = insni(block, "%s_bush" % name)
    item = insni(item, name.replace("berry", "berries") if "berry" in name and plural_item else name)
    amm = h.none_to_x(amm, [[3, 2.0, 3.0], [2, 1.0, 2.0]])
    pools = []
    for i in range(len(amm)):
        cur_tri = amm[i]
        c0 = c.bsp(block, "age", cur_tri[0])
        pools.append(o.pl(o.ie(item), conditions=c0, functions=[f.uc(cur_tri[1], cur_tri[2]), f.ftn()]))
    write("%s_bush" % name, o.blt(pools, f.ed()), res_block)


def like_nether_wart(name, block=None, item=None, age=3, minimum=2.0, maximum=4.0):
    cond = c.bsp(insni(block, name), "age", str(age))
    f0 = [f.uc(minimum, maximum, False, cond), f.ftn(1, cond)]
    write(name, o.blt(o.pl(o.ie(insni(item, name), functions=f0), functions=f.ed())), res_block)


def shears(name, with_shears=None, without_shears=None, use_silk_touch=False,
           minimum=None, maximum=None, chances=None, explosion_decay=False, survives_explosion=False):
    """
    shears
    """
    with_shears = insni(with_shears, name)
    without_shears = insni(without_shears, name)
    functions = []
    conditions = []
    if minimum is not None:
        functions.append(f.sc(minimum) if maximum is None else f.uc(minimum, maximum))
    if explosion_decay:
        functions.append(f.ed())
    if chances is not None:
        conditions = [c.ftn(chances)]
    if survives_explosion:
        conditions.append(c.se())
    entry = o.ie(without_shears, conditions, functions)
    e0 = o.ie(with_shears, c.alt([c.sh(), c.st()]) if use_silk_touch else c.sh())
    write(name, o.blt(o.dp(o.ae([e0, entry]))), res_block)


def only_shears(name, item=None, use_silk_touch=False):
    c0 = c.alt([c.sh(), c.st()]) if use_silk_touch else c.sh()
    write(name, o.blt(o.pl(o.ie(insni(item, name)), conditions=c0)), res_block)


def empty_entity(name):
    write(name, o.elt(), res_entity)


def fish(name, item=None, has_cooked_fish=True, bone_meal_chance=0.05):
    p0 = o.dp(o.ie(insni(item, name), functions=f.fs(c.eof()) if has_cooked_fish else f.sc(1.0)))
    p1 = o.pl(o.ie("minecraft:bone_meal", c.rc(bone_meal_chance)))
    write(name, o.elt([p0, p1]), res_entity)


def test():
    h.is_testing = True
    i = input("Testing Loot Table Creation\nFull parameters? [Y] / [N]\n")
    if i == "Y":
        pass
    elif i == "N":
        pass
    h.is_testing = False


if __name__ == "__main__":
    test()
