# HashSet

可以将 `HashSet` 看作是一个 `HashMap`，只不过我们只关心键（实际上，`HashSet<T>` 只是 `HashMap<T, ()>` 的一个包装器）。

“这有什么意义呢？”你可能会问，“我直接把键存储在 `Vec` 里不就行了。”

`HashSet` 的独特之处在于它能保证不会有重复的元素。这是任何集合类型都应满足的特性，`HashSet` 只是其中一种实现方式（另见：`BTreeSet`）。

如果你插入一个已经存在于 `HashSet` 中的值（即新值与现有值相等且它们具有相同的哈希值），那么新值会替换旧值。

当你不希望某个东西出现多个实例，或者想知道某个东西是否已经存在时，这就非常有用了。

但集合的功能不止于此。

集合有四种主要操作（以下所有调用都会返回一个迭代器）：

- `union`：获取两个集合中的所有唯一元素。

- `difference`：获取第一个集合中存在但第二个集合中不存在的所有元素。

- `intersection`：获取仅同时存在于两个集合中的所有元素。

- `symmetric_difference`：获取存在于其中一个集合但不同时存在于两个集合中的所有元素。

在下面的示例中尝试所有这些操作：

```rust
use std::collections::HashSet;

fn main() {
    let mut a: HashSet<i32> = vec![1i32, 2, 3].into_iter().collect();
    let mut b: HashSet<i32> = vec![2i32, 3, 4].into_iter().collect();

    assert!(a.insert(4));
    assert!(a.contains(&4));

    // 如果已经存在某个值，`HashSet::insert()` 会返回 false。
    assert!(b.insert(4), "值 4 已经在集合 B 中！");
    // FIXME ^ 注释掉这一行

    b.insert(5);

    // 如果集合的元素类型实现了 `Debug`，
    // 那么该集合也实现了 `Debug`。
    // 它通常会以 `[elem1, elem2,...]` 的格式打印其元素。
    println!("A: {:?}", a);
    println!("B: {:?}", b);

    // 以任意顺序打印 [1, 2, 3, 4, 5]
    println!("并集: {:?}", a.union(&b).collect::<Vec<&i32>>());

    // 这应该打印 [1]
    println!("差集: {:?}", a.difference(&b).collect::<Vec<&i32>>());

    // 以任意顺序打印 [2, 3, 4]
    println!("交集: {:?}", a.intersection(&b).collect::<Vec<&i32>>());

    // 打印 [1, 5]
    println!("对称差集: {:?}",
             a.symmetric_difference(&b).collect::<Vec<&i32>>());
}
```

（示例改编自文档。）
