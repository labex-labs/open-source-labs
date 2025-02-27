# La déclaration `use`

La déclaration `use` peut être utilisée pour lier un chemin complet à un nouveau nom, pour une utilisation plus facile. Elle est souvent utilisée comme ceci :

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

Vous pouvez utiliser le mot-clé `as` pour lier les importations à un nom différent :

```rust
// Lie le chemin `deeply::nested::function` à `other_function`.
use deeply::nested::function as other_function;

fn function() {
    println!("appelé `function()`");
}

mod deeply {
    pub mod nested {
        pub fn function() {
            println!("appelé `deeply::nested::function()`");
        }
    }
}

fn main() {
    // Accès plus facile à `deeply::nested::function`
    other_function();

    println!("Entrée dans le bloc");
    {
        // Ceci est équivalent à `use deeply::nested::function as function`.
        // Cette `function()` masquera la fonction externe.
        use crate::deeply::nested::function;

        // Les liaisons `use` ont une portée locale. Dans ce cas,
        // le masquage de `function()` n'est que dans ce bloc.
        function();

        println!("Sortie du bloc");
    }

    function();
}
```
