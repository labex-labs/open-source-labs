# Usando la Sintaxis Corta de Inicialización de Campos

Debido a que los nombres de los parámetros y los nombres de los campos de la estructura son exactamente los mismos en la Lista 5-4, podemos usar la sintaxis de _sintaxis corta de inicialización de campos_ para volver a escribir `build_user` de modo que se comporte exactamente igual pero sin la repetición de `username` y `email`, como se muestra en la Lista 5-5.

```rust
fn build_user(email: String, username: String) -> User {
    User {
        active: true,
        username,
        email,
        sign_in_count: 1,
    }
}
```

Lista 5-5: Una función `build_user` que utiliza la sintaxis corta de inicialización de campos porque los parámetros `username` y `email` tienen el mismo nombre que los campos de la estructura

Aquí, estamos creando una nueva instancia de la estructura `User`, que tiene un campo llamado `email`. Queremos establecer el valor del campo `email` en el valor del parámetro `email` de la función `build_user`. Debido a que el campo `email` y el parámetro `email` tienen el mismo nombre, solo necesitamos escribir `email` en lugar de `email: email`.
