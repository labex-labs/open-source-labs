# Adicionando Mensagens de Falha Personalizadas

Você também pode adicionar uma mensagem personalizada para ser impressa com a mensagem de falha como argumentos opcionais para as macros `assert!`, `assert_eq!` e `assert_ne!`. Quaisquer argumentos especificados após os argumentos obrigatórios são passados para a macro `format!` (discutida em "Concatenação com o Operador + ou a Macro format!"), para que você possa passar uma string de formatação que contenha espaços reservados `{}` e valores para preencher esses espaços reservados. Mensagens personalizadas são úteis para documentar o que uma asserção significa; quando um teste falha, você terá uma ideia melhor de qual é o problema com o código.

Por exemplo, digamos que temos uma função que cumprimenta as pessoas pelo nome e queremos testar se o nome que passamos para a função aparece na saída:

Nome do arquivo: `src/lib.rs`

```rust
pub fn greeting(name: &str) -> String {
    format!("Olá {name}!")
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn greeting_contains_name() {
        let result = greeting("Carol");
        assert!(result.contains("Carol"));
    }
}
```

Os requisitos para este programa ainda não foram acordados, e temos certeza de que o texto `Olá` no início da saudação mudará. Decidimos que não queremos ter que atualizar o teste quando os requisitos mudarem, então, em vez de verificar a igualdade exata com o valor retornado da função `greeting`, apenas afirmaremos que a saída contém o texto do parâmetro de entrada.

Agora, vamos introduzir um bug neste código alterando `greeting` para excluir `name` para ver como a falha de teste padrão se parece:

```rust
pub fn greeting(name: &str) -> String {
    String::from("Olá!")
}
```

A execução deste teste produz o seguinte:

    running 1 test
    test tests::greeting_contains_name ... FAILED

    failures:

    ---- tests::greeting_contains_name stdout ----
    thread 'main' panicked at 'assertion failed:
    result.contains(\"Carol\")', src/lib.rs:12:9
    note: run with `RUST_BACKTRACE=1` environment variable to display
    a backtrace


    failures:
        tests::greeting_contains_name

Este resultado apenas indica que a asserção falhou e em qual linha a asserção está. Uma mensagem de falha mais útil imprimiria o valor da função `greeting`. Vamos adicionar uma mensagem de falha personalizada composta por uma string de formatação com um espaço reservado preenchido com o valor real que obtivemos da função `greeting`:

    #[test]
    fn greeting_contains_name() {
        let result = greeting("Carol");
        assert!(
            result.contains("Carol"),
            "A saudação não continha o nome, o valor era `{result}`"
        );
    }

Agora, quando executarmos o teste, obteremos uma mensagem de erro mais informativa:

    ---- tests::greeting_contains_name stdout ----
    thread 'main' panicked at 'A saudação não continha o nome, o valor
    era `Olá!`', src/lib.rs:12:9
    note: run with `RUST_BACKTRACE=1` environment variable to display
    a backtrace

Podemos ver o valor que realmente obtivemos na saída do teste, o que nos ajudaria a depurar o que aconteceu em vez do que estávamos esperando que acontecesse.
