# Стилизация легенды

Наконец, мы можем стилизовать легенду, чтобы сделать ее более наглядной. Мы используем функцию `get_frame`, чтобы получить рамку легенды, а затем функцию `set_facecolor`, чтобы установить цвет фона рамки.

```python
# Put a nicer background color on the legend.
legend.get_frame().set_facecolor('C0')
```
