# Executar os Testes

Agora que escrevemos nossos testes, podemos executá-los usando o comando `pytest`:

```bash
pytest
```

Para medir a cobertura de código (code coverage) dos seus testes, use o comando `coverage` para executar o pytest:

```bash
coverage run -m pytest
```

Você pode visualizar um relatório de cobertura simples no terminal com o seguinte comando:

```bash
coverage report
```
