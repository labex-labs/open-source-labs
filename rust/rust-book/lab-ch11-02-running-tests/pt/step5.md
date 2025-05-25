# Executando Testes Únicos

Podemos passar o nome de qualquer função de teste para `cargo test` para executar apenas esse teste:

```bash
[object Object]
```

Apenas o teste com o nome `one_hundred` foi executado; os outros dois testes não corresponderam a esse nome. A saída do teste nos informa que tínhamos mais testes que não foram executados, exibindo `2 filtered out` no final.

Não podemos especificar os nomes de vários testes dessa forma; apenas o primeiro valor fornecido para `cargo test` será usado. Mas existe uma maneira de executar vários testes.
