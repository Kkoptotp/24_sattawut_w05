from datetime import datetime, date, timedelta
import time

today = date.today()

# print(f"วันที่ {today}")
# print(f"วัน {today.day}")
# print(f"เดือน {today.month}")
# print(f"ปี {today.year}")

now = datetime.now()
# print(now)
# print(f"เวลาปัจจุบัน Hr: {now.hour}")
# print(f"เวลาปัจจุบัน m: {now.minute}")
# print(f"เวลาปัจจุบัน s: {now.second}")

# จัด Format ว ด ป
formatted_date = now.strftime("%d-%m-%Y")
formatted_time = now.strftime("%H-%M-%S")

# print(formatted_date)

# คำนวณวันที่
tomorow = today + timedelta(days=1)
print(tomorow)