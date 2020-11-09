import sys
import os
import json
import xml.etree.ElementTree as ET

path='/home/chahak/mtp-2/VOCdevkit/VOC2012/JPEGImages/'
path1='/home/chahak/mtp-2/VOCdevkit/VOC2012/Annotations/'

images=[]
for f in os.listdir(path):
	images.append(f)

annots=[]
for f in os.listdir(path1):
	annots.append(f)

descr={}

for a in annots:
	fulla=os.path.join(path1,a)
	tree=ET.parse(fulla)
	imgid=a.split('.')[0]
	capt=[]
	root=tree.getroot()
	for object in root.findall('object'):
		n=object.find('name').text
		capt.append(n)
	capt=sorted(set(capt))
	descr[imgid]=capt

out=[]
for i,img in enumerate(images):
    jimg={}
    jimg['file_path'] =os.path.join(path,img)
    title =  img.split('.')[0]
    jimg['id']=title
    jimg['captions']=descr[title]
    out.append(jimg)

json.dump(out, open('coco_raw.json', 'w'))



