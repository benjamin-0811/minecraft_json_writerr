import helper as h
import json as j
import state_objects as o


def write(name, text):
    h.write(name, j.dumps(text, indent=2), h.Results.BLOCKSTATE)


def cube(name, rotated_y=False, rotated_xy=False, mirrored=False):
    """
    - rotated_y: concrete_powder, dirt, grass_path, sand
    - rotated_xy: netherrack
    - mirrored: stone, infested_stone, bedrock
    """
    if rotated_y:
        model = [o.mo(name), o.mo(name, y=90), o.mo(name, y=180), o.mo(name, y=270)]
    elif rotated_xy:
        model = []
        for i in range(4):
            for k in range(4):
                model.append(o.mo(name, o.deg[i], o.deg[k]))
        print(model)
        return
    elif mirrored:
        mir = "%s_mirrored" % name
        model = [o.mo(name), o.mo(mir), o.mo(name, y=180), o.mo(mir, y=180)]
    else:
        model = o.mo(name)
    write(name, o.vs(o.dv(model)))


def grass_block(name, snowy_block=None):
    m0 = [o.mo(name), o.mo(name, y=90), o.mo(name, y=180), o.mo(name, y=270)]
    if snowy_block is None:
        save_id = h.current_id
        h.current_id = "minecraft"
        m1 = o.mo("grass_block")
        h.current_id = save_id
    else:
        m1 = o.mo(snowy_block)
    write(name, o.vs([o.va("snowy=false", m0), o.va("snowy=true", m1)]))


def pillar(name, horizontal=True):
    """
    - examples: basalt, bone_block, chain, wood, crimson-/warped_stem, hyphae
    - horizontal: log, pillar, hay_block
    """
    homo = "%s_horizontal" % name if horizontal else name
    x = o.va("axis=x", o.mo(homo, 90, 90))
    y = o.va("axis=y", o.mo(name))
    z = o.va("axis=z", o.mo(homo, 90))
    write(name, o.vs([x, y, z]))


def orientable(name, north=0):
    """
    - north = 0: coral_wall_fan, jack_o_lantern, ladder, lectern, loom
    - north = 90: attached_melon/pumpkin_stem
    - north = 180: glazed_terracotta, anvil
    - north = 270: unused
    """
    n = o.va("facing=north", o.mo(name, y=h.right_angle(north)))
    e = o.va("facing=east", o.mo(name, y=h.right_angle(north + 90)))
    s = o.va("facing=south", o.mo(name, y=h.right_angle(north + 180)))
    w = o.va("facing=west", o.mo(name, y=h.right_angle(north + 270)))
    write(name, o.vs([e, n, s, w]))


def button(name):
    n = "%s_button" % name
    p = "%s_button_pressed" % name
    v = o.ss(["face", "facing", "powered"], [o.fc, o.fcn, o.bl])
    x = [180] * 8 + [0] * 8 + [90] * 8
    y = [270, 270, 180, 180, 0, 0, 90, 90] + [90, 90, 0, 0, 180, 180, 270, 270] * 2
    u = [False] * 16 + [True] * 8
    write(name, o.vs([o.va(v[i], o.mo(n if i % 2 == 0 else p, x[i], y[i], u[i])) for i in range(24)]))


def door(name):
    tl = "%s_door_top_left" % name
    tr = "%s_door_top_right" % name
    bl = "%s_door_bottom_left" % name
    br = "%s_door_bottom_right" % name
    tlo = "%s_door_top_left_open" % name
    tro = "%s_door_top_right_open" % name
    blo = "%s_door_bottom_left_open" % name
    bro = "%s_door_bottom_right_open" % name
    m = [bl, blo, br, bro, tl, tlo, tr, tro] * 4
    v = o.ss(["facing", "half", "hinge", "open"], [o.fcn, o.lu, o.si, o.bl])
    y = [0, 90, 0, 270] * 2 + [270, 0, 270, 180] * 2 + [90, 180, 90, 0] * 2 + [180, 270, 180, 90] * 2
    write("%s_door" % name, o.vs([o.va(v[i], o.mo(m[i], y=y[i])) for i in range(32)]))


def trapdoor(name):
    t = "%s_trapdoor_top" % name
    b = "%s_trapdoor_bottom" % name
    d = "%s_trapdoor_open" % name
    m = [b, d, t, d] * 4
    v = o.ss(["facing", "half", "open"], [o.fcn, o.bt, o.bl])
    x = [0, 0, 0, 180] * 4
    y = [90, 90, 90, 270, 0, 0, 0, 180, 180, 180, 180, 0, 270, 270, 270, 90]
    write("%s_trapdoor" % name, o.vs([o.va(v[i], o.mo(m[i], x[i], y[i])) for i in range(16)]))


def fence(name):
    fs = "%s_fence_side" % name
    n = o.pa({"north": True}, o.mo(fs, uv_lock=True))
    e = o.pa({"east": True}, o.mo(fs, y=90, uv_lock=True))
    s = o.pa({"south": True}, o.mo(fs, y=180, uv_lock=True))
    w = o.pa({"west": True}, o.mo(fs, y=270, uv_lock=True))
    write("%s_fence" % name, o.mp([o.dp(o.mo("%s_fence_post" % name)), n, e, s, w]))


def fence_gate(name):
    g = "%s_fence_gate" % name
    go = "%s_fence_gate_open" % name
    gw = "%s_fence_gate_wall" % name
    gwo = "%s_fence_gate_wall_open" % name
    m = [g, go, gw, gwo] * 4
    v = o.ss(["facing", "in_wall", "open"], [o.fcn, o.bl, o.bl])
    y = [270] * 4 + [180] * 4 + [0] * 4 + [90] * 4
    write("%s_fence_gate" % name, o.vs([o.va(v[i], o.mo(m[i], y=y[i], uv_lock=True)) for i in range(16)]))


def pressure_plate(name):
    u = o.va("powered=false", o.mo("%s_pressure_plate" % name))
    d = o.va("powered=true", o.mo("%s_pressure_plate_down" % name))
    write("%s_pressure_plate" % name, o.vs([u, d]))


def slab(name, double=None):
    b = o.va("type=bottom", o.mo("%s_slab" % name))
    d = o.va("type=double", o.mo(h.ntx(double, "%s_slab_double" % name)))
    t = o.va("type=top", o.mo("%s_slab_top" % name))
    write("%s_slab" % name, o.vs([b, d, t]))


def stairs(name):
    s = "%s_stairs" % name
    si = "%s_stairs_inner" % name
    so = "%s_stairs_outer" % name
    m = [si, si, so, so, s] * 8
    v = o.ss(["facing", "half", "shape"], [o.fcn, o.bl, o.st])
    x = ([0] * 5 + [180] * 5) * 4
    y_ = [270, 0, 270, 0, 0, 0, 90, 0, 90, 0, 180, 270, 180, 270, 270, 270, 0, 270, 0, 270]
    y = y_ + [0, 90, 0, 90, 90, 90, 180, 90, 180, 90, 90, 180, 90, 180, 180, 180, 270, 180, 270, 180]
    vs = [o.va(v[i], o.mo(m[i], x[i], y[i], uv_lock=bool(x[i] | y[i]))) for i in range(40)]
    write("%s_stairs" % name, o.vs(vs))


def wall(name):
    p = "%s_wall_post" % name
    s = "%s_wall_side" % name
    st = "%s_wall_side_tall" % name
    lo = [o.pa({o.cm[i]: "low"}, o.mo(s, y=o.deg[i], uv_lock=True)) for i in range(4)]
    t = [o.pa({o.cm[i]: "tall"}, o.mo(st, y=o.deg[i], uv_lock=True)) for i in range(4)]
    write("%s_wall" % name, o.mp([o.pa({"up": True}, o.mo(p))] + lo + t))


def rail(name, has_curves=True, can_be_powered=False):
    """
    - has_curves: rail
    - can_be_powered: activator_rail, detector_rail, powered_rail
    """
    n = "%s_rail" % name
    ne = "%s_rail_raised_ne" % name
    sw = "%s_rail_raised_sw" % name
    s = "%s_rail" % name
    neo = "%s_rail_on_raised_ne" % name
    swo = "%s_rail_on_raised_sw" % name
    so = "%s_rail_on" % name
    c = "%s_rail_corner" % name
    co = "%s_rail_on_corner" % name
    if has_curves:
        if can_be_powered:
            m0 = [o.mo(s, y=90), o.mo(c, y=270), o.mo(s), o.mo(c, y=180), o.mo(c), o.mo(c, y=90)]
            m1 = [o.mo(neo, y=90), o.mo(neo), o.mo(swo), o.mo(swo, y=90)]
            m2 = [o.mo(so, y=90), o.mo(co, y=270), o.mo(so), o.mo(co, y=180), o.mo(co), o.mo(co, y=90)]
            m = [o.mo(ne, y=90), o.mo(ne), o.mo(sw), o.mo(sw, y=90)] + m0 + m1 + m2
            sh = o.cr * 2
            p = [False] * 10 + [True] * 10
            write(n, o.vs([o.va("powered=%s,shape=%s" % (str(p[i]).lower(), sh[i]), m[i]) for i in range(20)]))
        else:
            mo = [o.mo(s, y=90), o.mo(c, y=270), o.mo(s), o.mo(c, y=180), o.mo(c), o.mo(c, y=90)]
            m = [o.mo(ne, y=90), o.mo(ne), o.mo(sw), o.mo(sw, y=90)] + mo
            write(n, o.vs([o.va("shape=%s" % o.cr[i], m[i]) for i in range(10)]))
    else:
        if can_be_powered:
            mo = [o.mo(neo, y=90), o.mo(neo), o.mo(swo), o.mo(swo, y=90), o.mo(so, y=90), o.mo(so)]
            m = [o.mo(ne, y=90), o.mo(ne), o.mo(sw), o.mo(sw, y=90), o.mo(s, y=90), o.mo(s)] + mo
            sh = o.ra * 2
            p = [False] * 6 + [True] * 6
            write(n, o.vs([o.va("powered=%s,shape=%s" % (str(p[i]).lower(), sh[i]), m[i]) for i in range(12)]))
        else:
            m = [o.mo(ne, y=90), o.mo(ne), o.mo(sw), o.mo(sw, y=90), o.mo(s, y=90), o.mo(s)]
            write(n, o.vs([o.va("shape=%s" % o.ra[i], m[i]) for i in range(6)]))


def glass_pane(name):
    p = "%s_pane_post" % name
    s = "%s_pane_side" % name
    sa = "%s_pane_side_alt" % name
    ns = "%s_pane_noside" % name
    nsa = "%s_pane_noside_alt" % name
    c_ = [o.ss(o.cm[i], [o.bla]) for i in range(4)]
    c = [c_[0][0], c_[1][0], c_[2][0], c_[3][0], c_[0][1], c_[1][1], c_[2][1], c_[3][1]]
    m = [[s, 0], [s, 90], [sa, 0], [sa, 90], [ns, 0], [nsa, 0], [nsa, 90], [ns, 270]]
    write("%s_pane" % name, o.mp([o.dp(o.mo(p))] + [o.pa(c[i], o.mo(m[i][0], y=m[i][1])) for i in range(8)]))


def furnace(name):
    c = m = []
    for i in range(4):
        c = c + ["facing=%s,lit=false" % o.fcn[i], "facing=%s,lit=true" % o.fcn[i]]
        m = m + [o.mo(name, y=o.da1[i]), o.mo("%s_on" % name, y=o.da1[i])]
    write(name, o.vs([o.va(c[i], m[i]) for i in range(8)]))


def crop(name, age=8):
    write(name, o.vs([o.va("age=%d" % i, o.mo("%s_stage%d" % (name, i))) for i in range(age)]))


def torch(name, can_be_off=False):
    """
    - examples: torch, soul_torch
    - can_be_off: redstone_torch
    """
    on = "%s_torch" % name
    won = "%s_wall_torch" % name
    if can_be_off:
        off = "%s_torch_off" % name
        woff = "%s_wall_torch_off" % name
        write(on, o.vs([o.va("lit=false", o.mo(off)), o.va("lit=true", o.mo(on))]))
        c = o.ss(["facing", "lit"], [o.fcn, o.bl])
        v = []
        for i in range(4):
            v.append(o.va(c[i * 2], o.mo(woff, o.da2[i])))
            v.append(o.va(c[i * 2 + 1], o.mo(won, o.da2[i])))
        write(won, o.vs(v))
    else:
        cube(on)
        c = o.ss(["facing"], [o.fcn])
        write(won, o.vs([o.va(c[i], o.mo(won, o.da2[i])) for i in range(4)]))


def tall_block(name):
    write(name, o.vs([o.va("half=lower", o.mo("%s_bottom" % name)), o.va("half=upper", o.mo("%s_top" % name))]))


def lantern(name):
    v = [o.va("hanging=false", o.mo("%s_lantern" % name)), o.va("hanging=true", o.mo("%s_lantern_hanging" % name))]
    write("%s_lantern" % name, o.vs(v))


def campfire(name):
    save_id = h.current_id
    h.current_id = "minecraft"
    off = [o.mo("campfire_off", y=o.da0[i]) for i in range(4)]
    h.current_id = save_id
    c = m = []
    for i in range(4):
        c = c + ["facing=%s,lit=false" % o.fcn[i], "facing=%s,lit=true" % o.fcn[i]]
        m = m + [off[i], o.mo("%s_campfire" % name, y=o.da0[i])]
    write("%s_campfire" % name, o.vs([o.va(c[i], m[i]) for i in range(8)]))


def fire(name, below_block=True):
    """
    - examples: soul_fire
    - below_block: fire
    """
    n = "%s_fire" % name
    f0 = "%s_floor0" % n
    f1 = "%s_floor1" % n
    s0 = "%s_side0" % n
    s1 = "%s_side1" % n
    sa0 = "%s_side_alt0" % n
    sa1 = "%s_side_alt1" % n
    if below_block:
        u0 = "%s_up0" % n
        u1 = "%s_up1" % n
        ua0 = "%s_up_alt0" % n
        ua1 = "%s_up_alt1" % n
        c = {"up": False, "west": False, "east": False, "south": False, "north": False}
        p = o.pa(c, [f0, f1])
        for i in range(4):
            d = o.deg[i]
            p.append(o.pa([{o.cm[i]: True}, c], [o.mo(s0, y=d), o.mo(s1, y=d), o.mo(sa0, y=d), o.mo(sa1, y=d)]))
        p.append(o.pa({"up": True}, [o.mo(u0), o.mo(u1), o.mo(ua0), o.mo(ua1)]))
        write(n, o.mp([p[i] for i in range(6)]))
    else:
        p = o.dp([f0, f1])
        for i in range(4):
            d = o.deg[i]
            p.append(o.dp([o.mo(s0, y=d), o.mo(s1, y=d), o.mo(sa0, y=d), o.mo(sa1, y=d)]))
        write(n, o.mp([p[i] for i in range(5)]))


def mushroom_block(name, unique_inside=False, is_stem=False):
    n = "%s_mushroom_stem" % name if is_stem else "%s_mushroom_block" % name
    x = [0] * 4 + [270, 90]
    y = o.deg + [0] * 2
    u = [False] + [True] * 5
    p = [o.pa({o.dr[i]: True}, o.mo(n, x[i], y[i], u[i])) for i in range(6)]
    if unique_inside:
        save_id = h.current_id
        h.current_id = "minecraft"
        p0 = [o.pa({o.dr[i]: False}, o.mo("mushroom_block_inside", x[i], y[i], u[i])) for i in range(6)]
        h.current_id = save_id
    else:
        p0 = [o.pa({o.dr[i]: False}, o.mo("%s_mushroom_block_inside" % name, x[i], y[i], u[i])) for i in range(6)]
    write(n, o.mp(p + p0))


def cauldron(name, has_levels=True):
    """
    - examples: lava_cauldron
    - has_levels: water_cauldron
    """
    if has_levels:
        l1 = o.va("level=1", o.mo("%s_cauldron_level1" % name))
        l2 = o.va("level=2", o.mo("%s_cauldron_level2" % name))
        f = o.va("level=3", o.mo("%s_cauldron_full" % name))
        write("%s_cauldron" % name, o.vs([l1, l2, f]))
    else:
        cube("%s_cauldron" % name)


def test():
    h.is_testing = True
    i = input("Testing Blockstate Creation\nFull parameters? [Y] / [N]\n")
    if i == "Y":
        cube("xx", mirrored=True)
        grass_block("xx", "yy")
        pillar("xx", True)
        orientable("xx", 0)
        button("xx")
        door("xx")
        trapdoor("xx")
        fence("xx")
        fence_gate("xx")
        pressure_plate("xx")
        slab("xx", "yy")
        stairs("xx")
        wall("xx")
        rail("xx", True, True)
        glass_pane("xx")
        furnace("xx")
        crop("xx", 4)
        torch("xx", True)
        tall_block("xx")
        lantern("xx")
        campfire("xx")
        fire("xx", True)
        mushroom_block("xx", True, False)
        cauldron("xx", False)
    elif i == "N":
        cube("xx")
        grass_block("xx")
        pillar("xx")
        orientable("xx")
        button("xx")
        door("xx")
        trapdoor("xx")
        fence("xx")
        fence_gate("xx")
        pressure_plate("xx")
        slab("xx")
        stairs("xx")
        wall("xx")
        rail("xx")
        glass_pane("xx")
        furnace("xx")
        crop("xx")
        torch("xx")
        tall_block("xx")
        lantern("xx")
        campfire("xx")
        fire("xx")
        mushroom_block("xx")
        cauldron("xx")
    h.is_testing = False


if __name__ == "__main__":
    test()
