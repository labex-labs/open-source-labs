# Typüberprüfung

Wie man herausfindet, ob ein Objekt vom angegebenen Typ ist.

```python
if isinstance(a, list):
    print('a ist eine Liste')
```

Überprüfung auf einen von mehreren möglichen Typen.

```python
if isinstance(a, (list,tuple)):
    print('a ist eine Liste oder ein Tupel')
```

\*Vorsicht: Machen Sie nicht zu viel Typüberprüfung. Dies kann zu einer übermäßigen Codekomplexität führen. Normalerweise würden Sie dies nur tun, wenn dadurch häufige Fehler anderer, die Ihr Code verwenden, vermieden werden können.
