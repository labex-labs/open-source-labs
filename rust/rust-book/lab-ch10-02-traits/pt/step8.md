# Trait Bounds Mais Claras com Cláusulas where

Usar muitos trait bounds tem suas desvantagens. Cada genérico tem seus próprios trait bounds, então funções com múltiplos parâmetros de tipo genérico podem conter muitas informações de trait bound entre o nome da função e sua lista de parâmetros, tornando a assinatura da função difícil de ler. Por esta razão, Rust tem uma sintaxe alternativa para especificar trait bounds dentro de uma cláusula `where` após a assinatura da função. Então, em vez de escrever isto:

```rust
fn some_function<T: Display + Clone, U: Clone + Debug>(t: &T, u: &U) -> i32 {
```

podemos usar uma cláusula `where`, assim:

```rust
fn some_function<T, U>(t: &T, u: &U) -> i32
where
    T: Display + Clone,
    U: Clone + Debug,
{
```

A assinatura desta função é menos confusa: o nome da função, a lista de parâmetros e o tipo de retorno estão próximos, semelhante a uma função sem muitos trait bounds.
