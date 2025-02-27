# Видимость

По умолчанию элементы в модуле имеют приватную видимость, но это можно переопределить с помощью модификатора `pub`. Только публичные элементы модуля могут быть доступны из вне области модуля.

```rust
// Модуль с именем `my_mod`
mod my_mod {
    // Элементы в модулях по умолчанию имеют приватную видимость.
    fn private_function() {
        println!("вызвана `my_mod::private_function()`");
    }

    // Используйте модификатор `pub`, чтобы переопределить стандартную видимость.
    pub fn function() {
        println!("вызвана `my_mod::function()`");
    }

    // Элементы могут обращаться к другим элементам в том же модуле,
    // даже если они приватные.
    pub fn indirect_access() {
        print!("вызвана `my_mod::indirect_access()`, которая\n> ");
        private_function();
    }

    // Модули также могут быть вложенными
    pub mod nested {
        pub fn function() {
            println!("вызвана `my_mod::nested::function()`");
        }

        #[allow(dead_code)]
        fn private_function() {
            println!("вызвана `my_mod::nested::private_function()`");
        }

        // Функции, объявленные с использованием синтаксиса `pub(in path)`, доступны только
        // внутри заданного пути. `path` должен быть родительским или предком модуля
        pub(in crate::my_mod) fn public_function_in_my_mod() {
            print!("вызвана `my_mod::nested::public_function_in_my_mod()`, которая\n> ");
            public_function_in_nested();
        }

        // Функции, объявленные с использованием синтаксиса `pub(self)`, доступны только внутри
        // текущего модуля, что эквивалентно их оставлению приватными
        pub(self) fn public_function_in_nested() {
            println!("вызвана `my_mod::nested::public_function_in_nested()`");
        }

        // Функции, объявленные с использованием синтаксиса `pub(super)`, доступны только внутри
        // родительского модуля
        pub(super) fn public_function_in_super_mod() {
            println!("вызвана `my_mod::nested::public_function_in_super_mod()`");
        }
    }

    pub fn call_public_function_in_my_mod() {
        print!("вызвана `my_mod::call_public_function_in_my_mod()`, которая\n> ");
        nested::public_function_in_my_mod();
        print!("> ");
        nested::public_function_in_super_mod();
    }

    // pub(crate) делает функции доступными только внутри текущего пакета
    pub(crate) fn public_function_in_crate() {
        println!("вызвана `my_mod::public_function_in_crate()`");
    }

    // Вложенные модули следуют тем же правилам видимости
    mod private_nested {
        #[allow(dead_code)]
        pub fn function() {
            println!("вызвана `my_mod::private_nested::function()`");
        }

        // Приватные родительские элементы по-прежнему ограничивают видимость дочернего элемента,
        // даже если он объявлен видимым в большей области.
        #[allow(dead_code)]
        pub(crate) fn restricted_function() {
            println!("вызвана `my_mod::private_nested::restricted_function()`");
        }
    }
}

fn function() {
    println!("вызвана `function()`");
}

fn main() {
    // Модули позволяют избежать конфликтов между элементами с одинаковыми именами.
    function();
    my_mod::function();

    // Публичные элементы, включая те, внутри вложенных модулей, могут быть
    // доступны из вне родительского модуля.
    my_mod::indirect_access();
    my_mod::nested::function();
    my_mod::call_public_function_in_my_mod();

    // Элементы pub(crate) могут быть вызваны из любого места в том же пакете
    my_mod::public_function_in_crate();

    // Элементы pub(in path) могут быть вызваны только из внутри указанного модуля
    // Ошибка! функция `public_function_in_my_mod` является приватной
    //my_mod::nested::public_function_in_my_mod();
    // TODO ^ Попробуйте раскомментировать эту строку

    // Приватные элементы модуля не могут быть напрямую доступны, даже если
    // они вложены в публичный модуль:

    // Ошибка! `private_function` является приватной
    //my_mod::private_function();
    // TODO ^ Попробуйте раскомментировать эту строку

    // Ошибка! `private_function` является приватной
    //my_mod::nested::private_function();
    // TODO ^ Попробуйте раскомментировать эту строку

    // Ошибка! `private_nested` - приватный модуль
    //my_mod::private_nested::function();
    // TODO ^ Попробуйте раскомментировать эту строку

    // Ошибка! `private_nested` - приватный модуль
    //my_mod::private_nested::restricted_function();
    // TODO ^ Попробуйте раскомментировать эту строку
}
```
