# `for` ループ

## `for` と範囲

`for in` 構文を使って `Iterator` を反復処理できます。反復子を作成する最も簡単な方法の 1 つは、範囲表記 `a..b` を使うことです。これは、1 つずつのステップで `a`（含む）から `b`（含まない）までの値を生成します。

`while` の代わりに `for` を使って FizzBuzz を書いてみましょう。

```rust
fn main() {
    // `n` は各反復で 1、2、...、100 の値をとります
    for n in 1..101 {
        if n % 15 == 0 {
            println!("fizzbuzz");
        } else if n % 3 == 0 {
            println!("fizz");
        } else if n % 5 == 0 {
            println!("buzz");
        } else {
            println!("{}", n);
        }
    }
}
```

あるいは、両端を含む範囲には `a..=b` を使うことができます。上記のコードは次のように書けます。

```rust
fn main() {
    // `n` は各反復で 1、2、...、100 の値をとります
    for n in 1..=100 {
        if n % 15 == 0 {
            println!("fizzbuzz");
        } else if n % 3 == 0 {
            println!("fizz");
        } else if n % 5 == 0 {
            println!("buzz");
        } else {
            println!("{}", n);
        }
    }
}
```

## `for` と反復子

`for in` 構文は、いくつかの方法で `Iterator` と相互作用することができます。反復子トレイトのセクションで説明したように、デフォルトでは `for` ループは `into_iter` 関数をコレクションに適用します。ただし、これがコレクションを反復子に変換する唯一の方法ではありません。

`into_iter`、`iter`、`iter_mut` はすべて、コレクション内のデータに対する異なるビューを提供することで、コレクションを反復子に変換する方法を異なる形で扱います。

- `iter` - これは各反復でコレクションの各要素を借用します。したがって、コレクションはそのままで、ループの後も再利用可能です。

```rust
fn main() {
    let names = vec!["Bob", "Frank", "Ferris"];

    for name in names.iter() {
        match name {
            &"Ferris" => println!("There is a rustacean among us!"),
            // TODO ^ & を削除して、ただ "Ferris" と照合するようにしてみてください
            _ => println!("Hello {}", name),
        }
    }

    println!("names: {:?}", names);
}
```

- `into_iter` - これはコレクションを消費するため、各反復で正確なデータが提供されます。コレクションが消費されると、それは 'ループ内で移動' されたため、再利用できなくなります。

```rust
fn main() {
    let names = vec!["Bob", "Frank", "Ferris"];

    for name in names.into_iter() {
        match name {
            "Ferris" => println!("There is a rustacean among us!"),
            _ => println!("Hello {}", name),
        }
    }

    println!("names: {:?}", names);
    // FIXME ^ この行をコメントアウトしてください
}
```

- `iter_mut` - これはコレクションの各要素を可変的に借用し、コレクションをその場で変更できるようにします。

```rust
fn main() {
    let mut names = vec!["Bob", "Frank", "Ferris"];

    for name in names.iter_mut() {
        *name = match name {
            &mut "Ferris" => "There is a rustacean among us!",
            _ => "Hello",
        }
    }

    println!("names: {:?}", names);
}
```

上記のコードスニペットでは、`match` ブランチの型に注目してください。これが反復の型の主な違いです。型の違いは、もちろん実行できる異なるアクションを意味します。
