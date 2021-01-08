import threading
import time
import logging

class Juan:
    #Servir, reponer bandejas
    def __init__(self):

class Casino:
    #Fila de almuerzo, bandejon, cantidad de bandejas, juan
    def __init__(self):
        self.SacarB = threading.Semaphore(1)
        self.sacar_b = False

    def SacarBandeja(self):
        self.SacarB.acquire()
        if self.sacar_b:
            self.SacarB.release()
            return False
        else:
            self.sacar_b = True
            self.SacarB.release()
            self.SacarB.acquire()
            self.sacar_b = False
            self.SacarB.release()
            return True

class Cliente:
    #Sacar bandeja, servirse, comer, dejar bandeja y acompañar
    def __init__(self, casino, i):
        threading.Thread.__init__(self)
        self.casino = casino
        self.nombre = "Cliente-"+str(i)
    
    def run(self):
        return
