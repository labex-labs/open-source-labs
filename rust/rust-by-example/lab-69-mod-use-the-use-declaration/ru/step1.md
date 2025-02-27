# Объявление `use`

Объявление `use` можно использовать для связывания полного пути с новым именем для более удобного доступа. Оно часто используется так:

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

Вы можете использовать ключевое слово `as`, чтобы связать импорты с другим именем:

```rust
// Свяжите путь `deeply::nested::function` с `other_function`.
use deeply::nested::function as other_function;

fn function() {
    println!("called `function()`");
}

mod deeply {
    pub mod nested {
        pub fn function() {
            println!("called `deeply::nested::function()`");
        }
    }
}

fn main() {
    // Более удобный доступ к `deeply::nested::function`
    other_function();

    println!("Entering block");
    {
        // Это эквивалентно `use deeply::nested::function as function`.
        // Эта `function()` будет скрывать внешнюю.
        use crate::deeply::nested::function;

        // Связи `use` имеют локальную область видимости. В этом случае
        // скрытие `function()` происходит только в этом блоке.
        function();

        println!("Leaving block");
    }

    function();
}
```
