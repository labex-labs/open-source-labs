# 可視性

デフォルトでは、モジュール内の項目はプライベートな可視性を持ちますが、これは `pub` 修飾子でオーバーライドできます。モジュールのスコープ外からは、モジュールのパブリックな項目のみにアクセスできます。

```rust
// `my_mod` という名前のモジュール
mod my_mod {
    // モジュール内の項目はデフォルトでプライベートな可視性になります。
    fn private_function() {
        println!("called `my_mod::private_function()`");
    }

    // デフォルトの可視性をオーバーライドするには `pub` 修飾子を使用します。
    pub fn function() {
        println!("called `my_mod::function()`");
    }

    // 項目は同じモジュール内の他の項目にアクセスできます。
    // プライベートであっても。
    pub fn indirect_access() {
        print!("called `my_mod::indirect_access()`, that\n> ");
        private_function();
    }

    // モジュールはネストすることもできます。
    pub mod nested {
        pub fn function() {
            println!("called `my_mod::nested::function()`");
        }

        #[allow(dead_code)]
        fn private_function() {
            println!("called `my_mod::nested::private_function()`");
        }

        // `pub(in path)` 構文を使用して宣言された関数は、
        // 与えられたパス内でのみ可視です。`path` は親または祖先モジュールでなければなりません。
        pub(in crate::my_mod) fn public_function_in_my_mod() {
            print!("called `my_mod::nested::public_function_in_my_mod()`, that\n> ");
            public_function_in_nested();
        }

        // `pub(self)` 構文を使用して宣言された関数は、
        // 現在のモジュール内でのみ可視で、これはそれらをプライベートにしたままであることと同じです。
        pub(self) fn public_function_in_nested() {
            println!("called `my_mod::nested::public_function_in_nested()`");
        }

        // `pub(super)` 構文を使用して宣言された関数は、
        // 親モジュール内でのみ可視です。
        pub(super) fn public_function_in_super_mod() {
            println!("called `my_mod::nested::public_function_in_super_mod()`");
        }
    }

    pub fn call_public_function_in_my_mod() {
        print!("called `my_mod::call_public_function_in_my_mod()`, that\n> ");
        nested::public_function_in_my_mod();
        print!("> ");
        nested::public_function_in_super_mod();
    }

    // pub(crate) は関数を現在のクレート内でのみ可視にします。
    pub(crate) fn public_function_in_crate() {
        println!("called `my_mod::public_function_in_crate()`");
    }

    // ネストされたモジュールは可視性に関して同じルールを適用します。
    mod private_nested {
        #[allow(dead_code)]
        pub fn function() {
            println!("called `my_mod::private_nested::function()`");
        }

        // プライベートな親項目は、子項目の可視性を依然として制限します。
        // より大きなスコープ内で可視と宣言されていたとしても。
        #[allow(dead_code)]
        pub(crate) fn restricted_function() {
            println!("called `my_mod::private_nested::restricted_function()`");
        }
    }
}

fn function() {
    println!("called `function()`");
}

fn main() {
    // モジュールは同じ名前の項目間での曖昧さを解消します。
    function();
    my_mod::function();

    // パブリックな項目、ネストされたモジュール内のものを含めて、
    // 親モジュールの外からアクセスできます。
    my_mod::indirect_access();
    my_mod::nested::function();
    my_mod::call_public_function_in_my_mod();

    // pub(crate) 項目は同じクレート内のどこからでも呼び出せます。
    my_mod::public_function_in_crate();

    // pub(in path) 項目は指定されたモジュール内からのみ呼び出せます。
    // エラー！関数 `public_function_in_my_mod` はプライベートです。
    //my_mod::nested::public_function_in_my_mod();
    // TODO ^ この行のコメントを外してみてください。

    // モジュールのプライベートな項目は、
    // パブリックなモジュールにネストされていたとしても、直接アクセスできません。

    // エラー！`private_function` はプライベートです。
    //my_mod::private_function();
    // TODO ^ この行のコメントを外してみてください。

    // エラー！`private_function` はプライベートです。
    //my_mod::nested::private_function();
    // TODO ^ この行のコメントを外してみてください。

    // エラー！`private_nested` はプライベートなモジュールです。
    //my_mod::private_nested::function();
    // TODO ^ この行のコメントを外してみてください。

    // エラー！`private_nested` はプライベートなモジュールです。
    //my_mod::private_nested::restricted_function();
    // TODO ^ この行のコメントを外してみてください。
}
```
