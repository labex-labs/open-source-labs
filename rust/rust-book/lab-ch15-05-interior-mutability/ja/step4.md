# 内部可変性のユースケース：モックオブジェクト

テスト中には、プログラマーが特定の動作を観察し、それが正しく実装されていることをアサートするために、ある型の代わりに別の型を使用することがあります。この置き換え用の型は「テストダブル」と呼ばれます。映画制作におけるスタントダブルのように考えてください。ある人が登場して、特別に難しいシーンを演じる俳優の代わりになります。テストを実行しているとき、テストダブルは他の型に代わって機能します。「モックオブジェクト」は、テスト中に何が起こったかを記録する特定の種類のテストダブルであり、正しいアクションが行われたことをアサートできるようになります。

Rust には、他の言語にあるのと同じ意味でのオブジェクトはありません。また、他の言語のように、標準ライブラリにモックオブジェクト機能が組み込まれていません。ただし、モックオブジェクトと同じ目的を果たす構造体を作成することは確かにできます。

ここでテストするシナリオを見てみましょう。ある値を最大値と比較して追跡し、現在の値が最大値に近い程度に応じてメッセージを送信するライブラリを作成します。たとえば、このライブラリは、ユーザーが許可されている API 呼び出し回数の制限を追跡するために使用できます。

私たちのライブラリは、値が最大値にどれだけ近いかを追跡し、いつどのようなメッセージを送信すべきかを提供する機能のみを提供します。私たちのライブラリを使用するアプリケーションは、メッセージを送信するメカニズムを提供する必要があります。アプリケーションは、アプリケーション内にメッセージを置いたり、メールを送信したり、テキストメッセージを送信したり、その他の何かを行うことができます。ライブラリはその詳細を知る必要はありません。必要なのは、私たちが提供する `Messenger` と呼ばれるトレイトを実装するものだけです。リスト 15-20 にライブラリコードを示します。

ファイル名：`src/lib.rs`

```rust
pub trait Messenger {
  1 fn send(&self, msg: &str);
}

pub struct LimitTracker<'a, T: Messenger> {
    messenger: &'a T,
    value: usize,
    max: usize,
}

impl<'a, T> LimitTracker<'a, T>
where
    T: Messenger,
{
    pub fn new(
        messenger: &'a T,
        max: usize
    ) -> LimitTracker<'a, T> {
        LimitTracker {
            messenger,
            value: 0,
            max,
        }
    }

  2 pub fn set_value(&mut self, value: usize) {
        self.value = value;

        let percentage_of_max =
            self.value as f64 / self.max as f64;

        if percentage_of_max >= 1.0 {
            self.messenger
               .send("Error: You are over your quota!");
        } else if percentage_of_max >= 0.9 {
            self.messenger
               .send("Urgent: You're at 90% of your quota!");
        } else if percentage_of_max >= 0.75 {
            self.messenger
               .send("Warning: You're at 75% of your quota!");
        }
    }
}
```

リスト 15-20：値が最大値にどれだけ近いかを追跡し、値が特定のレベルに達したときに警告するライブラリ

このコードの重要な部分の 1 つは、`Messenger` トレイトに `send` と呼ばれる 1 つのメソッドがあり、これは `self` への不変参照とメッセージのテキストを取ります \[1\]。このトレイトは、モックオブジェクトが実装する必要があるインターフェイスであり、モックを実際のオブジェクトと同じように使用できるようになります。もう 1 つの重要な部分は、`LimitTracker` の `set_value` メソッドの動作をテストしたいことです \[2\]。`value` パラメータに渡す値を変更することはできますが、`set_value` はアサーション用に何も返しません。`Messenger` トレイトを実装するものと `max` の特定の値を持つ `LimitTracker` を作成した場合、`value` に異なる数値を渡すと、メッセンジャーに適切なメッセージを送信するように指示されることを言えるようになりたいです。

`send` を呼び出したときにメールやテキストメッセージを送信する代わりに、送信されたメッセージを追跡するだけのモックオブジェクトが必要です。モックオブジェクトの新しいインスタンスを作成し、そのモックオブジェクトを使用する `LimitTracker` を作成し、`LimitTracker` の `set_value` メソッドを呼び出し、その後、モックオブジェクトに期待されるメッセージがあることを確認します。リスト 15-21 は、それを行うためのモックオブジェクトの実装の試みを示していますが、借用チェッカーはそれを許可しません。

ファイル名：`src/lib.rs`

```rust
#[cfg(test)]
mod tests {
    use super::*;

  1 struct MockMessenger {
      2 sent_messages: Vec<String>,
    }

    impl MockMessenger {
      3 fn new() -> MockMessenger {
            MockMessenger {
                sent_messages: vec![],
            }
        }
    }

  4 impl Messenger for MockMessenger {
        fn send(&self, message: &str) {
          5 self.sent_messages.push(String::from(message));
        }
    }

    #[test]
  6 fn it_sends_an_over_75_percent_warning_message() {
        let mock_messenger = MockMessenger::new();
        let mut limit_tracker = LimitTracker::new(
            &mock_messenger,
            100
        );

        limit_tracker.set_value(80);

        assert_eq!(mock_messenger.sent_messages.len(), 1);
    }
}
```

リスト 15-21：借用チェッカーに許可されない `MockMessenger` の実装の試み

このテストコードは、送信されたメッセージを追跡するための `String` 値の `Vec` を持つ `sent_messages` フィールドを持つ `MockMessenger` 構造体を定義しています \[1\] \[2\]。また、空のメッセージリストで始まる新しい `MockMessenger` 値を作成するのを便利にするために、関連付けられた関数 `new` を定義しています \[3\]。その後、`MockMessenger` 用に `Messenger` トレイトを実装して \[4\]、`MockMessenger` を `LimitTracker` に渡せるようにします。`send` メソッドの定義で \[5\]、パラメータとして渡されたメッセージを受け取り、`sent_messages` の `MockMessenger` リストに保存します。

テストでは、`LimitTracker` に `value` を `max` 値の 75％ 以上に設定するように指示したときに何が起こるかをテストしています \[6\]。まず、空のメッセージリストで始まる新しい `MockMessenger` を作成します。次に、新しい `LimitTracker` を作成し、新しい `MockMessenger` への参照と `max` 値 100 を渡します。`LimitTracker` の `set_value` メソッドに値 80 を渡して呼び出します。これは 100 の 75％ 以上です。その後、`MockMessenger` が追跡しているメッセージのリストに現在 1 つのメッセージがあることをアサートします。

ただし、このテストには 1 つの問題があります。ここに示すように：

```bash
error[E0596]: cannot borrow `self.sent_messages` as mutable, as it is behind a
`&` reference
  --> src/lib.rs:58:13
   |
2  |     fn send(&self, msg: &str);
   |             ----- help: consider changing that to be a mutable reference:
`&mut self`
...
58 |             self.sent_messages.push(String::from(message));
   |             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ `self` is a
`&` reference, so the data it refers to cannot be borrowed as mutable
```

`send` メソッドが `self` への不変参照を取るため、`MockMessenger` を変更してメッセージを追跡することはできません。また、エラーメッセージの提案を受けて `&mut self` を代わりに使用しようとしても、`send` のシグネチャが `Messenger` トレイト定義のシグネチャと一致しなくなるため（試してみて、どのようなエラーメッセージが表示されるか見てみてください）、できません。

これは内部可変性が役立つ状況です！`sent_messages` を `RefCell<T>` 内に保存し、その後 `send` メソッドが `sent_messages` を変更して見たメッセージを保存できるようにします。リスト 15-22 にそれがどのように見えるかを示します。

ファイル名：`src/lib.rs`

```rust
#[cfg(test)]
mod tests {
    use super::*;
    use std::cell::RefCell;

    struct MockMessenger {
      1 sent_messages: RefCell<Vec<String>>,
    }

    impl MockMessenger {
        fn new() -> MockMessenger {
            MockMessenger {
              2 sent_messages: RefCell::new(vec![]),
            }
        }
    }

    impl Messenger for MockMessenger {
        fn send(&self, message: &str) {
            self.sent_messages
              3.borrow_mut()
               .push(String::from(message));
        }
    }

    #[test]
    fn it_sends_an_over_75_percent_warning_message() {
        --snip--

        assert_eq!(
          4 mock_messenger.sent_messages.borrow().len(),
            1
        );
    }
}
```

リスト 15-22：外部の値が不変と見なされる間に内部の値を変更するために `RefCell<T>` を使用する

`sent_messages` フィールドは現在、`Vec<String>` ではなく `RefCell<Vec<String>>` 型になっています \[1\]。`new` 関数では、空のベクトルの周りに新しい `RefCell<Vec<String>>` インスタンスを作成します \[2\]。

`send` メソッドの実装では、最初のパラメータは依然として `self` の不変借用であり、これはトレイト定義と一致します。`self.sent_messages` の `RefCell<Vec<String>>` に対して `borrow_mut` を呼び出して \[3\]、`RefCell<Vec<String>>` 内の値（つまりベクトル）に対する可変参照を取得します。その後、ベクトルの可変参照に対して `push` を呼び出して、テスト中に送信されたメッセージを追跡します。

最後に行う変更は、アサーションです。内部のベクトルに何個の要素があるかを確認するには、`RefCell<Vec<String>>` に対して `borrow` を呼び出して、ベクトルに対する不変参照を取得します \[4\]。

ここで `RefCell<T>` をどのように使用するかを見てきたので、それがどのように機能するかを掘り下げてみましょう！
