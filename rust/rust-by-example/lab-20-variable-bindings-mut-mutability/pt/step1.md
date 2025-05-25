# Mutabilidade

As ligações de variáveis são imutáveis por padrão, mas isso pode ser contornado usando o modificador `mut`.

```rust
fn main() {
    let _immutable_binding = 1;
    let mut mutable_binding = 1;

    println!("Antes da mutação: {}", mutable_binding);

    // Ok
    mutable_binding += 1;

    println!("Após a mutação: {}", mutable_binding);

    // Erro! Não é possível atribuir um novo valor a uma variável imutável
    _immutable_binding += 1;
}
```

O compilador emitirá um diagnóstico detalhado sobre erros de mutabilidade.
