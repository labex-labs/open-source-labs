# `Result`

`Result` é uma versão mais rica do tipo `Option` que descreve um possível _erro_ em vez de uma possível _ausência_.

Ou seja, `Result<T, E>` pode ter um de dois resultados:

- `Ok(T)`: Um elemento `T` foi encontrado
- `Err(E)`: Um erro foi encontrado com o elemento `E`

Por convenção, o resultado esperado é `Ok`, enquanto o resultado inesperado é `Err`.

Assim como `Option`, `Result` tem muitos métodos associados a ele. `unwrap()`, por exemplo, retorna o elemento `T` ou causa um `panic`. Para o tratamento de casos, existem muitos combinadores entre `Result` e `Option` que se sobrepõem.

Ao trabalhar com Rust, você provavelmente encontrará métodos que retornam o tipo `Result`, como o método `parse()`. Nem sempre é possível converter uma string em outro tipo, então `parse()` retorna um `Result` indicando uma possível falha.

Vamos ver o que acontece quando `parse()` uma string com sucesso e sem sucesso:

```rust
fn multiply(first_number_str: &str, second_number_str: &str) -> i32 {
    // Let's try using `unwrap()` to get the number out. Will it bite us?
    let first_number = first_number_str.parse::<i32>().unwrap();
    let second_number = second_number_str.parse::<i32>().unwrap();
    first_number * second_number
}

fn main() {
    let twenty = multiply("10", "2");
    println!("double is {}", twenty);

    let tt = multiply("t", "2");
    println!("double is {}", tt);
}
```

No caso sem sucesso, `parse()` nos deixa com um erro para o `unwrap()` causar um `panic`. Além disso, o `panic` encerra nosso programa e fornece uma mensagem de erro desagradável.

Para melhorar a qualidade da nossa mensagem de erro, devemos ser mais específicos sobre o tipo de retorno e considerar o tratamento explícito do erro.

## Usando `Result` em `main`

O tipo `Result` também pode ser o tipo de retorno da função `main` se especificado explicitamente. Normalmente, a função `main` terá a forma:

```rust
fn main() {
    println!("Hello World!");
}
```

No entanto, `main` também pode ter um tipo de retorno `Result`. Se ocorrer um erro dentro da função `main`, ela retornará um código de erro e imprimirá uma representação de depuração do erro (usando a trait \[`Debug`\]). O exemplo a seguir mostra tal cenário e aborda aspectos cobertos na \[seção seguinte].

```rust
use std::num::ParseIntError;

fn main() -> Result<(), ParseIntError> {
    let number_str = "10";
    let number = match number_str.parse::<i32>() {
        Ok(number)  => number,
        Err(e) => return Err(e),
    };
    println!("{}", number);
    Ok(())
}
```
