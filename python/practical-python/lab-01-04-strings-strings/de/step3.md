# String-Darstellung

Jedes Zeichen in einer Zeichenkette wird intern als sogenannter Unicode-"Codepunkt" gespeichert, der eine Ganzzahl ist. Sie können einen genauen Codepunkt-Wert mithilfe der folgenden Escape-Sequenzen angeben:

```python
a = '\xf1'          # a = 'ñ'
b = '\u2200'        # b = '∀'
c = '\U0001D122'    # c = '𝄢'
d = '\N{FOR ALL}'   # d = '∀'
```

Die [Unicode-Charakterdatenbank](https://unicode.org/charts) ist eine Referenz für alle verfügbaren Zeichensymbole.
