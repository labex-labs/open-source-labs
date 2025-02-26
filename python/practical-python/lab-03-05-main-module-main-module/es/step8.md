# E/S estándar

La Entrada/Salida estándar (o stdio) son archivos que funcionan de la misma manera que los archivos normales.

```python
sys.stdout
sys.stderr
sys.stdin
```

Por defecto, la función `print` se dirige a `sys.stdout`. La entrada se lee de `sys.stdin`. Las trazas de pila y los errores se dirigen a `sys.stderr`.

Tenga en cuenta que el _stdio_ puede estar conectado a terminales, archivos, tuberías, etc.

```bash
$ python3 prog.py > results.txt
# o
$ cmd1 | python3 prog.py | cmd2
```
