# Rebanadas de Cadena como Parámetros

Sabendo que se pueden tomar rebanadas de literales y valores de `String` nos lleva a una mejora más en `first_word`, y es su firma:

```rust
fn first_word(s: &String) -> &str {
```

Un Rustaceano más experimentado escribiría la firma mostrada en la Lista 4-9 en su lugar porque nos permite usar la misma función tanto en valores de `&String` como en valores de `&str`.

```rust
fn first_word(s: &str) -> &str {
```

Lista 4-9: Mejora de la función `first_word` usando una rebanada de cadena para el tipo del parámetro `s`

Si tenemos una rebanada de cadena, podemos pasarla directamente. Si tenemos un `String`, podemos pasar una rebanada del `String` o una referencia al `String`. Esta flexibilidad aprovecha las _coerciones de dereferencia_, una característica que cubriremos en "Coerciones de Dereferencia Implícitas con Funciones y Métodos".

Definir una función para tomar una rebanada de cadena en lugar de una referencia a un `String` hace que nuestra API sea más general y útil sin perder ninguna funcionalidad:

Nombre del archivo: `src/main.rs`

```rust
fn main() {
    let my_string = String::from("hello world");

    // `first_word` funciona en rebanadas de `String`s, ya sea parciales
    // o completas
    let word = first_word(&my_string[0..6]);
    let word = first_word(&my_string[..]);
    // `first_word` también funciona en referencias a `String`s, que
    // son equivalentes a rebanadas completas de `String`s
    let word = first_word(&my_string);

    let my_string_literal = "hello world";

    // `first_word` funciona en rebanadas de literales de cadena,
    // ya sea parciales o completas
    let word = first_word(&my_string_literal[0..6]);
    let word = first_word(&my_string_literal[..]);

    // Debido a que los literales de cadena *son* rebanadas de cadena ya,
    // esto también funciona, sin la sintaxis de rebanada!
    let word = first_word(my_string_literal);
}
```
