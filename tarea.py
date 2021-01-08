import threading
import time
import logging


logging.basicConfig(level=logging.DEBUG,format='[%(levelname)s] (%(threadName)-s) %(message)s')
#logging.debug("Comida "+str(i)+" servida!")

cantidad_clientes = 3
cantidad_bandejas = 2
bandejon = 0

semaforo_servir = threading.Semaphore(1)
semaforo_sacarB = threading.Semaphore(cantidad_bandejas)
semaforo_dejarB = threading.Semaphore(1)
semaforo_rellenar = threading.Semaphore(1)
semaforo_juan = threading.Semaphore(1)


e_juan = threading.Event()

def rellenar():
    global bandejon
    print("Rellenando...")
    while bandejon !=0 :
        semaforo_sacarB.release()
    time.sleep(3)
    semaforo_rellenar.release()
    logging.debug("Bandejas listas")
    return


def sacarB():
    logging.debug("Sacar bandeja")
    return


def dejarB():
    logging.debug("Dejar bandeja")
    global bandejon
    bandejon+=1
    semaforo_dejarB.release()
    return

def juan(accion):
    while accion!=1:
        logging.debug("Comienza hebra")
        event_is_set = e_juan.wait()
    
        logging.debug('event set: %s', event_is_set)
        
        logging.debug("Unset event")
        e_juan.clear()
        semaforo_juan.release()


    '''
    global cantidad_bandejas
    logging.debug("Sriviendo...")

    time.sleep(3)
    semaforo_servir.release()
    logging.debug("Listo comida")

    if accion==2:
        rellenar()
    '''
    return

def cliente(i):

    if i != 1:
        
        logging.debug("Comienza hebra")
        time.sleep(2)
        logging.debug("Setting event")
        semaforo_juan.acquire()
        e_juan.set()
        
        logging.debug("Event set")
        logging.debug("lalallalalal")
    if i == 3:
        juan(1)
        

    '''
    almuerzo = 0
    print("Hola! Soy el cliente "+str(i))

    if i==1:
        almuerzo = 1
        print("Acompaño al cliente "+str(i+1))

    else:
        print("Sacando bandeja...")
        if semaforo_sacarB.acquire():
            sacarB()
        else: 
            semaforo_rellenar.acquire()
            #semaforo_juan.release()
            
        logging.debug("Pedir comida "+str(i))
        e_juan.set()
        semaforo_servir.acquire()
        juan(1)
        print("Comiendo..."+str(i))
        time.sleep(5)
        print("Dejando bandeja..."+str(i))
        semaforo_dejarB.acquire()
        dejarB()
    '''
    return

def casino():
    print("Casino abierto!")
    t_j = threading.Thread(target=juan,name="Juan",args=(0, ))
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
