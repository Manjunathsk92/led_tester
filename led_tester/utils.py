import re

def parseFile(inp):
	if inp.startswith('http'):
		print("")
		return None, None
	else:
		#read from disk
		N, instructions= None, []
		with open (inp, 'r') as f:
			N=int(f.readline())
			for line in f.readlines():
				instructions.append(line)
			return N, instructions
		
	return

def parseInstruction(line):
		pat = re.compile(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*")
		while pat.search(line):
			return(pat.search(line)[1], int(pat.search(line)[2]), int(pat.search(line)[3]), int(pat.search(line)[4]), int(pat.search(line)[5]))
		return ("Invalid", 0,0,0,0)
class LEDTester:
	
	def __init__(self, N):
		self.grid_size= N
		self.grid= [ [0]*N for _ in range(N)]
	
	
	def apply(self,instruction):
		cmd, x1, y1, x2, y2 = parseInstruction(instruction)
		if x2 > self.grid_size:
			x2=self.grid_size-1
		
		if y2 > self.grid_size:
			y2=self.grid_size-1
		
		if x2 < 0:
			x2=0
		if y2<0:
			y2=0
		if x1<0:
			x1=0
		if y1<0:
			y1=0
		
		if (cmd == 'turn on'):
			for i in range(x1, x2+1):
				for j in range(y1, y2+1):
					self.grid[i][j] = 1
		elif (cmd == 'turn off'):
			for i in range(x1, x2+1):
				for j in range(y1, y2+1):
					self.grid[i][j] = 0
		elif (cmd == 'switch'):
			for i in range(x1, x2+1):
				for j in range(y1, y2+1):
					if (self.grid[i][j] == 1):
						self.grid[i][j] = 0
					else:
						self.grid[i][j] = 1
		return 
					
	def countLights(self):
		count = 0
		#for i in range(self.grid_size):
		#	for j in range(self.grid_size):
		#		print(self.grid[i][j], end=' ')
		#	print()
		for i in range(self.grid_size):
			for j in range(self.grid_size):
				if (self.grid[i][j] == 1):
					count+=1
		return count
		
		
		
		
		