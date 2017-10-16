if __name__ == "__main__":

	import csv
	import random


	players = []

	#Step 1: Import CSV & Prep Data
	def import_CSV():
		with open('soccer_players.csv') as csv_file:
			reader = csv.reader(csv_file)
			for row in reader:
				del row[1] #remove height attribute
				players.append(row)
			del players[0] #remove header row


	#Step 2: build two sets of people ones with experience and ones without
	experienced_players = []
	inexperienced_players = []

	def group_players():
		for player in players:
			if player[1] == "YES":
				experienced_players.append(player)
			else:
				inexperienced_players.append(player)

	#Step 3: Create teams Sharks, Dragons, Raptors with list
	dragons = []
	raptors = []
	sharks = [] 
	
	#Step 4: Randomly assign 18 players to teams - 6 per team; 3 with experience - 3 w/o
	def assign_players():
		for experienced_player in range(int(len(experienced_players)/3)):
			dragons.append(experienced_players.pop(experienced_player))
		
		for inexperienced_player in range(int(len(inexperienced_players)/3)):
			dragons.append(inexperienced_players.pop(inexperienced_player))

		for experienced_player in range(int(len(experienced_players)/2)):
			raptors.append(experienced_players.pop(experienced_player))

		for inexperienced_player in range(int(len(inexperienced_players)/2)):
			raptors.append(inexperienced_players.pop(inexperienced_player))

		for experienced_player in range(int(len(experienced_players))):
			sharks.append(experienced_players.pop())

		for inexperienced_player in range(int(len(inexperienced_players))):
			sharks.append(inexperienced_players.pop())

	#Step 5: Create a text file named teams.txt 
	def build_txt():
		txt_file = open("teams.txt", "w")
		txt_file.write("Dragons")
		for dragon in dragons:
			txt_file.write("\n")
			txt_file.write(", ".join(dragon))

		txt_file.write("\n \nRaptors")
		for raptor in raptors:
			txt_file.write("\n")
			txt_file.write(", ".join(raptor))

		txt_file.write("\n \nSharks")
		for shark in sharks:
			txt_file.write("\n")
			txt_file.write(", ".join(shark))


	import_CSV()
	group_players()
	assign_players()
	build_txt()











