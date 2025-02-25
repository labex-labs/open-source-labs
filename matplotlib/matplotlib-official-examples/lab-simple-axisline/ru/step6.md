# Создаем вторую ось y

Наконец, мы создадим новую вторую ось y справа от графика с смещением (20, 0) и присвоим ей метку.

```python
ax.axis["right2"] = ax.new_fixed_axis(loc="right", offset=(20, 0))
ax.axis["right2"].label.set_text("Label Y2")
```
