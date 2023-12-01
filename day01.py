import subprocess

def copy2clip(txt):
	cmd='echo '+txt.strip()+'|clip'
	print(txt)
	return subprocess.check_call(cmd, shell=True)




f = open("input.txt").read().strip().split("\n")
# f = [int(i) for i in f]
# f = [[int(j)] for j in i.split(" ") for i in f]
o = 0
for i in range(len(f)):
	x = f[i]
	y = ""
	for i in range(len(x)):
		if x[i] in "0123456789":
			y += x[i]
		# PART TWO CODE
		words = ["zero","one","two","three","four","five","six","seven","eight","nine"]
		for j in words:
			if x[i:i+len(j)] == j:
				y += str(words.index(j))
		
	o+= int(y[0]+y[-1])
print(o)


copy2clip(str(o))