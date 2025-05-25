# Criar um Gráfico de Escala Personalizada

O tipo final de transformação de escala que exploraremos é a personalizada (custom). Isso nos permite definir nossas próprias funções forward e inverse para a transformação da escala. Neste exemplo, definiremos uma função personalizada para calcular a raiz quadrada dos dados. Para criar um gráfico de escala personalizada, usamos o método `set_yscale()` e passamos a string `'function'`. Também definimos as funções `forward()` e `inverse()` e as passamos como argumentos para o parâmetro `functions`. Também adicionamos um título e uma grelha ao gráfico.

```python
# Function x**(1/2)
def forward(x):
    return x**(1/2)

def inverse(x):
    return x**2

plt.plot(x, y)
plt.yscale('function', functions=(forward, inverse))
plt.title('Custom Scale')
plt.grid(True)
```
