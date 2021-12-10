#importando bibliotecas
import numpy as np
import matplotlib.pyplot as plt


#Lendo o arquivo pulando as duas primeiras linhas
data = np.genfromtxt('RxT_Giovanni.dat',skip_header=2)  



#le as linhas do arquivo e armazena os valores de V em intervalos
new_data = []    
for counter, j in  enumerate(np.arange(2, 300.5, 0.5)):
  new_data.append([])
  for i in range(len(data)):
      if (data[i][0]>= j) and (data[i][0] < j+0.5):
        new_data[counter].append(data[i][1])

        
new_data_final = np.zeros((len(new_data), 3))
for i in range(len(new_data)-1):
  new_data_final[i][1] = np.mean(new_data[i])
  new_data_final[i][2] = np.std(new_data[i])
for counter, j in  enumerate(np.arange(2, 300.5, 0.5)):
  new_data_final[counter][0] = (2*j + 0.5)/2

#np.savetxt('media_desvio.csv',new_data_final, delimiter=',')
print(new_data_final)
plt.scatter(new_data_final[:, 0], new_data_final[:, 1])
plt.scatter(data[:,0], data[:, 1], color='red')

plt.show()