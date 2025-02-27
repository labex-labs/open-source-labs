# 反復子

`Iterator` トレイトは、配列などのコレクションに対する反復子を実装するために使用されます。

このトレイトでは、`next` 要素に対してただ1つのメソッドが定義される必要があり、これは `impl` ブロックで手動で定義することも、（配列や範囲の場合のように）自動的に定義することもできます。

一般的なケースにおける便利さとして、`for` 構文は `.into_iter()` メソッドを使っていくつかのコレクションを反復子に変換します。

```rust
struct Fibonacci {
    curr: u32,
    next: u32,
}

// `Fibonacci` に対して `Iterator` を実装します。
// `Iterator` トレイトでは、`next` 要素に対してただ1つのメソッドが定義される必要があります。
impl Iterator for Fibonacci {
    // この型を `Self::Item` を使って参照できます。
    type Item = u32;

    // ここでは、`.curr` と `.next` を使って数列を定義します。
    // 戻り値の型は `Option<T>` です。
    //     * `Iterator` が終了した場合、`None` が返されます。
    //     * それ以外の場合、次の値が `Some` にラップされて返されます。
    // 戻り値の型で `Self::Item` を使っているので、
    // 型を変更しても関数のシグネチャを更新する必要はありません。
    fn next(&mut self) -> Option<Self::Item> {
        let current = self.curr;

        self.curr = self.next;
        self.next = current + self.next;

        // フィボナッチ数列には終点がないので、`Iterator` は
        // 決して `None` を返さず、常に `Some` が返されます。
        Some(current)
    }
}

// フィボナッチ数列生成器を返します。
fn fibonacci() -> Fibonacci {
    Fibonacci { curr: 0, next: 1 }
}

fn main() {
    // `0..3` は、0、1、2 を生成する `Iterator` です。
    let mut sequence = 0..3;

    println!("0..3 に対する4つの連続した `next` 呼び出し");
    println!("> {:?}", sequence.next());
    println!("> {:?}", sequence.next());
    println!("> {:?}", sequence.next());
    println!("> {:?}", sequence.next());

    // `for` は、`Iterator` が `None` を返すまで反復します。
    // 各 `Some` 値はアンラップされ、変数（ここでは `i`）に束縛されます。
    println!("`for` を使って 0..3 を反復する");
    for i in 0..3 {
        println!("> {}", i);
    }

    // `take(n)` メソッドは、`Iterator` を最初の `n` 項までに絞ります。
    println!("フィボナッチ数列の最初の4項は: ");
    for i in fibonacci().take(4) {
        println!("> {}", i);
    }

    // `skip(n)` メソッドは、最初の `n` 項を捨てることで `Iterator` を短縮します。
    println!("フィボナッチ数列の次の4項は: ");
    for i in fibonacci().skip(4).take(4) {
        println!("> {}", i);
    }

    let array = [1u32, 3, 3, 7];

    // `iter` メソッドは、配列/スライスに対して `Iterator` を生成します。
    println!("次の配列 {:?} を反復する", &array);
    for i in array.iter() {
        println!("> {}", i);
    }
}
```
