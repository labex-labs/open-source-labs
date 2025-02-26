# Skript-Vorlage

Schließlich ist hier eine häufige Code-Vorlage für Python-Programme, die als Befehlszeilentools laufen:

```python
#!/usr/bin/env python3
#./prog.py

# Import-Anweisungen (Bibliotheken)
import modules

# Funktionen
def spam():
  ...

def blah():
  ...

# Hauptfunktion
def main(argv):
    # Analysiere die Befehlszeilenargumente, die Umgebung usw.
  ...

if __name__ == '__main__':
    import sys
    main(sys.argv)
```
