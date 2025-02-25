# Добавление горизонтальных сеточных линий

Наконец, мы добавим горизонтальные сеточные линии к диаграммам "ящик с усами" с использованием функции `yaxis.grid()`.

```python
for ax in [ax1, ax2]:
    ax.yaxis.grid(True)
    ax.set_xlabel('Three Separate Samples')
    ax.set_ylabel('Observed Values')

plt.show()
```
