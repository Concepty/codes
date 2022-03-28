import os
import glob

#method 1 sort
#method 2 recursive function
#method 3 stack

MODULE_DIR = os.path.dirname(os.path.abspath(__file__))
if 0:
	files = [f.split('/')[5:] for f in glob.glob('/'.join([MODULE_DIR, 'glob_example']) + '/**/*.*', recursive = True)]

	files = glob.glob('/'.join([MODULE_DIR, 'glob_example']) + '/**/*.*', recursive = True)

	for file in files:
		print(file)

if 1:
	def is_dir(path: list) -> bool:
		if '.' in path.split('/')[-1]: return False
		else: return True

	def get_paths(path):
		paths = glob.glob(path + '/*')
		for i, p in enumerate(paths):
			if is_dir(p):
				del paths[i]
				paths += get_paths(p)
		return paths
	
	pa = get_paths('/'.join([MODULE_DIR, 'glob_example']))
	
	#try again
	
	for p in pa:
		print(p)

if 0:
	stack = []
	
	stack += glob.glob('/'.join([MODULE_DIR, 'glob_example']))
	print(stack)