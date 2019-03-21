x=[]
import time
while(1):
    try:
        x.append("hello")
        time.sleep(0.5)
        print(x)
    except KeyboardInterrupt:
        break