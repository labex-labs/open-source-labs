# _Early returns_ (Retornos antecipados)

No exemplo anterior, lidamos explicitamente com os erros usando combinadores. Outra forma de lidar com essa análise de casos é usar uma combinação de instruções `match` e _early returns_ (retornos antecipados).

Ou seja, podemos simplesmente parar de executar a função e retornar o erro se um ocorrer. Para alguns, essa forma de código pode ser mais fácil de ler e escrever. Considere esta versão do exemplo anterior, reescrita usando _early returns_:

```rust
use std::num::ParseIntError;

fn multiply(first_number_str: &str, second_number_str: &str) -> Result<i32, ParseIntError> {
    let first_number = match first_number_str.parse::<i32>() {
        Ok(first_number)  => first_number,
        Err(e) => return Err(e),
    };

    let second_number = match second_number_str.parse::<i32>() {
        Ok(second_number)  => second_number,
        Err(e) => return Err(e),
    };

    Ok(first_number * second_number)
}

fn print(result: Result<i32, ParseIntError>) {
    match result {
        Ok(n)  => println!("n is {}", n),
        Err(e) => println!("Error: {}", e),
    }
}

fn main() {
    print(multiply("10", "2"));
    print(multiply("t", "2"));
}
```

Neste ponto, aprendemos a lidar explicitamente com erros usando combinadores e _early returns_. Embora geralmente queiramos evitar _panicking_ (pânico), lidar explicitamente com todos os nossos erros é complicado.

Na próxima seção, introduziremos `?` para os casos em que simplesmente precisamos de `unwrap` (desembrulhar) sem possivelmente induzir um _panic_.
