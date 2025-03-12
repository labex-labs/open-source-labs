# Ausführen ausgewählter Tests und Verwendung der Testermittlung

Das `unittest`-Modul in Python ist ein leistungsstarkes Werkzeug, das es Ihnen ermöglicht, Ihren Code effektiv zu testen. Es bietet mehrere Möglichkeiten, bestimmte Tests auszuführen oder automatisch alle Tests in Ihrem Projekt zu finden und auszuführen. Dies ist sehr nützlich, da es Ihnen hilft, sich während des Testens auf bestimmte Teile Ihres Codes zu konzentrieren oder die gesamte Testsuite Ihres Projekts schnell zu überprüfen.

## Ausführen bestimmter Tests

Manchmal möchten Sie möglicherweise nur bestimmte Testmethoden oder Testklassen anstelle der gesamten Testsuite ausführen. Dies können Sie erreichen, indem Sie die Musteroption (pattern option) mit dem `unittest`-Modul verwenden. Dies gibt Ihnen mehr Kontrolle darüber, welche Tests ausgeführt werden, was hilfreich sein kann, wenn Sie einen bestimmten Teil Ihres Codes debuggen.

1. Um nur die Tests auszuführen, die sich auf das Erstellen eines Stock-Objekts beziehen:

```bash
python3 -m unittest teststock.TestStock.test_create
```

In diesem Befehl teilt `python3 -m unittest` Python mit, das `unittest`-Modul auszuführen. `teststock` ist der Name der Testdatei, `TestStock` ist der Name der Testklasse und `test_create` ist die spezifische Testmethode, die wir ausführen möchten. Durch Ausführen dieses Befehls können Sie schnell überprüfen, ob der Code, der sich auf das Erstellen eines `Stock`-Objekts bezieht, wie erwartet funktioniert.

2. Um alle Tests in der `TestStock`-Klasse auszuführen:

```bash
python3 -m unittest teststock.TestStock
```

Hier lassen wir den Namen der spezifischen Testmethode weg. Dieser Befehl führt also alle Testmethoden innerhalb der `TestStock`-Klasse in der `teststock`-Datei aus. Dies ist nützlich, wenn Sie die Gesamtfunktionalität der Testfälle für das `Stock`-Objekt überprüfen möchten.

## Verwendung der Testermittlung

Das `unittest`-Modul kann automatisch alle Testdateien in Ihrem Projekt finden und ausführen. Dies erspart Ihnen die Mühe, jede Testdatei manuell anzugeben, die ausgeführt werden soll, insbesondere in größeren Projekten mit vielen Testdateien.

1. Benennen Sie die aktuelle Datei um, um dem Namensmuster für die Testermittlung zu folgen:

```bash
mv teststock.py test_stock.py
```

Der Testermittlungsmechanismus in `unittest` sucht nach Dateien, die dem Namensmuster `test_*.py` folgen. Indem wir die Datei in `test_stock.py` umbenennen, erleichtern wir es dem `unittest`-Modul, die Tests in dieser Datei zu finden und auszuführen.

2. Führen Sie die Testermittlung aus:

```bash
python3 -m unittest discover
```

Dieser Befehl teilt dem `unittest`-Modul mit, automatisch alle Testdateien zu finden und auszuführen, die dem Muster `test_*.py` im aktuellen Verzeichnis entsprechen. Es wird durch das Verzeichnis suchen und alle gefundenen Testfälle in den passenden Dateien ausführen.

3. Sie können auch ein Verzeichnis angeben, in dem nach Tests gesucht werden soll:

```bash
python3 -m unittest discover -s . -p "test_*.py"
```

Dabei bedeuten:

- `-s .` gibt das Verzeichnis an, in dem die Ermittlung beginnen soll (in diesem Fall das aktuelle Verzeichnis). Der Punkt (`.`) repräsentiert das aktuelle Verzeichnis. Sie können dies in einen anderen Verzeichnispfad ändern, wenn Sie in einem anderen Ort nach Tests suchen möchten.
- `-p "test_*.py"` ist das Muster, nach dem Testdateien übereinstimmen müssen. Dies stellt sicher, dass nur Dateien mit Namen, die mit `test_` beginnen und die `.py`-Erweiterung haben, als Testdateien betrachtet werden.

Sie sollten sehen, dass alle 12 Tests ausgeführt und bestanden werden, genau wie zuvor.

4. Benennen Sie die Datei wieder in den ursprünglichen Namen um, um die Konsistenz mit dem Lab zu gewährleisten:

```bash
mv test_stock.py teststock.py
```

Nachdem Sie die Testermittlung ausgeführt haben, benennen we wieder die Datei in ihren ursprünglichen Namen um, um die Lab-Umgebung konsistent zu halten.

Durch die Verwendung der Testermittlung können Sie alle Tests in einem Projekt einfach ausführen, ohne jede Testdatei einzeln angeben zu müssen. Dies macht den Testprozess effizienter und fehleranfälliger.
