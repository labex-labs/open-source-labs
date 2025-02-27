# 木構造データ構造の作成: 子ノードを持つノード

まずは、子ノードを知っているノードを持つ木を構築します。`Node`という名前の構造体を作成します。これは、自身の`i32`値と、子ノードの`Node`値への参照を保持します。

ファイル名: `src/main.rs`

```rust
use std::cell::RefCell;
use std::rc::Rc;

#[derive(Debug)]
struct Node {
    value: i32,
    children: RefCell<Vec<Rc<Node>>>,
}
```

`Node`がその子ノードを所有するようにし、その所有権を変数と共有して、木内の各`Node`に直接アクセスできるようにしたいと思います。これを行うために、`Vec<T>`の要素を`Rc<Node>`型の値として定義します。また、どのノードが他のノードの子ノードであるかを変更できるようにするため、`children`には`Vec<Rc<Node>>`の周りに`RefCell<T>`を持っています。

次に、構造体の定義を使用して、値が`3`で子ノードがない`leaf`という名前の1つの`Node`インスタンスと、値が`5`で子ノードの1つが`leaf`である`branch`という名前の別のインスタンスを作成します。これは、リスト15-27に示されています。

ファイル名: `src/main.rs`

```rust
fn main() {
    let leaf = Rc::new(Node {
        value: 3,
        children: RefCell::new(vec![]),
    });

    let branch = Rc::new(Node {
        value: 5,
        children: RefCell::new(vec![Rc::clone(&leaf)]),
    });
}
```

リスト15-27: 子ノードがない`leaf`ノードと、子ノードの1つが`leaf`である`branch`ノードの作成

`leaf`内の`Rc<Node>`をクローンして`branch`に格納します。これは、`leaf`内の`Node`が現在2つの所有者を持つことを意味します。つまり、`leaf`と`branch`です。`branch`から`leaf`にアクセスすることは、`branch.children`を通じてできますが、`leaf`から`branch`にアクセスする方法はありません。その理由は、`leaf`が`branch`への参照を持っておらず、それらが関連していることを知らないからです。`leaf`が`branch`がその親であることを知るようにしたいと思います。次にそれを行います。
