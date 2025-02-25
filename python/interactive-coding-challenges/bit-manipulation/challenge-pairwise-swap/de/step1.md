# Paarweise Vertauschung

## Problem

Gegeben eine positive ganze Zahl, tausche die ungeraden und geraden Bits mit möglichst wenigen Operationen. Beispielsweise sollte die Ausgabe `0110 1111 1001` sein, wenn die Eingabe `1001 1111 0110` ist.

## Anforderungen

Die folgenden Anforderungen müssen erfüllt sein:

- Die Eingabe ist immer eine positive ganze Zahl.
- Das Programm funktioniert mit 32 Bits.
- Die Ausgabe ist eine ganze Zahl.
- Die Eingaben sind gültig (nicht None).
- Das Programm passt in den Speicher.

## Beispielverwendung

Die folgenden Beispiele veranschaulichen die Verwendung des Programms:

- None -> Exception
- 0 -> 0
- -1 -> -1
- Allgemeiner Fall:

```
    Eingabe  = 1001 1111 0110
    Ergebnis = 0110 1111 1001
```
