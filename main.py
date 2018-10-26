# coding: utf-8
import sys
import settings
import requests
import json
import datetime
import os
import yaml

# 変数定義
URL = "https://api.clashroyale.com/v1"
ACCESS_KEY = settings.ACCESS_KEY
TARGET_API = URL+"/players/"
HEADERS = {
    "content-type": "application/json; charset=utf-8",
    "cache-control": "max-age=60",
    "authorization": "Bearer  %s" % ACCESS_KEY}

# 現在時刻
now = datetime.datetime.now()
DATE = '{0:%Y_%m_%d_%H00}'.format(now)

# ファイルパス関連
SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
PLAYER_BATTLE_LOG_DIR = os.path.join(SCRIPT_DIR, "pro_player_battle_log", )
PRO_PLAYER_LIST_FILE = os.path.join(SCRIPT_DIR, "pro_player_list.yml")
with open(PRO_PLAYER_LIST_FILE) as f:
    PRO_PLAYERS = yaml.load(f)
print(PRO_PLAYERS)


def main():
    for player_tag in PRO_PLAYERS["PRO_PLAYER_LIST"]:
        # player_tag = "#8QRCJQ9Y"
        # player_tag = "%2328UGR809L" #takano7
        print(player_tag)
        # 宝箱
        # url = TARGET_API+player_tag+"/upcomingchests"
        url = TARGET_API+player_tag+"/battlelog"

    # APIを叩いてプレイヤー情報を取得
        r = requests.get(url, headers=HEADERS)
        data = r.json()
        print(json.dumps(data, indent=4))

    # JSON FILE作成
        write_file = os.path.join(PLAYER_BATTLE_LOG_DIR, player_tag + "_" + DATE)
        with open(write_file, 'w') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

if __name__ == '__main__':
    sys.exit(main())

# import yaml

# with open('input.yaml') as file:
#     obj = yaml.load(file)
#     print(obj['z'])