# Programmargumente

## Standardbibliothek

Die Befehlszeilenargumente können über `std::env::args` abgerufen werden, das einen Iterator zurückgibt, der für jedes Argument eine `String` zurückgibt:

```rust
use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();

    // Das erste Argument ist der Pfad, der verwendet wurde, um das Programm aufzurufen.
    println!("Mein Pfad ist {}.", args[0]);

    // Die restlichen Argumente sind die übergebenen Befehlszeilenparameter.
    // Rufen Sie das Programm wie folgt auf:
    //   $./args arg1 arg2
    println!("Ich habe {:?} Argumente: {:?}.", args.len() - 1, &args[1..]);
}
```

```shell
$./args 1 2 3
Mein Pfad ist./args.
Ich habe 3 Argumente: ["1", "2", "3"].
```

## Crates

Alternativ gibt es zahlreiche Crates, die zusätzliche Funktionalität bei der Erstellung von Befehlszeilenanwendungen bieten können. Das \[Rust Cookbook\] zeigt bewährte Praktiken auf, wie man eine der beliebteren Befehlszeilenargument-Crates, `clap`, verwendet.
