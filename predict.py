import os
import shutil

os.chdir('E:/Pyfiles/sub1/LLGAN')
os.system('python scripts/script.py --predict')

identifier = 'fake'
source = 'E:/Pyfiles/sub1/LLGAN/ablation/enlightening/test_200/images/'
destination = 'E:/Pyfiles/sub1/RGAN/LR/'

for filename in os.listdir(source):
	if identifier in filename:
		shutil.move(source + filename, destination + filename)

os.chdir('E:/Pyfiles/sub1/RGAN')
os.system('python test.py')