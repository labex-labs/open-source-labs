# Arbeiten mit Python-Zahlen

Python bietet umfassende Unterstützung für numerische Operationen. In der Programmierung sind Zahlen grundlegende Datentypen, die für Berechnungen und die Darstellung von Mengen verwendet werden. In diesem Schritt werden Sie die grundlegende Manipulation von Zahlen in Python kennenlernen, was für die Durchführung verschiedener mathematischer Operationen in Ihren Programmen unerlässlich ist.

## Grundlegende arithmetische Operationen

Um mit Python-Zahlen zu beginnen, müssen Sie zunächst eine Python-Interaktive Shell öffnen. Dies können Sie tun, indem Sie `python3` in Ihrem Terminal eingeben. Die Python-Interaktive Shell ermöglicht es Ihnen, Python-Code Zeile für Zeile zu schreiben und auszuführen, was ideal für das Testen und Lernen ist.

```bash
python3
```

Sobald Sie in der Python-Interaktive Shell sind, können Sie einige grundlegende arithmetische Operationen ausprobieren. Python folgt den Standardregeln der Mathematik für die Arithmetik, wie z.B. der Operatorrangfolge (PEMDAS: Klammern, Exponenten, Multiplikation und Division, Addition und Subtraktion).

```python
>>> 3 + 4*5    # Multiplikation hat eine höhere Priorität als Addition, also wird zuerst 4*5 berechnet und dann zu 3 addiert
23
>>> 23.45 / 1e-02    # Hier wird die wissenschaftliche Notation für 0.01 verwendet. Die Division wird durchgeführt, um das Ergebnis zu erhalten
2345.0
```

## Ganzzahlige Division

Python 3 behandelt die Division anders als Python 2. Das Verständnis dieser Unterschiede ist wichtig, um unerwartete Ergebnisse in Ihrem Code zu vermeiden.

```python
>>> 7 / 4    # In Python 3 gibt die normale Division immer einen Float zurück, auch wenn das Ergebnis eine Ganzzahl sein könnte
1.75
>>> 7 // 4   # Ganzzahlige Division (abschneiden des Dezimalteils) gibt Ihnen den Quotienten als Ganzzahl
1
```

## Methoden für Zahlen

Zahlen in Python haben mehrere nützliche Methoden, die oft übersehen werden. Diese Methoden können komplexe numerische Operationen und Konvertierungen vereinfachen. Lassen Sie uns einige von ihnen untersuchen:

```python
>>> x = 1172.5
>>> x.as_integer_ratio()    # Diese Methode stellt die Fließkommazahl als Bruch dar, was für einige mathematische Berechnungen nützlich sein kann
(2345, 2)
>>> x.is_integer()    # Prüft, ob die Fließkommazahl ein ganzzahliger Wert ist. In diesem Fall ist 1172.5 keine Ganzzahl, also gibt es False zurück
False

>>> y = 12345
>>> y.numerator    # Für Ganzzahlen ist der Zähler die Zahl selbst
12345
>>> y.denominator    # Für Ganzzahlen ist der Nenner immer 1
1
>>> y.bit_length()    # Diese Methode gibt Ihnen die Anzahl der Bits an, die benötigt werden, um die Zahl binär darzustellen, was bei bitweisen Operationen nützlich sein kann
14
```

Diese Methoden sind besonders nützlich, wenn Sie bestimmte numerische Operationen oder Konvertierungen durchführen müssen. Sie können Ihnen Zeit sparen und Ihren Code effizienter machen.

Wenn Sie mit der Exploration der Python-Interaktiven Shell fertig sind, können Sie sie beenden, indem Sie eingeben:

```python
>>> exit()
```
