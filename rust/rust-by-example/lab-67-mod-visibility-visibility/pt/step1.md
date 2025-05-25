# Visibilidade

Por padrão, os itens em um módulo têm visibilidade privada, mas isso pode ser substituído pelo modificador `pub`. Somente os itens públicos de um módulo podem ser acessados fora do escopo do módulo.

```rust
// Um módulo chamado `my_mod`
mod my_mod {
    // Itens em módulos têm visibilidade privada por padrão.
    fn private_function() {
        println!("chamando `my_mod::private_function()`");
    }

    // Use o modificador `pub` para substituir a visibilidade padrão.
    pub fn function() {
        println!("chamando `my_mod::function()`");
    }

    // Itens podem acessar outros itens no mesmo módulo,
    // mesmo que privados.
    pub fn indirect_access() {
        print!("chamando `my_mod::indirect_access()`, que\n> ");
        private_function();
    }

    // Módulos também podem ser aninhados
    pub mod nested {
        pub fn function() {
            println!("chamando `my_mod::nested::function()`");
        }

        #[allow(dead_code)]
        fn private_function() {
            println!("chamando `my_mod::nested::private_function()`");
        }

        // Funções declaradas usando a sintaxe `pub(in path)` são visíveis
        // apenas no caminho especificado. `path` deve ser um módulo pai ou ancestral
        pub(in crate::my_mod) fn public_function_in_my_mod() {
            print!("chamando `my_mod::nested::public_function_in_my_mod()`, que\n> ");
            public_function_in_nested();
        }

        // Funções declaradas usando a sintaxe `pub(self)` são visíveis apenas
        // no módulo atual, o que é o mesmo que deixá-las privadas
        pub(self) fn public_function_in_nested() {
            println!("chamando `my_mod::nested::public_function_in_nested()`");
        }

        // Funções declaradas usando a sintaxe `pub(super)` são visíveis apenas
        // no módulo pai
        pub(super) fn public_function_in_super_mod() {
            println!("chamando `my_mod::nested::public_function_in_super_mod()`");
        }
    }

    pub fn call_public_function_in_my_mod() {
        print!("chamando `my_mod::call_public_function_in_my_mod()`, que\n> ");
        nested::public_function_in_my_mod();
        print!("> ");
        nested::public_function_in_super_mod();
    }

    // pub(crate) torna as funções visíveis apenas dentro do crate atual
    pub(crate) fn public_function_in_crate() {
        println!("chamando `my_mod::public_function_in_crate()`");
    }

    // Módulos aninhados seguem as mesmas regras de visibilidade
    mod private_nested {
        #[allow(dead_code)]
        pub fn function() {
            println!("chamando `my_mod::private_nested::function()`");
        }

        // Itens pais privados ainda restringirão a visibilidade de um item filho,
        // mesmo que seja declarado como visível em um escopo maior.
        #[allow(dead_code)]
        pub(crate) fn restricted_function() {
            println!("chamando `my_mod::private_nested::restricted_function()`");
        }
    }
}

fn function() {
    println!("chamando `function()`");
}

fn main() {
    // Módulos permitem a desambiguação entre itens com o mesmo nome.
    function();
    my_mod::function();

    // Itens públicos, incluindo aqueles dentro de módulos aninhados, podem ser
    // acessados fora do módulo pai.
    my_mod::indirect_access();
    my_mod::nested::function();
    my_mod::call_public_function_in_my_mod();

    // Itens pub(crate) podem ser chamados de qualquer lugar no mesmo crate
    my_mod::public_function_in_crate();

    // Itens pub(in path) só podem ser chamados dentro do módulo especificado
    // Erro! A função `public_function_in_my_mod` é privada
    //my_mod::nested::public_function_in_my_mod();
    // TODO ^ Tente descomentar esta linha

    // Itens privados de um módulo não podem ser acessados diretamente, mesmo que
    // aninhados em um módulo público:

    // Erro! `private_function` é privado
    //my_mod::private_function();
    // TODO ^ Tente descomentar esta linha

    // Erro! `private_function` é privado
    //my_mod::nested::private_function();
    // TODO ^ Tente descomentar esta linha

    // Erro! `private_nested` é um módulo privado
    //my_mod::private_nested::function();
    // TODO ^ Tente descomentar esta linha

    // Erro! `private_nested` é um módulo privado
    //my_mod::private_nested::restricted_function();
    // TODO ^ Tente descomentar esta linha
}
```
