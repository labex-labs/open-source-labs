# Erstellen eines Kontext-Managers

Ein Kontext-Manager ist ein spezieller Objekttyp in Python. In Python können Objekte verschiedene Methoden haben, die ihr Verhalten definieren. Ein Kontext-Manager definiert speziell zwei wichtige Methoden: `__enter__` und `__exit__`. Diese Methoden arbeiten zusammen mit der `with`-Anweisung. Die `with`-Anweisung wird verwendet, um einen bestimmten Kontext für einen Codeblock einzurichten. Stellen Sie sich das wie die Erstellung einer kleinen Umgebung vor, in der bestimmte Dinge passieren, und wenn der Codeblock beendet ist, kümmert sich der Kontext-Manager um die Aufräumarbeiten.

In diesem Schritt werden wir einen Kontext-Manager erstellen, der eine sehr nützliche Funktion hat. Er wird die Standardausgabe (`sys.stdout`) temporär umleiten. Die Standardausgabe ist der Ort, an den die normale Ausgabe Ihres Python-Programms geht, normalerweise die Konsole. Indem wir sie umleiten, können wir die Ausgabe stattdessen in eine Datei senden. Dies ist praktisch, wenn Sie die Ausgabe speichern möchten, die sonst nur auf der Konsole angezeigt würde.

Zuerst müssen wir eine neue Datei erstellen, um unseren Kontext-Manager-Code zu schreiben. Wir werden diese Datei `redirect.py` nennen. Sie können sie mit dem folgenden Befehl im Terminal erstellen:

```bash
touch /home/labex/project/redirect.py
```

Jetzt, da die Datei erstellt ist, öffnen Sie sie in einem Editor. Sobald sie geöffnet ist, fügen Sie den folgenden Python-Code zur Datei hinzu:

```python
import sys

class redirect_stdout:
    def __init__(self, out_file):
        self.out_file = out_file

    def __enter__(self):
        self.stdout = sys.stdout
        sys.stdout = self.out_file
        return self.out_file

    def __exit__(self, ty, val, tb):
        sys.stdout = self.stdout
```

Lassen Sie uns analysieren, was dieser Kontext-Manager tut:

1. `__init__`: Dies ist die Initialisierungsmethode. Wenn wir eine Instanz der `redirect_stdout`-Klasse erstellen, übergeben wir ein Dateiobjekt. Diese Methode speichert dieses Dateiobjekt in der Instanzvariablen `self.out_file`. So merkt sie sich, wohin wir die Ausgabe umleiten möchten.
2. `__enter__`:
   - Zuerst speichert es die aktuelle `sys.stdout`. Dies ist wichtig, weil wir sie später wiederherstellen müssen.
   - Dann ersetzt es die aktuelle `sys.stdout` durch unser Dateiobjekt. Ab diesem Zeitpunkt geht jede Ausgabe, die normalerweise an die Konsole gehen würde, stattdessen in die Datei.
   - Schließlich gibt es das Dateiobjekt zurück. Dies ist nützlich, weil wir möglicherweise das Dateiobjekt innerhalb des `with`-Blocks verwenden möchten.
3. `__exit__`:
   - Diese Methode stellt die ursprüngliche `sys.stdout` wieder her. So geht die Ausgabe nach Abschluss des `with`-Blocks wieder normalerweise an die Konsole.
   - Sie nimmt drei Parameter entgegen: Ausnahmetyp (`ty`), Ausnahme-Wert (`val`) und Stapelüberwachung (`tb`). Diese Parameter sind für das Kontext-Manager-Protokoll erforderlich. Sie werden verwendet, um alle Ausnahmen zu behandeln, die innerhalb des `with`-Blocks auftreten können.

Jetzt testen wir unseren Kontext-Manager. Wir werden ihn verwenden, um die Ausgabe einer Tabelle in eine Datei umzuleiten. Zuerst starten Sie die Python-Shell:

```bash
python3
```

Führen Sie dann den folgenden Python-Code in der Shell aus:

```python
>>> import stock, reader, tableformat
>>> from redirect import redirect_stdout
>>> portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
>>> formatter = tableformat.create_formatter('text')
>>> with redirect_stdout(open('out.txt', 'w')) as file:
...     tableformat.print_table(portfolio, ['name','shares','price'], formatter)
...     file.close()
...
>>> # Let's check the content of the output file
>>> print(open('out.txt').read())
      name     shares      price
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44
```

Toll! Unser Kontext-Manager hat wie erwartet funktioniert. Er hat die Tabellenausgabe erfolgreich in die Datei `out.txt` umgeleitet.

Kontext-Manager sind eine sehr mächtige Funktion in Python. Sie helfen Ihnen, Ressourcen richtig zu verwalten. Hier sind einige häufige Anwendungsfälle für Kontext-Manager:

- Dateioperationen: Wenn Sie eine Datei öffnen, kann ein Kontext-Manager sicherstellen, dass die Datei ordnungsgemäß geschlossen wird, auch wenn ein Fehler auftritt.
- Datenbankverbindungen: Er kann sicherstellen, dass die Datenbankverbindung geschlossen wird, nachdem Sie sie verwendet haben.
- Sperren in Thread-Programmen: Kontext-Manager können Ressourcen auf sichere Weise sperren und entsperren.
- Temporäres Ändern von Umgebungs-Einstellungen: Sie können einige Einstellungen für einen Codeblock ändern und sie dann automatisch wiederherstellen.

Dieses Muster ist sehr wichtig, weil es sicherstellt, dass Ressourcen ordnungsgemäß aufgeräumt werden, auch wenn eine Ausnahme innerhalb des `with`-Blocks auftritt.

Wenn Sie mit dem Testen fertig sind, können Sie die Python-Shell beenden:

```python
>>> exit()
```
