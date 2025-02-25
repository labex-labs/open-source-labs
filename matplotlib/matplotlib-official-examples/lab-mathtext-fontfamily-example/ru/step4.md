# Задаем шрифт для заголовка

Мы также можем изменить семейство шрифтов для заголовка с использованием параметра `math_fontfamily`.

```python
ax.set_title(r"$Title\ in\ math\ mode:\ \int_{0}^{\infty } x^2 dx$",
             math_fontfamily='stixsans', size=14)
```
