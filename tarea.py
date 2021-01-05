import threading
import time
import logging

'''
logging.basicConfig(level=logging.DEBUG,format='[%(levelname)s] (%(threadName)-s) %(message)s')
def juan(n):
    time.sleep(3)
    logging.debug("lalalla soy juan")
    print("Soy juan",n)
    print(threading.currentThread().getName())

thread_j = threading.Thread(target=juan,name="juan",args=(1, ))

thread_j.start() 
thread_j.join()
'''

#tarea:

cant_clientes = 4
cant_bandejas = 8
bandejero = 0
semaforo = threading.Semaphore(1)

logging.basicConfig(level=logging.DEBUG,format='[%(levelname)s] (%(threadName)-s) %(message)s')

def cliente(i):
    print("Soy cliente ",i)
    global cant_bandejas
    print("Pidiendo comida...")
    cant_bandejas -= 1
    semaforo.acquire()
    juan(i)
    semaforo.release()    

    return 

def juan(i):
    print("sirviendo a cliente ",i,"...\n")
    time.sleep(3)
    logging.debug("Comida "+str(i)+" servida!")

    return

def fila_almuerzo():
    return

#t_juan = threading.Thread(target=juan,name="juan")
t_cliente = threading.Thread(target=cliente,name="cliente")

#t_juan.start()
threads = []
for i in range(1,cant_clientes):
    t = threading.Thread(target=cliente,args=(i, ))
    threads.append(t)
    t.start()

for j in threads:
    j.join()

print(cant_bandejas)

#t_juan.join()

