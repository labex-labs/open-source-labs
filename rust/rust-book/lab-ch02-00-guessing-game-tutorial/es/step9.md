# Generando un número secreto

A continuación, necesitamos generar un número secreto que el usuario intentará adivinar. El número secreto debe ser diferente cada vez para que el juego sea divertido de jugar más de una vez. Usaremos un número aleatorio entre 1 y 100 para que el juego no sea demasiado difícil. Rust todavía no incluye funcionalidad de números aleatorios en su librería estándar. Sin embargo, el equipo de Rust proporciona un crado `rand` en *https://crates.io/crates/rand* con dicha funcionalidad.
