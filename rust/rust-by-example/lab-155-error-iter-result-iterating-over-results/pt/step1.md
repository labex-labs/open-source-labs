# Iterando sobre `Result`s

Uma operação `Iter::map` pode falhar, por exemplo:

```rust
fn main() {
    let strings = vec!["tofu", "93", "18"];
    let numbers: Vec<_> = strings
        .into_iter()
        .map(|s| s.parse::<i32>())
        .collect();
    println!("Results: {:?}", numbers);
}
```

Vamos analisar as estratégias para lidar com isso.

## Ignorar os itens com falha com `filter_map()`

`filter_map` chama uma função e filtra os resultados que são `None`.

```rust
fn main() {
    let strings = vec!["tofu", "93", "18"];
    let numbers: Vec<_> = strings
        .into_iter()
        .filter_map(|s| s.parse::<i32>().ok())
        .collect();
    println!("Results: {:?}", numbers);
}
```

## Coletar os itens com falha com `map_err()` e `filter_map()`

`map_err` chama uma função com o erro, então, adicionando isso à solução `filter_map` anterior, podemos salvá-los de lado durante a iteração.

```rust
fn main() {
    let strings = vec!["42", "tofu", "93", "999", "18"];
    let mut errors = vec![];
    let numbers: Vec<_> = strings
        .into_iter()
        .map(|s| s.parse::<u8>())
        .filter_map(|r| r.map_err(|e| errors.push(e)).ok())
        .collect();
    println!("Numbers: {:?}", numbers);
    println!("Errors: {:?}", errors);
}
```

## Falhar em toda a operação com `collect()`

`Result` implementa `FromIterator` para que um vetor de resultados (`Vec<Result<T, E>>`) possa ser transformado em um resultado com um vetor (`Result<Vec<T>, E>`). Assim que um `Result::Err` é encontrado, a iteração será encerrada.

```rust
fn main() {
    let strings = vec!["tofu", "93", "18"];
    let numbers: Result<Vec<_>, _> = strings
        .into_iter()
        .map(|s| s.parse::<i32>())
        .collect();
    println!("Results: {:?}", numbers);
}
```

Esta mesma técnica pode ser usada com `Option`.

## Coletar todos os valores válidos e falhas com `partition()`

```rust
fn main() {
    let strings = vec!["tofu", "93", "18"];
    let (numbers, errors): (Vec<_>, Vec<_>) = strings
        .into_iter()
        .map(|s| s.parse::<i32>())
        .partition(Result::is_ok);
    println!("Numbers: {:?}", numbers);
    println!("Errors: {:?}", errors);
}
```

Ao olhar para os resultados, você notará que tudo ainda está envolvido em `Result`. Um pouco mais de código boilerplate é necessário para isso.

```rust
fn main() {
    let strings = vec!["tofu", "93", "18"];
    let (numbers, errors): (Vec<_>, Vec<_>) = strings
        .into_iter()
        .map(|s| s.parse::<i32>())
        .partition(Result::is_ok);
    let numbers: Vec<_> = numbers.into_iter().map(Result::unwrap).collect();
    let errors: Vec<_> = errors.into_iter().map(Result::unwrap_err).collect();
    println!("Numbers: {:?}", numbers);
    println!("Errors: {:?}", errors);
}
```
