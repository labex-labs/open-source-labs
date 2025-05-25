# Criar uma figura com quatro subplots

Criaremos uma figura com quatro subplots para ilustrar os diferentes aspectos da rasterização.

```python
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, layout="constrained")
```
