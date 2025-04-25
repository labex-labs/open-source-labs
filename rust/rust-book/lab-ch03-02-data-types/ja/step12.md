# 無効な配列要素のアクセス

配列の末尾を超えた要素にアクセスしようとするとどうなるか見てみましょう。第 2 章の当て推測ゲームに似たコードを実行して、ユーザーから配列インデックスを取得するとします。

ファイル名：`src/main.rs`

```rust
use std::io;

fn main() {
    let a = [1, 2, 3, 4, 5];

    println!("Please enter an array index.");

    let mut index = String::new();

    io::stdin()
     .read_line(&mut index)
     .expect("Failed to read line");

    let index: usize = index
     .trim()
     .parse()
     .expect("Index entered was not a number");

    let element = a[index];

    println!(
        "The value of the element at index {index} is: {element}"
    );
}
```

このコードは正常にコンパイルされます。`cargo run`を使ってこのコードを実行し、`0`、`1`、`2`、`3`、または`4`を入力すると、プログラムは配列のそのインデックスに対応する値を表示します。代わりに配列の末尾を超えた数値を入力すると、たとえば`10`を入力すると、次のような出力が表示されます。

    thread 'main' panicked at 'index out of bounds: the len is 5 but the index is
    10', src/main.rs:19:19
    note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace

このプログラムは、インデックス操作で無効な値を使用した時点で「実行時」エラーを起こしました。プログラムはエラーメッセージとともに終了し、最後の`println!`文を実行しませんでした。インデックスを使って要素にアクセスしようとするとき、Rust は指定したインデックスが配列の長さ未満であることをチェックします。インデックスが長さ以上の場合、Rust はパニックになります。このチェックは実行時に行わなければなりません。特にこの場合、コンパイラは後でコードを実行するときにユーザーが何を入力するかを予測することはできません。

これは、Rust のメモリセーフティ原則が機能している例です。多くの低レベル言語では、この種のチェックは行われず、間違ったインデックスを指定すると、無効なメモリにアクセスできてしまいます。Rust は、メモリアクセスを許可せずに続行せずに即座に終了することで、この種のエラーから保護します。第 9 章では、Rust のエラーハンドリングと、パニックにならず、無効なメモリアクセスを許さない、読みやすく安全なコードを書く方法についてさらに説明します。
