import requests
from enums import League

def make_request(id, limit:int = 20, account:str = ''):
    """Sends request to the Path of Exile Ladder API and returns entries based on the
    parameters submitted

    :param id: name of the league
    :param limit: number of entries to include
    :param account: name of the account
    :return: returns requests.Reponse type based on request sent
    """

    if id == '':
        print("WARNING: Id cannot be empty.")
        return

    request = 'http://api.pathofexile.com/ladders/{}'.format(id.value)
    if limit != 20:
        request += "?limit={}".format(limit)
    if account != '':
        request += "{}accountName={}".format('&' if limit != 20 else '?', account)

    print(request)

    return requests.get(request)

def parse_ladder():
    pass

r = make_request(League.SSFHCFlashback, account="exdunn")
print(r.text)