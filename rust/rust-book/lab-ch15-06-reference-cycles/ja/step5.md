# 子ノードから親ノードへの参照の追加

子ノードがその親を認識できるようにするには、`Node`構造体の定義に`parent`フィールドを追加する必要があります。問題は、`parent`の型を決定することです。`Rc<T>`を含めることはできないことがわかっています。なぜなら、それは`leaf.parent`が`branch`を指し、`branch.children`が`leaf`を指す参照サイクルを作成し、それらの`strong_count`値が 0 にならなくなるからです。

別の方法で関係を考えると、親ノードはその子ノードを所有するはずです。つまり、親ノードが破棄された場合、その子ノードも破棄されるべきです。一方、子ノードは親ノードを所有してはいけません。つまり、子ノードが破棄された場合でも、親ノードは依然として存在する必要があります。これは弱参照のケースです！

したがって、`Rc<T>`の代わりに、`parent`の型を`Weak<T>`、具体的には`RefCell<Weak<Node>>`を使用することにします。これで、`Node`構造体の定義は次のようになります。

ファイル名：`src/main.rs`

```rust
use std::cell::RefCell;
use std::rc::{Rc, Weak};

#[derive(Debug)]
struct Node {
    value: i32,
    parent: RefCell<Weak<Node>>,
    children: RefCell<Vec<Rc<Node>>>,
}
```

ノードは親ノードを参照できるようになりますが、親ノードを所有するわけではありません。リスト 15-28 では、`main`を更新してこの新しい定義を使用し、`leaf`ノードが親ノードである`branch`を参照する方法を持つようにします。

ファイル名：`src/main.rs`

```rust
fn main() {
    let leaf = Rc::new(Node {
        value: 3,
      1 parent: RefCell::new(Weak::new()),
        children: RefCell::new(vec![]),
    });

  2 println!(
        "leaf parent = {:?}",
        leaf.parent.borrow().upgrade()
    );

    let branch = Rc::new(Node {
        value: 5,
      3 parent: RefCell::new(Weak::new()),
        children: RefCell::new(vec![Rc::clone(&leaf)]),
    });

  4 *leaf.parent.borrow_mut() = Rc::downgrade(&branch);

  5 println!(
        "leaf parent = {:?}",
        leaf.parent.borrow().upgrade()
    );
}
```

リスト 15-28: 親ノードである`branch`への弱参照を持つ`leaf`ノード

`leaf`ノードを作成する方法は、`parent`フィールドを除けばリスト 15-27 と同じようになります。`leaf`は最初は親がいないため、新しい空の`Weak<Node>`参照インスタンスを作成します\[1\]。

この時点で、`upgrade`メソッドを使用して`leaf`の親への参照を取得しようとすると、`None`値が得られます。最初の`println!`文の出力でこれがわかります\[2\]。

```rust
leaf parent = None
```

`branch`ノードを作成すると、`branch`には親ノードがないため、`parent`フィールドにも新しい`Weak<Node>`参照があります\[3\]。`branch`の子ノードの 1 つとして`leaf`がある状態です。`branch`内の`Node`インスタンスがあると、`leaf`を変更して親への`Weak<Node>`参照を与えることができます\[4\]。`leaf`の`parent`フィールド内の`RefCell<Weak<Node>>`の`borrow_mut`メソッドを使用し、その後`Rc::downgrade`関数を使用して、`branch`内の`Rc<Node>`から`branch`への`Weak<Node>`参照を作成します。

`leaf`の親を再度表示すると\[5\]、今回は`Some`バリアントが`branch`を保持しているのがわかります。つまり、`leaf`は今や親にアクセスできるようになりました！`leaf`を表示するときも、リスト 15-26 のように最終的にスタックオーバーフローにつながるサイクルを回避できます。`Weak<Node>`参照は`(Weak)`として表示されます。

    leaf parent = Some(Node { value: 5, parent: RefCell { value: (Weak) },
    children: RefCell { value: [Node { value: 3, parent: RefCell { value: (Weak) },
    children: RefCell { value: [] } }] } })

無限出力がないことは、このコードが参照サイクルを作成していないことを示しています。また、`Rc::strong_count`と`Rc::weak_count`を呼び出して得られる値を見ることでもわかります。
