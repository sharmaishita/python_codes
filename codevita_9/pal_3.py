from sys import stdin,stdout
def op(ans): return stdout.write(str(ans) + '\n')

def izpal (ins):
	return ins[:len(ins)//2] == ins[len(ins) : (len(ins)-1)//2 : -1]

ins = input()
count1,anz = 1,[]

for count1 in range(1, len(ins)-2):
	if izpal (ins[:count1]):
		count2 = count1 + 1
		while count2 < len(ins):
			if (izpal (ins[count1:count2])and izpal (ins[count2:])):
				anz.append(ins[:count1]);anz.append(ins[count1:count2]);anz.append(ins[count2:])
				for xx in anz:
					op(xx)
				exit()
			count2 += 1
	count1 += 1
op('Wrong')
'''
namannayantenet
aaaaa
aaaabaaaa
'''
