# Filtrando para Executar Vários Testes

Podemos especificar parte de um nome de teste, e qualquer teste cujo nome corresponda a esse valor será executado. Por exemplo, como dois dos nomes de nossos testes contêm `add`, podemos executar esses dois executando `cargo test add`:

```bash
[object Object]
```

Este comando executou todos os testes com `add` no nome e filtrou o teste chamado `one_hundred`. Observe também que o módulo no qual um teste aparece se torna parte do nome do teste, então podemos executar todos os testes em um módulo filtrando pelo nome do módulo.
