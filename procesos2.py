import multiprocessing
import random
import time
import json

class producer(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue

    def run(self) :
        with open(r"C:\Users\TRIGUN\Desktop\UPS_OCTAVO\COMPUTO_PARALELO\Python-Parallel-Programming-Cookbook-Second-Edition\Tarea\vehiculos.json") as file:
            data = json.load(file)            

        for vehiculos in data['vehiculos']:                                                
            self.queue.put(vehiculos)                   
             
        
       
class consumer(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
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
        while True:
            time.sleep(0.01)#EL PROCESO ES MAS BESTIA YA QUE TENGO QUE HACERLE ESPERAR A LA CARGA DE DATOS DE LA COLA
            #print("Tamaño de la Cola: ",self.queue.qsize())
            item = self.queue.get()
            if (self.queue.empty()):
                print("LA COLA ESTA VACIA...:(")
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
            #self.queue.task_done()
            
        print("Total: ",self.contA,"Audi:   Precio Total:${:,.2f}".format(self.costoAudi))
        print("Total: ",self.contJ,"Jeep:   Precio Total:${:,.2f}".format(self.costoJeep))
        print("Total: ",self.contN,"Nissan: Precio Total:${:,.2f}".format(self.costoNissan))
        print("Total: ",self.contD,"Dodge:  Precio Total:${:,.2f}".format(self.costoDodge))

        """
            else :
                time.sleep(2)
                item = self.queue.get()
                print ('Proceso consumido : item %d popped \
                        from by %s \n'\
                       % (item, self.name))
                time.sleep(1)"""

if __name__ == '__main__':
    queue = multiprocessing.Queue(maxsize=100)#MAXIMO DE ELEMENTOS QUE SE PUEDEN CARGAR EN LA COLA 
    process_producer = producer(queue)
    process_consumer = consumer(queue)


    start_time = time.time()
    process_producer.start()
    process_consumer.start()

    process_producer.join()
    process_consumer.join()        
    end_time = time.time()
    print(" Tiempo Procesos={:,.2f}".format((end_time - start_time)))