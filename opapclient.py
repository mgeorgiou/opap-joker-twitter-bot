import opap

url = "https://api.opap.gr/"

def get_opap_last_draw():
    return opap.get_last_draw("joker")
