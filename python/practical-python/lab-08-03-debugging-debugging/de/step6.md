# Unter Debugger ausführen

Sie können auch ein ganzes Programm unter Debugger ausführen.

```bash
$ python3 -m pdb someprogram.py
```

Es wird automatisch vor der ersten Anweisung in den Debugger eintreten. Dadurch können Sie Breakpoints setzen und die Konfiguration ändern.

Häufige Debuggerbefehle:

```code
(Pdb) help            # Hilfe erhalten
(Pdb) w(here)         # Stapelverfolgung ausgeben
(Pdb) d(own)          # Einen Stapelebene nach unten bewegen
(Pdb) u(p)            # Einen Stapelebene nach oben bewegen
(Pdb) b(reak) loc     # Einen Breakpoint setzen
(Pdb) s(tep)          # Eine Anweisung ausführen
(Pdb) c(ontinue)      # Die Ausführung fortsetzen
(Pdb) l(ist)          # Quellcode auflisten
(Pdb) a(rgs)          # Argumente der aktuellen Funktion ausgeben
(Pdb)!statement      # Anweisung ausführen
```

Für Breakpoints kann die Position einer der folgenden sein.

```code
(Pdb) b 45            # Zeile 45 in der aktuellen Datei
(Pdb) b file.py:45    # Zeile 45 in file.py
(Pdb) b foo           # Funktion foo() in der aktuellen Datei
(Pdb) b module.foo    # Funktion foo() in einem Modul
```
