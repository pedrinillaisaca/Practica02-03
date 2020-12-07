import numpy as np
from mpi4py import MPI 
import json
import sys
import time
comm = MPI.COMM_WORLD 
rank = comm.rank

start_time = time.time() 

#mapa={"Audi":0,"Jeep":0,"Nissan":0,"Dodge":0}#RESPETA EL FORMATO DEL MAPA
with open(r"C:\Users\TRIGUN\Desktop\UPS_OCTAVO\COMPUTO_PARALELO\Python-Parallel-Programming-Cookbook-Second-Edition\Tarea\vehiculos.json") as file:
    data = json.load(file)
listTemp=[]
for vehiculos in data['vehiculos']:                       
    lisAux=[]
    aux=float(vehiculos['costo'].replace("$",""))
    lisAux.append(vehiculos['marca_vehiculo'])
    lisAux.append(vehiculos['costo'])
    listTemp.append(lisAux)

lista=np.zeros(5,dtype=np.float)#formato de salida
recvdata=lista
#lista1=np.zeros(4,dtype=np.int)#formato de salida    
lista1=np.zeros(5,dtype=np.float)#formato de salida    
def contar(aux):
    global lista1 
    for i in aux:
        if i[0]=="Audi":            
            lista1[0]+=float(i[1].replace("$","")) 
        elif i[0]=="Jeep":
            lista1[1]+=float(i[1].replace("$",""))
        elif i[0]=="Nissan":
            lista1[2]+=float(i[1].replace("$",""))
        elif i[0]=="Dodge":
            lista1[3]+=float(i[1].replace("$",""))           

intervalo=len(listTemp)/4#Lo Divido por 4 por que es una constante, Ademas es el numero de autos de los que deseo conocer su valor total.
if rank==0:
    aux=listTemp[0:int(intervalo-1)]#Esto hace que en verdad el algoritmo sea paralelo
    contar(aux)
elif rank==1:
    aux=listTemp[int(intervalo):int((intervalo*2)-1)]#Esto hace que en verdad el algoritmo sea paralelo
    contar(aux)
elif rank==2:
    aux=listTemp[int(intervalo*2):int((intervalo*3)-1)]#Esto hace que en verdad el algoritmo sea paralelo                                               
    contar(aux)
elif rank==3:
    aux=listTemp[int(intervalo*3):int(intervalo*4)]#Esto hace que en verdad el algoritmo sea paralelo
    contar(aux)

end_time = time.time()
lista1[4]=float(end_time - start_time)
#PILAS AQUI!!!!!!!!!!!!!!            
senddata = lista1
#print(" process %s sending %s " %(rank , senddata))
comm.Reduce(senddata,recvdata,root=0,op=MPI.SUM)
if rank==0:
    #print("Trabajando %s after Reduce: %s" % (rank,recvdata))
    print("Audi:   Precio Total:{:,.2f}".format(recvdata[0]))
    print("Jeep:   Precio Total:{:,.2f}".format(recvdata[1]))
    print("Nissan: Precio Total:{:,.2f}".format(recvdata[2]))
    print("Dodge:  Precio Total:{:,.2f}".format(recvdata[3]))
    print("Tiempo de Ejecución:{:,.2f}".format(recvdata[4]))


