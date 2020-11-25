import logging
import threading
import json
import time
import os

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

ruta ='Data_Vehiculo.json'
#hilos
Hyundai = []
Chevrolet = []
Toyota = []
Ford = []

condition = threading.Condition()

class VChevrolet(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def consume(self):
        sumatoria = 0;
        with condition:
            if Chevrolet != 0:
                #Lectura del archivo CSV
                with open(ruta) as file:
                    data = json.load(file)
                    for datas in data:
                        if datas["marca_vehiculo"] == 'Chevrolet':
                            costo = datas["costo_vehiculo"]
                            Chevrolet.append(costo)
                            #Eliminacion del signo de dolar
                            eliminarCaracter = costo.replace("$","")
                            costoF= float(eliminarCaracter)
                            sumatoria = sumatoria+costoF;
                    print("Cantidad de Vehiculos Chevrolet: " , len(Chevrolet))
                    print("Valor total de los Vehiculos de Chevrolet: ${:,.2f}" .format(sumatoria))
    def run(self):
        time.sleep(2)
        self.consume()

class VToyota(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def consume(self):
        sumatoria = 0;
        with condition:
            if Toyota!=0:
                # Lectura del archivo CSV
                with open(ruta) as file:
                    data = json.load(file)
                    for datas in data:
                        if datas["marca_vehiculo"] == 'Toyota':
                            costo = datas["costo_vehiculo"]
                            Toyota.append(costo)
                            # Eliminacion del signo de dolar
                            eliminarCaracter = costo.replace("$", "")
                            costoF = float(eliminarCaracter)
                            sumatoria = sumatoria + costoF;
                    print("Cantidad de Vehiculos Toyota: ", len(Toyota))
                    print("Valor total de los Vehiculos de Toyota: ${:,.2f}" .format(sumatoria))
    def run(self):
        time.sleep(2)
        self.consume()

class VFord(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def consume(self):
        sumatoria = 0;
        with condition:
            if Ford !=0:
                # Lectura del archivo CSV
                with open(ruta) as file:
                    data = json.load(file)
                    for datas in data:
                        if datas["marca_vehiculo"] == 'Ford':
                            costo = datas["costo_vehiculo"]
                            Ford.append(costo)
                            # Eliminacion del signo de dolar
                            eliminarCaracter = costo.replace("$", "")
                            costoF = float(eliminarCaracter)
                            sumatoria = sumatoria + costoF;
                    print("Cantidad de Vehiculos Ford: ", len(Ford))
                    print("Valor total de los Vehiculos de Ford: ${:,.2f}" .format(sumatoria))
    def run(self):
        time.sleep(2)
        self.consume()

class VHyundai(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def consume(self):
        sumatoria = 0;
        with condition:
            if Hyundai !=0 :
                # Lectura del archivo CSV
                with open(ruta) as file:
                    data = json.load(file)
                    for datas in data:
                        if datas["marca_vehiculo"] == 'Hyundai':
                            costo = datas["costo_vehiculo"]
                            Hyundai.append(costo)
                            # Eliminacion del signo de dolar
                            eliminarCaracter = costo.replace("$", "")
                            costoF = float(eliminarCaracter)
                            sumatoria = sumatoria + costoF;
                    print("Cantidad de Vehiculos Ford: ", len(Hyundai))
                    print("Valor total de los Vehiculos de Hyundai: ${:,.2f} " .format(sumatoria))
    def run(self):
        time.sleep(2)
        self.consume()

if __name__ == '__main__':
    chevrolet =VChevrolet(name="Chevrolet")
    chevrolet.start()
    chevrolet.join()

    toyota= VToyota(name="Toyota")
    toyota.start()
    toyota.join()

    ford =VFord(name="Ford")
    ford.start()
    ford.join()

    hyundai =VHyundai(name="Hyundai")
    hyundai.start()
    hyundai.join()

