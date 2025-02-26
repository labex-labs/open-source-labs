# Hauptprogramme vs. Bibliotheksimporte

Jede Python-Datei kann entweder als Hauptprogramm oder als Bibliotheksimport ausgeführt werden:

```bash
$ python3 prog.py # Wird als Hauptprogramm ausgeführt
```

```python
import prog   # Wird als Bibliotheksimport ausgeführt
```

In beiden Fällen ist `__name__` der Name des Moduls. Es wird jedoch nur auf `__main__` gesetzt, wenn es als Hauptprogramm ausgeführt wird.

Normalerweise möchten Sie nicht, dass Anweisungen, die Teil des Hauptprogramms sind, beim Bibliotheksimport ausgeführt werden. Daher ist es üblich, eine `if`-Prüfung in Code zu haben, der auf beide Weise verwendet werden kann.

```python
if __name__ == '__main__':
    # Wird nicht ausgeführt, wenn mit import geladen...
```
