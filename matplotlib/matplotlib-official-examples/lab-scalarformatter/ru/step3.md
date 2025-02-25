# Создать подграфики для примерных графиков

Мы создадим сетку подграфиков размером 3 x 3, чтобы показать наши примерные графики.

```python
fig, axs = plt.subplots(
    3, 3, figsize=(9, 9), layout="constrained", gridspec_kw={"hspace": 0.1})
```
