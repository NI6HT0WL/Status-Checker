# This script checks for ICMP responses from a list of domains
# or IP addresses and prints whether they respond
# it is set to run every 15 seconds

from pythonping import ping
from re import search
from time import time, sleep
from datetime import datetime

# Define colours
def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

# Define current date & time
def getTime():
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    print("Time:", current_time)

# Define sites to check status
sitesToCheck = ["google.com", "1.2.4.2", "bbc.co.uk"]

# Pings each site from array and checks for reply
# if site responds to ICMP then print live
# if site responds with request timed out then print not live
def pingCheck():
    for site in sitesToCheck:
        pingSite = ping(site, count=1, verbose=False)

        if search("Request timed out", str(pingSite)):
            print(colored(255, 0, 0, site + ": Not Live"))
        else:
            print(colored(0, 128, 0, site + ": Live"))

# Run every 15 seconds
while True:
    sleep(15 - time() % 15)
    getTime()
    pingCheck()