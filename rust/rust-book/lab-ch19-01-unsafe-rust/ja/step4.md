# 不健全な関数またはメソッドを呼び出す

unsafe ブロックで実行できる 2 番目の操作は、不健全な関数を呼び出すことです。不健全な関数とメソッドは、通常の関数とメソッドとまったく同じように見えますが、定義の残りの部分の前に追加の`unsafe`があります。このコンテキストでの`unsafe`キーワードは、この関数を呼び出す際に守る必要がある要件があることを示しています。なぜなら、Rust はこれらの要件を満たしていることを保証できないからです。`unsafe`ブロック内で不健全な関数を呼び出すことで、私たちはこの関数のドキュメントを読んでおり、関数の契約を守る責任を負うことを言っています。

ここに、本体で何もしない`dangerous`という不健全な関数があります。

```rust
unsafe fn dangerous() {}
```

```rust
unsafe {
    dangerous();
}
```

私たちは、別の`unsafe`ブロック内で`dangerous`関数を呼び出さなければなりません。`unsafe`ブロックなしで`dangerous`を呼び出そうとすると、エラーが発生します。

```bash
error[E0133]: call to unsafe function is unsafe and requires
unsafe function or block
 --> src/main.rs:4:5
  |
4 |     dangerous();
  |     ^^^^^^^^^^^ call to unsafe function
  |
  = note: consult the function's documentation for information on
how to avoid undefined behavior
```

`unsafe`ブロックを使うことで、私たちは Rust に対して、関数のドキュメントを読んでおり、それを適切に使う方法を理解しており、関数の契約を満たしていることを確認したことを主張しています。

不健全な関数の本体は、実質的に`unsafe`ブロックであるため、不健全な関数内で他の不健全な操作を行うには、別の`unsafe`ブロックを追加する必要はありません。
