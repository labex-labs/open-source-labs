# Создаем первый подграфик

Мы создадим первый подграфик с параметром `rstride`, установленным в `10`, и параметром `cstride`, установленным в `0`.

```python
ax1.plot_wireframe(X, Y, Z, rstride=10, cstride=0)
ax1.set_title("Column (x) stride set to 0")
```
