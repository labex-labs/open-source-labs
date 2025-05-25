# Executando Testes em Paralelo ou Consecutivamente

Quando você executa vários testes, por padrão eles são executados em paralelo usando threads, o que significa que eles terminam de rodar mais rápido e você recebe feedback mais rapidamente. Como os testes estão sendo executados ao mesmo tempo, você deve garantir que seus testes não dependam uns dos outros ou de qualquer estado compartilhado, incluindo um ambiente compartilhado, como o diretório de trabalho atual ou variáveis de ambiente.

Por exemplo, digamos que cada um de seus testes execute algum código que cria um arquivo no disco chamado _test-output.txt_ e grava alguns dados nesse arquivo. Então, cada teste lê os dados nesse arquivo e afirma que o arquivo contém um valor específico, que é diferente em cada teste. Como os testes são executados ao mesmo tempo, um teste pode sobrescrever o arquivo no tempo entre outro teste escrever e ler o arquivo. O segundo teste falhará, não porque o código está incorreto, mas porque os testes interferiram uns com os outros durante a execução em paralelo. Uma solução é garantir que cada teste grave em um arquivo diferente; outra solução é executar os testes um de cada vez.

Se você não quiser executar os testes em paralelo ou se quiser um controle mais preciso sobre o número de threads usados, você pode enviar a flag `--test-threads` e o número de threads que deseja usar para o binário de teste. Dê uma olhada no exemplo a seguir:

```bash
cargo test -- --test-threads=1
```

Definimos o número de threads de teste para `1`, dizendo ao programa para não usar nenhum paralelismo. Executar os testes usando uma thread levará mais tempo do que executá-los em paralelo, mas os testes não interferirão uns com os outros se compartilharem estado.
