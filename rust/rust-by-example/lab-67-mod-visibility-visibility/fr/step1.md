# Visibilité

Par défaut, les éléments d'un module ont une visibilité privée, mais cela peut être modifié avec le modificateur `pub`. Seuls les éléments publics d'un module peuvent être accédés depuis l'extérieur de la portée du module.

```rust
// Un module nommé `my_mod`
mod my_mod {
    // Les éléments dans les modules ont une visibilité privée par défaut.
    fn private_function() {
        println!("appelé `my_mod::private_function()`");
    }

    // Utilisez le modificateur `pub` pour modifier la visibilité par défaut.
    pub fn function() {
        println!("appelé `my_mod::function()`");
    }

    // Les éléments peuvent accéder à d'autres éléments dans le même module,
    // même lorsqu'ils sont privés.
    pub fn indirect_access() {
        print!("appelé `my_mod::indirect_access()`, qui\n> ");
        private_function();
    }

    // Les modules peuvent également être imbriqués
    pub mod nested {
        pub fn function() {
            println!("appelé `my_mod::nested::function()`");
        }

        #[allow(dead_code)]
        fn private_function() {
            println!("appelé `my_mod::nested::private_function()`");
        }

        // Les fonctions déclarées avec la syntaxe `pub(in path)` ne sont visibles que
        // dans le chemin donné. `path` doit être un module parent ou ancêtre
        pub(in crate::my_mod) fn public_function_in_my_mod() {
            print!("appelé `my_mod::nested::public_function_in_my_mod()`, qui\n> ");
            public_function_in_nested();
        }

        // Les fonctions déclarées avec la syntaxe `pub(self)` ne sont visibles que dans
        // le module actuel, ce qui est équivalent à les laisser privées
        pub(self) fn public_function_in_nested() {
            println!("appelé `my_mod::nested::public_function_in_nested()`");
        }

        // Les fonctions déclarées avec la syntaxe `pub(super)` ne sont visibles que dans
        // le module parent
        pub(super) fn public_function_in_super_mod() {
            println!("appelé `my_mod::nested::public_function_in_super_mod()`");
        }
    }

    pub fn call_public_function_in_my_mod() {
        print!("appelé `my_mod::call_public_function_in_my_mod()`, qui\n> ");
        nested::public_function_in_my_mod();
        print!("> ");
        nested::public_function_in_super_mod();
    }

    // pub(crate) rend les fonctions visibles uniquement dans la crate actuelle
    pub(crate) fn public_function_in_crate() {
        println!("appelé `my_mod::public_function_in_crate()`");
    }

    // Les modules imbriqués suivent les mêmes règles de visibilité
    mod private_nested {
        #[allow(dead_code)]
        pub fn function() {
            println!("appelé `my_mod::private_nested::function()`");
        }

        // Les éléments parents privés restreindront toujours la visibilité d'un élément enfant,
        // même s'il est déclaré visible dans une portée plus large.
        #[allow(dead_code)]
        pub(crate) fn restricted_function() {
            println!("appelé `my_mod::private_nested::restricted_function()`");
        }
    }
}

fn function() {
    println!("appelé `function()`");
}

fn main() {
    // Les modules permettent de distinguer entre des éléments ayant le même nom.
    function();
    my_mod::function();

    // Les éléments publics, y compris ceux à l'intérieur de modules imbriqués, peuvent être
    // accédés depuis l'extérieur du module parent.
    my_mod::indirect_access();
    my_mod::nested::function();
    my_mod::call_public_function_in_my_mod();

    // Les éléments pub(crate) peuvent être appelés depuis n'importe où dans la même crate
    my_mod::public_function_in_crate();

    // Les éléments pub(in path) ne peuvent être appelés que depuis le module spécifié
    // Erreur! La fonction `public_function_in_my_mod` est privée
    //my_mod::nested::public_function_in_my_mod();
    // TODO ^ Essayez de décommenter cette ligne

    // Les éléments privés d'un module ne peuvent pas être directement accédés, même si
    // ils sont imbriqués dans un module public :

    // Erreur! `private_function` est privée
    //my_mod::private_function();
    // TODO ^ Essayez de décommenter cette ligne

    // Erreur! `private_function` est privée
    //my_mod::nested::private_function();
    // TODO ^ Essayez de décommenter cette ligne

    // Erreur! `private_nested` est un module privé
    //my_mod::private_nested::function();
    // TODO ^ Essayez de décommenter cette ligne

    // Erreur! `private_nested` est un module privé
    //my_mod::private_nested::restricted_function();
    // TODO ^ Essayez de décommenter cette ligne
}
```
