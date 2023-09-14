# Code to Compile and Auto run Cpp/C code without much hassle 
from os import path,system
import argparse
import subprocess
system("clear")

# Create an ArgumentParser object
parser = argparse.ArgumentParser(description="A simple Script to compiler Cpp/C/java code and Auto run.")

# Define the expected arguments
parser.add_argument("-f", dest="File_Name", required=True, help="Name of The File to be COmpiled")
#parser.add_argument("-t", dest="type", required=False, default="cpp", help="Only if the File is in C then pass <C> parameter")

# Parse the command-line arguments
args = parser.parse_args()

# Access the parsed arguments
fileName = args.File_Name

if ".cpp" in fileName:
  fileType = "cpp"
elif ".c" in fileName:
  fileType = "c"
elif ".java" in fileName:
  fileType = "java"  
else:
  print("Error! Not a C/C++/java File:",fileName)    
  exit()

result = subprocess.run(["pwd"],shell=True, stdout=subprocess.PIPE, text=True)
cwd = result.stdout.strip()
fileLoc = f"{cwd}/{fileName}"


# The cooky Stuff
if path.exists(fileLoc):
  if fileType == "cpp":
    newFileName = fileName.split('.')[0]
    result = subprocess.run([f"g++ {fileName} -o {newFileName}"],shell=True, stdout=subprocess.PIPE, text=True)
    return_code = result.returncode
    if return_code == 0:
      system(f"./{newFileName}")
    else:
      exit()  

  elif fileType == "c":
    newFileName = fileName.split('.')[0]
    result = subprocess.run([f"gcc {fileName} -o {newFileName}"],shell=True, stdout=subprocess.PIPE, text=True)
    return_code = result.returncode
    if return_code == 0:
      system(f"./{newFileName}")
    else:
      exit() 

  elif fileType == "java":
    newFileName = fileName.split('.')[0]
    result = subprocess.run([f"javac {fileName}"],shell=True, stdout=subprocess.PIPE, text=True)
    return_code = result.returncode
    if return_code == 0:
      system(f"java {newFileName}")
    else:
      exit()     
  else:
    print("ERROR! Not a C/C++/java File:",fileName)  
    exit()
else:
  print("ERROR! No Such File exists with Name:",fileName)  
  exit()
print("\n------------------------------------------------")  
