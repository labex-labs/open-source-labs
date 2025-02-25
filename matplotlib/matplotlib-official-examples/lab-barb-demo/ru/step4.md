# Настраиваем график ветровых стрелок

Мы можем настроить график ветровых стрелок, изменив параметры функции barbs. Например, мы можем изменить длину и точку опоры векторов, заполнить круги для пустой стрелочки и изменить цвета флагов и штрихов.

```python
plt.barbs(X, Y, U, V, length=8, pivot='middle', fill_empty=True, rounding=False,
          sizes=dict(emptybarb=0.25, spacing=0.2, height=0.3), flagcolor='r',
          barbcolor=['b', 'g'], flip_barb=True, barb_increments=dict(half=10, full=20, flag=100))
plt.show()
```
