# `use`宣言

`use`宣言は、より簡単なアクセスのために、完全修飾名を新しい名前にバインドするために使用できます。よくこのように使われます。

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

`as`キーワードを使って、インポートを別の名前にバインドすることもできます。

```rust
// `deeply::nested::function`パスを`other_function`にバインドします。
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
    // `deeply::nested::function`へのアクセスを簡単にします
    other_function();

    println!("Entering block");
    {
        // これは`use deeply::nested::function as function`と同等です。
        // この`function()`は外側のものを上書きします。
        use crate::deeply::nested::function;

        // `use`のバインドはローカルスコープを持ちます。この場合、
        // `function()`の上書きはこのブロック内だけです。
        function();

        println!("Leaving block");
    }

    function();
}
```
