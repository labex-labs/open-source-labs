# O Caminho de Busca do Módulo

`sys.path` é um diretório que contém a lista de todos os diretórios verificados pela instrução `import`. Veja:

```python
>>> import sys
>>> sys.path
... veja o resultado ...
>>>
```

Se você importar algo e ele não estiver localizado em um desses diretórios, você receberá uma exceção `ImportError`.
