# Códigos de Formato

Códigos de formato (após o `:` dentro de `{}`) são semelhantes ao `printf()` em C. Códigos comuns incluem:

```code
d       Decimal integer
b       Binary integer
x       Hexadecimal integer
f       Float as [-]m.dddddd
e       Float as [-]m.dddddde+-xx
g       Float, but selective use of E notation
s       String
c       Character (from integer)
```

Modificadores comuns ajustam a largura do campo e a precisão decimal. Esta é uma lista parcial:

```code
:>10d   Integer right aligned in 10-character field
:<10d   Integer left aligned in 10-character field
:^10d   Integer centered in 10-character field
:0.2f   Float with 2 digit precision
```
