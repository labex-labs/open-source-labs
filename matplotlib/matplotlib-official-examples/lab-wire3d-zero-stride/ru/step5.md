# Создаем второй подграфик

Мы создадим второй подграфик с параметром `rstride`, установленным в `0`, и параметром `cstride`, установленным в `10`.

```python
ax2.plot_wireframe(X, Y, Z, rstride=0, cstride=10)
ax2.set_title("Row (y) stride set to 0")
```
