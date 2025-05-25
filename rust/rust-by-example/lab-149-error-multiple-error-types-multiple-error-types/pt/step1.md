# Múltiplos tipos de erro

Os exemplos anteriores foram sempre muito convenientes; `Result`s interagem com outros `Result`s e `Option`s interagem com outros `Option`s.

Às vezes, um `Option` precisa interagir com um `Result`, ou um `Result<T, Error1>` precisa interagir com um `Result<T, Error2>`. Nesses casos, queremos gerenciar nossos diferentes tipos de erro de uma forma que os torne compostos e fáceis de interagir.

No código a seguir, duas instâncias de `unwrap` geram diferentes tipos de erro. `Vec::first` retorna um `Option`, enquanto `parse::<i32>` retorna um `Result<i32, ParseIntError>`:

```rust
fn double_first(vec: Vec<&str>) -> i32 {
    let first = vec.first().unwrap(); // Generate error 1
    2 * first.parse::<i32>().unwrap() // Generate error 2
}

fn main() {
    let numbers = vec!["42", "93", "18"];
    let empty = vec![];
    let strings = vec!["tofu", "93", "18"];

    println!("The first doubled is {}", double_first(numbers));

    println!("The first doubled is {}", double_first(empty));
    // Error 1: the input vector is empty

    println!("The first doubled is {}", double_first(strings));
    // Error 2: the element doesn't parse to a number
}
```

Nas próximas seções, veremos várias estratégias para lidar com esse tipo de problema.
