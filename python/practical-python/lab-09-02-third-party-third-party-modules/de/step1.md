# Der Modulsuchpfad

`sys.path` ist ein Verzeichnis, das die Liste aller Verzeichnisse enthält, die vom `import`-Statement überprüft werden. Schauen Sie sich es an:

```python
>>> import sys
>>> sys.path
... schauen Sie sich das Ergebnis an...
>>>
```

Wenn Sie etwas importieren und es nicht in einem dieser Verzeichnisse liegt, erhalten Sie eine `ImportError`-Ausnahme.
