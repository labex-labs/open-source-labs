# strong_count と weak_count の変化を視覚化する

新しい内部スコープを作成し、`branch`の作成をそのスコープに移動することで、`Rc<Node>`インスタンスの`strong_count`と`weak_count`値がどのように変化するか見てみましょう。これにより、`branch`が作成され、その後スコープ外になるときに破棄されるときに何が起こるかを確認できます。変更内容はリスト15-29に示されています。

ファイル名: `src/main.rs`

```rust
fn main() {
    let leaf = Rc::new(Node {
        value: 3,
        parent: RefCell::new(Weak::new()),
        children: RefCell::new(vec![]),
    });

  1 println!(
        "leaf strong = {}, weak = {}",
        Rc::strong_count(&leaf),
        Rc::weak_count(&leaf),
    );

  2 {
        let branch = Rc::new(Node {
            value: 5,
            parent: RefCell::new(Weak::new()),
            children: RefCell::new(vec![Rc::clone(&leaf)]),
        });

        *leaf.parent.borrow_mut() = Rc::downgrade(&branch);

      3 println!(
            "branch strong = {}, weak = {}",
            Rc::strong_count(&branch),
            Rc::weak_count(&branch),
        );

      4 println!(
            "leaf strong = {}, weak = {}",
            Rc::strong_count(&leaf),
            Rc::weak_count(&leaf),
        );
  5 }

  6 println!(
        "leaf parent = {:?}",
        leaf.parent.borrow().upgrade()
    );
  7 println!(
        "leaf strong = {}, weak = {}",
        Rc::strong_count(&leaf),
        Rc::weak_count(&leaf),
    );
}
```

リスト15-29: 内部スコープで`branch`を作成し、強参照と弱参照のカウントを調べる

`leaf`が作成された後、その`Rc<Node>`の強参照カウントは1で、弱参照カウントは0です\[1\]。内部スコープ内で\[2\]、`branch`を作成して`leaf`と関連付けます。この時点でカウントを表示すると\[3\]、`branch`内の`Rc<Node>`の強参照カウントは1で、弱参照カウントは1になります（`leaf.parent`が`Weak<Node>`で`branch`を指しているため）。`leaf`のカウントを表示すると\[4\]、`branch`が`leaf`の`Rc<Node>`のクローンを`branch.children`に格納しているため、強参照カウントは2になりますが、弱参照カウントは依然として0です。

内部スコープが終了すると\[5\]、`branch`がスコープ外になり、`Rc<Node>`の強参照カウントが0に減少するため、その`Node`が破棄されます。`leaf.parent`の弱参照カウントが1であることは、`Node`が破棄されるかどうかには影響しません。したがって、メモリリークは起こりません！

スコープ終了後に`leaf`の親にアクセスしようとすると、再び`None`が得られます\[6\]。プログラムの終了時に\[7\]、`leaf`内の`Rc<Node>`の強参照カウントは1で、弱参照カウントは0です。なぜなら、変数`leaf`が再び`Rc<Node>`への唯一の参照になっているからです。

カウントと値の破棄を管理するすべてのロジックは、`Rc<T>`と`Weak<T>`およびそれらの`Drop`トレイトの実装に組み込まれています。`Node`の定義で子ノードから親ノードへの関係が`Weak<T>`参照であることを指定することで、親ノードが子ノードを指し、逆も同じである場合でも、参照サイクルとメモリリークを作成することなく済みます。
