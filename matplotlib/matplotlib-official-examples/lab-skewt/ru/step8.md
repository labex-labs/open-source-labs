# Создаем диаграмму SkewT-logP

Теперь мы создадим диаграмму SkewT-logP с использованием проекции SkewXAxes, которую мы зарегистрировали ранее. Сначала мы создадим объект Figure и добавим подграфик с проекцией SkewXAxes. Затем мы построим на диаграмме данные о температуре и точке росы с использованием функции semilogy. Наконец, мы установим пределы и деления для осей X и Y и отобразим график.

```python
fig = plt.figure(figsize=(6.5875, 6.2125))
ax = fig.add_subplot(projection='skewx')

ax.semilogy(T, p, color='C3')
ax.semilogy(Td, p, color='C2')

ax.axvline(0, color='C0')

ax.yaxis.set_major_formatter(ScalarFormatter())
ax.yaxis.set_minor_formatter(NullFormatter())
ax.set_yticks(np.linspace(100, 1000, 10))
ax.set_ylim(1050, 100)

ax.xaxis.set_major_locator(MultipleLocator(10))
ax.set_xlim(-50, 50)

plt.grid(True)
plt.show()
```
