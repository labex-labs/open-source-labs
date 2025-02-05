# 可见性

默认情况下，模块中的项具有私有可见性，但可以使用 `pub` 修饰符来覆盖它。只有模块的公共项才能在模块作用域之外访问。

```rust
// 一个名为 `my_mod` 的模块
mod my_mod {
    // 模块中的项默认具有私有可见性。
    fn private_function() {
        println!("调用了 `my_mod::private_function()`");
    }

    // 使用 `pub` 修饰符来覆盖默认可见性。
    pub fn function() {
        println!("调用了 `my_mod::function()`");
    }

    // 项可以访问同一模块中的其他项，
    // 即使是私有的。
    pub fn indirect_access() {
        print!("调用了 `my_mod::indirect_access()`，即\n> ");
        private_function();
    }

    // 模块也可以嵌套
    pub mod nested {
        pub fn function() {
            println!("调用了 `my_mod::nested::function()`");
        }

        #[allow(dead_code)]
        fn private_function() {
            println!("调用了 `my_mod::nested::private_function()`");
        }

        // 使用 `pub(in path)` 语法声明的函数仅在给定路径内可见。
        // `path` 必须是父模块或祖先模块
        pub(in crate::my_mod) fn public_function_in_my_mod() {
            print!("调用了 `my_mod::nested::public_function_in_my_mod()`，即\n> ");
            public_function_in_nested();
        }

        // 使用 `pub(self)` 语法声明的函数仅在当前模块内可见，
        // 这与将它们设为私有相同
        pub(self) fn public_function_in_nested() {
            println!("调用了 `my_mod::nested::public_function_in_nested()`");
        }

        // 使用 `pub(super)` 语法声明的函数仅在父模块内可见
        pub(super) fn public_function_in_super_mod() {
            println!("调用了 `my_mod::nested::public_function_in_super_mod()`");
        }
    }

    pub fn call_public_function_in_my_mod() {
        print!("调用了 `my_mod::call_public_function_in_my_mod()`，即\n> ");
        nested::public_function_in_my_mod();
        print!("> ");
        nested::public_function_in_super_mod();
    }

    // pub(crate) 使函数仅在当前 crate 内可见
    pub(crate) fn public_function_in_crate() {
        println!("调用了 `my_mod::public_function_in_crate()`");
    }

    // 嵌套模块遵循相同的可见性规则
    mod private_nested {
        #[allow(dead_code)]
        pub fn function() {
            println!("调用了 `my_mod::private_nested::function()`");
        }

        // 即使子项在更大的作用域内声明为可见，
        // 私有父项仍会限制子项的可见性。
        #[allow(dead_code)]
        pub(crate) fn restricted_function() {
            println!("调用了 `my_mod::private_nested::restricted_function()`");
        }
    }
}

fn function() {
    println!("调用了 `function()`");
}

fn main() {
    // 模块允许区分具有相同名称的项。
    function();
    my_mod::function();

    // 公共项，包括嵌套模块内的公共项，可以
    // 从父模块外部访问。
    my_mod::indirect_access();
    my_mod::nested::function();
    my_mod::call_public_function_in_my_mod();

    // pub(crate) 项可以在同一 crate 中的任何位置调用
    my_mod::public_function_in_crate();

    // pub(in path) 项只能从指定的模块内调用
    // 错误！函数 `public_function_in_my_mod` 是私有的
    //my_mod::nested::public_function_in_my_mod();
    // TODO ^ 尝试取消注释此行

    // 模块的私有项不能直接访问，即使
    // 嵌套在公共模块中：

    // 错误！`private_function` 是私有的
    //my_mod::private_function();
    // TODO ^ 尝试取消注释此行

    // 错误！`private_function` 是私有的
    //my_mod::nested::private_function();
    // TODO ^ 尝试取消注释此行

    // 错误！`private_nested` 是一个私有模块
    //my_mod::private_nested::function();
    // TODO ^ 尝试取消注释此行

    // 错误！`private_nested` 是一个私有模块
    //my_mod::private_nested::restricted_function();
    // TODO ^ 尝试取消注释此行
}
```
