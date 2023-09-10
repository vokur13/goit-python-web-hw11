from datetime import datetime

s = "10-01-2020"
print(datetime.strptime(s, "%d-%m-%Y"))  # 2020-01-10 00:00:00
