# Sintaxe de Trait Bound

A sintaxe `impl Trait` funciona para casos simples, mas na verdade é açúcar sintático para uma forma mais longa conhecida como _trait bound_ (limite de trait); ela se parece com isto:

```rust
pub fn notify<T: Summary>(item: &T) {
    println!("Breaking news! {}", item.summarize());
}
```

Esta forma mais longa é equivalente ao exemplo na seção anterior, mas é mais verbosa. Colocamos os limites de trait com a declaração do parâmetro de tipo genérico após dois pontos e dentro de colchetes angulares.

A sintaxe `impl Trait` é conveniente e torna o código mais conciso em casos simples, enquanto a sintaxe de trait bound mais completa pode expressar mais complexidade em outros casos. Por exemplo, podemos ter dois parâmetros que implementam `Summary`. Fazer isso com a sintaxe `impl Trait` se parece com isto:

```rust
pub fn notify(item1: &impl Summary, item2: &impl Summary) {
```

Usar `impl Trait` é apropriado se quisermos que esta função permita que `item1` e `item2` tenham tipos diferentes (desde que ambos os tipos implementem `Summary`). Se quisermos forçar ambos os parâmetros a ter o mesmo tipo, no entanto, devemos usar um trait bound, assim:

```rust
pub fn notify<T: Summary>(item1: &T, item2: &T) {
```

O tipo genérico `T` especificado como o tipo dos parâmetros `item1` e `item2` restringe a função de forma que o tipo concreto do valor passado como um argumento para `item1` e `item2` deve ser o mesmo.
