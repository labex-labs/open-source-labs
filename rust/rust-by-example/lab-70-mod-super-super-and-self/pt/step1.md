# `super` e `self`

As palavras-chave `super` e `self` podem ser usadas no caminho para remover ambiguidade ao acessar itens e evitar a codificação desnecessária de caminhos.

```rust
fn function() {
    println!("chamada `function()`");
}

mod cool {
    pub fn function() {
        println!("chamada `cool::function()`");
    }
}

mod my {
    fn function() {
        println!("chamada `my::function()`");
    }

    mod cool {
        pub fn function() {
            println!("chamada `my::cool::function()`");
        }
    }

    pub fn indirect_call() {
        // Vamos acessar todas as funções nomeadas `function` deste escopo!
        print!("chamada `my::indirect_call()`, que\n> ");

        // A palavra-chave `self` refere-se ao escopo do módulo atual - neste caso, `my`.
        // Chamar `self::function()` e chamar `function()` diretamente produzem o mesmo resultado, porque se referem à mesma função.
        self::function();
        function();

        // Também podemos usar `self` para acessar outro módulo dentro de `my`:
        self::cool::function();

        // A palavra-chave `super` refere-se ao escopo pai (fora do módulo `my`).
        super::function();

        // Isso se ligará à `cool::function` no escopo do *crate*.
        // Neste caso, o escopo do crate é o escopo mais externo.
        {
            use crate::cool::function as root_function;
            root_function();
        }
    }
}

fn main() {
    my::indirect_call();
}
```
