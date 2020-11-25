import multiprocessing
import json
import time
costoAudi=0.0
costoJeep=0.0
costoNissan=0.0
costoDodge=0.0

def procesoFuncionA(lista1):   
    global costoAudi
    if lista1[0]=="Audi":        
        costoAudi=float(lista1[1].replace("$", ""))
    else:
        costoAudi=0
    return costoAudi        
    

def procesoFuncionJ(lista1):  
    global costoJeep     
    if lista1[0]=="Jeep":        
        costoJeep=float(lista1[1].replace("$", "")) 
    else:
        costoJeep=0

    return costoJeep
    
       
def procesoFuncionN(lista1): 
    global costoNissan      
    if lista1[0]=="Nissan":        
        costoNissan=float(lista1[1].replace("$", ""))
    else:
        costoNissan=0         
    return costoNissan
    

def procesoFuncionD(lista1):       
    global costoDodge
    if lista1[0]=="Dodge":        
        costoDodge=float(lista1[1].replace("$", ""))
    else:
        costoDodge=0
    return costoDodge
    
   
if __name__=='__main__':
    lista=[]    
    with open(r"C:\Users\TRIGUN\Desktop\UPS_OCTAVO\COMPUTO_PARALELO\Python-Parallel-Programming-Cookbook-Second-Edition\Tarea\vehiculos.json") as file:
        data = json.load(file)

    for vehiculos in data['vehiculos']:                       
        marca=vehiculos['marca_vehiculo']
        costo=vehiculos['costo']
        sublist=[marca,costo]
        lista.append(sublist)        
        
    #print(len(lista))                 
    pool=multiprocessing.Pool(processes=10)
    pool_outputs_A=pool.map(procesoFuncionA,lista)
    pool_outputs_J=pool.map(procesoFuncionJ,lista)
    pool_outputs_N=pool.map(procesoFuncionN,lista)
    pool_outputs_D=pool.map(procesoFuncionD,lista)
               
    start_time = time.time()

    pool.close()
    pool.join()
        
    end_time = time.time()
    print(" Tiempo Procesos={:,.2f}".format((end_time - start_time)))

    print("Audi:   Precio Total:${:,.2f}".format(sum(pool_outputs_A)))
    print("Jeep:   Precio Total:${:,.2f}".format(sum(pool_outputs_J)))
    print("Nissan: Precio Total:${:,.2f}".format(sum(pool_outputs_N)))
    print("Dodge:  Precio Total:${:,.2f}".format(sum(pool_outputs_D)))

    """print("Audi:   Precio Total:${:,.2f}".format(pool_outputs_A.count(1)))
    print("Jeep:   Precio Total:${:,.2f}".format(pool_outputs_J.count(1)))
    print("Nissan: Precio Total:${:,.2f}".format(pool_outputs_N.count(1)))
    print("Dodge:  Precio Total:${:,.2f}".format(pool_outputs_D.count(1)))"""
    
    #print(pool_outputs_A.count(1))
