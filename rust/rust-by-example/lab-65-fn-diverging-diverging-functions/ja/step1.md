# 発散関数

発散関数は決して戻りません。それらは空の型である `!` を使ってマークされます。

```rust
fn foo() ->! {
    panic!("This call never returns.");
}
```

他のすべての型とは対照的に、この型はインスタンス化できません。なぜなら、この型が持ち得るすべての可能な値の集合は空だからです。これは、ちょうど 1 つの可能な値しか持たない `()` 型とは異なることに注意してください。

たとえば、この関数は通常通り戻りますが、戻り値には情報がありません。

```rust
fn some_fn() {
    ()
}

fn main() {
    let _a: () = some_fn();
    println!("This function returns and you can see this line.");
}
```

この関数とは対照的に、この関数は決して呼び出し元に制御を戻しません。

```rust
#![feature(never_type)]

fn main() {
    let x:! = panic!("This call never returns.");
    println!("You will never see this line!");
}
```

これは抽象的な概念のように見えるかもしれませんが、実際には非常に便利で使い勝手が良い場合が多いです。この型の主な利点は、他の任意の型にキャストできることです。したがって、正確な型が必要な場所、たとえば `match` ブランチで使用できます。これにより、次のようなコードを書くことができます。

```rust
fn main() {
    fn sum_odd_numbers(up_to: u32) -> u32 {
        let mut acc = 0;
        for i in 0..up_to {
            // この match 式の戻り値の型は u32 でなければならないことに注意してください
            // "addition"変数の型のためです。
            let addition: u32 = match i%2 == 1 {
                // "i"変数は u32 型で、完全に問題ありません。
                true => i,
                // 一方、"continue"式は u32 を返しません
                // しかし、これはまだ大丈夫です。なぜなら、それは決して戻らないため、
                // match 式の型要件を違反しません。
                false => continue,
            };
            acc += addition;
        }
        acc
    }
    println!("Sum of odd numbers up to 9 (excluding): {}", sum_odd_numbers(9));
}
```

また、ネットワークサーバーのような無限ループする関数（たとえば `loop {}`）やプロセスを終了する関数（たとえば `exit()`）の戻り値の型でもあります。
