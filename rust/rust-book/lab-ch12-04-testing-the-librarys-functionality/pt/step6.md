# Armazenando as Linhas Correspondentes

Para finalizar esta função, precisamos de uma maneira de armazenar as linhas correspondentes que queremos retornar. Para isso, podemos criar um vetor mutável antes do loop `for` e chamar o método `push` para armazenar uma `line` no vetor. Após o loop `for`, retornamos o vetor, como mostrado na Listagem 12-19.

Nome do arquivo: `src/lib.rs`

```rust
pub fn search<'a>(
    query: &str,
    contents: &'a str,
) -> Vec<&'a str> {
    let mut results = Vec::new();

    for line in contents.lines() {
        if line.contains(query) {
            results.push(line);
        }
    }

    results
}
```

Listagem 12-19: Armazenando as linhas que correspondem para que possamos retorná-las

Agora, a função `search` deve retornar apenas as linhas que contêm `query`, e nosso teste deve passar. Vamos executar o teste:

```bash
$ cargo test
--snip--
running 1 test
test tests::one_result ... ok

test result: ok. 1 passed
0 failed
0 ignored
0 measured
0
filtered out
finished in 0.00s
```

Nosso teste passou, então sabemos que funciona!

Neste ponto, poderíamos considerar oportunidades para refatorar a implementação da função de busca, mantendo os testes passando para manter a mesma funcionalidade. O código na função de busca não é tão ruim, mas não aproveita alguns recursos úteis de iteradores. Voltaremos a este exemplo no Capítulo 13, onde exploraremos iteradores em detalhes e veremos como melhorá-lo.
