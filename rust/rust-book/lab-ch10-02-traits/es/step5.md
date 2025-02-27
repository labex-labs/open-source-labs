# Traits como Parámetros

Ahora que sabes cómo definir e implementar traits, podemos explorar cómo usar traits para definir funciones que acepten muchos tipos diferentes. Usaremos el trait `Summary` que implementamos en los tipos `NewsArticle` y `Tweet` en la Lista 10-13 para definir una función `notify` que llame al método `summarize` en su parámetro `item`, que es de algún tipo que implementa el trait `Summary`. Para hacer esto, usamos la sintaxis `impl Trait`, como esto:

```rust
pub fn notify(item: &impl Summary) {
    println!("Breaking news! {}", item.summarize());
}
```

En lugar de un tipo concrete para el parámetro `item`, especificamos la palabra clave `impl` y el nombre del trait. Este parámetro acepta cualquier tipo que implemente el trait especificado. En el cuerpo de `notify`, podemos llamar a cualquier método en `item` que provenga del trait `Summary`, como `summarize`. Podemos llamar a `notify` y pasar cualquier instancia de `NewsArticle` o `Tweet`. El código que llama a la función con cualquier otro tipo, como una `String` o un `i32`, no se compilará porque esos tipos no implementan `Summary`.
