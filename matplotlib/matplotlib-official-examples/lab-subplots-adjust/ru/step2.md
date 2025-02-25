# Создаем графики

Далее создадим два графика с использованием `imshow` и случайных массивов, сгенерированных с помощью `numpy.random`. Также добавим цветовую шкалу к графикам. Запустите следующий код:

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

plt.subplot(211)
plt.imshow(np.random.random((100, 100)))
plt.subplot(212)
plt.imshow(np.random.random((100, 100)))

cax = plt.axes([0.85, 0.1, 0.075, 0.8])
plt.colorbar(cax=cax)

plt.show()
```
