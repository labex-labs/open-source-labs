# Ausnahmen auslösen

Um eine Ausnahme auszulösen, verwenden Sie den `raise`-Befehl.

```python
raise RuntimeError('What a kerfuffle')
```

Dies wird dazu führen, dass das Programm mit einem Ausnahmentraceback abgebrochen wird. Es sei denn, es wird von einem `try-except`-Block gefangen.

```bash
% python3 foo.py
Traceback (most recent call last):
  File "foo.py", line 21, in <module>
    raise RuntimeError("What a kerfuffle")
RuntimeError: What a kerfuffle
```
