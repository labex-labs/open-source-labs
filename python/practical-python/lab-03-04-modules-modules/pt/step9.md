# Carregamento de Módulos

Cada módulo carrega e executa apenas _uma vez_. _Observação: Importações repetidas apenas retornam uma referência ao módulo carregado anteriormente._

`sys.modules` é um dicionário de todos os módulos carregados.

```python
>>> import sys
>>> sys.modules.keys()
['copy_reg', '__main__', 'site', '__builtin__', 'encodings', 'encodings.encodings', 'posixpath', ...]
>>>
```

**Atenção:** Uma confusão comum surge se você repetir uma declaração `import` após alterar o código-fonte de um módulo. Devido ao cache de módulos `sys.modules`, importações repetidas sempre retornam o módulo carregado anteriormente - mesmo que uma alteração tenha sido feita. A maneira mais segura de carregar código modificado no Python é sair e reiniciar o interpretador.
