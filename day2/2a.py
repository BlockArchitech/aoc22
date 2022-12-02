moves = {
	'X': 'A',
    'Y': 'B',
    'Z': 'C',
}
points = {
	'A': 1,
    'B': 2,
    'C': 3,
	'X': 1,
    'Y': 2,
    'Z': 3,
}
endtype = {
	'win': 6,
    'loss': 0,
    'draw': 3,
}
labels = {
	'A': "Rock",
	'B': "Paper",
	'C': "Scissors",
	'X': "Rock",
	'Y': "Paper",
	'Z': "Scissors",
}

def game(you: str, opponent: str) -> int:
	match you:
		case "X":
			print(f'X -> {moves["X"]}')
			if opponent == "A":
				return points['X'] + endtype['draw']
			elif opponent == "B":
				return points['X'] + endtype['loss']
			elif opponent == "C":
				return points['X'] + endtype['win']
			else:
				raise TypeError(f'"{opponent}" is an invalid move.')
		case "Y":
			print(f'Y -> {moves["Y"]}')
			if opponent == "A":
				return points['Y'] + endtype['win']
			elif opponent == "B":
				return points['Y'] + endtype['draw']
			elif opponent == "C":
				return points['Y'] + endtype['loss']
			else:
				raise TypeError(f'"{opponent}" is an invalid move.')

		case "Z":
			print(f'Z -> {moves["Z"]}')
			if opponent == "A":
				return points['Z'] + endtype['loss']
			elif opponent == "B":
				return points['Z'] + endtype['win']
			elif opponent == "C":
				return points['Z'] + endtype['draw']
			else:
				raise TypeError(f'"{opponent}" is an invalid move.')
		case _:
			raise TypeError(f'"{you}" is an invalid move.')

with open('2.in', 'r') as f:
	score = 0
	for line in f:
		you, opponent = line.strip().split()
		score += game(opponent, you)
	print(score)