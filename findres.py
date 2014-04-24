#!/usr/bin/python
#findres.py

import os
import sys
import glob
import fileinput

#### Function Define ##########
def findFirstUser(path,drawableName):
	for (root,dirs,files) in os.walk(path):
		for file in files:
			filePath = os.path.join(root,file)
			ext = os.path.splitext(file)[-1]
			used = None
			if ext==".java":
				used = findInFile(filePath, "R.drawable."+drawableName)
			elif ext==".xml":
				used = findInFile(filePath, "@drawable/"+drawableName)

			if used:
				return filePath

	return None


def findInFile(file,str):
	f=open(file)
	content=f.read()
	f.close()
	return content.find(str) >= 0
    


#### Main Loop ###############

if len(sys.argv)<=1:
	print("Usages:")
	print("\t"+__file__+"<android project path>")
	sys.exit(-1)

rootPath=sys.argv[1]
print("RootPath is "+rootPath)

# Walk
totalLength = 0
for drawable in glob.glob(rootPath + "/res/drawable*"):
	print("\n### Start "+drawable)

	for pngPath in glob.glob(drawable+"/*.png"):
		pngName = os.path.splitext(os.path.basename(pngPath))[0]
		without9 = pngName.split('.')[0]
		user = findFirstUser(rootPath,without9)
		if not user:
			length = os.path.getsize(pngPath)
			print(str(length) + "\t" + pngPath)
			totalLength+=length
			#os.remove(pngPath);

print("totalLength is "+str(totalLength))
	
