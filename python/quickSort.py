#!/usr/bin/python
#-*- coding: utf-8 -*-    
import random  
''''' 
随机生成0~10000000之间的数值 
'''  
def getrandata(num):  
    a=[]  
    i=0  
    while i<num:  
        a.append(random.randint(0,100))  
        i+=1  
    return a  

'''
BubbleSort冒泡排序：
时间复杂度 Best: O(n) Worst: O(n^2)
空间复杂度 O(1)
'''
def bubbleSort(a):
	i=len(a) #initialise L
	while i>1:
		for j in range(i-1):
			if a[j]>a[j+1]:
				a[j],a[j+1]=a[j+1],a[j]
		i-=1
	return a

'''
InsertSort插入排序：
时间复杂度 Best: O(n) Worst: O(n^2)
空间复杂度 O(1)
'''
def insertSort(a):
	for i in range(1,len(a)):
		for j in range(i):
			if a[i]<a[j]:
				a.insert(j,a[i])
				a.pop(i+1)
				break
	return a

'''
DirectSort直接排序
时间复杂度 O(n^2)
空间复杂度 O(m)
'''
def directSort(a):
	result=[]
	while len(a)!=0:
		t=1e12
		for i,num in enumerate(a):
			if num<t:
				t=num
				r=i
		result.append(t)
		a.pop(r)
	return result

def test(size, choice):
	base=getrandata(size)
	print "Original array is:%s"%(base)
	if choice=='bubble':
		result=bubbleSort(base)
	elif choice=='insert':
		result=insertSort(base)
	elif choice=='direct':
		result=directSort(base)
	print "array after %s is %s"%(choice, result)

if __name__ == '__main__':
	import argparse
	parser=argparse.ArgumentParser(description='Sorting Algorithm')
	parser.add_argument('size',type=int)
	parser.add_argument('choice',type=str)
	args=parser.parse_args()
	test(args.size, args.choice)
