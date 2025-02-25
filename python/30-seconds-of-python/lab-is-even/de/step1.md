# Überprüfen, ob eine Zahl gerade ist

Schreiben Sie eine Funktion `is_even(num)`, die eine Zahl als Argument übernimmt und `True` zurückgibt, wenn die Zahl gerade ist, und `False`, wenn die Zahl ungerade ist. Um zu überprüfen, ob eine Zahl gerade oder ungerade ist, können Sie den Modulo (`%`)-Operator verwenden. Wenn eine Zahl gerade ist, hat sie keinen Rest, wenn sie durch 2 geteilt wird. Wenn eine Zahl ungerade ist, hat sie einen Rest von 1, wenn sie durch 2 geteilt wird.

```python
def is_even(num):
  return num % 2 == 0
```

```python
is_even(3) # False
```
