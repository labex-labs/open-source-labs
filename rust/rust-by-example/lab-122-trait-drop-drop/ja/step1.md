# Drop

`Drop`トレイトには 1 つのメソッドしかありません。それは`drop`で、オブジェクトがスコープ外になると自動的に呼び出されます。`Drop`トレイトの主な用途は、実装クラスが所有するリソースを解放することです。

`Box`、`Vec`、`String`、`File`、および`Process`は、リソースを解放するために`Drop`トレイトを実装する型のいくつかの例です。`Drop`トレイトは、任意のカスタムデータ型に対しても手動で実装することができます。

次の例では、`drop`関数にコンソールへの出力を追加して、それが呼び出されたときに通知します。

```rust
struct Droppable {
    name: &'static str,
}

// `drop` のこの単純な実装は、コンソールへの出力を追加します。
impl Drop for Droppable {
    fn drop(&mut self) {
        println!("> Dropping {}", self.name);
    }
}

fn main() {
    let _a = Droppable { name: "a" };

    // ブロック A
    {
        let _b = Droppable { name: "b" };

        // ブロック B
        {
            let _c = Droppable { name: "c" };
            let _d = Droppable { name: "d" };

            println!("Exiting block B");
        }
        println!("Just exited block B");

        println!("Exiting block A");
    }
    println!("Just exited block A");

    // 変数は `drop` 関数を使用して手動で破棄できます
    drop(_a);
    // TODO ^ Try commenting this line

    println!("end of the main function");

    // `_a` はここでは再度 `drop` されません。既に（手動で）`drop` されているためです
}
```
