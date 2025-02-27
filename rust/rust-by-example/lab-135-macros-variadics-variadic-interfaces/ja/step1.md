# 可変個インターフェイス

_可変個_ インターフェイスは任意の数の引数を取ります。たとえば、`println!` はフォーマット文字列によって決まる任意の数の引数を取ることができます。

前節の `calculate!` マクロを可変個に拡張することができます。

```rust
macro_rules! calculate {
    // 単一の `eval` のパターン
    (eval $e:expr) => {
        {
            let val: usize = $e; // 型を整数に強制する
            println!("{} = {}", stringify!{$e}, val);
        }
    };

    // 複数の `eval` を再帰的に分解する
    (eval $e:expr, $(eval $es:expr),+) => {{
        calculate! { eval $e }
        calculate! { $(eval $es),+ }
    }};
}

fn main() {
    calculate! { // 見てごらん！可変個の `calculate!` です！
        eval 1 + 2,
        eval 3 + 4,
        eval (2 * 3) + 1
    }
}
```

出力:

```txt
1 + 2 = 3
3 + 4 = 7
(2 * 3) + 1 = 7
```
