def derivada_direita(f, x0, delta):
  return (f(x0 + delta) - f(x0))/delta
def derivada_centrada(f, x0, delta):
  return (f(x0 + delta) - f(x0-delta))/(2*delta)
def erro(numerico, real = -22.919557190595612):
  return abs(real - numerico)/abs(real)
f = lambda x:x**3*np.sin(x)

#método de newton
def newton(funcao, a, epsilon):
  '''
  Função que encontra uma raiz de uma função arbitrária pelo método de Newton

  Argumentos:

  funcao: função
     
  a: estimativa inicial de raiz(float)

  epsilon: tolerância de cálculo do valor da raiz(float)
  
  '''
  b = a  - f(a)/derivada(f, a) 
  #Itera até que a diferença entre os pontos seja menor a tolerância estabelecida
  while (abs(b-a)> epsilon):
    a = b 
    b = a  - f(a)/derivada(f, a)
  return b
