# `super` と `self`

`super` と `self` キーワードは、アイテムにアクセスする際の曖昧さを解消し、不必要なハードコーディングを防ぐためにパスに使用できます。

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
        // このスコープから `function` という名前のすべての関数にアクセスしましょう！
        print!("called `my::indirect_call()`, that\n> ");

        // `self` キーワードは、現在のモジュールスコープ（この場合は `my`）を指します。
        // `self::function()` を呼び出して、直接 `function()` を呼び出しても同じ結果になります。
        // なぜなら、同じ関数を参照しているからです。
        self::function();
        function();

        // `self` を使って `my` 内の別のモジュールにアクセスすることもできます。
        self::cool::function();

        // `super` キーワードは、親スコープ（`my` モジュールの外）を指します。
        super::function();

        // これは、クレートスコープ内の `cool::function` にバインドされます。
        // この場合、クレートスコープは最も外側のスコープです。
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
