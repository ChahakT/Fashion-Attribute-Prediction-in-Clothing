import sys
import os
import json
import xml.etree.ElementTree as ET

path='/home/chahak/mtp-2/VOCdevkit/VOC2012/JPEGImages/'
path1='/home/chahak/mtp-2/VOCdevkit/VOC2012/Annotations/'
path_to_file = '/home/chahak/mtp-2/PVOC/'

annots=[]
for f in os.listdir(path1):
	annots.append(f)

descr={}

for i,a in enumerate(annots):
	fulla=os.path.join(path1,a)
	tree=ET.parse(fulla)
	imgid=a.split('.')[0]
	capt=[]
	root=tree.getroot()
	for object in root.findall('object'):
		n=object.find('name').text
		capt.append(n)
	capt=sorted	(set(capt))
	descr[imgid]=capt

f=open(path_to_file +'PVOC_testImages.txt', 'r')
images=f.read().splitlines()
images.sort()

f.close()
out=[]
for i, img in images:
	title =  img.split('.')[0]
	jimg=descr[title]
    out.append(jimg)

 f=open(path_to_file +'PVOC_test_caps.txt','w')
 for im in out:
 	f.write("%s\n" % im)

f.close()