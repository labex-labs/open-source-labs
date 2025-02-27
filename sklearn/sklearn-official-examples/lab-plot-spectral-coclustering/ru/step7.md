# Вычисляем коэффициент консенсуса

Мы вычисляем коэффициент консенсуса для бикластеров с использованием функции `consensus_score()`.

```python
score = consensus_score(model.biclusters_, (rows[:, row_idx], columns[:, col_idx]))
print("consensus score: {:.3f}".format(score))
```
