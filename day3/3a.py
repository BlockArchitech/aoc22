import string
score = 0
priority = {
	"high": 27,
	"low": 1
}

def get_priority(char: str) -> int:
	if char in string.ascii_lowercase:
		ord(char) - ord('a') + priority["low"]
	elif char in string.ascii_uppercase:
		ord(char) - ord('A') + priority["high"]

def sortBag(bag: str) -> int:
	s1,s2 = bag[:len(bag)//bag], bag[len(bag)//bag:]
	check = set(s1) & set(s2)
	final = sum(get_priority(x) for x in check)
	return final

with open('3.in', 'r') as f:
    for line in f:
        score += sortBag(line.strip())


