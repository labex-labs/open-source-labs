# Testes de Documentação

A principal forma de documentar um projeto Rust é através da anotação do código-fonte. Os comentários de documentação são escritos na especificação CommonMark Markdown e suportam blocos de código. O Rust garante a correção, então esses blocos de código são compilados e usados como testes de documentação.

````rust
/// Primeira linha é um breve resumo descrevendo a função.
///
/// As linhas seguintes apresentam documentação detalhada. Blocos de código começam com triplas aspas e têm `fn main()` implícito
/// e `extern crate <nome_do_crate>`. Suponha que estamos testando o crate `doccomments`:
///
/// ```
/// let result = doccomments::add(2, 3);
/// assert_eq!(result, 5);
/// ```
pub fn add(a: i32, b: i32) -> i32 {
    a + b
}

/// Normalmente, os comentários de documentação podem incluir seções "Exemplos", "Panics" e "Falhas".
///
/// A função seguinte divide dois números.
///
/// # Exemplos
///
/// ```
/// let result = doccomments::div(10, 2);
/// assert_eq!(result, 5);
/// ```
///
/// # Panics
///
/// A função gera uma exceção (panic) se o segundo argumento for zero.
///
/// ```rust
/// // gera uma exceção em caso de divisão por zero
/// doccomments::div(10, 0);
/// ```
pub fn div(a: i32, b: i32) -> i32 {
    if b == 0 {
        panic!("Erro de divisão por zero");
    }

    a / b
}
````

Os blocos de código na documentação são testados automaticamente ao executar o comando `cargo test` normal:

```shell
[object Object]
```

## Motivação por trás dos testes de documentação

O principal objetivo dos testes de documentação é servir como exemplos que exercitam a funcionalidade, o que é um dos princípios mais importantes. Permite usar exemplos da documentação como trechos de código completos. Mas usar `?` faz com que a compilação falhe, pois `main` retorna `unit`. A capacidade de ocultar algumas linhas de código da documentação vem em auxílio: pode-se escrever `fn try_main() -> Result<(), ErrorType>`, ocultá-la e `unwrap`-la em `main` oculto. Parece complicado? Aqui está um exemplo:

````rust
/// Usando `try_main` oculto em testes de documentação.
///
/// ```
/// # // Linhas ocultas começam com o símbolo '#', mas ainda são compiláveis!
/// # fn try_main() -> Result<(), String> { // linha que envolve o corpo mostrado na documentação
/// let res = doccomments::try_div(10, 2)?;
/// # Ok(()) // retornando de try_main
/// # }
/// # fn main() { // iniciando main que irá unwrap()
/// #    try_main().unwrap(); // chamando try_main e unwrapping
/// #                         // para que o teste gere uma exceção (panic) em caso de erro
/// # }
/// ```
pub fn try_div(a: i32, b: i32) -> Result<i32, String> {
    if b == 0 {
        Err(String::from("Divisão por zero"))
    } else {
        Ok(a / b)
    }
}
````
