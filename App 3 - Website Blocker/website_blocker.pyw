import time
from datetime import datetime as dt

host_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"

website_list = ["www.facebook.com", "facebook.com", "www.twitter.com", "twitter.com", "https://twitter.com"]

while True:
    starting_time = dt(dt.now().year, dt.now().month, dt.now().day, 8)
    current_time = dt.now()
    ending_time = dt(dt.now().year, dt.now().month, dt.now().day, 17)

    if starting_time < current_time < ending_time:
        print("Working Hours...")
        with open(host_path, "r+") as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")

    else:
        with open(host_path, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)

            file.truncate()
        print("Fun Hours...")

    time.sleep(5)
