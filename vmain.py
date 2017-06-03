import time
import threading
from vprocesos import *

def main():
	v1=threading.Thread(target=vacaVive, args=())
	v1.start()
	time.sleep(1)
	v2=threading.Thread(target=vacaVive, args=())
	v2.start()
	time.sleep(1)
	v3=threading.Thread(target=vacaVive, args=())
	v3.start()
	time.sleep(1)

main()
