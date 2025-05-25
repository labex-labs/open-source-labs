# Definir a Função de Passeio Aleatório

Definimos uma função que gera um passeio aleatório com um determinado número de passos e tamanho máximo do passo. A função recebe duas entradas: `num_steps` é o número total de passos no passeio aleatório e `max_step` é o tamanho máximo de cada passo. Usamos `numpy.random` para gerar números aleatórios para os passos e `numpy.cumsum` para calcular a soma cumulativa dos passos para obter a posição final.

```python
def random_walk(num_steps, max_step=0.05):
    """Return a 3D random walk as (num_steps, 3) array."""
    start_pos = np.random.random(3)
    steps = np.random.uniform(-max_step, max_step, size=(num_steps, 3))
    walk = start_pos + np.cumsum(steps, axis=0)
    return walk
```
