# Gerando Dados para o Gráfico de Dispersão

Em seguida, geramos dados para o gráfico de dispersão. Criamos 100 pontos de dados com valores aleatórios de x e y entre 0 e 0.9, e raios aleatórios entre 0 e 10. A cor de cada ponto de dados é determinada pela raiz quadrada de sua área.

```python
N = 100
r0 = 0.6
x = 0.9 * np.random.rand(N)
y = 0.9 * np.random.rand(N)
area = (20 * np.random.rand(N))**2  # 0 to 10 point radii
c = np.sqrt(area)
```
