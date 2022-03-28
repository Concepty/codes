import os
import threading
import time
import random
from collections import namedtuple


def cpu_task():
	i = 60000000
	for _ in range(i):
		1+1

def sleep_task():
	time.sleep(1)

def func_time(callable):
	init = time.time()
	callable()
	end = time.time()
	print(end - init)

if 0:
	def p_entry1():
		i = 10000000
		def rest():
			for _ in range(i):
				1+1
		for order in range(30):
			print('', order)
			rest()
	def p_entry2():
		i = 10000000
		def rest():
			for _ in range(i):
				1+1
		for order in range(30):
			print('    ', order)
			rest()
	def p_entry3():
		i = 10000000
		def rest():
			for _ in range(i):
				1+1
		for order in range(30):
			print('        ', order)
			rest()

	T1 = threading.Thread(target = p_entry1)
	T2 = threading.Thread(target = p_entry2)
	T3 = threading.Thread(target = p_entry3)
	
	T1.start()
	T2.start()
	T3.start()
	T1.join()
	T2.join()
	T3.join()

if 0:
	func_time(cpu_task)
	func_time(sleep_task)

if 0:
	def cpu_task_long():
		for _ in range(1000000000): # 16.4
			1+1
		print('cpu done')
	def sleep_task_long():
		time.sleep(16.4)
		print('sleep done')

	def cpu_thread_entry():
		cpu_task_long()
		
	def sleep_thread_entry():
		sleep_task_long()
		
	
	T1 = threading.Thread(target = cpu_thread_entry)
	#T2 = threading.Thread(target = sleep_thread_entry)
	
	
	T1.start()
	#T2.start()
	#cpu_task_long()
	sleep_task_long()
	
	T1.join()
	#T2.join()

if 0:
	cycle = 30
	count = 0
	print(count)
	
	def cpu_thread_entry():
		for _ in range(cycle):
			cpu_task()
		print('cpu done')
	def sleep_thread_entry():
		for _ in range(cycle):
			sleep_task()
		print('sleep done')
	
	T1 = threading.Thread(target = cpu_thread_entry)
	T2 = threading.Thread(target = sleep_thread_entry)
	
	init = time.time()
	T1.start()
	T2.start()
	
	T1.join()
	T2.join()
	end = time.time()
	
	print('cpu + sleep', end - init, 'seconds')

if 0:
	cycle = 30
	count = 0
	print(count)
	
	def cpu_thread_entry():
		for _ in range(cycle):
			cpu_task()
		print('cpu done')
	def sleep_thread_entry():
		for _ in range(cycle):
			sleep_task()
		print('sleep done')
	
	T1 = threading.Thread(target = cpu_thread_entry)
	T2 = threading.Thread(target = cpu_thread_entry)
	
	init = time.time()
	T1.start()
	T2.start()
	
	T1.join()
	T2.join()
	end = time.time()
	
	print('cpu + cpu', end - init, 'seconds')

if 0:
	cycle = 30
	count = 0
	print(count)
	
	def cpu_thread_entry():
		for _ in range(cycle):
			cpu_task()
		print('cpu done')
	def sleep_thread_entry():
		for _ in range(cycle):
			sleep_task()
		print('sleep done')
	
	T1 = threading.Thread(target = sleep_thread_entry)
	T2 = threading.Thread(target = sleep_thread_entry)
	
	init = time.time()
	T1.start()
	T2.start()
	
	T1.join()
	T2.join()
	end = time.time()
	
	print('sleep + sleep', end - init, 'seconds')

#not the way global interpreter Lock prevent
if 0:
	global_count = 0
	def increase1():
		global global_count
		for _ in range(50):
			global_count += 1
			print(global_count)
	def increase2():
		global global_count
		for _ in range(50,100,1):
			global_count += 1
			print('       ', global_count)	
	T1 = threading.Thread(target = increase1)
	T2 = threading.Thread(target = increase2)
	
	T1.start()
	T2.start()
	
	T1.join()
	T2.join()

#Question
if 1:
	class RandChecker:
		def __init__(self):
			self.rand = random.random()
			self.checker_list = [0] * 500
		
		def sync(self):
			for i in range(500):
				self.checker_list[i] = self.rand
				print(1)
		
		def test_sync(self):
			pivot  = self.checker_list[0]
			for i in range(500):
				if self.checker_list[i] != pivot:
					print('Error!!')
					return
			print('Success')
			return
		
		def interrupt(self):
			for _ in range(30):
				self.rand = random.random()
				print(111111)
		
	a = RandChecker()
	
	T1 = threading.Thread(target = a.sync)
	T2 = threading.Thread(target = a.interrupt)
	
	T1.start()
	T2.start()
	
	T1.join()
	T2.join()
	
	a.test_sync()