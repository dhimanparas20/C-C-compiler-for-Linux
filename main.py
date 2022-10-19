#Python code to compile c/c++
from time import sleep
from datetime import datetime
from os import system,path

system("clear")
# some colors and presets to use 
VIOLET = '\033[95m'
BLUE = '\033[94m'
CYAN = '\033[96m'
GREEN = '\033[92m'
BROWN = '\033[93m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
RED = '\033[91m'
END = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
HIGH = '\x1b[6;30;42m'
HIGHLIGHT = '\x1b[6;30;43m'

if (path.exists('output') != True):
  system("mkdir output && mkdir output/c_out output/cpp_out")
elif (path.exists('output/c_out') != True):
  system("mkdir output/c_out")
elif (path.exists('output/cpp_out') != True):
  system("mkdir output/cpp_out")  
 
def compile(ext,comp,path,end)  :
  print(f"{RED}---------------------------------------------{END}")
  print(f"{CYAN}|--        COMPILING {ext} PROGRAM          --|")
  t_start = datetime.now()
  system(f"{comp} {file_name} -o output/{path}/{file_name[:end]}.out")
  t_end = datetime.now()
  print(f"\n{BOLD}{VIOLET} Total compile time taken: {t_end-t_start}")
  print(f"\n{CYAN}|--        RUNNING {ext} PROGRAM           --|{END}")
  print(f"{RED}---------------------------------------------{END}\n")
  system(f"./output/{path}/{file_name[:end]}.out")
  
print(f"{RED}-----------------------------------------------------------------------")  
print(f"{YELLOW}|    Enter the name of file to compile and run (with extention name)  |")
print(F"{RED}-----------------------------------------------------------------------{END}")    
file_name = input(f"\n{BROWN}Name :{BLUE} ")

if path.exists(file_name) == True and file_name[-4:] == ".cpp": 
  compile(".cpp","g++","cpp_out",-4)
elif path.exists(file_name) == True and file_name[-2:] == ".c":
  compile(".c","gcc","c_out",-2)

else :
  print(f"\n{GREEN}No such file found try again.\n")  
  sleep(2)
  system("python3 main.py")
