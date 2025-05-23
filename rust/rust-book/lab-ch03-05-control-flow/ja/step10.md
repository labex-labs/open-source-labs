# for を使ったコレクションの反復処理

配列などのコレクションの要素を反復処理する際には、`while`構文を使うことができます。たとえば、リスト 3-4 のループは配列`a`の各要素を出力します。

ファイル名：`src/main.rs`

```rust
fn main() {
    let a = [10, 20, 30, 40, 50];
    let mut index = 0;

    while index < 5 {
        println!("the value is: {}", a[index]);

        index += 1;
    }
}
```

リスト 3-4：`while`ループを使ったコレクションの各要素の反復処理

ここでは、コードは配列の要素をインクリメントしながら反復処理します。インデックスは`0`から始まり、配列の最後のインデックスに達するまで（つまり、`index < 5`がもはや`true`でなくなるまで）ループします。このコードを実行すると、配列のすべての要素が表示されます：

```bash
$ cargo run
   Compiling loops v0.1.0 (file:///projects/loops)
    Finished dev [unoptimized + debuginfo] target(s) in 0.32s
     Running `target/debug/loops`
the value is: 10
the value is: 20
the value is: 30
the value is: 40
the value is: 50
```

予想通り、5 つの配列値がターミナルに表示されます。`index`がいつか`5`の値に達しても、ループは配列から 6 番目の値を取得しようとする前に実行を停止します。

ただし、この方法はエラーが発生しやすく、インデックス値やテスト条件が間違っている場合、プログラムがパニックになる可能性があります。たとえば、`a`配列の定義を 4 つの要素に変更したが、条件を`while index < 4`に更新するのを忘れた場合、コードはパニックになります。また、これは遅くもあります。なぜなら、コンパイラは、ループの各反復でインデックスが配列の範囲内かどうかの条件付きチェックを実行するための実行時コードを追加するからです。

より簡潔な代替策として、`for`ループを使って、コレクションの各項目に対してコードを実行することができます。`for`ループはリスト 3-5 のコードのようになります。

ファイル名：`src/main.rs`

```rust
fn main() {
    let a = [10, 20, 30, 40, 50];

    for element in a {
        println!("the value is: {element}");
    }
}
```

リスト 3-5：`for`ループを使ったコレクションの各要素の反復処理

このコードを実行すると、リスト 3-4 と同じ出力が表示されます。より重要なことは、コードの安全性が向上し、配列の末尾を超えたり、十分に進まなかって項目を見落としたりすることから生じるバグの可能性が排除されたことです。

`for`ループを使えば、配列の値の数を変更した場合にも、リスト 3-4 で使用した方法のように、他のコードを変更する必要がありません。

`for`ループの安全性と簡潔さのため、これは Rust で最も一般的に使用されるループ構文になっています。たとえば、リスト 3-3 で`while`ループを使ったカウントダウンの例のように、特定の回数だけコードを実行したい場合でも、ほとんどの Rust プログラマーは`for`ループを使います。その方法は、標準ライブラリによって提供される`Range`を使うことで、ある数から始まり、別の数の前まで順番にすべての数を生成することです。

以下は、`for`ループとまだ説明していない別のメソッドである`rev`を使って、範囲を逆順にすることでカウントダウンを行った場合のコードです：

ファイル名：`src/main.rs`

```rust
fn main() {
    for number in (1..4).rev() {
        println!("{number}!");
    }
    println!("LIFTOFF!!!");
}
```

このコードはもっと綺麗ですよね？
