
points = {
	'A': 1,
    'B': 2,
    'C': 3,
	'rock': 1,
	'paper': 2,
	'scissors': 3,
	'loss': 0,
	'win': 6,
	'draw': 3
}

labels = {
	'A': "Rock",
	'B': "Paper",
	'C': "Scissors",
	'X': "Rock",
	'Y': "Paper",
	'Z': "Scissors",
}
moves = {
	'X': 'loss',
    'Y': 'draw',
    'Z': 'win',
}
with open('2.in', 'r') as f:
	score = 0
	for line in f:
		move, end = line.strip().split()
		if end == "X":
			if move == "A":
				score += points['scissors'] + points['loss']
			elif move == "B":
				score += points['rock'] + points['loss']
			elif move == "C":
				score += points['paper'] + points['loss']
		elif end == "Y":
			if move == "A":
				score += points['rock'] + points['draw']
			elif move == "B":
				score += points['paper'] + points['draw']
			elif move == "C":
				score += points['scissors'] + points['draw']
		elif end == "Z":
			if move == "A":
				score += points['paper'] + points['win']
			elif move == "B":
				score += points['scissors'] + points['win']
			elif move == "C":
				score += points['rock'] + points['win']
	print(score)
				
		