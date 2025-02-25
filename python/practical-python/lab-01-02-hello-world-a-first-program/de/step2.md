# Interaktiver Modus

Wenn Sie Python starten, erhalten Sie einen _interaktiven_ Modus, in dem Sie experimentieren können.

Wenn Sie beginnen, Anweisungen einzugeben, werden diese sofort ausgeführt. Es gibt keinen Editier-/Kompilier-/Ausführungs-/Debug-Zyklus.

```python
>>> print('hello world')
hello world
>>> 37*42
1554
>>> for i in range(5):
...     print(i)
...
0
1
2
3
4
>>>
```

Dieser sogenannte _read-eval-print-loop_ (oder REPL) ist sehr nützlich für das Debugging und die Exploration.

**STOP**: Wenn Sie nicht herausfinden können, wie Sie mit Python interagieren sollen, halten Sie an, was Sie tun, und finden Sie heraus, wie es geht. Wenn Sie eine IDE verwenden, kann es hinter einer Menüoption oder einem anderen Fenster versteckt sein. Viele Teile dieses Kurses gehen davon aus, dass Sie mit dem Interpreter interagieren können.

Lassen Sie uns die Elemente des REPL genauer betrachten:

- `>>>` ist der Interpreter-Prompt zum Starten einer neuen Anweisung.
- `...` ist der Interpreter-Prompt zum Fortsetzen einer Anweisung. Geben Sie eine leere Zeile ein, um das Tippen zu beenden und das Eingetippte auszuführen.

Der `...`-Prompt kann je nach Umgebung angezeigt werden oder auch nicht. Für diesen Kurs wird er als Leerzeichen dargestellt, um das Kopieren/Einfügen von Codesamples zu erleichtern.

Das Unterstrich-Zeichen `_` enthält das letzte Ergebnis.

```python
>>> 37 * 42
1554
>>> _ * 2
3108
>>> _ + 50
3158
>>>
```

_Dies gilt nur im interaktiven Modus._ Sie verwenden `_` niemals in einem Programm.
