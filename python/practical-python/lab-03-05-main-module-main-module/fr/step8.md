# Entrée/Sortie standard

L'entrée/sortie standard (ou stdio) sont des fichiers qui fonctionnent de la même manière que les fichiers normaux.

```python
sys.stdout
sys.stderr
sys.stdin
```

Par défaut, l'instruction `print` est dirigée vers `sys.stdout`. L'entrée est lue à partir de `sys.stdin`. Les traces de pile et les erreurs sont dirigées vers `sys.stderr`.

Notez que le _stdio_ peut être connecté à des terminaux, des fichiers, des tubes, etc.

```bash
$ python3 prog.py > results.txt
# ou
$ cmd1 | python3 prog.py | cmd2
```
