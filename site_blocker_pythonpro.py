#website blocking script
"""
if u want to block the websites replace path_temp with host_path.
change file extension to .pyw
open task schedulaer,
create task
assign name..
selcect hightestpriv..select windows version
 choose trigger windows..assign time
 choose actions windwos ..and new
 selcect this file
 choose condition windows and uncheck power option
"""
import time
from datetime import datetime as dt
#replace path_temp with host_path to run it as a pyhtin script in background
path_temp="hosts"
host_path="C:\Windows\System32\drivers\etc\hosts"
redirect_ip="127.0.0.1"
#list of websites u want to block
block_website=["www.9anime.to","9anime.to","ww4.gogoanime.io","https://kissanime.co/","https://9anime.is/","https://kissanime.co/"]
while(True):
    #tm_wday is from 0=mon to 6=sun .so the program deosnt run on saturday
    day=time.localtime().tm_wday

    if dt(dt.now().year,dt.now().month,dt.now().day,0) <dt.now()<dt(dt.now().year,dt.now().month,dt.now().day,23) and day!=5:
        print("study hours..project_python")
        #read the hosts file and copy the content into a variable
        with open(path_temp,'r+') as file1:
            content=file1.read()
            #we check whether the hosts file contains the website to be blocked
            for site in block_website:
                #if the website is listed then we do nothing
                if site in content:
                    pass
                    #else we write the website and the redirect_ip address into the hosts file
                else:
                    file1.write(redirect_ip+"   "+site+"\n")
#if the process is outside provided time then
    else:
        print("fun hours..project_python  ")
        # delete all the websites lemtioned in th ehosts file
        with open(path_temp,'r+') as file2:
            content_lines=file2.readlines()
            file2.seek(0)
            #we check whether the site name is present in each line of the file. if not, then we write the line saved in content_lines
            for line in content_lines:
                #in each line we check whether the name of blocked websites is present
                if not any(site in line for site in block_website):
                    file2.write(line)
            #after the writing the orignal data , deletes the remaining data containing list of blocked websites
            file2.truncate()
    time.sleep(5)
