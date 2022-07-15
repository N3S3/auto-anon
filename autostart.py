#!/usr/bin/python3

import os
import subprocess
import time
import optparse


print("""This a Autostartscript wich is updating, upgrading the OS and starts the Anonymous-Script by keeganjk to connect via the TOR-Network and much more everytime You boot the OS.""")
time.sleep(4)


print("Update and upgrade the OS.")
time.sleep(1)
os.system("sudo apt update && sudo apt full-upgrade -y")

print("Checking Git Installation.")
time.sleep(1)
os.system("sudo apt install git")

print("Checking Anon-Script.")
time.sleep(1)
os.system("sudo git clone https://github.com/keeganjk/kali-anonymous.git")
os.chdir("/home/user/kali-anonymous/")
os.system("sudo chmod +x setup")
os.system("sudo bash setup")


print("""d8888          888                        d8888                            
        d88888          888                       d88888                            
       d88P888          888                      d88P888                            
      d88P 888 888  888 888888 .d88b.           d88P 888 88888b.   .d88b.  88888b.  
     d88P  888 888  888 888   d88""88b         d88P  888 888 "88b d88""88b 888 "88b 
    d88P   888 888  888 888   888  888        d88P   888 888  888 888  888 888  888 
   d8888888888 Y88b 888 Y88b. Y88..88P       d8888888888 888  888 Y88..88P 888  888 
  d88P     888  "Y88888  "Y888 "Y88P"       d88P     888 888  888  "Y88P"  888  888 
                                                                                  """)

time.sleep(5)

parser  = optparse.OptionParser()
b_info  = os.system("sudo anonymous")
starter = os.system("sudo anonymous start")
stopper = os.system("sudo anonymous stop")
stati   = os.system("sudo anonymous status")
updat   = os.system("sudo anonymous update")

parser.add_option("-i", "--info",      dest = "b_info",  help = "Displays basic Info")
parser.add_option("-s", "--start",     dest = "starter", help = "Starts the anonymous script")
parser.add_option("-q", "--quit",      dest = "stopper", help = "Stops the anonymous script")
parser.add_option("-c", "--condition", dest = "stati",   help = "Checks the condition of the script")
parser.add_option("-u", "--update",    dest = "updat",   help = "Updates the anonymous script")
