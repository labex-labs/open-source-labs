# Modulladen

Jedes Modul lädt und führt nur _einmal_ aus. _Hinweis: Wiederholte Imports geben lediglich einen Verweis auf das zuvor geladene Modul zurück._

`sys.modules` ist ein Wörterbuch aller geladenen Module.

```python
>>> import sys
>>> sys.modules.keys()
['copy_reg', '__main__','site', '__builtin__', 'encodings', 'encodings.encodings', 'posixpath',...]
>>>
```

**Vorsicht:** Ein häufiger Irrtum tritt auf, wenn Sie einen `import`-Befehl nach Änderung des Quellcodes eines Moduls wiederholen. Aufgrund des Modulcaches `sys.modules` geben wiederholte Imports immer das zuvor geladene Modul zurück – auch wenn eine Änderung vorgenommen wurde. Der sicherste Weg, geänderter Code in Python zu laden, ist es, den Interpreter zu beenden und neu zu starten.
