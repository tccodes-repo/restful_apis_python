import requests

URLBASE = "https://api.groupme.com/v3"

def make_group(token, name):
        group_id = None
        params = {"token": token}
        payload ={"name": name} 
        headers = {"content-type": "application/json"}
        url = URLBASE + "/groups"
        
        r = requests.post(url, headers=headers, params=params, json=payload)
        if r.status_code != 201:
            raise Exception("Bad request. Unable to create group. " + r.text)
        else:
            group = r.json()["response"]
            group_id = group["id"]
        return group_id

def make_bot(group_id):
    bot_id = None
    payload = {"bot":{"name":"me", "group_id":group_id }}
    headers = {"content-type": "application/json"}
    params = {"token": TOKEN}
    url = URLBASE + "/bots"

    r = requests.post(url, headers=headers, params=params, json=payload)
    if r.status_code != 201:
        raise Exception("Bad request. Unable to create bot. " + r.text)
    else:
        bot = r.json()["response"]["bot"]
        bot_id = bot["bot_id"]
    return bot_id

def send_message(bot_id, message):
        
    payload = {"bot_id":bot_id, "text": message}
    headers = {"content-type": "application/json"}
    params = {"token": TOKEN}
    url = URLBASE + "/bots/post"

    r = requests.post(url, headers=headers, params=params, json=payload)
    if r.status_code != 202:
        raise Exception("Unable to post message")
    

if __name__ == "__main__":
    TOKEN = ""
    grp_id = make_group(TOKEN, "test_group")
    b_id = make_bot(grp_id)
    send_message(b_id, "Just testing GroupMe's REST API.")
    print("Done")