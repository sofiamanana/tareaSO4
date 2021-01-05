import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG,format='[%(levelname)s] (%(threadName)-s) %(message)s')
def cliente():
    logging.debug("Cliente creado")

    return

def juan(c_clientes,c_bandejas):
    logging.debug("lalala")
    threads = []
    for i in range(c_clientes):
        t_c = threading.Thread(target=cliente,name=str(i))
        threads.append(t_c)
        t_c.start()
    for i in threads:
        i.join()
    return

c_clientes = 4
c_bandejas = 5

t_juan = threading.Thread(target=juan,name="juan",args=(c_clientes,c_bandejas))
t_juan.start()
t_juan.join()