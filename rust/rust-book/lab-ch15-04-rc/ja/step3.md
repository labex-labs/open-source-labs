# Rc`<T>`をクローンすると参照カウントが増える

15-18 の動作例を変更して、`a`の`Rc<List>`への参照を作成および破棄する際に参照カウントがどのように変化するかを見てみましょう。

15-19 では、`main`を変更して、リスト`c`の周りに内部スコープを持たせます。そうすることで、`c`がスコープ外になったときの参照カウントの変化を見ることができます。

ファイル名：`src/main.rs`

```rust
--snip--

fn main() {
    let a = Rc::new(Cons(5, Rc::new(Cons(10, Rc::new(Nil)))));
    println!(
        "count after creating a = {}",
        Rc::strong_count(&a)
    );
    let b = Cons(3, Rc::clone(&a));
    println!(
        "count after creating b = {}",
        Rc::strong_count(&a)
    );
    {
        let c = Cons(4, Rc::clone(&a));
        println!(
            "count after creating c = {}",
            Rc::strong_count(&a)
        );
    }
    println!(
        "count after c goes out of scope = {}",
        Rc::strong_count(&a)
    );
}
```

リスト 15-19：参照カウントを表示する

プログラムの各時点で参照カウントが変化するときに、`Rc::strong_count`関数を呼び出すことで参照カウントを表示します。この関数は`count`ではなく`strong_count`と名付けられています。なぜなら、`Rc<T>`型には`weak_count`もあるからです。「Weak`<T>`を使った参照サイクルの防止」で`weak_count`が何のために使われるかを見ていきます。

このコードは次のように表示されます。

    count after creating a = 1
    count after creating b = 2
    count after creating c = 3
    count after c goes out of scope = 2

`a`の`Rc<List>`は初期参照カウントが 1 であることがわかります。その後、`clone`を呼び出すたびに、カウントが 1 増えます。`c`がスコープ外になると、カウントが 1 減少します。参照カウントを増やすために`Rc::clone`を呼ぶ必要があるのと同じように、参照カウントを減らすために関数を呼ぶ必要はありません。`Drop`トレイトの実装は、`Rc<T>`値がスコープ外になるときに自動的に参照カウントを減らします。

この例では見えないことですが、`main`の最後で`b`、そして`a`がスコープ外になると、カウントが 0 になり、`Rc<List>`が完全にクリーンアップされます。`Rc<T>`を使用することで、単一の値に複数の所有者を持たせることができ、カウントにより、所有者のいずれかがまだ存在する限り、値が有効なままであることが保証されます。

不変参照を介して、`Rc<T>`は読み取り専用でプログラムの複数の部分間でデータを共有することを可能にします。`Rc<T>`が複数の可変参照も持てるようになっていた場合、第 4 章で説明した借用規則の 1 つに違反する可能性があります。同じ場所に対する複数の可変借用は、データ競合や不整合を引き起こす可能性があるからです。しかし、データを変更できることは非常に便利です！次のセクションでは、内部可変性パターンと、この不変性制約とともに使用できる`RefCell<T>`型について説明します。
