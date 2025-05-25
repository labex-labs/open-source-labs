# Especificando Múltiplos Trait Bounds com a Sintaxe +

Também podemos especificar mais de um trait bound. Digamos que quiséssemos que `notify` usasse formatação de exibição (display formatting) além de `summarize` em `item`: especificamos na definição de `notify` que `item` deve implementar tanto `Display` quanto `Summary`. Podemos fazer isso usando a sintaxe `+`:

```rust
pub fn notify(item: &(impl Summary + Display)) {
```

A sintaxe `+` também é válida com trait bounds em tipos genéricos:

```rust
pub fn notify<T: Summary + Display>(item: &T) {
```

Com os dois trait bounds especificados, o corpo de `notify` pode chamar `summarize` e usar `{}` para formatar `item`.
