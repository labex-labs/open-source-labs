# Representación de cadenas

Cada carácter en una cadena se almacena internamente como un llamado "punto de código" Unicode, que es un entero. Puedes especificar un valor exacto de punto de código usando las siguientes secuencias de escape:

```python
a = '\xf1'          # a = 'ñ'
b = '\u2200'        # b = '∀'
c = '\U0001D122'    # c = '𝄢'
d = '\N{FOR ALL}'   # d = '∀'
```

La [Unicode Character Database](https://unicode.org/charts) es una referencia para todos los códigos de caracteres disponibles.
