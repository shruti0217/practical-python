# bounce.py
#
# Exercise 1.5

'''
	A rubber ball is dropped from a height of 100 meters 
	and each time it hits the ground,
	 it bounces back up to 3/5 the height it fell.
	  Write a program bounce.py that prints a table showing the height of the first 
	  10 bounces.

'''

if __name__=='__main__':
	height = 100
	for i in range(0,10):
		height *= 3/5
		print(f"{i+1} {round(height,4)}")
