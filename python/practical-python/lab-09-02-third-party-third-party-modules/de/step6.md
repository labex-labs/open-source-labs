# Virtuelle Umgebungen

Eine übliche Lösung für Paketinstallationsprobleme ist es, sich eine sogenannte "virtuelle Umgebung" zu erstellen. Natürlich gibt es keine "eindeutige Methode", um dies zu tun - tatsächlich gibt es mehrere konkurrierende Tools und Techniken. Wenn Sie jedoch eine standardmäßige Python-Installation verwenden, können Sie versuchen, Folgendes einzugeben:

```bash
$ sudo apt install python3-venv
$ python -m venv mypython
bash %
```

Nach ein paar Minuten Wartezeit haben Sie ein neues Verzeichnis `mypython`, das eine eigene kleine Python-Installation ist. Innerhalb dieses Verzeichnisses finden Sie ein `bin/`-Verzeichnis (Unix) oder ein `Scripts/`-Verzeichnis (Windows). Wenn Sie das dort gefundene `activate`-Skript ausführen, wird diese Python-Version "aktiviert", sodass sie die Standard-`python`-Befehl für die Shell wird. Beispielsweise:

```bash
$ source mypython/bin/activate
(mypython) bash %
```

Von hier aus können Sie nun Python-Pakete für sich installieren. Beispielsweise:

    (mypython) $ python -m pip install pandas

...

Für das Experimentieren und Ausprobieren verschiedener Pakete wird eine virtuelle Umgebung normalerweise gut funktionieren. Wenn Sie andererseits eine Anwendung erstellen und diese bestimmte Paketabhängigkeiten hat, ist das ein etwas anderes Problem.
