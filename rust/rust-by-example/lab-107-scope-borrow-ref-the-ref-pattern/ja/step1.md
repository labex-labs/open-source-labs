# ref パターン

`let` バインドを通じたパターンマッチングや構造化による分解を行う際、`ref` キーワードを使用して構造体/タプルのフィールドへの参照を取得できます。以下の例は、これが役立ついくつかのケースを示しています。

```rust
#[derive(Clone, Copy)]
struct Point { x: i32, y: i32 }

fn main() {
    let c = 'Q';

    // 代入の左辺での `ref` バローは、右辺での `&` バローと同等です。
    let ref ref_c1 = c;
    let ref_c2 = &c;

    println!("ref_c1 equals ref_c2: {}", *ref_c1 == *ref_c2);

    let point = Point { x: 0, y: 0 };

    // 構造体を分解する際にも `ref` は有効です。
    let _copy_of_x = {
        // `ref_to_x` は `point` の `x` フィールドへの参照です。
        let Point { x: ref ref_to_x, y: _ } = point;

        // `point` の `x` フィールドのコピーを返します。
        *ref_to_x
    };

    // `point` の可変コピー
    let mut mutable_point = point;

    {
        // `ref` は `mut` と組み合わせて可変参照を取得するために使用できます。
        let Point { x: _, y: ref mut mut_ref_to_y } = mutable_point;

        // 可変参照を介して `mutable_point` の `y` フィールドを変更します。
        *mut_ref_to_y = 1;
    }

    println!("point is ({}, {})", point.x, point.y);
    println!("mutable_point is ({}, {})", mutable_point.x, mutable_point.y);

    // ポインタを含む可変タプル
    let mut mutable_tuple = (Box::new(5u32), 3u32);

    {
        // `mutable_tuple` を分解して `last` の値を変更します。
        let (_, ref mut last) = mutable_tuple;
        *last = 2u32;
    }

    println!("tuple is {:?}", mutable_tuple);
}
```
