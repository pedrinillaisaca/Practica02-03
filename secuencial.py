import time
import json

class Proceso():    
    def __init__(self):
        self.contA=0
        self.contJ=0
        self.contN=0
        self.contD=0
        #self.precio=0.0
        self.costoAudi=0.0
        self.costoJeep=0.0
        self.costoNissan=0.0
        self.costoDodge=0.0
    def run(self) :
        with open(r"C:\Users\TRIGUN\Desktop\UPS_OCTAVO\COMPUTO_PARALELO\Python-Parallel-Programming-Cookbook-Second-Edition\Tarea\vehiculos5000.json") as file:
            data = json.load(file)            

        for vehiculos in data['vehiculos']:
            if vehiculos['marca_vehiculo']=="Audi":
                self.costoAudi+=float(vehiculos['costo'].replace("$", ""))
                self.contA+=1
            elif vehiculos['marca_vehiculo']=="Jeep":
                self.costoJeep+=float(vehiculos['costo'].replace("$", ""))
                self.contJ+=1
            elif vehiculos['marca_vehiculo']=="Nissan":
                self.costoNissan+=float(vehiculos['costo'].replace("$", ""))
                self.contN+=1
            elif vehiculos['marca_vehiculo']=="Dodge":
                self.costoDodge+=float(vehiculos['costo'].replace("$", ""))
                self.contD+=1
        print("Total: ",self.contA,"Audi:   Precio Total:${:,.2f}".format(self.costoAudi))
        print("Total: ",self.contJ,"Jeep:   Precio Total:${:,.2f}".format(self.costoJeep))
        print("Total: ",self.contN,"Nissan: Precio Total:${:,.2f}".format(self.costoNissan))
        print("Total: ",self.contD,"Dodge:  Precio Total:${:,.2f}".format(self.costoDodge))                

                                                           
                                        

if __name__ == '__main__':
    p=Proceso()
    start_time = time.time()        
    p.run()
    end_time = time.time()
    print(" Tiempo Secuencial={:,.2f}".format((end_time - start_time)))

    