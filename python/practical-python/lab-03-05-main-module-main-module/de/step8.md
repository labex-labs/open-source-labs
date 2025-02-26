# Standard-Eingabe/Ausgabe

Standard-Eingabe/Ausgabe (oder stdio) sind Dateien, die genauso wie normale Dateien funktionieren.

```python
sys.stdout
sys.stderr
sys.stdin
```

Standardmäßig wird die Ausgabe von `print` an `sys.stdout` geleitet. Die Eingabe wird von `sys.stdin` gelesen. Rückverfolgungen und Fehler werden an `sys.stderr` geleitet.

Bedenken Sie, dass _stdio_ an Terminals, Dateien, Rohre usw. angeschlossen sein kann.

```bash
$ python3 prog.py > results.txt
# oder
$ cmd1 | python3 prog.py | cmd2
```
