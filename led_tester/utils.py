def parseFile(input):
	if input.startswith('http'):
		pass
		return None, None
	else:
		#read from disk
		N, instructions= None, []
		with open (input, 'r') as f:
			N=int(f.readline())
			for line in f.readlines():
				instructions.append(line)
			return N, instructions
		
	return

