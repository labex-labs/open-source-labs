# Assertionen

Die `assert`-Anweisung ist eine interne Prüfung für das Programm. Wenn ein Ausdruck nicht wahr ist, wird eine `AssertionError`-Ausnahme ausgelöst.

Syntax der `assert`-Anweisung.

```python
assert <expression> [, 'Diagnostische Nachricht']
```

Beispielsweise.

```python
assert isinstance(10, int), 'Erwartet int'
```

Sie sollte nicht verwendet werden, um die Benutzereingabe zu überprüfen (z. B. Daten, die auf einem Webformular eingegeben werden). Ihr Zweck liegt eher in internen Prüfungen und Invarianten (Bedingungen, die immer wahr sein sollten).
