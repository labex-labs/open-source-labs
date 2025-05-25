# Criar uma Figura com Dois Subplots

Primeiramente, precisamos criar uma figura com dois _subplots_ (subgráficos). Usaremos o método `plt.subplots()` para criar uma figura com dois _subplots_ lado a lado.

```python
import matplotlib.pyplot as plt

fig, (ax, ax2) = plt.subplots(1, 2, figsize=[5.5, 2.8])
```
