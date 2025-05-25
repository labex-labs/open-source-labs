# Escrevendo um Teste Falho para a Função de Pesquisa Sem Distinção entre Maiúsculas e Minúsculas

Primeiro, adicionamos uma nova função `search_case_insensitive` que será chamada quando a variável de ambiente tiver um valor. Continuaremos a seguir o processo TDD (Test-Driven Development), então a primeira etapa é novamente escrever um teste falho. Adicionaremos um novo teste para a nova função `search_case_insensitive` e renomearemos nosso teste antigo de `one_result` para `case_sensitive` para esclarecer as diferenças entre os dois testes, conforme mostrado na Listagem 12-20.

Nome do arquivo: `src/lib.rs`

```rust
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn case_sensitive() {
        let query = "duct";
        let contents = "\
Rust:
safe, fast, productive.
Pick three.
Duct tape.";

        assert_eq!(
            vec!["safe, fast, productive."],
            search(query, contents)
        );
    }

    #[test]
    fn case_insensitive() {
        let query = "rUsT";
        let contents = "\
Rust:
safe, fast, productive.
Pick three.
Trust me.";

        assert_eq!(
            vec!["Rust:", "Trust me."],
            search_case_insensitive(query, contents)
        );
    }
}
```

Listagem 12-20: Adicionando um novo teste falho para a função sem distinção entre maiúsculas e minúsculas que estamos prestes a adicionar

Observe que também editamos o `contents` do teste antigo. Adicionamos uma nova linha com o texto `"Duct tape."` usando um _D_ maiúsculo que não deve corresponder à consulta `"duct"` quando estamos pesquisando de maneira com distinção entre maiúsculas e minúsculas. Alterar o teste antigo dessa forma ajuda a garantir que não quebremos acidentalmente a funcionalidade de pesquisa com distinção entre maiúsculas e minúsculas que já implementamos. Este teste deve passar agora e deve continuar a passar enquanto trabalhamos na pesquisa sem distinção entre maiúsculas e minúsculas.

O novo teste para a pesquisa _sem_ distinção entre maiúsculas e minúsculas usa `"rUsT"` como sua consulta. Na função `search_case_insensitive` que estamos prestes a adicionar, a consulta `"rUsT"` deve corresponder à linha contendo `"Rust:"` com um _R_ maiúsculo e corresponder à linha `"Trust me."` mesmo que ambos tenham letras diferentes da consulta. Este é o nosso teste falho, e ele falhará ao compilar porque ainda não definimos a função `search_case_insensitive`. Sinta-se à vontade para adicionar uma implementação esqueleto que sempre retorna um vetor vazio, semelhante à forma como fizemos para a função `search` na Listagem 12-16, para ver o teste compilar e falhar.
