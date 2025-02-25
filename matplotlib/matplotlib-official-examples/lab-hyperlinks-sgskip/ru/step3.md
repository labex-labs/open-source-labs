# Создаем изображение с гиперссылкой

В этом шаге мы создадим изображение и добавим к нему гиперссылку. Вот код для создания изображения:

```python
fig = plt.figure()
delta = 0.025
x = y = np.arange(-3.0, 3.0, delta)
X, Y = np.meshgrid(x, y)
Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
Z = (Z1 - Z2) * 2

im = plt.imshow(Z, interpolation='bilinear', cmap=cm.gray,
                origin='lower', extent=[-3, 3, -3, 3])
```

Для добавления гиперссылки к изображению мы должны использовать метод `set_url()` объекта изображения. Этот метод принимает URL-адрес в качестве аргумента. Вот обновленный код:

```python
im.set_url('https://www.google.com/')
```

Изображение будет иметь гиперссылку на `https://www.google.com/`. Наконец, мы можем сохранить график в файл SVG с использованием `fig.savefig()`:

```python
fig.savefig('image.svg')
```
