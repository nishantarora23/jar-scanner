# importing python modules
import glob
import os
import shutil
from zipfile import ZipFile

# path of the parent directory
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
         print(file, "has been successfully extracted to ", zip_folder)
         for files in glob.glob(os.path.join(zip_folder, ear_ext)):
               shutil.copy(files, bucket_dir)
         for files in glob.glob(os.path.join(zip_folder, war_ext)):
               shutil.copy(files, bucket_dir)
   if glob.glob(ear_ext):
      ear_files=glob.glob(ear_ext)
      print("The list of ear files detected:", ear_files)
      for file in ear_files:
         ear_folder = file + "_ear"
         os.mkdir(ear_folder)
         with ZipFile(file, 'r') as zipObj:
            # Extract all the contents of EAR file in current directory
            zipObj.extractall(ear_folder)
         print(file, "has been successfully extracted to ", ear_folder)
         for files in glob.glob(os.path.join(ear_folder, war_ext)):
               shutil.copy(files, bucket_dir)
   if glob.glob(war_ext):
      war_files=glob.glob(war_ext)
      print("The list of war files detected:", war_files)
      for file in war_files:
          war_folder = file + "_war"
          os.mkdir(war_folder)
          with ZipFile(file, 'r') as zipObj:
            # Extract all the contents of WAR file in current directory
            zipObj.extractall(war_folder)
          print(file, "has been successfully extracted to ", war_folder)
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
print("Total No. of unique jars: ",sorted(all_jars))
print(len(all_jars))

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
# printing lists
print("No. of jars suppressed in  project: ", len(suppression_jar)-1)
print("Suppression jars: ", sorted(set(suppression_jar)))
