# Das Finden von Modulen

Python konsultiert eine Pfadliste (`sys.path`), wenn es nach Modulen sucht.

```python
>>> import sys
>>> sys.path
[
  '',
  '/usr/local/lib/python36/python36.zip',
  '/usr/local/lib/python36',
...
]
```

Das aktuelle Arbeitsverzeichnis steht normalerweise zuerst in der Liste.
