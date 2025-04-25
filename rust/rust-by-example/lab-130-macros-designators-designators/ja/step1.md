# 指定子

マクロの引数は、ドル記号`$`で接頭辞を付けられ、*指定子*で型付けされます。

```rust
macro_rules! create_function {
    // このマクロは、指定子 `ident` の引数を取り、
    // `$func_name` という名前の関数を作成します。
    // `ident` 指定子は、変数/関数名に使用されます。
    ($func_name:ident) => {
        fn $func_name() {
            // `stringify!`マクロは、`ident` を文字列に変換します。
            println!("You called {:?}()",
                     stringify!($func_name));
        }
    };
}

// 上記のマクロを使って、`foo`と `bar` という名前の関数を作成します。
create_function!(foo);
create_function!(bar);

macro_rules! print_result {
    // このマクロは、`expr` 型の式を取り、
    // それを文字列としてその結果とともに表示します。
    // `expr` 指定子は、式に使用されます。
    ($expression:expr) => {
        // `stringify!` は、式をそのまま文字列に変換します。
        println!("{:?} = {:?}",
                 stringify!($expression),
                 $expression);
    };
}

fn main() {
    foo();
    bar();

    print_result!(1u32 + 1);

    // ブロックも式であることを思い出してください！
    print_result!({
        let x = 1u32;

        x * x + 2 * x - 1
    });
}
```

これらは利用可能な指定子のいくつかです。

- `block`
- `expr`は式に使用されます
- `ident`は変数/関数名に使用されます
- `item`
- `literal`はリテラル定数に使用されます
- `pat`（_パターン_）
- `path`
- `stmt`（_文_）
- `tt`（_トークンツリー_）
- `ty`（_型_）
- `vis`（_可視性修飾子_）

完全なリストについては、\[Rust Reference\]を参照してください。
