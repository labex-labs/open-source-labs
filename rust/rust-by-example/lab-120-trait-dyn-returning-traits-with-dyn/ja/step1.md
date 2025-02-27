# `dyn` を使ったトレイトの返却

Rust コンパイラは、各関数の戻り値の型がどれだけのメモリを必要とするかを知る必要があります。これは、すべての関数が具体的な型を返さなければならないことを意味します。他の言語とは異なり、`Animal` のようなトレイトを持っている場合、`Animal` を返す関数を書くことはできません。なぜなら、その異なる実装では異なる量のメモリが必要になるからです。

しかし、簡単な回避策があります。トレイト オブジェクトを直接返す代わりに、関数は `Animal` を _含む_ `Box` を返します。`box` は、ヒープ内の一部のメモリへの参照にすぎません。参照は静的に既知のサイズを持っており、コンパイラはそれがヒープ割り当ての `Animal` を指すことを保証できるため、関数からトレイトを返すことができます！

Rust は、ヒープ上にメモリを割り当てるときにできる限り明示的になろうとしています。そのため、関数がこのようにヒープ上のトレイトへのポインタを返す場合、戻り値の型を `dyn` キーワードを使って書く必要があります。たとえば、`Box<dyn Animal>` です。

```rust
struct Sheep {}
struct Cow {}

trait Animal {
    // インスタンス メソッドのシグネチャ
    fn noise(&self) -> &'static str;
}

// `Sheep` に対して `Animal` トレイトを実装する。
impl Animal for Sheep {
    fn noise(&self) -> &'static str {
        "baaaaah!"
    }
}

// `Cow` に対して `Animal` トレイトを実装する。
impl Animal for Cow {
    fn noise(&self) -> &'static str {
        "moooooo!"
    }
}

// `Animal` を実装する何らかの構造体を返すが、コンパイル時にどれが返されるかはわからない。
fn random_animal(random_number: f64) -> Box<dyn Animal> {
    if random_number < 0.5 {
        Box::new(Sheep {})
    } else {
        Box::new(Cow {})
    }
}

fn main() {
    let random_number = 0.234;
    let animal = random_animal(random_number);
    println!("You've randomly chosen an animal, and it says {}", animal.noise());
}
```
