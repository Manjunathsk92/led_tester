import re
import urllib.request
import os

#Function to parse the input file. 
def parseFile(inp):
	#read from the server
	if inp.startswith('http'):
		N, instructions= None, []
		try:    
    			urllib.request.urlopen(inp)
		except:
    			print ("Given URL doesn't exist")
    			return 0,0
		req = urllib.request.urlopen(inp)
		buffer = req.read().decode('utf-8')
		parsed_buffer=buffer.splitlines()
		N=(parsed_buffer[0])
		N=int(N)
		for line in range(1,len(parsed_buffer)):
			instructions.append(parsed_buffer[line])
		return N, instructions
	else:
		#read from disk
		if not os.path.isfile(inp):
			print("File doesn't exist")
		else:
			N, instructions= None, []
			with open (inp, 'r') as f:
				N=int(f.readline())
				for line in f.readlines():
					instructions.append(line)
			#return the value of N and all the instructions in a list. 		
			return N, instructions
		
	return 0,0

#function to parse every instruction and return the command, x and y coordinates
def parseInstruction(line):
		#pattern to match
		pat = re.compile(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*")
		line=str(line)
		
		while pat.search(line):
			#return the command, x and y coordinates
			return(pat.search(line)[1], int(pat.search(line)[2]), int(pat.search(line)[3]), int(pat.search(line)[4]), int(pat.search(line)[5]))
		#return invalid if command is not turn on, turn off, switch.
		return ("Invalid", 0,0,0,0)
	
#class for LEDTester	
class LEDTester:
	
	#function to initialize the object attributes
	def __init__(self, N):
		self.grid_size= N
		self.grid= [ [0]*N for _ in range(N)]
	
	#function to apply the commands to the grid 
	def apply(self,instruction):
		#receive the parsed instruction
		cmd, x1, y1, x2, y2 = parseInstruction(instruction)
		if x2 > self.grid_size-1:
			x2=self.grid_size-1
		
		if y2 > self.grid_size-1:
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
	
	#function to count the lights that are left on after all the commands are executed				
	def countLights(self):
		count = 0
		for i in range(self.grid_size):
			for j in range(self.grid_size):
				if (self.grid[i][j] == 1):
					count+=1
		return count
		
		
		
		
		