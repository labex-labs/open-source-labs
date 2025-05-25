# Criando uma Figura com um Único Subplot

A maneira mais simples de criar um único subplot é usando a função `subplots()` sem nenhum argumento. Esta função retorna um objeto `Figure` e um único objeto `Axes`.

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
```
