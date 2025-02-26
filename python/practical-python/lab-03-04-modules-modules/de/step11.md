# Modulsuchpfad

Wie erwähnt, enthält `sys.path` die Suchpfade. Sie können diese manuell anpassen, wenn erforderlich.

```python
import sys
sys.path.append('/project/foo/pyfiles')
```

Pfade können auch über Umgebungsvariablen hinzugefügt werden.

```python
% env PYTHONPATH=/project/foo/pyfiles python3
Python 3.6.0 (default, Feb 3 2017, 05:53:21)
[GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.38)]
>>> import sys
>>> sys.path
['','/project/foo/pyfiles',...]
```

Allgemein sollte es nicht erforderlich sein, den Modulsuchpfad manuell anzupassen. Es kann jedoch vorkommen, wenn Sie versuchen, Python-Code zu importieren, der sich an einem ungewöhnlichen Ort befindet oder nicht von dem aktuellen Arbeitsverzeichnis aus leicht zugänglich ist.

Für diese Übung zu Modulen ist es von entscheidender Wichtigkeit, sicherzustellen, dass Sie Python in einer geeigneten Umgebung ausführen. Module stellen für neue Programmierer oft Probleme im Zusammenhang mit dem aktuellen Arbeitsverzeichnis oder mit den Pfadeinstellungen von Python dar. Für diesen Kurs wird angenommen, dass Sie all Ihren Code im Verzeichnis `~/project` schreiben. Um die besten Ergebnisse zu erzielen, sollten Sie sich auch im selben Verzeichnis befinden, wenn Sie den Interpreter starten. Wenn nicht, müssen Sie sicherstellen, dass `~/project` zu `sys.path` hinzugefügt wird.
