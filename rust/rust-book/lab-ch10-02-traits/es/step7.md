# Especificando Varios Límites de Trait con la Sintaxis +

También podemos especificar más de un límite de trait. Digamos que queremos que `notify` use la formateación de visualización así como `summarize` en `item`: especificamos en la definición de `notify` que `item` debe implementar tanto `Display` como `Summary`. Lo podemos hacer usando la sintaxis `+`:

```rust
pub fn notify(item: &(impl Summary + Display)) {
```

La sintaxis `+` también es válida con límites de trait en tipos genéricos:

```rust
pub fn notify<T: Summary + Display>(item: &T) {
```

Con los dos límites de trait especificados, el cuerpo de `notify` puede llamar a `summarize` y usar `{}` para formatear `item`.
