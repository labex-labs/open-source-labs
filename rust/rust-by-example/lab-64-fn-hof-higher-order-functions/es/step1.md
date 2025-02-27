# Funciones de Orden Superior

Rust proporciona Funciones de Orden Superior (HOF, por sus siglas en inglés). Estas son funciones que toman una o más funciones y/o producen una función más útil. Las HOF y los iteradores perezosos le dan a Rust su sabor funcional.

```rust
fn is_odd(n: u32) -> bool {
    n % 2 == 1
}

fn main() {
    println!("Encuentra la suma de todos los números impares al cuadrado menores que 1000");
    let upper = 1000;

    // Enfoque imperativo
    // Declara la variable acumuladora
    let mut acc = 0;
    // Itera: 0, 1, 2,... hasta el infinito
    for n in 0.. {
        // Eleva el número al cuadrado
        let n_squared = n * n;

        if n_squared >= upper {
            // Rompe el bucle si se ha excedido el límite superior
            break;
        } else if is_odd(n_squared) {
            // Acumula el valor, si es impar
            acc += n_squared;
        }
    }
    println!("estilo imperativo: {}", acc);

    // Enfoque funcional
    let sum_of_squared_odd_numbers: u32 =
        (0..).map(|n| n * n)                             // Todos los números naturales al cuadrado
            .take_while(|&n_squared| n_squared < upper) // Por debajo del límite superior
            .filter(|&n_squared| is_odd(n_squared))     // Que son impares
            .sum();                                     // Súmalos
    println!("estilo funcional: {}", sum_of_squared_odd_numbers);
}
```

`Option` e `Iterator` implementan su parte justa de HOF.
