# Enthalte notwendige Dateien

Das Build-Backend von setuptools benötigt eine weitere Datei namens `MANIFEST.in`, um nicht-Python-Dateien im Projekt zu enthalten.

Erstelle eine `MANIFEST.in` mit dem folgenden Inhalt:

```none
# MANIFEST.in

include flaskr/schema.sql
graft flaskr/static
graft flaskr/templates
global-exclude *.pyc
```

Dies sagt dem Build, alle Dateien im `static`- und `templates`-Verzeichnis sowie die `schema.sql`-Datei zu kopieren, während alle Bytecode-Dateien ausgeschlossen werden.
