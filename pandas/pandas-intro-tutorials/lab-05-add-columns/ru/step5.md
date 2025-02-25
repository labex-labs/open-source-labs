# Преобразовать метки колонок в нижний регистр

Наконец, мы преобразуем метки колонок в нижний регистр с использованием функции.

```python
# Convert column labels to lowercase
air_quality_renamed = air_quality_renamed.rename(columns=str.lower)
```
