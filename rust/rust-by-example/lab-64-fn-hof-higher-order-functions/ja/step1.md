# 高階関数

Rust には高階関数（HOF：Higher Order Function）が用意されています。これらは、1 つ以上の関数を引数として受け取り、またはより有用な関数を生成する関数です。HOF と遅延イテレータにより、Rust に関数型言語の雰囲気が与えられます。

```rust
fn is_odd(n: u32) -> bool {
    n % 2 == 1
}

fn main() {
    println!("Find the sum of all the squared odd numbers under 1000");
    let upper = 1000;

    // 命令型アプローチ
    // 累積変数を宣言
    let mut acc = 0;
    // 反復処理：0, 1, 2,... 無限大まで
    for n in 0.. {
        // 数値を 2 乗する
        let n_squared = n * n;

        if n_squared >= upper {
            // 上限を超えた場合、ループを終了
            break;
        } else if is_odd(n_squared) {
            // 奇数の場合、値を累積
            acc += n_squared;
        }
    }
    println!("命令型スタイル：{}", acc);

    // 関数型アプローチ
    let sum_of_squared_odd_numbers: u32 =
        (0..).map(|n| n * n)                             // すべての自然数を 2 乗
            .take_while(|&n_squared| n_squared < upper) // 上限未満
            .filter(|&n_squared| is_odd(n_squared))     // 奇数であるもの
            .sum();                                     // 合計する
    println!("関数型スタイル：{}", sum_of_squared_odd_numbers);
}
```

`Option` と `Iterator` は、HOF の多くを実装しています。
