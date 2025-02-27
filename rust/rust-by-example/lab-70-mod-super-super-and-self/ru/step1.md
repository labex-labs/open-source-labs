# `super` и `self`

Ключевые слова `super` и `self` могут использоваться в пути для устранения двусмысленности при доступе к элементам и предотвращения ненужного жесткого кодирования путей.

```rust
fn function() {
    println!("called `function()`");
}

mod cool {
    pub fn function() {
        println!("called `cool::function()`");
    }
}

mod my {
    fn function() {
        println!("called `my::function()`");
    }

    mod cool {
        pub fn function() {
            println!("called `my::cool::function()`");
        }
    }

    pub fn indirect_call() {
        // Давайте обратимся ко всем функциям с именем `function` из этого скоупа!
        print!("called `my::indirect_call()`, that\n> ");

        // Ключевое слово `self` ссылается на текущий модульный скоуп - в данном случае `my`.
        // Вызов `self::function()` и прямой вызов `function()` дают
        // один и тот же результат, потому что они ссылаются на одну и ту же функцию.
        self::function();
        function();

        // Мы также можем использовать `self` для доступа к другому модулю внутри `my`:
        self::cool::function();

        // Ключевое слово `super` ссылается на родительский скоуп (за пределами модуля `my`).
        super::function();

        // Это будет ссылаться на `cool::function` в скоупе *коробки*.
        // В данном случае скоуп коробки - это самый внешний скоуп.
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
