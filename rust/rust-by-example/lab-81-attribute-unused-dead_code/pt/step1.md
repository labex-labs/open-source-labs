# `dead_code`

O compilador fornece um _aviso_ `dead_code` que emitirá um alerta sobre funções não utilizadas. Um _atributo_ pode ser usado para desabilitar esse aviso.

```rust
fn used_function() {}

// `#[allow(dead_code)]` é um atributo que desabilita o aviso `dead_code`
#[allow(dead_code)]
fn unused_function() {}

fn noisy_unused_function() {}
// FIXME ^ Adicione um atributo para suprimir o aviso

fn main() {
    used_function();
}
```

Observe que, em programas reais, você deve eliminar o código morto. Nestes exemplos, permitiremos o código morto em alguns lugares devido à natureza interativa dos exemplos.
