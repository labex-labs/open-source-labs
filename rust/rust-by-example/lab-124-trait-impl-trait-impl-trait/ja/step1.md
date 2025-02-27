# `impl Trait`

`impl Trait`は2つの場所で使用できます。

1. 引数型として
2. 戻り値型として

## 引数型として

関数がトレイトに対してジェネリックである場合でも、特定の型にこだわらない場合は、引数の型として`impl Trait`を使用して関数宣言を簡略化できます。

たとえば、次のコードを考えてみましょう。

```rust
fn parse_csv_document<R: std::io::BufRead>(src: R) -> std::io::Result<Vec<Vec<String>>> {
    src.lines()
     .map(|line| {
            // ソースの各行に対して
            line.map(|line| {
                // 行が正常に読み取られた場合、処理します。読み取れなかった場合はエラーを返します
                line.split(',') // コンマで区切られた行を分割します
                 .map(|entry| String::from(entry.trim())) // 前後の空白を削除します
                 .collect() // 1行のすべての文字列をVec<String>に収集します
            })
        })
     .collect() // すべての行をVec<Vec<String>>に収集します
}
```

`parse_csv_document`はジェネリックで、BufReadを実装する任意の型、たとえば`BufReader<File>`や`[u8]`を受け取ることができますが、`R`がどの型であるかは重要ではなく、`R`は`src`の型を宣言するためだけに使用されるため、関数は次のように書くこともできます。

```rust
fn parse_csv_document(src: impl std::io::BufRead) -> std::io::Result<Vec<Vec<String>>> {
    src.lines()
     .map(|line| {
            // ソースの各行に対して
            line.map(|line| {
                // 行が正常に読み取られた場合、処理します。読み取れなかった場合はエラーを返します
                line.split(',') // コンマで区切られた行を分割します
                 .map(|entry| String::from(entry.trim())) // 前後の空白を削除します
                 .collect() // 1行のすべての文字列をVec<String>に収集します
            })
        })
     .collect() // すべての行をVec<Vec<String>>に収集します
}
```

引数型として`impl Trait`を使用すると、使用する関数の形式を明示的に指定できないことに注意してください。つまり、`parse_csv_document::<std::io::Empty>(std::io::empty())`は2番目の例では機能しません。

## 戻り値型として

関数が`MyTrait`を実装する型を返す場合、その戻り値型を`-> impl MyTrait`と書くことができます。これにより、型シグネチャを大幅に簡略化できます！

```rust
use std::iter;
use std::vec::IntoIter;

// この関数は2つの`Vec<i32>`を結合し、それを返すイテレータを返します。
// その戻り値型がどれほど複雑であるか見てみましょう！
fn combine_vecs_explicit_return_type(
    v: Vec<i32>,
    u: Vec<i32>,
) -> iter::Cycle<iter::Chain<IntoIter<i32>, IntoIter<i32>>> {
    v.into_iter().chain(u.into_iter()).cycle()
}

// これはまったく同じ関数ですが、戻り値型に`impl Trait`を使用しています。
// どれほど簡単であるか見てみましょう！
fn combine_vecs(
    v: Vec<i32>,
    u: Vec<i32>,
) -> impl Iterator<Item=i32> {
    v.into_iter().chain(u.into_iter()).cycle()
}

fn main() {
    let v1 = vec![1, 2, 3];
    let v2 = vec![4, 5];
    let mut v3 = combine_vecs(v1, v2);
    assert_eq!(Some(1), v3.next());
    assert_eq!(Some(2), v3.next());
    assert_eq!(Some(3), v3.next());
    assert_eq!(Some(4), v3.next());
    assert_eq!(Some(5), v3.next());
    println!("all done");
}
```

より重要なことは、一部のRust型は書き出すことができません。たとえば、すべてのクロージャには独自の名前のない具体的な型があります。`impl Trait`構文が登場する前は、クロージャを返すためにヒープ上に割り当てる必要がありました。しかし今では、次のようにすべてを静的に行うことができます。

```rust
// 入力に`y`を加える関数を返します
fn make_adder_function(y: i32) -> impl Fn(i32) -> i32 {
    let closure = move |x: i32| { x + y };
    closure
}

fn main() {
    let plus_one = make_adder_function(1);
    assert_eq!(plus_one(2), 3);
}
```

また、`map`や`filter`クロージャを使用するイテレータを返すためにも`impl Trait`を使用できます！これにより、`map`と`filter`の使用が簡単になります。クロージャ型には名前がないため、関数がクロージャを持つイテレータを返す場合、明示的な戻り値型を書き出すことができません。しかし、`impl Trait`を使用することで簡単に行うことができます。

```rust
fn double_positives<'a>(numbers: &'a Vec<i32>) -> impl Iterator<Item = i32> + 'a {
    numbers
     .iter()
     .filter(|x| x > &&0)
     .map(|x| x * 2)
}

fn main() {
    let singles = vec![-3, -2, 2, 3];
    let doubles = double_positives(&singles);
    assert_eq!(doubles.collect::<Vec<i32>>(), vec![4, 6]);
}
```
