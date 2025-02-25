# Создаем фигуру и подграфики

В этом шаге мы создадим фигуру с двумя подграфиками для накопленных распределений. Также установим размер фигуры в 9x4.

```python
fig = plt.figure(figsize=(9, 4), layout="constrained")
axs = fig.subplots(1, 2, sharex=True, sharey=True)
```
