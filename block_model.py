import helper as h
import json as j
import model_objects as o


def write(name, parent, ambient_occlusion=True, keys=None, values=None):
    h.write(name, j.dumps(o.cbm(parent, ambient_occlusion, keys, values), indent=2), h.Results.BLOCK_MODEL)


def cube(name, texture=None, mirrored=False):
    """
    - texture = name
    """
    p = (True, "all", texture or name)
    write(name, "cube_all", *p)
    if mirrored:
        write(f"{name}_mirrored", "cube_mirrored_all", *p)


def column(name, side=None, top=None, is_horizontal=False):
    """
    - side = name
    - top = name + "top"
    - examples: log, pillar, ancient_debris, blackstone, bookshelf, etc.
    """
    c = "cube_column"
    write(name, f"{c}_horizontal" if is_horizontal else c, True, ["end", "side"], [top or f"{name}_top", side or name])


def pillar(name, side=None, top=None):
    """
    - normal and horizontal column.
    - side = name
    - top = name + "top"
    - examples: log, pillar, hay_block
    """
    p = (side or name, top or f"{name}_top")
    column(name, *p, False)
    column(f"{name}_horizontal", *p, True)


def bottom_top(name, side=None, top=None, bottom=None):
    """
    - side == name
    - top = name + "top"
    - bottom = name + "bottom"
    - examples: barrel, nylium, grass_block_snow, mycelium, piston_inventory, etc.
    """
    v = [bottom or f"{name}_bottom", side or name, top or f"{name}_top"]
    write(name, "cube_bottom_top", True, ["bottom", "side", "top"], v)


def stairs(name, side=None, top=None, bottom=None):
    """
    - name without "stairs"
    - side = name
    - top = name
    - bottom = name
    """
    s = f"{name}_stairs"
    p = (True, ["bottom", "side", "top"], [bottom or name, side or name, top or name])
    write(s, "stairs", *p)
    write(f"{s}_inner", "inner_stairs", *p)
    write(f"{s}_outer", "outer_stairs", *p)


def slab(name, side=None, top=None, bottom=None):
    """
    - name without "slab"
    - side = name
    - top = name
    - bottom = name
    """
    s = f"{name}_slab"
    p = (True, ["bottom", "side", "top"], [bottom or name, side or name, top or name])
    write(s, "slab", *p)
    write(f"{s}_top", "slab_top", *p)


def fence(name, texture=None):
    """
    - name without "fence"
    - texture = name
    """
    f = f"{name}_fence"
    p = (True, "texture", texture or name)
    write(f"{f}_inventory", "fence_inventory", *p)
    write(f"{f}_post", "fence_post", *p)
    write(f"{f}_side", "fence_side", *p)


def fence_gate(name, texture=None):
    """
    - name without "fence_gate"
    - texture = name
    """
    f = f"{name}_fence_gate"
    p = (True, "texture", texture or name)
    tmpl = "template_fence_gate"
    write(f, tmpl, *p)
    write(f"{f}_open", f"{tmpl}_open", *p)
    write(f"{f}_wall", f"{tmpl}_wall", *p)
    write(f"{f}_wall_open", f"{tmpl}_wall_open", *p)


def pressure_plate(name, texture=None):
    """
    - name without "pressure_plate"
    - texture = name
    """
    pp = f"{name}_pressure_plate"
    p = (True, "texture", texture or name)
    tmpl = "pressure_plate"
    write(pp, f"{tmpl}_up", *p)
    write(f"{pp}_down", f"{tmpl}_down", *p)


def button(name, texture=None):
    """
    - name without "button"
    - texture = name
    """
    b = f"{name}_button"
    p = (True, "texture", texture or name)
    write(b, "button", *p)
    write(f"{b}_inventory", "button_inventory", *p)
    write(f"{b}_pressed", "button_pressed", *p)


def door(name, top=None, bottom=None):
    """
    - name without "door"
    - top = name + "door_top"
    - bottom = name + "door_bottom"
    """
    d = f"{name}_door"
    b = f"{d}_bottom"
    t = f"{d}_top"
    p = (True, ["bottom", "top"], [bottom or b, top or t])
    write(f"{b}_left", "door_bottom_left", *p)
    write(f"{b}_left_open", "door_bottom_left_open", *p)
    write(f"{b}_right", "door_bottom_right", *p)
    write(f"{b}_right_open", "door_bottom_right_open", *p)
    write(f"{t}_left", "door_top_left", *p)
    write(f"{t}_left_open", "door_top_left_open", *p)
    write(f"{t}_right", "door_top_right", *p)
    write(f"{t}_right_open", "door_top_right_open", *p)


def trapdoor(name, texture=None):
    """
    - name without "trapdoor"
    - texture = name + "trapdoor"
    """
    t = f"{name}_trapdoor"
    p = (True, "texture", texture or t)
    tmpl = "template_orientable_trapdoor"
    write(f"{t}_top", f"{tmpl}_top", *p)
    write(f"{t}_bottom", f"{tmpl}_bottom", *p)
    write(f"{t}_open", f"{tmpl}_open", *p)


def wall(name, texture=None):
    """
    - name without "wall"
    - texture = name
    """
    w = f"{name}_wall"
    p = (True, "wall", texture or name)
    tmpl = "template_wall"
    write(f"{w}_inventory", "wall_inventory", *p)
    write(f"{w}_post", f"{tmpl}_post", *p)
    write(f"{w}_side", f"{tmpl}_side", *p)
    write(f"{w}_side_tall", f"{tmpl}_side_tall", *p)


def leaves(name, texture=None):
    """
    - name without "leaves"
    - texture = name + "leaves"
    """
    write(f"{name}_leaves", "leaves", True, "all", texture or f"{name}_leaves")


def particle(name, texture):
    """
    - examples: sign, banner, barrier, bed, shulker_box, chests, etc.
    """
    write(name, None, True, "particle", texture)


def cross(name, texture=None, tinted=False):
    """
    - texture = name
    - examples: sapling, flower, coral, cobweb, mushroom, fungus, etc.
    - tinted: bamboo_sapling, fern, grass, kelp, sugar_cane, etc.
    """
    write(name, "tinted_cross" if tinted else "cross", True, "cross", texture or name)


def stem_fruit(name, stem=None, attached=None):
    """
    - name without "stem"
    - stem = name + "stem"
    - attached = "attached" + name + "stem"
    - examples: pumpkin_plant, melon_plant
    """
    s = f"{name}_stem"
    a = f"attached_{s}"
    stem = stem or s
    write(a, "stem_fruit", True, ["stem", "upperstem"], [stem, attached or a])
    for i in range(8):
        write(f"{s}_stage{i}", f"stem_growth{i}", True, "stem", stem)


def glass_pane(name, pane=None, edge=None):
    """
    - name without "glass_pane"
    - pane = name + "glass_pane"
    - edge = name + "glass_pane_top"
    """
    pane = pane or name
    p = f"{name}_pane"
    p1 = (True, ["edge", "pane"], [edge or f"{p}_top", pane])
    p2 = (True, "pane", pane)
    tmpl = "template_glass_pane"
    write(f"{p}_post", f"{tmpl}_post", *p1)
    write(f"{p}_side", f"{tmpl}_side", *p1)
    write(f"{p}_side_alt", f"{tmpl}_side_alt", *p1)
    write(f"{p}_noside", f"{tmpl}_noside", *p2)
    write(f"{p}_noside_alt", f"{tmpl}_noside_alt", *p2)


def rail(name, texture=None, has_curves=True, can_be_powered=False):
    """
    - name without "rail"
    - texture = name + "rail"
    - has_curves: rail
    - can_be_powered: activator_rail, detector_rail, powered_rail
    """
    texture = texture or f"{name}_rail"
    r = f"{name}_raised"
    p1 = (True, "rail")
    p2 = (*p1, texture)
    tmpl = "template_rail_raised"
    write(name, "rail_flat", *p2)
    write(f"{r}_ne", f"{tmpl}_ne", *p2)
    write(f"{r}_sw", f"{tmpl}_sw", *p2)
    if has_curves:
        write(f"{name}_corner", "rail_curved", *p1, values=f"{texture}_corner")
    if can_be_powered:
        rail(f"{name}_on", f"{texture}_on", has_curves, False)


def crop(name, texture=None, stages=8):
    """
    - texture = name
    - examples (stages): carrot (4), nether_wart (3), wheat (8), etc.
    """
    texture = texture or name
    for i in range(stages):
        write(f"{name}_stage{i}", "crop", True, "crop", f"{texture}_stage{i}")


def carpet(name, texture=None):
    """
    - texture = name + "carpet"
    """
    c = f"{name}_carpet"
    write(c, "carpet", True, "wool", texture or c)


def single_face(name, texture=None, ambient_occlusion=True):
    """
    - texture = name
    - examples: mushroom_block, mushroom_stem
    """
    write(name, "template_single_face", ambient_occlusion, "texture", texture or name)


def mushroom(name, texture=None, unique_stem=False, unique_inside=False):
    """
    - mushroom related blocks
    - texture = name
    """
    texture = texture or name
    cross(name, texture, False)
    b = f"{texture}_block"
    single_face(f"{name}_block", b, True)
    cube(f"{name}block_inventory", b, False)
    if unique_stem:
        s = f"{texture}_stem"
        single_face(f"{name}_stem", s, True)
        cube(f"{name}_stem_inventory", s, False)
    if unique_inside:
        single_face(f"{name}_block_inside", f"{b}inside", False)


def double_cross(name, texture=None, tinted=False):
    """
    - texture = name
    - examples: rose_bush, peony, lilac
    - tinted: large_fern, tall_grass
    """
    texture = texture or name
    cross(f"{name}_top", f"{texture}_top", tinted)
    cross(f"{name}_bottom", f"{texture}_bottom", tinted)


def potted_plant(name, texture=None, tinted=False):
    """
    - name without "potted"
    - texture = name
    - examples: potted_flower, potted_sapling
    - tinted: potted_fern
    """
    p = "flower_pot_cross"
    write(f"potted_{name}", f"tinted_{p}" if tinted else p, True, "plant", texture or name)


def torch(name, texture=None, can_be_off=False):
    """
    - name without "torch"
    - texture = name + "torch"
    - examples: torch, soul_torch
    - can_be_off: redstone_torch
    """
    t = f"{name}_torch"
    w = f"{name}_wall_torch"
    p = [True, "torch", texture or f"{name}_torch"]
    tmpl = "template_torch"
    tw = f"{tmpl}_wall"
    write(t, tmpl, *p)
    write(w, tw, *p)
    if can_be_off:
        p[2] = f"{texture}_off"
        write(f"{t}_off", tmpl, *p)
        write(f"{w}_off", tw, *p)


def orientable(name, side=None, front=None, top=None, bottom=None, on_off=False, with_bottom=False, vertical=False):
    """
    - side = name + "side"
    - front = name + "front"
    - top = name + "top"
    - bottom = name + "bottom"
    - examples: carved_pumpkin, jack_o_lantern
    - on_off: blast_furnace, furnace, smoker
    - with_bottom: bee_nest, bee_hive, loom
    - vertical: dispenser, dropper
    """
    top = top or f"{name}_top"
    front = front or f"{name}_front"
    side = side or f"{name}_side"
    if with_bottom:
        bottom = bottom or f"{name}_bottom"
        keys = ["bottom", "front", "side", "top"]
        write(name, "orientable_with_bottom", True, keys, [bottom, front, side, top])
        if on_off:
            write(f"{name}_on", "orientable_with_bottom", True, keys, [bottom, f"{front}_on", side, top])
    else:
        keys = ["front", "side", "top"]
        write(name, "orientable", True, keys, [front, side, top])
        if on_off:
            write(f"{name}_on", "orientable", True, keys, [f"{front}_on", side, top])
    if vertical:
        keys = ["front", "side"]
        write(f"{name}_vertical", "orientable_vertical", True, keys, [f"{front}_vertical", side])
        if on_off:
            write(f"{name}_vertical_on", "orientable_vertical", True, keys, [f"{front}_vertical_on", side])


def campfire(name, fire=None, log=None):
    """
    - name without "campfire"
    - fire = name + "campfire_fire"
    - log = name + "campfire_log_lit"
    """
    c = f"{name}_campfire"
    write(c, "template_campfire", True, ["fire", "lit_log"], [fire or f"{c}_fire", log or f"{c}_log_lit"])


def lantern(name, texture=None):
    """
    - name without "lantern"
    - texture = name + "lantern"
    """
    n = f"{name}_lantern"
    p = (True, "lantern", texture or n)
    write(n, "template_lantern", *p)
    write(f"{n}_hanging", "template_hanging_lantern", *p)


def fire_block(name, texture_0=None, texture_1=None, below_block=True):
    """
    - name without "fire"
    - texture_0 = name + "fire_0"
    - texture_1 = name + "fire_1"
    - example: soul_fire
    - below_block: fire
    """
    f = f"{name}_fire"
    tmpl = "template_fire"
    p0 = (True, "fire", texture_0 or f"{f}_0")
    p1 = (True, "fire", texture_1 or f"{f}_1")
    write(f"{f}_floor0", f"{tmpl}_floor", *p0)
    write(f"{f}_floor1", f"{tmpl}_floor", *p1)
    write(f"{f}_side0", f"{tmpl}_side", *p0)
    write(f"{f}_side1", f"{tmpl}_side", *p1)
    write(f"{f}_side_alt0", f"{tmpl}_side_alt", *p0)
    write(f"{f}_side_alt1", f"{tmpl}_side_alt", *p1)
    if below_block:
        write(f"{f}_up0", f"{tmpl}_up", *p0)
        write(f"{f}_up1", f"{tmpl}_up", *p1)
        write(f"{f}_up_alt0", f"{tmpl}_up_alt", *p0)
        write(f"{f}_up_alt1", f"{tmpl}_up_alt", *p1)


def fire_set(name, below_block=True, torch_on_off=False):
    """
    - fire related blocks
    """
    fire_block(name, below_block=below_block)
    torch(name, can_be_off=torch_on_off)
    lantern(name)
    campfire(name)


def wood_set(name):
    """
    - wood related blocks
    """
    lo = f"{name}_log"
    ls = f"stripped_{lo}"
    w = f"{name}_wood"
    s = f"{name}_sapling"
    p = f"{name}_planks"
    pillar(lo)
    column(w, lo, lo)
    pillar(ls)
    column(f"stripped_{w}", ls, ls)
    leaves(name)
    cross(s)
    cube(p)
    stairs(name, p, p, p)
    slab(name, p, p, p)
    fence(name, p)
    fence_gate(name, p)
    door(name)
    trapdoor(name)
    button(name, p)
    pressure_plate(name, p)
    particle(f"{name}_sign", p)
    potted_plant(s)


def coral(name, texture=None, fan=None, block=None, dead=None, dead_fan=None, dead_block=None):
    """
    - name without "coral"
    - texture = name + "coral"
    - fan = name + "coral_fan"
    - block = name + "coral_block"
    - dead = "dead" + name + "coral"
    - dead_fan = "dead" + name + "coral_fan"
    - dead_block = "dead" + name + "coral_block"
    """
    c = f"{name}_coral"
    d = f"dead_{c}"
    fan = fan or f"{c}_fan"
    dead_fan = dead_fan or f"{d}_fan"
    p = [True, "fan", fan]
    cross(c, texture or c)
    write(f"{c}_fan", "coral_fan", *p)
    write(f"{c}_wall_fan", "coral_wall_fan", *p)
    cube(f"{c}_block", block or f"{c}_block")
    p[2] = dead_fan
    cross(d, dead or d)
    write(f"{d}_fan", "coral_fan", *p)
    write(f"{d}_wall_fan", "coral_wall_fan", *p)
    cube(f"{d}_block", dead_block or f"{d}_block")


def fluid(name, texture=None, has_levels=False):
    """
    - texture = name + "still"
    - examples: lava_cauldron, powder_snow_cauldron
    - has_levels: water_cauldron
    """
    texture = texture or f"{name}_still"
    k = ["bottom", "content", "inside", "particle", "side", "top"]
    c = "cauldron"
    s = o.smbm(f"{c}_side")
    v = [o.smbm(f"{c}_bottom"), o.snbm(texture), o.smbm(f"{c}_inner"), s, s, o.smbm(f"{c}_top")]
    textures = o.ct(k, v)
    particle(name, texture)
    res = h.Results.BLOCK_MODEL
    c = f"{name}_cauldron"
    p = (True, textures)
    tmpl = "template_cauldron"
    if has_levels:
        h.write(f"{c}_level1", j.dumps(o.cm(f"{tmpl}_level1", *p), indent=2), res)
        h.write(f"{c}_level2", j.dumps(o.cm(f"{tmpl}_level2", *p), indent=2), res)
        h.write(f"{c}_full", j.dumps(o.cm(f"{tmpl}_full", *p), indent=2), res)
    else:
        h.write(c, j.dumps(o.cm(f"{tmpl}_full", *p), indent=2), res)


def test():
    h.is_testing = True
    i = input("Testing Block Model Creation\nFull parameters? [Y] / [N]\n")
    if i == "Y":
        cube("xx", "yy", True)
        pillar("xx", "yy", "zz")
        bottom_top("xx", "yy", "zz", "uu")
        stairs("xx", "yy", "zz", "uu")
        slab("xx", "yy", "zz", "uu")
        fence("xx", "yy")
        fence_gate("xx", "yy")
        pressure_plate("xx", "yy")
        button("xx", "yy")
        door("xx", "yy", "zz")
        trapdoor("xx", "yy")
        wall("xx", "yy")
        leaves("xx", "yy")
        particle("xx", "yy")
        cross("xx", "yy", True)
        stem_fruit("xx", "yy", "zz")
        glass_pane("xx", "yy", "zz")
        rail("xx", "yy", True, True)
        crop("xx", "yy", 6)
        carpet("xx", "yy")
        single_face("xx", "yy", True)
        mushroom("xx", "yy", True, True)
        double_cross("xx", "yy", True)
        potted_plant("xx", "yy", True)
        torch("xx", "yy", True)
        orientable("xx", "yy", "zz", "uu", "vv", True, True, True)
        campfire("xx", "yy", "zz")
        lantern("xx", "yy")
        fire_block("xx", "yy", "zz", True)
        fire_set("xx", True, True)
        wood_set("xx")
        coral("xx", "yy", "zz", "uu", "dyy", "dzz", "duu")
        fluid("xx", "yy", True)
    elif i == "N":
        cube("xx")
        pillar("xx")
        bottom_top("xx")
        stairs("xx")
        slab("xx")
        fence("xx")
        fence_gate("xx")
        pressure_plate("xx")
        button("xx")
        door("xx")
        trapdoor("xx")
        wall("xx")
        leaves("xx")
        particle("xx", "yy")
        cross("xx")
        stem_fruit("xx")
        glass_pane("xx")
        rail("xx")
        crop("xx")
        carpet("xx")
        single_face("xx")
        mushroom("xx")
        double_cross("xx")
        potted_plant("xx")
        torch("xx")
        orientable("xx")
        campfire("xx")
        lantern("xx")
        fire_block("xx")
        fire_set("xx")
        wood_set("xx")
        coral("xx")
        fluid("xx")
    h.is_testing = False


if __name__ == "__main__":
    test()
