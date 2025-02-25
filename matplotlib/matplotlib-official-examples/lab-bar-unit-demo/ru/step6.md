# Добавляем метки и заголовок к графику

Последним шагом является добавление меток и заголовка к графику. Мы добавим заголовок к графику, метку для оси x и легенду для графика.

```python
ax.set_title('Cup height by group and beverage choice')
ax.set_xlabel('Group')
ax.legend()
ax.autoscale_view()
```
