# Konstanten

Das Problem, das gelöst werden soll, ist es, die Verwendung von Konstanten in Golang für Zeichen-, Zeichenfolge-, boolesche und numerische Werte zu demonstrieren.

## Anforderungen

Die Aufgabe hat die folgenden Anforderungen:

- Verwenden Sie das Schlüsselwort `const`, um einen Konstantenwert zu deklarieren.
- Konstanten sollten Zeichen-, Zeichenfolge-, boolesche und numerische Werte sein.
- Ein Konstantendeklarationssatz kann überall dort auftauchen, wo ein `var`-Satz auftauchen kann.
- Zeigen Sie, dass konstante Ausdrücke mit beliebiger Genauigkeit arithmetische Operationen durchführen.
- Ein numerischer Konstante hat keinen Typ, bis ihm ein Typ zugewiesen wird, beispielsweise durch eine explizite Konvertierung.
- Eine Zahl kann durch Verwendung in einem Kontext, der einen erfordert, wie einer Variablenezuweisung oder einer Funktionsaufruf, einen Typ zugewiesen werden.

## Beispiel

```sh
$ go run constant.go
constant
6e+11
600000000000
-0.28470407323754404
```
