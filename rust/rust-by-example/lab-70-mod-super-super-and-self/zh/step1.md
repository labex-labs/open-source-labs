# `super` 和 `self`

`super` 和 `self` 关键字可用于路径中，以消除访问项时的歧义，并防止路径出现不必要的硬编码。

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
        // 让我们从这个作用域中访问所有名为 `function` 的函数！
        print!("called `my::indirect_call()`, that\n> ");

        // `self` 关键字指代当前模块作用域——在这种情况下是 `my`。
        // 调用 `self::function()` 和直接调用 `function()` 都会得到
        // 相同的结果，因为它们指代同一个函数。
        self::function();
        function();

        // 我们也可以使用 `self` 来访问 `my` 内部的另一个模块：
        self::cool::function();

        // `super` 关键字指代父作用域（在 `my` 模块之外）。
        super::function();

        // 这将绑定到 *包* 作用域中的 `cool::function`。
        // 在这种情况下，包作用域是最外层作用域。
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
