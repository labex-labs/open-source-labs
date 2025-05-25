# Laços (Looping)

A instrução `while` executa um laço (loop).

```python
while num_bills * bill_thickness < sears_height:
    print(day, num_bills, num_bills * bill_thickness)
    day = day + 1
    num_bills = num_bills * 2

print('Number of days', day)
```

As instruções indentadas abaixo do `while` serão executadas enquanto a expressão após o `while` for `true`.
