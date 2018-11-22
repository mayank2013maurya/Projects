from glob2 import glob
from datetime import  datetime

current_time = datetime.now()
filename = current_time.strftime("%Y-%m-%d-%H-%M-%S-%f") + ".txt"

with open(filename, "w") as file:
    req_files = glob("*.txt")

    for each_file in req_files:

        with open(each_file, "r") as current_file:
            content = current_file.read()
            file.write(content+"\n")
