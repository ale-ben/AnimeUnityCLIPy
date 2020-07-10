import json


def replace_characters(json_string):
    forbidden_chars = [{'old': '\n', 'new': '\u2424'}, {'old': '\/', 'new': '/'}]
    for char in forbidden_chars:
        json_string = str.replace(json_string, char['old'], char['new'])
    return json_string


def decode_json(json_str):
    json_str = replace_characters(json_str)
    obj_arr = json.loads(json_str)
    return obj_arr


def get_formatted_search_results(res_obj):
    for i in range(len(res_obj)):
        del res_obj[i]['user_id']
        for epI in range(len(res_obj[i]['episodes'])):
            del res_obj[i]['episodes'][epI]['user_id']
        res_obj[i]['anime_url'] = f"{res_obj[i]['id']}-{res_obj[i]['slug']}"
    return res_obj


def encode_json(res_obj):
    json_str = json.dumps(res_obj)
    return json_str
