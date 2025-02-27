# 関数

関数は `fn` キーワードを使って宣言されます。その引数には、変数と同じように型注釈が付けられ、関数が値を返す場合、返却型は矢印 `->` の後に指定する必要があります。

関数内の最後の式が返却値として使われます。あるいは、`return` 文を使って、関数内のループや `if` 文の中からでも、より早く値を返すことができます。

関数を使って FizzBuzz を書き直してみましょう！

```rust
// C/C++ とは異なり、関数定義の順序に制限はありません
fn main() {
    // ここでこの関数を使うことができ、後で定義することもできます
    fizzbuzz_to(100);
}

// ブール値を返す関数
fn is_divisible_by(lhs: u32, rhs: u32) -> bool {
    // 端数ケース、早期返却
    if rhs == 0 {
        return false;
    }

    // これは式であり、ここでは `return` キーワードは必要ありません
    lhs % rhs == 0
}

// 値を返さない関数は、実際には単位型 `()` を返します
fn fizzbuzz(n: u32) -> () {
    if is_divisible_by(n, 15) {
        println!("fizzbuzz");
    } else if is_divisible_by(n, 3) {
        println!("fizz");
    } else if is_divisible_by(n, 5) {
        println!("buzz");
    } else {
        println!("{}", n);
    }
}

// 関数が `()` を返す場合、シグネチャから返却型を省略できます
fn fizzbuzz_to(n: u32) {
    for n in 1..=n {
        fizzbuzz(n);
    }
}
```
