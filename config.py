import json

STREAK3 = "<a:streak3:1525696855890198530>"
STREAK10 = "<a:streak10:1525696853390135488>"
STREAK30 = "<a:streak50:1525696852341559306>"
STREAK100 = "<a:streak100:1525696854304493620>"
STREAK150_plus = "<a:streak150:1525696851137921144>"

## default_data

pf_default = {"KLT" : 0, "Streak":0, "last_time_streak": 0,"last_time_mess" : 0, "message_today":0,"today_mess_allow" : False}

## load and save

def load_json():
    with open("pf.json","r") as f:
        data = json.load(f)
    return data

def save_json(data):
    with open("pf.json", "w") as f:
        json.dump(data,f,indent=4)

## user data adder

def add_user(data, user_id : str):
    if user_id not in data: 
        data[user_id] = pf_default.copy()
    for k,v in pf_default.items(): 
        if k not in data[user_id]:
            data[user_id][k]= v

def streak_emoji_change(user_streak):

    emoji = None
    if user_streak > 150:
        emoji = STREAK150_plus
    elif user_streak >100:
        emoji = STREAK100
    elif user_streak >30:
        emoji = STREAK30
    elif user_streak >10:
        emoji = STREAK10
    else:
        emoji = STREAK3
    return emoji

## 

MAX_MESSAGE = 1

COINS = "<a:KLT_coin:1525697095993004174>"

VERIFY = "<:7verify7:1495226080695681164>"
CROSS = "<:7cross7:1495226068028883046>"



