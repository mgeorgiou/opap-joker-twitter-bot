import opap
import requests, json

url = "https://api.opap.gr"

def get_opap_last_draw():
    return opap.get_last_draw("joker")

def get_last_joker_draw():
    gameid = opap.get_draw_id("joker")
    surl = url + "/draws/v3.0/" + gameid + "/last-result-and-active"

    resp = requests.get(surl)
    j = resp.text
    jdata = json.loads(j)

    response_model = {
        "winningNumbers" : list(jdata["last"]["winningNumbers"]["list"]),
        "bonusNumber"    : int(jdata["last"]["winningNumbers"]["bonus"][0]),
        "drawTime"       : int(jdata["last"]["drawTime"]),
        "drawId"         : int(jdata["last"]["drawId"])
    }

    return response_model
