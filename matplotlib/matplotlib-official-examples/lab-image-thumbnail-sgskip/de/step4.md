# Verzeichnis überprüfen

In diesem Schritt überprüfen Sie, ob das angegebene Verzeichnis existiert. Wenn das Verzeichnis nicht existiert, beenden Sie das Programm und geben Sie eine Fehlermeldung aus.

```python
if not args.imagedir.is_dir():
    sys.exit(f"Could not find input directory {args.imagedir}")
```
