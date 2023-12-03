f = open("input.txt").read().strip().split("\n")
f = [list(i.strip()) for i in f]

def get_count():
	o = 0
	for i in f:
		c = 0
		for y in i:
			if y not in "0123456789":
				o += c
				c = 0
			else:
				c = c * 10 + int(y)
		o += c
	return o
p1 = get_count()
o = 0
	
def remove(i,j):
	if i < 0 or j < 0 or i >= len(f) or j >= len(f[0]): return
	if f[i][j] not in "0123456789": return
	f[i][j] = "."
	remove(i,j+1)
	remove(i,j-1)

def get_num(i,j, visited = []):
	if i < 0 or j < 0 or i >= len(f) or j >= len(f[0]): return ""
	if f[i][j] not in "0123456789": return ""
	if (i,j) in visited: return ""
	v = visited
	v.append((i,j))
	g = get_num(i,j-1,v) + f[i][j] + get_num(i,j+1,v)
	return g

def gears(i,j):
	o = 1
	c = 0
	for x in [-1,0,1]:
		for y in [-1,0,1]:
			g = get_num(i+x,j+y)
			if g != "":
				o *= int(g)
				c += 1
	if c == 2: return o
	else: return -1


p2 = 0
for i in range(len(f)):
	for j in range(len(f[i])):
		if f[i][j] == "*":
			g = gears(i,j)
			if g != -1:
				p2 += g

for i in range(len(f)):
	for j in range(len(f[i])):
		if f[i][j]  not in "0123456789.":
			for x in [-1,0,1]:
				for y in [-1,0,1]:
					remove(i+x,j+y)
			
p1 -= get_count()

print(p1,p2)
