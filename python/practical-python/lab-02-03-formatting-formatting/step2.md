# Format codes

Format codes (after the `:` inside the `{}`) are similar to C `printf()`. Common codes
include:

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

Common modifiers adjust the field width and decimal precision. This is a partial list:

```code
:>10d   Integer right aligned in 10-character field
:<10d   Integer left aligned in 10-character field
:^10d   Integer centered in 10-character field
:0.2f   Float with 2 digit precision
```
