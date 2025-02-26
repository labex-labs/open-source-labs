# Lesen von Attributen mit einfacher Vererbung

In Vererbungs hierarchien werden Attribute indem man in der Reihenfolge den Vererbungsbaum hinauf läuft, gefunden.

```python
class A: pass
class B(A): pass
class C(A): pass
class D(B): pass
class E(D): pass
```

Bei einfacher Vererbung gibt es einen einzigen Pfad zum obersten Element. Man stoppt bei der ersten Übereinstimmung.
