import requests
import json
from enums import League

def make_request(id, account = None, ascendancy = None, limit = None):
    """Sends request to the Path of Exile Ladder API and returns entries based on the
    parameters submitted

    :param id: name of the league
    :param limit: number of entries to include
    :param account: name of the account
    :return: returns requests.Reponse type based on request sent
    """

    if id is None:
        print("WARNING: Id cannot be empty.")
        return

    print(League.map_enum_to_str(id))
    request = 'http://api.pathofexile.com/ladders/{}?'.format(League.map_enum_to_str(id))

    if account is not None:
        request += "accountName={}&".format(account)
    if limit is not None:
        request += "limit={}&".format(limit)
    # if limit != 20:
    #     request += "?limit={}".format(limit)
    # if account != '':
    #     request += "{}accountName={}".format('&' if limit != 20 else '?', account)

    print(request)

    return requests.get(request)

def parse_response(reponse):
    """Parse JSON string response from Path of Exile ladder API

    :param response: JSON string response returned by GET request to PoE Ladder API
    :return: dictionary of accounts
    """
    data = json.loads(reponse.text)

    # print("******************PARSING REQUEST**********************")
    # for entry in data["entries"]:
    #     print("{} the level {} {} ({})".
    #           format(entry["character"]["name"],
    #                  entry["character"]["level"],
    #                  entry["character"]["class"],
    #                  "Dead" if entry["dead"] else "Alive"))

    return data['entries']

# r = make_request(Lea, limit=20)
# print(r)
# parse_response(r)