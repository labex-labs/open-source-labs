# Entrada/Saída Padrão (Standard I/O)

Entrada/Saída Padrão (ou stdio) são arquivos que funcionam da mesma forma que arquivos normais.

```python
sys.stdout
sys.stderr
sys.stdin
```

Por padrão, a função `print` é direcionada para `sys.stdout`. A entrada é lida de `sys.stdin`. Tracebacks e erros são direcionados para `sys.stderr`.

Esteja ciente de que _stdio_ pode ser conectado a terminais, arquivos, pipes, etc.

```bash
$ python3 prog.py > results.txt
# or
$ cmd1 | python3 prog.py | cmd2
```
