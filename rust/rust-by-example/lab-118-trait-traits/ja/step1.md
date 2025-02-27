# トレイト

`トレイト` は、未知の型 `Self` に対して定義されたメソッドのコレクションです。同じトレイト内で宣言された他のメソッドにアクセスできます。

トレイトは任意のデータ型に対して実装できます。以下の例では、メソッドのグループである `Animal` を定義します。その後、`Animal` トレイトを `Sheep` データ型に対して実装し、`Sheep` で `Animal` のメソッドを使用できるようにします。

```rust
struct Sheep { naked: bool, name: &'static str }

trait Animal {
    // 関連付けられた関数のシグネチャ; `Self` は実装型を指します。
    fn new(name: &'static str) -> Self;

    // メソッドのシグネチャ; これらは文字列型を返します。
    fn name(&self) -> &'static str;
    fn noise(&self) -> &'static str;

    // トレイトはデフォルトのメソッド定義を提供できます。
    fn talk(&self) {
        println!("{} says {}", self.name(), self.noise());
    }
}

impl Sheep {
    fn is_naked(&self) -> bool {
        self.naked
    }

    fn shear(&mut self) {
        if self.is_naked() {
            // 実装型のメソッドは、実装型のトレイトメソッドを使用できます。
            println!("{} is already naked...", self.name());
        } else {
            println!("{} gets a haircut!", self.name);

            self.naked = true;
        }
    }
}

// `Sheep` に対して `Animal` トレイトを実装します。
impl Animal for Sheep {
    // `Self` は実装型: `Sheep` です。
    fn new(name: &'static str) -> Sheep {
        Sheep { name: name, naked: false }
    }

    fn name(&self) -> &'static str {
        self.name
    }

    fn noise(&self) -> &'static str {
        if self.is_naked() {
            "baaaaah?"
        } else {
            "baaaaah!"
        }
    }

    // デフォルトのトレイトメソッドはオーバーライドできます。
    fn talk(&self) {
        // たとえば、少し沈黙を加えることができます。
        println!("{} pauses briefly... {}", self.name, self.noise());
    }
}

fn main() {
    // この場合、型注釈が必要です。
    let mut dolly: Sheep = Animal::new("Dolly");
    // TODO ^ Try removing the type annotations.

    dolly.talk();
    dolly.shear();
    dolly.talk();
}
```
