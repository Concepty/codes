import glob
import os



def copy_tree(f, root, depth):
	paths = glob.glob(root + '/*')
	for p in paths:
		if os.path.isdir(p):
			f.write('{indents}<Directory = {name}>\n'.format(indents = '\t' * (depth+1), name = p.split('/')[-1]))
			copy_tree(f, p, depth+1)
			f.write('{indents}<Directory END>\n'.format(indents = '\t' * (depth+1)))
		else:
			f.write('{indents}<File = {name}/>\n'.format(indents = '\t' * (depth+1), name = p.split('/')[-1]))
with open('test_xml.xml', 'w') as f:
	root = 'glob_example'
	depth = 2
	f.write('{indents}<Directory = {name}>\n'.format(indents = '\t' * (depth), name = root.split('/')[-1]))
	copy_tree(f, root, depth)
	f.write('{indents}<Directory END>\n'.format(indents = '\t' * (depth)))