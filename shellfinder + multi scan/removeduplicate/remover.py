import os
from colorama import Fore,init

if os.name == "nt":
	os.system("cls")
else:
	os.system("clear")

init(convert=True)

class settings:
	y = Fore.YELLOW
	r = Fore.RED
	b = Fore.BLUE



print("""{}
Duplicate Remover by @AXVDIGITAL
""".format(settings.y,settings.r,settings.y,settings.r,settings.y,settings.r,settings.y,settings.r,settings.y,settings.r,settings.y))
lines_seen = set()
namafile = input("[#] Input List : ")
outfile = open('result.txt', "w")
infile = open(namafile, "r")
for line in infile:
	if line not in lines_seen:
		outfile.write(line)
		lines_seen.add(line)
outfile.close()
infile.close()
if os.name == "nt":
	os.system("del sitelist.txt")
else:
	os.system("rm -rf sitelist.txt")
print("[{}+{}] Done......✔️".format(settings.r,settings.y))
print("\n[{}+{}] Sites saved as {}result.txt{}!".format(settings.r,settings.y,settings.b,settings.y))