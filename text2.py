import os,re
def get_filename(filepath,filetype):
	import os
	filename=[]
	for root,dirs,files in os.walk(filepath):
		for file in files:
			expanded_name=os.path.splitext(file)
			if expanded_name[1]==filetype:
				lujing=os.path.join(root,file)
				filename.append(lujing)
	return filename
	
def main():
	srcfilepath=r'F:\text'
	filetype='.txt'
	filename=get_filename(srcfilepath,filetype)
	sum=0
	for i in range(len(filename)):
		f=open(filename[i],'r')
		cont=f.readlines()
		sum=sum+len(cont)
		print(filename[i],len(cont))
	print("Total number of rows:"+str(sum))
		
main()
