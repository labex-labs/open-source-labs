# Warum `super()`?

Verwenden Sie immer `super()` beim Überschreiben von Methoden.

```python
class Loud:
    def noise(self):
        return super().noise().upper()
```

`super()` delegiert an die _nächste Klasse_ in der MRO.

Das Knackige dabei ist, dass Sie nicht wissen, was es ist. Vor allem wissen Sie es nicht, wenn Mehrfachvererbung verwendet wird.
