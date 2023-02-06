import helper as h
import itertools as it


boolean = [False, True]
boolean_alt = [True, False]
compass = ["north", "east", "south", "west"]
directions = compass + ["up", "down"]
facing = sorted(compass)
face = ["ceiling", "floor", "wall"]
side = ["left", "right"]
axis = ["x", "y", "z"]
rail = ["ascending_east", "ascending_north", "ascending_south", "ascending_west", "east_west", "north_south"]
curved_rail = sorted(rail + ["north_east", "north_west", "south_east", "south_west"])
slab = ["bottom", "double", "top"]
bottom_top = ["bottom", "top"]
stair = ["inner_left", "inner_right", "outer_left", "outer_right", "straight"]
lower_upper = ["lower", "upper"]
degrees = [0, 90, 180, 270]
degrees_alt0 = [270, 180, 0, 90]
degrees_alt1 = degrees_alt0.copy()
degrees_alt1.reverse()
degrees_alt2 = [270, 0, 90, 180]

bl = boolean
bla = boolean_alt
cm = compass
dr = directions
fcn = facing
fc = face
si = side
ax = axis
ra = rail
cr = curved_rail
sl = slab
bt = bottom_top
st = stair
lu = lower_upper
deg = degrees
da0 = degrees_alt0
da1 = degrees_alt1
da2 = degrees_alt2


def snbm(name):
    return h.texpath(name, h.current_id, "block")


def variants(var_list):
    """
    - a model for each state
    - var_list: dict or list[dict]
    - use variant() for var_list
    """
    return {"variants": h.ml(var_list)}


def variant(a_state, a_model):
    """
    - state: str, string representation of a blocks state
    - a_model: dict or list[dict]
    - use model() for a_model
    """
    return {"" if a_state is None else a_state: a_model}


def default_variant(a_model):
    """
    - variant() without a state (no requirements)
    - a_model: dict or list[dict]
    - use model() for a_model
    """
    return variant(None, a_model)


def multipart(parts):
    """
    - multiple models combined into one
    - parts: dict or list[dict]
    - use part() for parts
    """
    return {"multipart": h.ml(parts)}


def part(a_state, a_model):
    """
    - state: dict or list[dict]
    - a_model: dict or list[dict]
    - use model() for a_model
    """
    text = {}
    if a_state is not None:
        text["when"] = {"OR": a_state} if isinstance(a_state, list) else a_state
    text["apply"] = a_model
    return text


def default_part(a_model):
    """
    - part() without a state (no requirements)
    - a_model: dict or list[dict]
    - use model() for a_model
    """
    return part(None, a_model)


def model(a_model, x=0, y=0, uv_lock=False, weight=None):
    """
    - block model
    - use weight only when making a list of models
    """
    text = {"model": snbm(a_model)}
    if y != 0:
        text["y"] = y
    if x != 0:
        text["x"] = x
    if uv_lock:
        text["uv_lock"] = True
    h.innatd(text, "weight", weight)
    return text


def states(keys, values):
    """
    - makes a list of all possible states
    - keys: list of keys
    - values: list of list with all possible state values
    """
    keys = h.ml(keys)
    values = h.ml(values)
    if keys is None or values is None:
        return None
    length = len(keys)
    if length != len(values):
        return None
    text = []
    combs = list(it.product(*values))
    for i in range(len(combs)):
        d = {}
        for j in range(length):
            d[keys[j]] = combs[i][j]
        text.append(state(d))
    return text


def state(a_state):
    """
    - a_state: dict with all the variables
    """
    text = ""
    keys = list(a_state.keys())
    values = list(a_state.values())
    length = len(a_state)
    for i in range(length - 1):
        text = text + "%s=%s," % (keys[i], state_value(values[i]))
    text = text + "%s=%s" % (keys[length - 1], state_value(values[length - 1]))
    return text


def state_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, str):
        return value
    else:
        return None


vs = variants
va = variant
dv = default_variant
mp = multipart
pa = part
dp = default_part
mo = model
ss = states
stt = state
sv = state_value


if __name__ == "__main__":
    print(state({"kk": "ky", "ll": "ly", "mm": "my", "b0": False, "b1": True}))
    print(states(["a", "b"], [["1", "2"], ["_", "?"]]))
    print(states(["face", "facing", "powered"], [face, facing, boolean]))
    print(curved_rail)
