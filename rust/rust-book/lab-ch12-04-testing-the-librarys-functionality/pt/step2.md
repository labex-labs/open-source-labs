# Escrevendo um Teste que Falha

Como não precisamos mais deles, vamos remover as instruções `println!` de `src/lib.rs` e `src/main.rs` que usamos para verificar o comportamento do programa. Em seguida, em `src/lib.rs`, adicionaremos um módulo `tests` com uma função de teste, como fizemos no Capítulo 11. A função de teste especifica o comportamento que queremos que a função `search` tenha: ela receberá uma consulta e o texto a ser pesquisado e retornará apenas as linhas do texto que contêm a consulta. A Listagem 12-15 mostra este teste, que ainda não compilará.

Nome do arquivo: `src/lib.rs`

```rust
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn one_result() {
        let query = "duct";
        let contents = "\
Rust:
safe, fast, productive.
Pick three.";

        assert_eq!(
            vec!["safe, fast, productive."],
            search(query, contents)
        );
    }
}
```

Listagem 12-15: Criando um teste que falha para a função `search` que gostaríamos de ter

Este teste pesquisa a string `"duct"`. O texto que estamos pesquisando tem três linhas, das quais apenas uma contém `"duct"` (observe que a barra invertida após a aspa dupla de abertura diz ao Rust para não colocar um caractere de nova linha no início do conteúdo desta string literal). Afirmamos que o valor retornado da função `search` contém apenas a linha que esperamos.

Ainda não podemos executar este teste e observá-lo falhar porque o teste nem mesmo compila: a função `search` ainda não existe! De acordo com os princípios do TDD, adicionaremos código suficiente para fazer o teste compilar e executar, adicionando uma definição da função `search` que sempre retorna um vetor vazio, conforme mostrado na Listagem 12-16. Então, o teste deve compilar e falhar porque um vetor vazio não corresponde a um vetor contendo a linha `"safe, fast, productive."`.

Nome do arquivo: `src/lib.rs`

```rust
pub fn search<'a>(
    query: &str,
    contents: &'a str,
) -> Vec<&'a str> {
    vec![]
}
```

Listagem 12-16: Definindo apenas o suficiente da função `search` para que nosso teste compile

Observe que precisamos definir uma _lifetime_ explícita `'a` na assinatura de `search` e usar essa _lifetime_ com o argumento `contents` e o valor de retorno. Lembre-se no Capítulo 10 que os parâmetros de _lifetime_ especificam qual _lifetime_ de argumento está conectado à _lifetime_ do valor de retorno. Neste caso, indicamos que o vetor retornado deve conter _slices_ de string que referenciam _slices_ do argumento `contents` (em vez do argumento `query`).

Em outras palavras, dizemos ao Rust que os dados retornados pela função `search` viverão tanto quanto os dados passados para a função `search` no argumento `contents`. Isso é importante! Os dados referenciados _por_ um _slice_ precisam ser válidos para que a referência seja válida; se o compilador presumir que estamos fazendo _slices_ de string de `query` em vez de `contents`, ele fará sua verificação de segurança incorretamente.

Se esquecermos as anotações de _lifetime_ e tentarmos compilar esta função, obteremos este erro:

```bash
error[E0106]: missing lifetime specifier
  --> src/lib.rs:31:10
   |
29 |     query: &str,
   |            ----
30 |     contents: &str,
   |               ----
31 | ) -> Vec<&str> {
   |          ^ expected named lifetime parameter
   |
   = help: this function's return type contains a borrowed value, but the
signature does not say whether it is borrowed from `query` or `contents`
help: consider introducing a named lifetime parameter
   |
28 ~ pub fn search<'a>(
29 ~     query: &'a str,
30 ~     contents: &'a str,
31 ~ ) -> Vec<&'a str> {
   |
```

Rust não pode saber qual dos dois argumentos precisamos, então precisamos dizer explicitamente. Como `contents` é o argumento que contém todo o nosso texto e queremos retornar as partes desse texto que correspondem, sabemos que `contents` é o argumento que deve ser conectado ao valor de retorno usando a sintaxe de _lifetime_.

Outras linguagens de programação não exigem que você conecte argumentos a valores de retorno na assinatura, mas essa prática se tornará mais fácil com o tempo. Você pode querer comparar este exemplo com os exemplos em "Validando Referências com _Lifetimes_".

Agora vamos executar o teste:

```bash
[object Object]
```

Ótimo, o teste falha, exatamente como esperávamos. Vamos fazer o teste passar!
