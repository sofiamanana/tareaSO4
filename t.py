import threading
import time
import logging
import datetime

#logging.basicConfig(level=logging.DEBUG,format='[%(levelname)s] (%(threadName)-s) %(message)s')

#Clases:

logging.basicConfig(level=logging.DEBUG,format='[%(levelname)s] (%(threadName)-s) %(message)s')

class Juan:
    def __init__(self):
        self.Servir = threading.Semaphore(1)
        self.Reponer = threading.Semaphore(1)

    def Servir(self):
        return

    def Reponer(self):
        return

class Casino:
    def __init__(self): #agregar parametro despues
        self.bandejas = 3
        self.bandejero = 0
        self.c_actual = 0
        self.cantidad_total = 4
        self.s_bandejero = threading.Semaphore(self.bandejas/2)
        self.s_cliente = threading.Semaphore(self.cantidad_total)
        

    def entra_c(self):
        self.s_cliente.acquire()
        self.c_actual+=1

    def sale_c(self):
        self.s_cliente.release()
        self.c_actual-=1

    def servir_c(self):
        return

class Cliente(threading.Thread):
    def __init__(self,i,casino):
        threading.Thread.__init__(self)
        self.nombre = "Cliente-"+str(i)
        self.Comiendo = threading.Semaphore(1)
        self.Ayudando = False
        self.casino = casino

    def existir(self):
        self.casino.entra_c()
        self.casino.sale_c()





    

'''
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
'''