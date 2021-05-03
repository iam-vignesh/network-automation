import os
import csv


print("+------------------------------------------------------------------+")
with open('PATH TO FILE\\filename.csv', newline='') as csvfile:
    filereader = csv.reader(csvfile)
    next(filereader)
    for row in filereader:
        ips = (row[0])
        print(f"Pinging....{ips}")
        ping_response = os.popen(f"ping {ips}").read()
        if "Received = 4" in ping_response:
            print(f"{ips} is UP. Ping Successful!")
        else:
            print(f"Ping to {ips} failed. Log entry created!")
            down_ip = []
            down_ip.append(ips)
            with open('down iplist.csv', 'a' , newline='') as writefile:
                w = csv.writer(writefile)
                w.writerow(down_ip)
        print("+------------------------------------------------------------------+")


