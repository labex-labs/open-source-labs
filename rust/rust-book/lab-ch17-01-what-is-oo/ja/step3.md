# 実装の詳細を隠すカプセル化

OOP と一般的に関連付けられるもう一つの側面は、「カプセル化」の概念です。これは、オブジェクトの実装の詳細が、そのオブジェクトを使用するコードにはアクセスできないことを意味します。したがって、オブジェクトとやり取りする唯一の方法は、その公開 API を通じることです。オブジェクトを使用するコードは、オブジェクトの内部にアクセスして、直接データや振る舞いを変更することはできません。これにより、プログラマはオブジェクトの内部を変更してリファクタリングする際に、オブジェクトを使用するコードを変更する必要がなくなります。

第 7 章では、カプセル化を制御する方法について説明しました。コード内のどのモジュール、型、関数、メソッドが公開されるべきかを決定するために、`pub`キーワードを使用できます。デフォルトでは、それ以外のすべては非公開になります。たとえば、`i32`値のベクトルを含むフィールドを持つ`AveragedCollection`構造体を定義できます。この構造体には、ベクトル内の値の平均を含むフィールドもあります。つまり、平均値は誰かが必要になるたびに必要に応じて計算する必要はありません。言い換えれば、`AveragedCollection`は計算済みの平均値をキャッシュしてくれます。リスト 17-1 に`AveragedCollection`構造体の定義を示します。

ファイル名：`src/lib.rs`

```rust
pub struct AveragedCollection {
    list: Vec<i32>,
    average: f64,
}
```

リスト 17-1: 整数のリストとコレクション内の要素の平均を保持する`AveragedCollection`構造体

この構造体は`pub`とマークされており、他のコードが使用できるようになっていますが、構造体内のフィールドは非公開のままです。この場合、これが重要なのは、リストに値を追加または削除するたびに、平均値も更新されることを確認するためです。これは、構造体に`add`、`remove`、`average`メソッドを実装することで行います。リスト 17-2 を参照してください。

ファイル名：`src/lib.rs`

```rust
impl AveragedCollection {
    pub fn add(&mut self, value: i32) {
        self.list.push(value);
        self.update_average();
    }

    pub fn remove(&mut self) -> Option<i32> {
        let result = self.list.pop();
        match result {
            Some(value) => {
                self.update_average();
                Some(value)
            }
            None => None,
        }
    }

    pub fn average(&self) -> f64 {
        self.average
    }

    fn update_average(&mut self) {
        let total: i32 = self.list.iter().sum();
        self.average = total as f64 / self.list.len() as f64;
    }
}
```

リスト 17-2: `AveragedCollection`における公開メソッド`add`、`remove`、`average`の実装

公開メソッド`add`、`remove`、`average`は、`AveragedCollection`のインスタンス内のデータにアクセスまたは変更する唯一の方法です。`add`メソッドを使用して`list`に項目を追加するか、`remove`メソッドを使用して削除すると、各呼び出しの実装は、`average`フィールドの更新を処理する非公開の`update_average`メソッドを呼び出します。

`list`と`average`フィールドを非公開にしておくことで、外部コードが直接`list`フィールドに項目を追加または削除する方法はありません。そうでなければ、`list`が変更されたときに`average`フィールドが同期しなくなる可能性があります。`average`メソッドは`average`フィールドの値を返し、外部コードが`average`を読み取ることはできますが、変更することはできません。

`AveragedCollection`構造体の実装の詳細をカプセル化したため、将来的にデータ構造などの側面を簡単に変更できます。たとえば、`list`フィールドに`Vec<i32>`の代わりに`HashSet<i32>`を使用することができます。`add`、`remove`、`average`の公開メソッドのシグネチャが同じままであれば、`AveragedCollection`を使用するコードは変更する必要がありません。もし`list`を代わりに公開にすると、必ずしもそうではなくなります。`HashSet<i32>`と`Vec<i32>`は、項目の追加と削除に異なるメソッドを持っているため、外部コードが直接`list`を変更している場合、おそらく変更する必要があります。

もしカプセル化がオブジェクト指向と見なされるための必須の側面であるならば、Rust はその要件を満たしています。コードの異なる部分に`pub`を使用するかどうかのオプションにより、実装の詳細のカプセル化が可能になります。
