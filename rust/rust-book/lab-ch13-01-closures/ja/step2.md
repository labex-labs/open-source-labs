# クロージャを使った環境のキャプチャ

まずは、クロージャを使って、定義された環境から値をキャプチャして後で使う方法を調べましょう。ここにシナリオがあります。私たちのTシャツ会社は、定期的に、メーリングリストに登録された誰かに独占的な限定版のTシャツをプレゼントして、販促活動を行っています。メーリングリストに登録された人は、任意で、自分の好きな色をプロフィールに追加することができます。無料のTシャツの対象者が好きな色を設定している場合、その色のTシャツをもらいます。好きな色を指定していない場合、会社が現在最も多く持っている色のTシャツをもらいます。

これを実装する方法はたくさんあります。この例では、`Red`と`Blue`の2つのバリアントを持つ`ShirtColor`という列挙型を使います（単純化のために利用可能な色の数を制限します）。会社の在庫を表す`Inventory`構造体を定義し、`shirts`というフィールドを持ち、これは現在の在庫のTシャツの色を表す`Vec<ShirtColor>`を含んでいます。`Inventory`に定義された`giveaway`メソッドは、無料のTシャツの当選者の任意のTシャツの色の好みを取得し、その人が受け取るTシャツの色を返します。この設定をリスト13-1に示します。

ファイル名: `src/main.rs`

```rust
#[derive(Debug, PartialEq, Copy, Clone)]
enum ShirtColor {
    Red,
    Blue,
}

struct Inventory {
    shirts: Vec<ShirtColor>,
}

impl Inventory {
    fn giveaway(
        &self,
        user_preference: Option<ShirtColor>,
    ) -> ShirtColor {
      1 user_preference.unwrap_or_else(|| self.most_stocked())
    }

    fn most_stocked(&self) -> ShirtColor {
        let mut num_red = 0;
        let mut num_blue = 0;

        for color in &self.shirts {
            match color {
                ShirtColor::Red => num_red += 1,
                ShirtColor::Blue => num_blue += 1,
            }
        }
        if num_red > num_blue {
            ShirtColor::Red
        } else {
            ShirtColor::Blue
        }
    }
}

fn main() {
    let store = Inventory {
      2 shirts: vec![
            ShirtColor::Blue,
            ShirtColor::Red,
            ShirtColor::Blue,
        ],
    };

    let user_pref1 = Some(ShirtColor::Red);
  3 let giveaway1 = store.giveaway(user_pref1);
    println!(
        "The user with preference {:?} gets {:?}",
        user_pref1, giveaway1
    );

    let user_pref2 = None;
  4 let giveaway2 = store.giveaway(user_pref2);
    println!(
        "The user with preference {:?} gets {:?}",
        user_pref2, giveaway2
    );
}
```

リスト13-1: Tシャツ会社の無料配布の状況

`main`で定義された`store`には、この限定版の販促活動のために配布する2枚の青いTシャツと1枚の赤いTシャツが残っています\[2\]。赤いTシャツが好きなユーザー\[3\]と何の好みもないユーザー\[4\]に対して、`giveaway`メソッドを呼び出します。

再び、このコードはたくさんの方法で実装できます。ここでは、クロージャに焦点を当てるため、クロージャを使った`giveaway`メソッドの本体を除いて、既に学んだ概念にとどまります。`giveaway`メソッドでは、`Option<ShirtColor>`型のパラメータとしてユーザーの好みを取得し、`user_preference`に対して`unwrap_or_else`メソッドを呼び出します\[1\]。`Option<T>`の`unwrap_or_else`メソッドは、標準ライブラリによって定義されています。1つの引数を取ります。引数なしで、`T`型の値を返すクロージャ（この場合、`Option<T>`の`Some`バリアントに格納されている型と同じ型、この場合は`ShirtColor`）。`Option<T>`が`Some`バリアントの場合、`unwrap_or_else`は`Some`内の値を返します。`Option<T>`が`None`バリアントの場合、`unwrap_or_else`はクロージャを呼び出し、クロージャが返す値を返します。

クロージャ式`|| self.most_stocked()`を`unwrap_or_else`の引数として指定します。これは、引数を持たないクロージャです（クロージャに引数がある場合は、2つの垂直パイプの間に表示されます）。クロージャの本体は`self.most_stocked()`を呼び出します。ここでクロージャを定義しており、必要になったときに`unwrap_or_else`の実装がクロージャを評価します。

このコードを実行すると、以下が表示されます。

```rust
The user with preference Some(Red) gets Red
The user with preference None gets Blue
```

ここで興味深い点は、現在の`Inventory`インスタンスで`self.most_stocked()`を呼び出すクロージャを渡したことです。標準ライブラリは、私たちが定義した`Inventory`や`ShirtColor`型、またはこのシナリオで使いたいロジックについて何も知る必要はありませんでした。クロージャは、`self`の`Inventory`インスタンスへの不変参照をキャプチャし、指定したコードとともに`unwrap_or_else`メソッドに渡します。一方、関数はこのようにして環境をキャプチャすることはできません。
