import threading
from threading import Thread, Lock
import time
from random import randint
from vprocesos import *

def constructor():
	v1=threading.Thread(target=vacaVive, args=())
	v1.start()

	v2=threading.Thread(target=vacaVive, args=())
	v2.start()

	v3=threading.Thread(target=vacaVive, args=())
	v3.start()
	
constructor()


