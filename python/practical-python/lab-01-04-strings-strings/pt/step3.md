# Representação de String

Cada caractere em uma string é armazenado internamente como um chamado "code-point" Unicode, que é um inteiro. Você pode especificar um valor de code-point exato usando as seguintes sequências de escape:

```python
a = '\xf1'          # a = 'ñ'
b = '\u2200'        # b = '∀'
c = '\U0001D122'    # c = '𝄢'
d = '\N{FOR ALL}'   # d = '∀'
```

O [Unicode Character Database](https://unicode.org/charts) é uma referência para todos os códigos de caracteres disponíveis.
