# Loops `for`

## `for` e `range`

A construção `for in` pode ser usada para iterar através de um `Iterator`. Uma das maneiras mais fáceis de criar um iterador é usar a notação de intervalo `a..b`. Isso gera valores de `a` (inclusivo) a `b` (exclusivo) em incrementos de um.

Vamos escrever FizzBuzz usando `for` em vez de `while`.

```rust
fn main() {
    // `n` assumirá os valores: 1, 2, ..., 100 em cada iteração
    for n in 1..101 {
        if n % 15 == 0 {
            println!("fizzbuzz");
        } else if n % 3 == 0 {
            println!("fizz");
        } else if n % 5 == 0 {
            println!("buzz");
        } else {
            println!("{}", n);
        }
    }
}
```

Alternativamente, `a..=b` pode ser usado para um intervalo inclusivo em ambas as extremidades. O código acima pode ser reescrito como:

```rust
fn main() {
    // `n` assumirá os valores: 1, 2, ..., 100 em cada iteração
    for n in 1..=100 {
        if n % 15 == 0 {
            println!("fizzbuzz");
        } else if n % 3 == 0 {
            println!("fizz");
        } else if n % 5 == 0 {
            println!("buzz");
        } else {
            println!("{}", n);
        }
    }
}
```

## `for` e iteradores

A construção `for in` é capaz de interagir com um `Iterator` de várias maneiras. Como discutido na seção sobre o trait `Iterator`, por padrão, o loop `for` aplicará a função `into_iter` à coleção. No entanto, este não é o único meio de converter coleções em iteradores.

`into_iter`, `iter` e `iter_mut` lidam com a conversão de uma coleção em um iterador de maneiras diferentes, fornecendo diferentes visões dos dados dentro dela.

- `iter` - Este método empresta cada elemento da coleção em cada iteração. Assim, deixando a coleção intacta e disponível para reutilização após o loop.

```rust
fn main() {
    let names = vec!["Bob", "Frank", "Ferris"];

    for name in names.iter() {
        match name {
            &"Ferris" => println!("Há um rustacean entre nós!"),
            // TODO ^ Tente remover o & e corresponder apenas a "Ferris"
            _ => println!("Olá {}", name),
        }
    }

    println!("names: {:?}", names);
}
```

- `into_iter` - Este método consome a coleção para que, em cada iteração, os dados exatos sejam fornecidos. Uma vez que a coleção foi consumida, ela não está mais disponível para reutilização, pois foi 'movida' dentro do loop.

```rust
fn main() {
    let names = vec!["Bob", "Frank", "Ferris"];

    for name in names.into_iter() {
        match name {
            "Ferris" => println!("Há um rustacean entre nós!"),
            _ => println!("Olá {}", name),
        }
    }

    println!("names: {:?}", names);
    // FIXME ^ Comente esta linha
}
```

- `iter_mut` - Este método empresta mutávelmente cada elemento da coleção, permitindo que a coleção seja modificada no local.

```rust
fn main() {
    let mut names = vec!["Bob", "Frank", "Ferris"];

    for name in names.iter_mut() {
        *name = match name {
            &mut "Ferris" => "Há um rustacean entre nós!",
            _ => "Olá",
        }
    }

    println!("names: {:?}", names);
}
```

Nos trechos acima, observe o tipo do ramo `match`, que é a principal diferença nos tipos de iteração. A diferença no tipo, é claro, implica ações diferentes que podem ser executadas.
