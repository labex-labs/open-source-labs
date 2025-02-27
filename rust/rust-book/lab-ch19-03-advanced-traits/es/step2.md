# Tipos Asociados

Los _tipos asociados_ conectan un tipo de marcador de posición con un trait de modo que las definiciones de métodos del trait pueden usar estos tipos de marcador de posición en sus firmas. El implementador de un trait especificará el tipo concrete que se usará en lugar del tipo de marcador de posición para una implementación particular. De esta manera, podemos definir un trait que use algunos tipos sin necesidad de conocer exactamente cuáles son esos tipos hasta que se implemente el trait.

Hemos descrito la mayoría de las características avanzadas de este capítulo como raras veces necesarias. Los tipos asociados se encuentran en un punto intermedio: se usan con menos frecuencia que las características explicadas en el resto del libro, pero más comúnmente que muchas de las otras características discutidas en este capítulo.

Un ejemplo de un trait con un tipo asociado es el trait `Iterator` que provee la biblioteca estándar. El tipo asociado se llama `Item` y representa el tipo de los valores sobre los que está iterando el tipo que implementa el trait `Iterator`. La definición del trait `Iterator` se muestra en la Lista 19-12.

```rust
pub trait Iterator {
    type Item;

    fn next(&mut self) -> Option<Self::Item>;
}
```

Lista 19-12: La definición del trait `Iterator` que tiene un tipo asociado `Item`

El tipo `Item` es un marcador de posición, y la definición del método `next` muestra que devolverá valores del tipo `Option<Self::Item>`. Los implementadores del trait `Iterator` especificarán el tipo concrete para `Item`, y el método `next` devolverá un `Option` que contiene un valor de ese tipo concrete.

Los tipos asociados pueden parecer un concepto similar a los genéricos, en el sentido de que estos últimos nos permiten definir una función sin especificar qué tipos puede manejar. Para examinar la diferencia entre estos dos conceptos, veremos una implementación del trait `Iterator` en un tipo llamado `Counter` que especifica que el tipo `Item` es `u32`:

Nombre de archivo: `src/lib.rs`

```rust
impl Iterator for Counter {
    type Item = u32;

    fn next(&mut self) -> Option<Self::Item> {
        --snip--
```

Esta sintaxis parece comparable a la de los genéricos. Entonces, ¿por qué no simplemente definir el trait `Iterator` con genéricos, como se muestra en la Lista 19-13?

```rust
pub trait Iterator<T> {
    fn next(&mut self) -> Option<T>;
}
```

Lista 19-13: Una definición hipotética del trait `Iterator` usando genéricos

La diferencia es que al usar genéricos, como en la Lista 19-13, debemos anotar los tipos en cada implementación; porque también podemos implementar `Iterator<``String``> para Counter` o cualquier otro tipo, podríamos tener múltiples implementaciones de `Iterator` para `Counter`. En otras palabras, cuando un trait tiene un parámetro genérico, se puede implementar para un tipo múltiples veces, cambiando los tipos concrete de los parámetros de tipo genérico cada vez. Cuando usamos el método `next` en `Counter`, tendríamos que proporcionar anotaciones de tipo para indicar qué implementación de `Iterator` queremos usar.

Con los tipos asociados, no necesitamos anotar los tipos porque no podemos implementar un trait para un tipo múltiples veces. En la Lista 19-12 con la definición que usa tipos asociados, podemos elegir cuál será el tipo de `Item` solo una vez porque solo puede haber una `impl Iterator for Counter`. No tenemos que especificar que queremos un iterador de valores de `u32` en todos los lugares donde llamamos a `next` en `Counter`.

Los tipos asociados también se convierten en parte del contrato del trait: los implementadores del trait deben proporcionar un tipo para sustituir el marcador de posición del tipo asociado. Los tipos asociados a menudo tienen un nombre que describe cómo se usará el tipo, y documentar el tipo asociado en la documentación de la API es una buena práctica.
