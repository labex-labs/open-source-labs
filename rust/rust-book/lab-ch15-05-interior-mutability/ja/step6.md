# Rc`<T>` と RefCell`<T>` を使って可変データの複数の所有者を許可する

`RefCell<T>` を使用する一般的な方法は、`Rc<T>` と組み合わせることです。`Rc<T>` は、あるデータの複数の所有者を持つことができますが、そのデータには不変なアクセスのみを提供します。`RefCell<T>` を保持する `Rc<T>` がある場合、複数の所有者を持ち、かつ変更することができる値を取得することができます！

たとえば、リスト 15-18 のコンセケンスリストの例を思い出してください。そこでは、`Rc<T>` を使って複数のリストが別のリストの所有権を共有できるようにしました。`Rc<T>` は不変値のみを保持するため、作成した後はリスト内の値を変更することができません。リスト内の値を変更する能力のために `RefCell<T>` を追加してみましょう。リスト 15-24 は、`Cons` の定義で `RefCell<T>` を使用することで、すべてのリストに格納されている値を変更できることを示しています。

ファイル名：`src/main.rs`

```rust
#[derive(Debug)]
enum List {
    Cons(Rc<RefCell<i32>>, Rc<List>),
    Nil,
}

use crate::List::{Cons, Nil};
use std::cell::RefCell;
use std::rc::Rc;

fn main() {
  1 let value = Rc::new(RefCell::new(5));

  2 let a = Rc::new(Cons(Rc::clone(&value), Rc::new(Nil)));

    let b = Cons(Rc::new(RefCell::new(3)), Rc::clone(&a));
    let c = Cons(Rc::new(RefCell::new(4)), Rc::clone(&a));

  3 *value.borrow_mut() += 10;

    println!("a after = {:?}", a);
    println!("b after = {:?}", b);
    println!("c after = {:?}", c);
}
```

リスト 15-24：変更可能な `List` を作成するために `Rc<RefCell<i32>>` を使用する

`Rc<RefCell<i32>>` のインスタンスである値を作成し、`value` という名前の変数に保存します \[1\]。これにより、後で直接アクセスできるようになります。その後、`value` を保持する `Cons` バリアントを持つ `List` を `a` で作成します \[2\]。`value` をクローンする必要があります。これにより、`a` と `value` の両方が内部の `5` の値の所有権を持ち、`value` から `a` に所有権を移すことも、`a` が `value` から借用することもありません。

リスト `a` を `Rc<T>` でラップします。そうすると、リスト `b` と `c` を作成する際、両方とも `a` を参照できるようになります。これは、リスト 15-18 で行ったことと同じです。

`a`、`b`、`c` のリストを作成した後、`value` の値に 10 を加えたいと思います \[3\]。これは、`value` の `borrow_mut` を呼び出すことで行います。これは、「`->` 演算子はどこにあるの？」で説明した自動の参照解除機能を使って、`Rc<T>` を内部の `RefCell<T>` 値に参照解除します。`borrow_mut` メソッドは `RefMut<T>` スマートポインタを返し、それに参照解除演算子を使用して内部の値を変更します。

`a`、`b`、`c` を出力すると、それぞれが `5` ではなく `15` の変更後の値を持っていることがわかります。

    a after = Cons(RefCell { value: 15 }, Nil)
    b after = Cons(RefCell { value: 3 }, Cons(RefCell { value: 15 }, Nil))
    c after = Cons(RefCell { value: 4 }, Cons(RefCell { value: 15 }, Nil))

このテクニックはとても便利です！`RefCell<T>` を使用することで、外見上は不変の `List` 値を持つことができます。ただし、`RefCell<T>` の内部可変性にアクセスするメソッドを使用することができるため、必要に応じてデータを変更することができます。借用規則の実行時チェックにより、データ競合から保護されます。時には、このデータ構造の柔軟性のために少しの速度を犠牲にする価値があります。`RefCell<T>` はマルチスレッドコードでは機能しません！`Mutex<T>` は `RefCell<T>` のスレッドセーフなバージョンであり、第 16 章で `Mutex<T>` について説明します。
