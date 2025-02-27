# Límites de Trait más Claros con Clausulas where

Usar demasiados límites de trait tiene sus inconvenientes. Cada tipo genérico tiene sus propios límites de trait, por lo que las funciones con múltiples parámetros de tipo genérico pueden contener mucha información de límites de trait entre el nombre de la función y su lista de parámetros, lo que hace que la firma de la función sea difícil de leer. Por esta razón, Rust tiene una sintaxis alternativa para especificar límites de trait dentro de una cláusula `where` después de la firma de la función. Entonces, en lugar de escribir esto:

```rust
fn some_function<T: Display + Clone, U: Clone + Debug>(t: &T, u: &U) -> i32 {
```

podemos usar una cláusula `where`, como esto:

```rust
fn some_function<T, U>(t: &T, u: &U) -> i32
where
    T: Display + Clone,
    U: Clone + Debug,
{
```

La firma de esta función es menos desordenada: el nombre de la función, la lista de parámetros y el tipo de retorno están juntos, similar a una función sin muchos límites de trait.
