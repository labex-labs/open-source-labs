# Sintaxis de Límite de Trait

La sintaxis `impl Trait` funciona para casos sencillos, pero en realidad es azúcar sintáctico para una forma más larga conocida como _límite de trait_; se ve así:

```rust
pub fn notify<T: Summary>(item: &T) {
    println!("Breaking news! {}", item.summarize());
}
```

Esta forma más larga es equivalente al ejemplo de la sección anterior, pero es más verbosa. Colocamos los límites de trait con la declaración del parámetro de tipo genérico después de dos puntos y dentro de corchetes angulares.

La sintaxis `impl Trait` es conveniente y produce un código más conciso en casos simples, mientras que la sintaxis más completa de límite de trait puede expresar más complejidad en otros casos. Por ejemplo, podemos tener dos parámetros que implementen `Summary`. Hacer esto con la sintaxis `impl Trait` se ve así:

```rust
pub fn notify(item1: &impl Summary, item2: &impl Summary) {
```

Usar `impl Trait` es adecuado si queremos que esta función permita que `item1` e `item2` tengan diferentes tipos (siempre y cuando ambos tipos implementen `Summary`). Sin embargo, si queremos forzar a que ambos parámetros tengan el mismo tipo, entonces debemos usar un límite de trait, como esto:

```rust
pub fn notify<T: Summary>(item1: &T, item2: &T) {
```

El tipo genérico `T` especificado como el tipo de los parámetros `item1` e `item2` restringe la función de modo que el tipo concrete del valor pasado como argumento para `item1` e `item2` debe ser el mismo.
