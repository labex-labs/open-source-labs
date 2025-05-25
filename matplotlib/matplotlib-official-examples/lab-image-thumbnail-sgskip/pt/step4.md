# Verificar Diretório

Nesta etapa, você verificará se o diretório especificado existe. Se o diretório não existir, você sairá do programa e imprimirá uma mensagem de erro.

```python
if not args.imagedir.is_dir():
    sys.exit(f"Could not find input directory {args.imagedir}")
```
