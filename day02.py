f = open("input.txt").read().strip().split("\n")
o = 0

for i in range(len(f)):
	x = [ j.strip().replace(", "," ").split(" ") for j in f[i].split(": ")[1].split(";")]
	d = {}
	print(x)
	for q in x:
		for j in range(0,len(q), 2):
			d[q[j+1]] = max(d.get(q[j+1],0),int(q[j]))
	# PART 1: if d["blue"] <= 14 and d["red"]<=12 and d["green"]<=13: o+=i+1
	o += d["blue"] * d["red"] * d["green"]
print(o)
