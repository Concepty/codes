import sys
import threading
import random

if 1:
	x = 0
	print('ref count of x', sys.getrefcount(x))
	print('ref count of x', sys.getrefcount(x))
	def thread_entry_increase():
		global x 
		for _ in range(1000000):
			x += 1
	def thread_entry_decrease():
		global x
		for _ in range(1000000):
			x -= 1

	T1 = threading.Thread(target = thread_entry_increase)
	T2 = threading.Thread(target = thread_entry_decrease)
	
	T1.start()
	T2.start()
	
	T1.join()
	T2.join()
	print('ref count of x', sys.getrefcount(x))
	print('x', x)
	print('ref count of x', sys.getrefcount(x))
	#should be 0 
	# -550047 or other trash
	# why GIL not working this way?
	# test for ref count safety

if 0:
	rand_list = []
	for _ in range(5000000):
		rand_list.append(random.random())
	
	def test_sorting_time():
		import time
		global rand_list
		init = time.time()
		rand_list.sort()
		end = time.time()
		print(end-init)
	
	def thread_entry_sort():
		global rand_list
		rand_list.sort()
	def thread_entry_inspect():
		global ran_list
		for i in range(30):
			print(rand_list[i])
	
	T1 = threading.Thread(target = thread_entry_sort)
	T2 = threading.Thread(target = thread_entry_inspect)
	
	T1.start()
	T2.start()
	
	T1.join()
	T2.join()