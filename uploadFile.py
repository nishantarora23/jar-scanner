import csv
import os

current_dir = os.getcwd()
bucket_dir = os.path.join(current_dir, "Bucket")

def upload(arr,type):
	
	testArray = [];
	for element in arr:
		var = []
		var.append(element)
		testArray.append(var)

	if type == 'suppression':	
		file = open(r'Requisite\suppression_jars.csv', 'w+', newline ='') 
	elif type == 'la':	
		file = open(r'Requisite\L&A.csv', 'w+', newline ='') 
			
	with file:     
		write = csv.writer(file) 
		write.writerows(testArray)
		
		
def uploadjar(file):
	filename = file.filename
	print(os.path.join(bucket_dir,filename))
	file.save(os.path.join(bucket_dir,filename))