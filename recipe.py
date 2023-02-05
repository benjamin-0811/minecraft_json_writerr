import helper as h
import json as j


def write(name, text):
    h.write(name, j.dumps(text, indent=2), h.Results.RECIPE)
