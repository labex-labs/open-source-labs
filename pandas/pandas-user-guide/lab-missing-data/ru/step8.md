# Понимаем скаляр `NA` для обозначения пропущенных значений

Наконец, мы обсудим экспериментальный скаляр `NA` в pandas, который можно использовать для обозначения пропущенных значений.

```python
s = pd.Series([1, 2, None], dtype="Int64")
s
```
