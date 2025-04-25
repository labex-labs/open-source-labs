# プログラム引数

## 標準ライブラリ

コマンドライン引数にアクセスするには `std::env::args` を使用できます。これは、各引数に対して `String` を生成する反復子を返します。

```rust
use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();

    // 最初の引数は、プログラムを呼び出すために使用されたパスです。
    println!("My path is {}.", args[0]);

    // 残りの引数は、渡されたコマンドラインパラメータです。
    // このようにプログラムを呼び出します：
    //   $./args arg1 arg2
    println!("I got {:?} arguments: {:?}.", args.len() - 1, &args[1..]);
}
```

```shell
$./args 1 2 3
My path is./args.
I got 3 arguments: ["1", "2", "3"].
```

## クレート

または、コマンドラインアプリケーションを作成する際に追加の機能を提供できる多数のクレートがあります。\[Rust Cookbook\] では、より人気のあるコマンドライン引数クレートの 1 つである `clap` を使用する際のベストプラクティスが示されています。
