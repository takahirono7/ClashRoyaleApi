# coding: utf-8
import json
import os

# 変数定義
# ファイルパス関連
SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
PLAYER_BATTLE_LOG_DIR = os.path.join(SCRIPT_DIR, "pro_player_battle_log", )
TARGET_JSON_FILE = os.path.join(SCRIPT_DIR, "test.json")

# 対象のjsonデータの読み込み
DATA_pre = open(TARGET_JSON_FILE, 'r')
DATA = json.load(DATA_pre)

print(len(DATA))

# # outputするjsonデータの定義
# OUTPUT_JSON_1v1 = {
# 	game_mode: type,
# 	battleTime: battleTime,
# 	win_or_lose: win_or_lose,
# 	crowns: crowns,
# 	used_cards: [],
# 	opponent_name: opponent_name,
# 	opponent_cards: [],
# }

# OUTPUT_JSON_2v2 = {
# 	game_mode: type,
# 	battleTime: battleTime,
# 	win_or_lose: win_or_lose,
# 	crowns: crowns,
# 	used_cards: [],
# 	team_name: team_name,
# 	team_cards: [],

# 	opponent_name_1: opponent_name_1,
# 	opponent_cards_1: [],
# 	opponent_name_2: opponent_name_2,
# 	opponent_cards_2: [],
# }
def win_or_lose(trophyChange):
	try:
		if td["team"][0]["trophyChange"] > 0:
			win_or_lose = "win"
		elif td["team"][0]["trophyChange"] < 0:
			win_or_lose = "lose"
		else:
			win_or_lose = "draw"
		return(win_or_lose)

	except Exception as e:
		print(e)


# td = target_data
for td in DATA:
	if td["type"] == "PvP":
		# print(td["team"][0]["cards"])
		deck = [card["name"] for card in td["team"][0]["cards"]]
		opponent_deck = [card["name"] for card in td["opponent"][0]["cards"]]
		# win_or_lose(td["team"][0]["trophyChange"])
		OUTPUT_JSON_1v1 = {
			"game_mode": td["type"],
			"battleTime": td["battleTime"],
			"win_or_lose": win_or_lose(td["team"][0]["trophyChange"]),
		# 	crowns: crowns,
			"used_cards": deck,
			"opponent_name": td["opponent"][0]["name"],
			"opponent_cards": [],
		}
		print(OUTPUT_JSON_1v1)
		break

	elif target_data["type"] == "2v2":
		break

