# importing python modules
import csv
import glob
import os
import shutil
from zipfile import ZipFile
import re
import time

#    path of the parent directory
current_dir = os.getcwd()
bucket_dir = os.path.join(current_dir, "Bucket")
if os.path.exists(bucket_dir):
    os.chdir(bucket_dir)
else:
    os.chdir(current_dir)
    os.mkdir("Bucket")
    os.chdir(bucket_dir)

# function to extract the EAR and WAR files


def extract():
   zip_ext="*.zip"
   war_ext="*.war"
   ear_ext="*.ear"
   if glob.glob(zip_ext):
      zip_files=glob.glob(zip_ext)
      print("The list of ear files detected:", zip_files)
      for file in zip_files:
         zip_folder = file + "_zip"
         os.mkdir(zip_folder)
         with ZipFile(file, 'r') as zipObj:
            # Extract all the contents of zip file in current directory
            zipObj.extractall(zip_folder)
         print(file, "has been scanned ")
         for files in glob.glob(os.path.join(zip_folder, ear_ext)):
               shutil.copy(files, bucket_dir)
         for files in glob.glob(os.path.join(zip_folder, war_ext)):
               shutil.copy(files, bucket_dir)
   if glob.glob(ear_ext):
      ear_files=glob.glob(ear_ext)
      print("\n\nThe list of ear files detected:", ear_files)
      for file in ear_files:
         ear_folder = file + "_ear"
         os.mkdir(ear_folder)
         with ZipFile(file, 'r') as zipObj:
            # Extract all the contents of EAR file in current directory
            zipObj.extractall(ear_folder)
         print(file, "has been scanned ")
         for files in glob.glob(os.path.join(ear_folder, war_ext)):
               shutil.copy(files, bucket_dir)
   if glob.glob(war_ext):
      war_files=glob.glob(war_ext)
      print("\n\nThe list of war files detected:", war_files)
      for file in war_files:
         name= file.split(".war")
         war_folder = name[0]
         os.mkdir(war_folder)
         with ZipFile(file, 'r') as zipObj:
            # Extract all the contents of WAR file in current directory
            zipObj.extractall(war_folder)
         print(file, "has been scanned ")
   else:
      print("There is no file to be extracted")

extract()

# Generating the list of all unique the jars
all_jars=[]
bucket_jars = os.path.join(bucket_dir + "\**\*.jar")
all_jars_files = glob.glob(bucket_jars,
                  recursive=True)
for file in all_jars_files:
   all_jars.append(os.path.basename(file))
all_jars = list(set(all_jars))

# Importing the product created jar list from CSV to suppression list

requisite_path = os.path.join(current_dir, "Requisite")
if os.path.isfile(os.path.join(requisite_path, "suppression_jars.csv")):
    os.chdir(requisite_path)
    suppression = open('suppression_jars.csv', 'r')
    # creating dictreader object
    file = csv.DictReader(suppression)
    # creating empty lists
    suppression_jar = []

# iterating over each row and append
# values to empty list
    for col in file:
        suppression_jar.append(col['Jars'])
suppression_jar = list(set(suppression_jar))

# Reading the list of jars from the L&A CSV file
if os.path.isfile(os.path.join(requisite_path, "L&A.csv")):
    os.chdir(requisite_path)
    license = open('L&A.csv', 'r')
    # creating dictreader object
    file = csv.DictReader(license)
    # creating empty lists
    license_jar = []

# iterating over each row and append
# values to empty list
    for col in file:
        license_jar.append(col['jars'])

third_party = []
for element in all_jars:
    if element not in suppression_jar:
        third_party.append(element)


deprecated_jars = []
newly_added_jars = []
active_license = []
for element in license_jar:
    if element not in third_party:
        deprecated_jars.append(element)
    elif element in third_party:
        active_license.append(element)

for element in third_party:
    if element not in license_jar:
        newly_added_jars.append(element)
newly_added_jars= sorted(set(newly_added_jars))



########################################################

version = []
deprected_withoutext = []
jars_oldversion = []
jars_newversion = []

for element in deprecated_jars:
    result = re.split(r"-\d.+", element)
    deprected_withoutext.append(result[0])


final_new_jars= []
versionchanged_jars = []
for element in newly_added_jars:
    name = re.split(r"-\d.+", element)
    if name[0] not in deprected_withoutext:
        final_new_jars.append(element)
    else:
        jars_newversion.append(element)
        versionchanged_jars.append(name[0])

#######################################################

my_dict = {}
unutilized_jars = []
test = []
for element in deprecated_jars:
    name = re.split(r"-\d.+", element)
    nameOfJar = name[0];
    ver = []
    if nameOfJar in versionchanged_jars:
        test.append(element)
        if nameOfJar in my_dict.keys():
            a = element.split(nameOfJar + "-")
            b = a[1].split(".jar")
            new_version = "approved version : " + b[0]
            my_dict[nameOfJar].append(new_version)
        else:
            a = element.split(nameOfJar+"-")
            b = a[1].split(".jar")
            old_version = "approved version : "+b[0]
            ver.append(old_version)
            my_dict.setdefault(nameOfJar,ver)
    else:
        unutilized_jars.append(element)

for element in jars_newversion:
    name = re.split(r"-\d.+", element)
    nameOfJar = name[0]

    if nameOfJar in my_dict.keys():
        a = element.split(nameOfJar + "-")
        b = a[1].split(".jar")
        new_version = "new version : " + b[0]
        my_dict[nameOfJar].append(new_version)
    else:
        print("check the flow if it enters this else condition")
        
print ("\n\nJAR-Scanner has successfully executed and the report has been generated...")
time.sleep(5)