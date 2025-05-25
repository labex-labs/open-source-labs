# A Declaração `use`

A declaração `use` pode ser usada para vincular um caminho completo a um novo nome, para facilitar o acesso. É frequentemente usada assim:

```rust
use crate::deeply::nested::{
    my_first_function,
    my_second_function,
    AndATraitType
};

fn main() {
    my_first_function();
}
```

Você pode usar a palavra-chave `as` para vincular importações a um nome diferente:

```rust
// Vincula o caminho `deeply::nested::function` a `other_function`.
use deeply::nested::function as other_function;

fn function() {
    println!("chamada `function()`");
}

mod deeply {
    pub mod nested {
        pub fn function() {
            println!("chamada `deeply::nested::function()`");
        }
    }
}

fn main() {
    // Acesso mais fácil a `deeply::nested::function`
    other_function();

    println!("Entrando no bloco");
    {
        // Isto é equivalente a `use deeply::nested::function as function`.
        // Este `function()` vai sombrear o externo.
        use crate::deeply::nested::function;

        // As ligações `use` têm um escopo local. Neste caso, o
        // sombreamento de `function()` está apenas neste bloco.
        function();

        println!("Saindo do bloco");
    }

    function();
}
```
