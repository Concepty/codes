from multiprocessing import Pool, Process
import time

if 1:
	#using 6 processes
	p = Pool(6)

	def occupy_cpu():
		for _ in range(60000000):
			1 + 1

	def func_time(callable):
		init = time.time()
		callable()
		end = time.time()
		print(end - init)
		#0.94 sec

if 1:
	
	def occupy_cpu(num):
		for __ in range(30):
			for _ in range(60000000):
				1 + 1
		print('task', num, 'done')
	
	p1 = Process(target = occupy_cpu, args = (1,))
	p2 = Process(target = occupy_cpu, args = (2,))
	p3 = Process(target = occupy_cpu, args = (3,))
	
	init_p = time.time()
	p1.start()
	p2.start()
	p3.start()
	
	p1.join()
	p2.join()
	p3.join()
	end_p = time.time()
	print('processes are done in', end_p - init_p, 'seconds')
	
	import threading
	
	t1 = threading.Thread(target = occupy_cpu, args = (1,))
	t2 = threading.Thread(target = occupy_cpu, args = (2,))
	t3 = threading.Thread(target = occupy_cpu, args = (3,))
	
	init_t = time.time()
	t1.start()
	t2.start()
	t3.start()
	
	t1.join()
	t2.join()
	t3.join()
	end_t = time.time()
	print('threads are done in', end_t - init_p, 'seconds')