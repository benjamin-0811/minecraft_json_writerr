import helper as h


def furnace_like(ingredient, result, exp, duration, recipe_type, group):
    pass


def furnace(ingredient, result, exp, duration, group):
    return furnace_like(ingredient, result, exp, duration, "smelting", group)


def blasting(ingredient, result, exp, duration, group):
    return furnace_like(ingredient, result, exp, duration, "blasting", group)


def smoking(ingredient, result, exp, duration, group):
    return furnace_like(ingredient, result, exp, duration, "smoking", group)


def campfire_cooking(ingredient, result, exp, duration, group):
    return furnace_like(ingredient, result, exp, duration, "campfire", group)


def shapeless_crafting():
    pass


def shaped_crafting():
    pass


def stonecutting():
    pass


def smithing():
    pass
