# RAII

Rust の変数は、スタックにデータを保持するだけでなく、リソースを「所有」します。たとえば、`Box<T>` はヒープ内のメモリを所有します。Rust は RAII（Resource Acquisition Is Initialization）を強制するため、オブジェクトがスコープ外になるときに、そのデストラクタが呼び出され、所有しているリソースが解放されます。

この動作は、「リソースリーク」のバグから保護します。したがって、手動でメモリを解放したり、メモリリークを心配する必要はありません！ 以下は簡単なサンプルです：

```rust
// raii.rs
fn create_box() {
    // ヒープ上に整数を割り当てる
    let _box1 = Box::new(3i32);

    // `_box1` はここで破棄され、メモリが解放されます
}

fn main() {
    // ヒープ上に整数を割り当てる
    let _box2 = Box::new(5i32);

    // ネストされたスコープ：
    {
        // ヒープ上に整数を割り当てる
        let _box3 = Box::new(4i32);

        // `_box3` はここで破棄され、メモリが解放されます
    }

    // ただ楽しみにたくさんのボックスを作成する
    // メモリを手動で解放する必要はありません！
    for _ in 0u32..1_000 {
        create_box();
    }

    // `_box2` はここで破棄され、メモリが解放されます
}
```

もちろん、`valgrind` を使ってメモリエラーを二重チェックすることができます：

```{=html}
<!-- REUSE-IgnoreStart -->
```

```{=html}
<!-- Prevent REUSE from parsing the copyright statement in the sample code -->
```

```shell
$ rustc raii.rs && valgrind./raii
==26873== Memcheck, a memory error detector
==26873== Copyright (C) 2002-2013, and GNU GPL'd, by Julian Seward et al.
==26873== Using Valgrind-3.9.0 and LibVEX; rerun with -h for copyright info
==26873== Command:./raii
==26873==
==26873==
==26873== HEAP SUMMARY:
==26873==     in use at exit: 0 bytes in 0 blocks
==26873==   total heap usage: 1,013 allocs, 1,013 frees, 8,696 bytes allocated
==26873==
==26873== All heap blocks were freed -- no leaks are possible
==26873==
==26873== For counts of detected and suppressed errors, rerun with: -v
==26873== ERROR SUMMARY: 0 errors from 0 contexts (suppressed: 2 from 2)
```

```{=html}
<!-- REUSE-IgnoreEnd -->
```

ここにはリークはありません！

## デストラクタ

Rust におけるデストラクタの概念は、\[`Drop`\] トレイトを通じて提供されます。デストラクタは、リソースがスコープ外になるときに呼び出されます。このトレイトはすべての型に対して実装する必要はありません。独自のデストラクタロジックが必要な場合にのみ、型に対して実装します。

以下の例を実行して、\[`Drop`\] トレイトがどのように機能するかを確認してみましょう。`main` 関数内の変数がスコープ外になると、カスタムデストラクタが呼び出されます。

```rust
struct ToDrop;

impl Drop for ToDrop {
    fn drop(&mut self) {
        println!("ToDrop is being dropped");
    }
}

fn main() {
    let x = ToDrop;
    println!("Made a ToDrop!");
}
```
