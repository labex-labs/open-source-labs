# HashSet

`HashSet` を、キーだけを気にする `HashMap` と考えてみてください（実際には、`HashSet<T>` は `HashMap<T, ()>` のラッパーにすぎません）。

「それで何がいいんですか？」とあなたは尋ねます。「`Vec` にキーを保存すればいいのに」。

`HashSet` の特徴は、重複する要素がないことが保証されていることです。これは、任意の集合コレクションが果たす契約です。`HashSet` はその 1 つの実装にすぎません。(参照：`BTreeSet`)

`HashSet` に既に存在する値を挿入すると（つまり、新しい値が既存の値と等しく、両方が同じハッシュを持つ場合）、新しい値が古い値を置き換えます。

これは、何かを 1 つ以上持ちたくない場合、または既に何かを持っているかどうかを知りたい場合に便利です。

しかし、集合はそれだけではありません。

集合には 4 つの主な操作があります（以下のすべての呼び出しはイテレータを返します）：

- `union`：両方の集合に含まれるすべての一意の要素を取得します。

- `difference`：最初の集合には含まれていますが、2 番目の集合には含まれていないすべての要素を取得します。

- `intersection`：両方の集合にのみ含まれるすべての要素を取得します。

- `symmetric_difference`：一方の集合または他方の集合に含まれているが、両方には含まれていないすべての要素を取得します。

以下の例でこれらすべてを試してみてください：

```rust
use std::collections::HashSet;

fn main() {
    let mut a: HashSet<i32> = vec![1i32, 2, 3].into_iter().collect();
    let mut b: HashSet<i32> = vec![2i32, 3, 4].into_iter().collect();

    assert!(a.insert(4));
    assert!(a.contains(&4));

    // `HashSet::insert()` は、
    // 既に値が存在していた場合に false を返します。
    assert!(b.insert(4), "Value 4 is already in set B!");
    // FIXME ^ この行をコメントアウトしてください

    b.insert(5);

    // コレクションの要素型が `Debug` を実装している場合、
    // コレクションは `Debug` を実装します。
    // 通常、要素を `[elem1, elem2,...]` の形式で表示します
    println!("A: {:?}", a);
    println!("B: {:?}", b);

    // 任意の順序で [1, 2, 3, 4, 5] を表示
    println!("Union: {:?}", a.union(&b).collect::<Vec<&i32>>());

    // これは [1] を表示するはずです
    println!("Difference: {:?}", a.difference(&b).collect::<Vec<&i32>>());

    // 任意の順序で [2, 3, 4] を表示
    println!("Intersection: {:?}", a.intersection(&b).collect::<Vec<&i32>>());

    // [1, 5] を表示
    println!("Symmetric Difference: {:?}",
             a.symmetric_difference(&b).collect::<Vec<&i32>>());
}
```

(例はドキュメントから引用しています。)
