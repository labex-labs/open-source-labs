# Importieren und Verwenden von Modulen

Nachdem wir nun ein Modul erstellt haben, ist es an der Zeit, zu verstehen, wie wir es importieren und seine Komponenten nutzen können. In Python ist ein Modul eine Datei, die Python-Definitionen und Anweisungen enthält. Wenn Sie ein Modul importieren, erhalten Sie Zugang zu allen Funktionen, Klassen und Variablen, die darin definiert sind. Dies ermöglicht es Ihnen, Code wiederzuverwenden und Ihre Programme effektiver zu organisieren.

1. Zunächst müssen wir im WebIDE ein neues Terminal öffnen. Dieses Terminal dient als Arbeitsbereich, in dem wir Python-Befehle ausführen können. Um ein neues Terminal zu öffnen, klicken Sie auf "Terminal" > "New Terminal".

2. Sobald das Terminal geöffnet ist, müssen wir den Python-Interpreter starten. Der Python-Interpreter ist ein Programm, das Python-Code liest und ausführt. Um ihn zu starten, geben Sie den folgenden Befehl im Terminal ein und drücken Sie die Eingabetaste:

```bash
python3
```

3. Jetzt, da der Python-Interpreter läuft, können wir unser Modul importieren. In Python verwenden wir die `import`-Anweisung, um ein Modul in unser aktuelles Programm einzubinden. Geben Sie den folgenden Befehl im Python-Interpreter ein:

```python
>>> import simplemod
Loaded simplemod
```

Sie werden bemerken, dass "Loaded simplemod" in der Ausgabe erscheint. Dies liegt daran, dass die `print`-Anweisung in unserem `simplemod`-Modul ausgeführt wird, wenn das Modul geladen wird. Wenn Python ein Modul importiert, führt es all den obersten Code in diesem Modul aus, einschließlich aller `print`-Anweisungen.

4. Nachdem wir das Modul importiert haben, können wir seine Komponenten mit der Punktnotation zugreifen. Die Punktnotation ist eine Möglichkeit, Attribute (Variablen und Funktionen) eines Objekts in Python zuzugreifen. In diesem Fall ist das Modul ein Objekt, und seine Funktionen, Variablen und Klassen sind seine Attribute. Hier sind einige Beispiele, wie Sie verschiedene Komponenten des `simplemod`-Moduls zugreifen können:

```python
>>> simplemod.x
42
>>> simplemod.foo()
x is 42
>>> spam_instance = simplemod.Spam()
>>> spam_instance.yow()
Yow!
```

In der ersten Zeile greifen wir auf die Variable `x` zu, die im `simplemod`-Modul definiert ist. In der zweiten Zeile rufen wir die Funktion `foo` aus dem `simplemod`-Modul auf. In der dritten und vierten Zeile erstellen wir eine Instanz der `Spam`-Klasse, die im `simplemod`-Modul definiert ist, und rufen ihre Methode `yow` auf.

5. Manchmal können Sie beim Versuch, ein Modul zu importieren, einen `ImportError` erhalten. Dieser Fehler tritt auf, wenn Python das Modul, das Sie importieren möchten, nicht finden kann. Um herauszufinden, wo Python nach Modulen sucht, können Sie die `sys.path`-Variable untersuchen. Die `sys.path`-Variable ist eine Liste von Verzeichnissen, die Python durchsucht, wenn es nach Modulen sucht. Geben Sie die folgenden Befehle im Python-Interpreter ein:

```python
>>> import sys
>>> sys.path
['', '/usr/lib/python310.zip', '/usr/lib/python3.10', '/usr/lib/python3.10/lib-dynload', '/usr/local/lib/python3.10/dist-packages', '/usr/lib/python3/dist-packages']
```

Das erste Element in der Liste (der leere String) repräsentiert das aktuelle Arbeitsverzeichnis. Hier sucht Python nach der Datei `simplemod.py`. Wenn Ihr Modul nicht in einem der in `sys.path` aufgeführten Verzeichnisse liegt, kann Python es nicht finden, und Sie erhalten einen `ImportError`. Stellen Sie sicher, dass Ihre `simplemod.py`-Datei im aktuellen Arbeitsverzeichnis oder in einem der anderen Verzeichnisse in `sys.path` liegt.
