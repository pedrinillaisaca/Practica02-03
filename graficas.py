import matplotlib.pyplot as plt
import numpy as np

plt.figure()
plt.title("Tiempos")
plt.xlabel("Vehiculos")   # Inserta el título del eje X
plt.ylabel("Segundos")   # Inserta el título del eje Y
secuencial=[0.01,0.1,0.5,0.25,0.5]
hilos=[1.58,1.63,1.96,2.15,2.44]
#procesos=[16.96,31.20,46.76,62.26,77.87]
mpi=[0.00,0.04,0.04,0.05,0.07]
plt.xticks(np.arange(5),('1000','2000','3000','4000','5000'))
plt.yticks(np.arange(0,0.5,2))
plt.plot(secuencial,marker='x',color="b",linestyle=':',label='Secuencial')
plt.plot(hilos,marker='*',color="r",linestyle='-.',label='Hilos')
#plt.plot(procesos,marker='x',color="g",linestyle='-',label='Procesos')
plt.plot(mpi,marker='o',color="c",linestyle='--',label='MPI')
plt.legend(loc='upper left')
plt.show()
