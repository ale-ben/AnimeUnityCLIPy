import logging_aux


@logging_aux.logger_wraps()
def get_formatted_search_results(res_obj):
    for i in range(len(res_obj)):
        del res_obj[i]['user_id']
        for epI in range(len(res_obj[i]['episodes'])):
            del res_obj[i]['episodes'][epI]['user_id']
        res_obj[i]['anime_url'] = f"{res_obj[i]['id']}-{res_obj[i]['slug']}"
    return res_obj


@logging_aux.logger_wraps()
def get_selected_anime_obj_by_id(search_res, id=None):
    for res in search_res:
        if str(res['id']) == id:
            return res
    return search_res[0]


def get_year(entry):
    return entry['date']


def order_search_res(search_res):
    search_res.sort(key=get_year)
    return search_res
