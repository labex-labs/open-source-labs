# Las Coincidencias Son Exhaustivas

Hay otro aspecto de `match` que debemos discutir: los patrones de los brazos deben cubrir todas las posibilidades. Considere esta versión de nuestra función `plus_one`, que tiene un error y no se compilará:

```rust
fn plus_one(x: Option<i32>) -> Option<i32> {
    match x {
        Some(i) => Some(i + 1),
    }
}
```

No manejamos el caso `None`, por lo que este código causará un error. Por suerte, es un error que Rust sabe cómo detectar. Si intentamos compilar este código, obtendremos este error:

```bash
error[E0004]: non-exhaustive patterns: `None` not covered
 --> src/main.rs:3:15
  |
3 |         match x {
  |               ^ pattern `None` not covered
  |
  note: `Option<i32>` defined here
      = note: el valor coincidido es del tipo `Option<i32>`
help: asegúrese de que todos los casos posibles estén siendo manejados agregando
un brazo de coincidencia con un patrón comodín o un patrón explícito como
se muestra
    |
4   ~             Some(i) => Some(i + 1),
5   ~             None => todo!(),
    |
```

Rust sabe que no cubrimos cada caso posible e incluso sabe qué patrón olvidamos. Las coincidencias en Rust son _exhaustivas_: debemos agotar cada última posibilidad para que el código sea válido. Especialmente en el caso de `Option<T>`, cuando Rust nos impide olvidar manejar explícitamente el caso `None`, nos protege de asumir que tenemos un valor cuando podríamos tener `null`, evitando así el error de mil millones discutido anteriormente.
