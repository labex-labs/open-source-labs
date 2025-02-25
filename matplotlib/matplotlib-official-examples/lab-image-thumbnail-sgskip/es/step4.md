# Verificar el directorio

En este paso, comprobarás si el directorio especificado existe. Si el directorio no existe, saldrás del programa e imprimirás un mensaje de error.

```python
if not args.imagedir.is_dir():
    sys.exit(f"Could not find input directory {args.imagedir}")
```
