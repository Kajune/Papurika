from janome.tokenizer import Tokenizer
import random

t = Tokenizer()

dim = 2

txt = []
start_indeces = [0]
for s in open('seisyo.txt', 'r', encoding="utf-8"):
	for token in t.tokenize(s, stream=True):
		txt.append(token.surface)
		if '。' in token.surface or '』' in token.surface:
			start_indeces.append(len(txt)+1)

for k in range(10):
	index = random.choice(start_indeces)
	flag = True
	while flag:
		search = []
		for i in range(dim):
			search.append(txt[index])
			print(txt[index], end='')
			if '。' in txt[index]:
				flag = False
				print()
				break
			index += 1

		indices = [i for i, x in enumerate(txt)]
		for i, word in enumerate(search):
			indices = [x+1 for i, x in enumerate(indices) if txt[x] == word]
		index = random.choice(indices)
