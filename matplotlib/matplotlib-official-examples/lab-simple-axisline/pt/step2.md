# Criar Figura e Subplot

Em seguida, criamos uma figura e adicionamos um subplot com `AxesZero`. Isso cria uma linha de eixo com rótulos para os eixos x e y, mas sem marcas de escala (tick marks) ou grades.

```python
fig = plt.figure()
fig.subplots_adjust(right=0.85)
ax = fig.add_subplot(axes_class=AxesZero)
```
