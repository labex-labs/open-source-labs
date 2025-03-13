# Verständnis des Modulladeverhaltens

In Python hat die Art und Weise, wie Module geladen werden, einige interessante Eigenschaften. In diesem Schritt werden wir diese Verhaltensweisen untersuchen, um zu verstehen, wie Python das Laden von Modulen verwaltet.

1. Zunächst sehen wir uns an, was passiert, wenn wir versuchen, ein Modul erneut innerhalb derselben Python-Interpreter-Sitzung zu importieren. Wenn Sie einen Python-Interpreter starten, ist es wie das Öffnen eines Arbeitsbereichs, in dem Sie Python-Code ausführen können. Nachdem Sie ein Modul importiert haben, könnte es so aussehen, als würde das erneute Importieren des Moduls es neu laden, aber das ist nicht der Fall.

```python
>>> import simplemod
```

Beachten Sie, dass Sie diesmal die Ausgabe "Loaded simplemod" nicht sehen. Dies liegt daran, dass **Python ein Modul pro Interpreter-Sitzung nur einmal lädt**. Nachfolgende `import`-Anweisungen laden das Modul nicht neu. Python merkt sich, dass es das Modul bereits geladen hat, und führt daher nicht erneut den Ladevorgang durch.

2. Nachdem Sie ein Modul importiert haben, können Sie die Variablen darin ändern. Ein Modul in Python ist wie ein Behälter, der Variablen, Funktionen und Klassen enthält. Nachdem Sie ein Modul importiert haben, können Sie auf seine Variablen zugreifen und sie ändern, genau wie bei jedem anderen Python-Objekt.

```python
>>> simplemod.x
42
>>> simplemod.x = 13
>>> simplemod.x
13
>>> simplemod.foo()
x is 13
```

Hier überprüfen wir zunächst den Wert der Variable `x` im `simplemod`-Modul, der zunächst `42` ist. Dann ändern wir seinen Wert auf `13` und überprüfen, ob die Änderung vorgenommen wurde. Wenn wir die Funktion `foo` im Modul aufrufen, spiegelt sie den neuen Wert von `x` wider.

3. Das erneute Importieren des Moduls setzt die Änderungen, die wir an seinen Variablen vorgenommen haben, nicht zurück. Selbst wenn wir versuchen, das Modul erneut zu importieren, lädt Python es nicht neu, sodass die Änderungen, die wir an seinen Variablen vorgenommen haben, bestehen bleiben.

```python
>>> import simplemod
>>> simplemod.x
13
```

4. Wenn Sie ein Modul zwangsweise neu laden möchten, müssen Sie die Funktion `importlib.reload()` verwenden. Manchmal haben Sie möglicherweise Änderungen am Code des Moduls vorgenommen und möchten, dass diese Änderungen sofort wirksam werden. Die Funktion `importlib.reload()` ermöglicht Ihnen genau das.

```python
>>> import importlib
>>> importlib.reload(simplemod)
Loaded simplemod
<module 'simplemod' from 'simplemod.py'>
>>> simplemod.x
42
>>> simplemod.foo()
x is 42
```

Das Modul wurde neu geladen, und der Wert von `x` wurde auf `42` zurückgesetzt. Dies zeigt, dass das Modul erneut aus seinem Quellcode geladen wurde und alle Variablen wie ursprünglich initialisiert wurden.

5. Python verfolgt alle geladenen Module im `sys.modules`-Wörterbuch. Dieses Wörterbuch fungiert als Registry, in der Python Informationen über alle Module speichert, die während der aktuellen Interpreter-Sitzung geladen wurden.

```python
>>> 'simplemod' in sys.modules
True
>>> sys.modules['simplemod']
<module 'simplemod' from 'simplemod.py'>
```

Indem Sie überprüfen, ob ein Modulname im `sys.modules`-Wörterbuch enthalten ist, können Sie feststellen, ob das Modul geladen wurde. Und indem Sie auf das Wörterbuch mit dem Modulnamen als Schlüssel zugreifen, können Sie Informationen über das Modul erhalten.

6. Sie können ein Modul aus diesem Wörterbuch entfernen, um Python zu zwingen, es beim nächsten Import neu zu laden. Wenn Sie ein Modul aus dem `sys.modules`-Wörterbuch entfernen, vergisst Python, dass es das Modul bereits geladen hat. Wenn Sie es das nächste Mal versuchen, zu importieren, wird Python es erneut aus seinem Quellcode laden.

```python
>>> del sys.modules['simplemod']
>>> import simplemod
Loaded simplemod
>>> simplemod.x
42
```

Das Modul wurde erneut geladen, weil es aus `sys.modules` entfernt wurde. Dies ist eine weitere Möglichkeit, sicherzustellen, dass Sie mit der neuesten Version des Codes eines Moduls arbeiten.
