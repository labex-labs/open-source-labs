# その環境をキャプチャするクロージャの使用

多くの反復子アダプタはクロージャを引数として取り、一般的に反復子アダプタの引数として指定するクロージャは、その環境をキャプチャするクロージャになります。

この例では、クロージャを取る `filter` メソッドを使用します。クロージャは反復子から 1 つの要素を取得し、`bool` を返します。クロージャが `true` を返す場合、その値は `filter` によって生成される反復処理に含まれます。クロージャが `false` を返す場合、その値は含まれません。

リスト 13-16 では、`filter` を使って、その環境から `shoe_size` 変数をキャプチャするクロージャを使って、`Shoe` 構造体インスタンスのコレクションを反復処理します。これにより、指定されたサイズの靴だけが返されます。

ファイル名：`src/lib.rs`

```rust
#[derive(PartialEq, Debug)]
struct Shoe {
    size: u32,
    style: String,
}

fn shoes_in_size(shoes: Vec<Shoe>, shoe_size: u32) -> Vec<Shoe> {
    shoes.into_iter().filter(|s| s.size == shoe_size).collect()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn filters_by_size() {
        let shoes = vec![
            Shoe {
                size: 10,
                style: String::from("sneaker"),
            },
            Shoe {
                size: 13,
                style: String::from("sandal"),
            },
            Shoe {
                size: 10,
                style: String::from("boot"),
            },
        ];

        let in_my_size = shoes_in_size(shoes, 10);

        assert_eq!(
            in_my_size,
            vec![
                Shoe {
                    size: 10,
                    style: String::from("sneaker")
                },
                Shoe {
                    size: 10,
                    style: String::from("boot")
                },
            ]
        );
    }
}
```

リスト 13-16: `shoe_size` をキャプチャするクロージャを使って `filter` メソッドを使用する

`shoes_in_size` 関数は、靴のベクトルと靴のサイズを引数として受け取ります。この関数は、指定されたサイズの靴のみを含むベクトルを返します。

`shoes_in_size` の本体では、`into_iter` を呼び出してベクトルの所有権を取得する反復子を作成します。その後、`filter` を呼び出して、その反復子を、クロージャが `true` を返す要素のみを含む新しい反復子に変換します。

クロージャはその環境から `shoe_size` パラメータをキャプチャし、その値を各靴のサイズと比較して、指定されたサイズの靴のみを残します。最後に、`collect` を呼び出すことで、変換された反復子から返される値を関数が返すベクトルに収集します。

このテストは、`shoes_in_size` を呼び出すと、指定した値と同じサイズの靴のみが返されることを示しています。
