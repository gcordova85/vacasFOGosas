import threading
import vclases
from threading import Thread, Lock
from vprocesos import *




def constructor():

	v1=threading.Thread(target=vacaVive, args=("Vaca1",))
	v1.start()

	# v2=threading.Thread(target=vacaVive, args=("vaca2",))
	# v2.start()

	# v3=threading.Thread(target=vacaVive, args=("vaca3",))
	# v3.start()
	
constructor()


