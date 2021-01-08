import threading
import time
import logging
'''
logging.basicConfig(level=logging.DEBUG,format='[%(levelname)s] (%(threadName)-s) %(message)s')
cantidad_clientes = 4
semaforo_juan = threading.Semaphore(1)
semaforo_sacarB = threading.Semaphore(1)
k = 0
def sacarB():
    logging.debug("sacando b")
    semaforo_sacarB.release()
    return

def juan(servir):
    return

def cliente(i):
    print("llego cliente ",i)
    logging.debug("Saca bandeja")
    semaforo_sacarB.acquire()
    sacarB()
    semaforo_juan.release()
    global k
    k = 1

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
        semaforo_juan.acquire()
    
    for t in t_c:
        t.join()
    
    t_j.join()
    return

casino()
'''
def wait_for_event(e):
    """Wait for the event to be set before doing anything"""
    logging.debug('wait_for_event starting')
    event_is_set = e.wait()
    logging.debug('event set: %s', event_is_set)


def wait_for_event_timeout(e, t):
    """Wait t seconds and then timeout"""
    while not e.is_set():
        logging.debug('wait_for_event_timeout starting')
        event_is_set = e.wait(t)
        logging.debug('event set: %s', event_is_set)
        if event_is_set:
            logging.debug('processing event')
        else:
            logging.debug('doing other work')


logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

e = threading.Event()
t1 = threading.Thread(
    name='block',
    target=wait_for_event,
    args=(e,),
)
t1.start()

t2 = threading.Thread(
    name='nonblock',
    target=wait_for_event_timeout,
    args=(e, 2),
)
t2.start()

logging.debug('Waiting before calling Event.set()')
time.sleep(3)
e.set()
logging.debug('Event is set')