import threading
import time
import logging
from t import Cliente, Casino

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


logging.basicConfig(level=logging.DEBUG,format='[%(levelname)s] (%(threadName)-s) %(message)s')

casino = Casino()

c = []
for i in range(3):
    c.append(Cliente((i+1),casino))

for i in c:
    i.start()
    
for i in c:
    i.join()
'''

logging.basicConfig(level=logging.DEBUG,format='[%(levelname)s] (%(threadName)-s) %(message)s')
#logging.debug("Comida "+str(i)+" servida!")

semaforo_servir = threading.Semaphore(1)
semaforo_sacarB = threading.Semaphore(1)
semaforo_dejarB = threading.Semaphore(1)
cantidad_clientes = 4
cantidad_bandejas = 2
bandejon = 0

def sacarB():
    logging.debug("Sacar bandeja")
    global cantidad_bandejas
    cantidad_bandejas-=1
    semaforo_sacarB.release()
    return


def dejarB():
    logging.debug("Dejar bandeja")
    global bandejon
    bandejon+=1
    semaforo_dejarB.release()
    return

def juan(servir):
    global cantidad_bandejas
    if servir==1:
        cantidad_bandejas-=1
        print("sirviendo...")
        time.sleep(3)
        semaforo_servir.release()
        logging.debug("Listo comida")
    
    
    return

def cliente(i):
    print("Hola! Soy el cliente "+str(i))
    if i==1:
        print("Acompaño al cliente "+str(i+1))
    else:
        print("Sacando bandeja...")
        semaforo_sacarB.acquire()
        sacarB()
        logging.debug("Pedir comida "+str(i))
        
        semaforo_servir.acquire()
        juan(1)
        print("Comiendo..."+str(i))
        time.sleep(5)
        print("Dejando bandeja..."+str(i))
        semaforo_dejarB.acquire()
        dejarB()



    return

def casino():
    print("Casino abierto!")

    t_j = threading.Thread(target=juan,name="juan",args=(0, ))
    t_j.start()
    print("Llego juan")

    global cantidad_clientes 


    t_c = []
    for i in range(cantidad_clientes):
        
        t = threading.Thread(target=cliente,name="Cliente-"+str(i+1),args=(i+1, ))
        t_c.append(t)
        t.start()
    
    t_j.join()
    return

casino()
