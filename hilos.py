
from threading import Thread
from queue import Queue
import time
import random
import json

class Producer(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue
        self.contItemsIngresados=0        
                
    def run(self):
        #aqui cargar los datos de JSON es gracioso poner es "r" para que leea  bienn el JSON
        with open(r"C:\Users\TRIGUN\Desktop\UPS_OCTAVO\COMPUTO_PARALELO\Python-Parallel-Programming-Cookbook-Second-Edition\Tarea\vehiculos.json") as file:
            data = json.load(file)

        for vehiculos in data['vehiculos']:            
            self.contItemsIngresados+=1
            #print("Ingresa: ",self.contItemsIngresados)
            self.queue.put(vehiculos)                   
            #time.sleep(0.1)   
              
class Consumer(Thread):        
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue
        self.contA=0
        self.contJ=0
        self.contN=0
        self.contD=0
        #self.precio=0.0
        self.costoAudi=0.0
        self.costoJeep=0.0
        self.costoNissan=0.0
        self.costoDodge=0.0
    def run(self):        
        while True:#not self.queue.empty():            
            item = self.queue.get()
            #print("no sale: ",item['marca_vehiculo'])
            if self.queue.empty():
                break            
            elif item['marca_vehiculo']=="Audi":
                self.costoAudi+=float(item['costo'].replace("$", ""))
                self.contA+=1
            elif item['marca_vehiculo']=="Jeep":
                self.costoJeep+=float(item['costo'].replace("$", ""))
                self.contJ+=1
            elif item['marca_vehiculo']=="Nissan":
                self.costoNissan+=float(item['costo'].replace("$", ""))
                self.contN+=1
            elif item['marca_vehiculo']=="Dodge":
                self.costoDodge+=float(item['costo'].replace("$", ""))
                self.contD+=1
            self.queue.task_done()
            #time.sleep(0.00001)
            print("Tamaño de la Cola: ",self.queue.qsize())
        #self.queue.join()                                                                
        print("Total: ",self.contA,"Audi:   Precio Total:${:,.2f}".format(self.costoAudi))
        print("Total: ",self.contJ,"Jeep:   Precio Total:${:,.2f}".format(self.costoJeep))
        print("Total: ",self.contN,"Nissan: Precio Total:${:,.2f}".format(self.costoNissan))
        print("Total: ",self.contD,"Dodge:  Precio Total:${:,.2f}".format(self.costoDodge)) 
        

if __name__ == '__main__':
    queue = Queue(maxsize=100)#La cola se bloqueara si llega su limite de elementos
    t1 = Producer(queue)
    t2 = Consumer(queue)    

    start_time = time.time() 

    t1.start()                    
    t2.start()
    

    t1.join() 
    t2.join()
    
    end_time = time.time()
    print(" Tiempo Hilos={:,.2f}".format((end_time - start_time)))