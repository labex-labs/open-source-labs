# 配列/スライス

タプルと同様に、配列とスライスもこのように分解することができます。

```rust
fn main() {
    // 配列の値を変更したり、スライスに変えたりしてみてください！
    let array = [1, -2, 6];

    match array {
        // 2番目と3番目の要素をそれぞれの変数にバインドします
        [0, second, third] =>
            println!("array[0] = 0, array[1] = {}, array[2] = {}", second, third),

        // 単一の値は_で無視できます
        [1, _, third] => println!(
            "array[0] = 1, array[2] = {} and array[1] was ignored",
            third
        ),

        // 一部をバインドして残りを無視することもできます
        [-1, second,..] => println!(
            "array[0] = -1, array[1] = {} and all the other ones were ignored",
            second
        ),
        // 以下のコードはコンパイルされません
        // [-1, second] =>...

        // または別の配列/スライスに格納することもできます（型は照合対象の値の型に依存します）
        [3, second, tail @..] => println!(
            "array[0] = 3, array[1] = {} and the other elements were {:?}",
            second, tail
        ),

        // これらのパターンを組み合わせることで、例えば最初と最後の値をバインドし、残りを単一の配列に格納することができます
        [first, middle @.., last] => println!(
            "array[0] = {}, middle = {:?}, array[2] = {}",
            first, middle, last
        ),
    }
}
```
