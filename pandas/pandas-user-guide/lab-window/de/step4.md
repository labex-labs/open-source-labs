# Führen Sie eine exponentiell gewichtete Fensteroperation durch

Führen Sie eine exponentiell gewichtete Fensteroperation durch und berechnen Sie dann den Mittelwert für jedes Fenster.

```python
# Führen Sie eine exponentiell gewichtete Fensteroperation durch und berechnen Sie den Mittelwert für jedes Fenster
s.ewm(span=3).mean()
```
