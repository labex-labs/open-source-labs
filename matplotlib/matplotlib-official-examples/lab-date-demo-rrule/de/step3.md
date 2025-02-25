# Setze die Wiederholungsregel

Du wirst benutzerdefinierte Datumsmarkierungen für jeden fünften Ostersonntag setzen. Dazu musst du die Wiederholungsregel mit der Funktion `rrulewrapper` setzen.

```python
rule = rrulewrapper(YEARLY, byeaster=1, interval=5)
```
