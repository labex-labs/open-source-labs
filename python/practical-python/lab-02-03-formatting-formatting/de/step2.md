# Formatcodes

Formatcodes (nach dem `:` innerhalb der `{}`) ähneln denen von C `printf()`. Gemeinsame Codes sind:

```code
d       Dezimalzahl als Ganzzahl
b       Binäre Zahl als Ganzzahl
x       Hexadezimale Zahl als Ganzzahl
f       Gleitkommazahl als [-]m.dddddd
e       Gleitkommazahl als [-]m.dddddde+-xx
g       Gleitkommazahl, aber selektive Verwendung von E-Notation
s       Zeichenkette
c       Zeichen (aus Ganzzahl)
```

Gemeinsame Modifikatoren passen die Feldbreite und die Dezimalgenauigkeit an. Dies ist eine Teilliste:

```code
:>10d   Ganzzahl rechtsbündig in einem 10-Zeichen-Feld
:<10d   Ganzzahl linksbündig in einem 10-Zeichen-Feld
:^10d   Ganzzahl zentriert in einem 10-Zeichen-Feld
:0.2f   Gleitkommazahl mit 2-stelliger Genauigkeit
```
