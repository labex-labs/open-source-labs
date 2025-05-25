# Criar um Gráfico de Escala com Transformação Mercator

Como um bônus, também criaremos um gráfico usando a função de transformação Mercator. Esta não é uma função embutida no Matplotlib, mas podemos definir nossas próprias funções forward e inverse para criar um gráfico de escala com transformação Mercator. Neste exemplo, definiremos as funções `forward()` e `inverse()` para a transformação Mercator. Também adicionamos um título e uma grelha ao gráfico.

```python
# Function Mercator transform
def forward(a):
    a = np.deg2rad(a)
    return np.rad2deg(np.log(np.abs(np.tan(a) + 1.0 / np.cos(a))))

def inverse(a):
    a = np.deg2rad(a)
    return np.rad2deg(np.arctan(np.sinh(a)))

t = np.arange(0, 170.0, 0.1)
s = t / 2.

plt.plot(t, s, '-', lw=2)
plt.yscale('function', functions=(forward, inverse))
plt.title('Mercator Transform Scale')
plt.grid(True)
plt.xlim([0, 180])
```
