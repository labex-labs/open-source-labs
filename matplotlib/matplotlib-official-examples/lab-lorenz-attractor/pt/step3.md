# Configurar os Parâmetros Iniciais

Configuramos os parâmetros iniciais para a simulação, incluindo o passo de tempo `dt`, o número de passos `num_steps` e os valores iniciais para `x`, `y` e `z`.

```python
dt = 0.01
num_steps = 10000

xyzs = np.empty((num_steps + 1, 3))  # Necessário um a mais para os valores iniciais
xyzs[0] = (0., 1., 1.05)  # Definir valores iniciais
```
