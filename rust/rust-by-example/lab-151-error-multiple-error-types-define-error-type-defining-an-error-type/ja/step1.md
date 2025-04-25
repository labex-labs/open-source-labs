# エラー型の定義

時には、単一のエラー型ですべての異なるエラーを隠すことでコードが簡略化されます。これをカスタム エラーで示します。

Rust では独自のエラー型を定義できます。一般的に、「良い」エラー型は次のようになります。

- 同じ型で異なるエラーを表現する
- ユーザーに分かりやすいエラー メッセージを表示する
- 他の型との比較が容易である
  - 良い例：`Err(EmptyVec)`
  - 悪い例：`Err("Please use a vector with at least one element".to_owned())`
- エラーに関する情報を保持できる
  - 良い例：`Err(BadChar(c, position))`
  - 悪い例：`Err("+ cannot be used here".to_owned())`
- 他のエラーとの組み合わせが良好である

```rust
use std::fmt;

type Result<T> = std::result::Result<T, DoubleError>;

// エラー型を定義します。これらはエラー ハンドリングのケースに応じてカスタマイズできます。
// これで、独自のエラーを書き、基礎となるエラーの実装に委ねる、またはその中間の何かを行うことができます。
#[derive(Debug, Clone)]
struct DoubleError;

// エラーの生成は、その表示方法とは完全に別です。
// 表示スタイルで複雑なロジックを混乱させることはありません。
//
// エラーに関する追加情報を格納していないことに注意してください。これは、その情報を保持するために型を変更せずには、どの文字列が解析に失敗したかを示すことができないことを意味します。
impl fmt::Display for DoubleError {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "invalid first item to double")
    }
}

fn double_first(vec: Vec<&str>) -> Result<i32> {
    vec.first()
        // エラーを新しい型に変更します。
     .ok_or(DoubleError)
     .and_then(|s| {
            s.parse::<i32>()
                // ここでも新しいエラー型に更新します。
             .map_err(|_| DoubleError)
             .map(|i| 2 * i)
        })
}

fn print(result: Result<i32>) {
    match result {
        Ok(n) => println!("The first doubled is {}", n),
        Err(e) => println!("Error: {}", e),
    }
}

fn main() {
    let numbers = vec!["42", "93", "18"];
    let empty = vec![];
    let strings = vec!["tofu", "93", "18"];

    print(double_first(numbers));
    print(double_first(empty));
    print(double_first(strings));
}
```
