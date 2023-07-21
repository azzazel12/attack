import requests
import re
url = open(input("[+] Masukan file list domain : "))
filternya = input(str("[+] masukan domain yang mau di filter, cth : id : "))
for url in url:
    dom = url.split(".")[-1]
    url = url.replace("\n", "")
    if filternya in dom:
        print(url)
        open("filter.txt", "a+").write(url + "\n")
        
#By AXVDIGITAL
