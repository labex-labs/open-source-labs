# Bit umkehren

## Problem

Gegeben eine binäre Zahl müssen wir ein Bit von 0 auf 1 umkehren, um die längste Folge von Einsen zu maximieren. Beispielsweise, wenn wir die binäre Zahl `000011110000` haben, können wir das vierte Bit von 0 auf 1 umkehren, um `000111110000` zu erhalten, was eine Folge von fünf Einsen hat. Unser Ziel ist es, eine Python-Funktion zu schreiben, die eine binäre Zahl als Eingabe nimmt und die Länge der längsten Folge von Einsen nach dem Umkehren eines Bits zurückgibt.

## Anforderungen

Die Anforderungen an unsere Python-Funktion lauten wie folgt:

- Die Eingabe muss eine Ganzzahl in Basis 2 sein.
- Wir können annehmen, dass die Eingabe eine 32-Bit-Zahl ist.
- Wir müssen die Länge der Eingabe nicht validieren.
- Die Ausgabe muss eine Ganzzahl sein.
- Wir können nicht annehmen, dass die Eingaben gültig sind.
- Wir können annehmen, dass wir eine positive Zahl verwenden, da Python keinen >>>-Operator hat.
- Wir können annehmen, dass dies in den Speicher passt.

## Beispielverwendung

Hier sind einige Beispiele dafür, wie unsere Python-Funktion verhalten sollte:

- `None` -> Exception
- `11111111111111111111111111111111` -> 32
- `00000000000000000000000000000000` -> 1
- `00001111110111011111001111110000` -> 10
