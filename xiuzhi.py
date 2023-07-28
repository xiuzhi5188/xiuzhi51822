import datetime
import time

while True:
    current_time = datetime.datetime.now()
    
    formatted_time = current_time.strftime("%H:%M:%S")
    print("当前时间：", formatted_time)
    
    time.sleep(1)
