
"""# Algoritmo de Neville"""

pontos = np.array([[-8.8, 12.6], [-2.3, 6.2], [2.7, 8.4], [1.4, -14.9], [5.1, 18.8]])

def neville(x, pontos):
  n = pontos.shape[0]
  A = np.zeros((n, n))
  A[:, 0] = pontos[:, 1]
  for j in range(1, (n)):
    for i in range(0, (n-j)):
      A[i, j] = 1/(pontos[i, 0] - pontos[i+j, 0])*(((x-pontos[i+j, 0])*A[i, j-1]) - ((x-pontos[i, 0])*A[i+1, j-1]))
  return A[0, n-1]

neville(x,pontos)

# Plotando os pontos e o polinômio interpolador

# Determinando os valores de x para os quais calcularemos o polinômio de Lagrange
x_range = np.linspace(-10,10,100)

# Criando lista para armazenar os valores do polinômio interpolador
y=[]

# Para cada x de x_range calcular o valor do polinômio interpolador e armazena em y
for x in x_range:
  y.append(neville(x,pontos))
y=np.array(y)

# Criando o gráfico 
plt.plot(x_range,y, 'k', label= 'P(x)')  # plotando o polinômio interpolador
plt.scatter(pontos[:,0],pontos[:,1], label='dados') #plotando os pontos de entrada
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
