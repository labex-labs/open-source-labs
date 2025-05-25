# Plotando Múltiplas Linhas

Também podemos plotar múltiplas linhas com diferentes estilos em uma única chamada de função usando arrays. Vamos plotar três linhas: uma linha vermelha tracejada, quadrados azuis e triângulos verdes:

```python
import numpy as np

t = np.arange(0., 5., 0.2)

plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()
```

Explicação:

- Usamos o módulo `numpy` para criar um array `t` com valores de tempo amostrados uniformemente.
- A função `plot` é chamada com três pares de valores `x` e `y`, seguidos pelas strings de formato `'r--'` (linha vermelha tracejada), `'bs'` (quadrados azuis) e `'g^'` (triângulos verdes).
