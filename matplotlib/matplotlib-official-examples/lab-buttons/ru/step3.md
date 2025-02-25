# Создаем функции обратного вызова для кнопок

Теперь создадим две функции обратного вызова для кнопок "Next" (Далее) и "Previous" (Предыдущая). Эти функции будут обновлять график новой синусоидальной волной с другой частотой.

```python
class Index:
    ind = 0

    def next(self, event):
        self.ind += 1
        i = self.ind % len(freqs)
        ydata = np.sin(2*np.pi*freqs[i]*t)
        l.set_ydata(ydata)
        plt.draw()

    def prev(self, event):
        self.ind -= 1
        i = self.ind % len(freqs)
        ydata = np.sin(2*np.pi*freqs[i]*t)
        l.set_ydata(ydata)
        plt.draw()

callback = Index()
```
