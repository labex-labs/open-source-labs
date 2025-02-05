# `use` 声明

`use` 声明可用于将完整路径绑定到一个新名称，以便更轻松地访问。它通常这样使用：

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

你可以使用 `as` 关键字将导入绑定到不同的名称：

```rust
// 将 `deeply::nested::function` 路径绑定到 `other_function`。
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
    // 更轻松地访问 `deeply::nested::function`
    other_function();

    println!("Entering block");
    {
        // 这等同于 `use deeply::nested::function as function`。
        // 这个 `function()` 将遮蔽外部的那个。
        use crate::deeply::nested::function;

        // `use` 绑定具有局部作用域。在这种情况下，
        // `function()` 的遮蔽仅在这个代码块内。
        function();

        println!("Leaving block");
    }

    function();
}
```
