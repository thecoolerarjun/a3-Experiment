from random import randint
from math import floor

def sim(n,d=True):
	correct=0;trials=0
	for i in range(n):
		a=randint(20,100);b=randint(20,100);trials+=1
		if(max(a,b)>floor(min(a,b)*1.05)):
			correct+=1
		else:
			correct+=randint(d,1)/(d+1)
	return(correct,trials)

def prob(jnd=0.05):
	val = list(range(20,101))
	a = 0
	b = len(val)**2

	for i in range(len(val)):
		a += len([j for j in val if j<val[i]/(1+jnd) or j>val[i]*(1+jnd)])
	p=a/b
	P=p+(1-p)*0.5
	return P