# @ Vinculaciones

El operador _arroba_ `@` nos permite crear una variable que almacena un valor al mismo tiempo que estamos probando ese valor para una coincidencia de patrón. En la Lista 18-29, queremos probar que el campo `id` de un `Message::Hello` esté en el rango `3..=7`. También queremos vincular el valor a la variable `id_variable` para poder usarlo en el código asociado al brazo. Podríamos nombrar esta variable `id`, igual que el campo, pero para este ejemplo usaremos un nombre diferente.

Nombre de archivo: `src/main.rs`

```rust
enum Message {
    Hello { id: i32 },
}

let msg = Message::Hello { id: 5 };

match msg {
    Message::Hello {
        id: id_variable @ 3..=7,
    } => println!("Encontré un id en el rango: {id_variable}"),
    Message::Hello { id: 10..=12 } => {
        println!("Encontré un id en otro rango")
    }
    Message::Hello { id } => println!("Algún otro id: {id}"),
}
```

Lista 18-29: Usando `@` para vincularse a un valor en un patrón mientras también lo prueba

Este ejemplo imprimirá `Encontré un id en el rango: 5`. Al especificar `id_variable @` antes del rango `3..=7`, estamos capturando cualquier valor que coincidiera con el rango mientras también probamos que el valor coincidiera con el patrón de rango.

En el segundo brazo, donde solo tenemos un rango especificado en el patrón, el código asociado al brazo no tiene una variable que contenga el valor real del campo `id`. El valor del campo `id` podría haber sido 10, 11 o 12, pero el código que va con ese patrón no sabe cuál es. El código del patrón no puede usar el valor del campo `id` porque no hemos guardado el valor de `id` en una variable.

En el último brazo, donde hemos especificado una variable sin un rango, sí tenemos el valor disponible para usarlo en el código del brazo en una variable llamada `id`. La razón es que hemos usado la sintaxis abreviada de campo de struct. Pero no hemos aplicado ninguna prueba al valor en el campo `id` en este brazo, como hicimos con los dos primeros brazos: cualquier valor coincidiría con este patrón.

Usar `@` nos permite probar un valor y guardarlo en una variable dentro de un solo patrón.
