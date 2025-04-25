# スレッドで move クロージャを使用する

`thread::spawn` に渡されるクロージャでは、`move` キーワードを頻繁に使用します。これは、クロージャが環境から使用する値の所有権を取得するため、それらの値の所有権を 1 つのスレッドから別のスレッドに移すためです。「クロージャで環境をキャプチャする」では、クロージャのコンテキストで `move` について説明しました。今回は、`move` と `thread::spawn` の相互作用に焦点を当てます。

リスト 16-1 では、`thread::spawn` に渡すクロージャには引数がありません。生成されたスレッドのコードでは、メインスレッドのデータを使用していません。生成されたスレッドでメインスレッドのデータを使用するには、生成されたスレッドのクロージャが必要な値をキャプチャする必要があります。リスト 16-3 は、メインスレッドでベクトルを作成し、生成されたスレッドで使用する試みを示しています。しかし、すぐにわかるように、これではまだ機能しません。

ファイル名：`src/main.rs`

```rust
use std::thread;

fn main() {
    let v = vec![1, 2, 3];

    let handle = thread::spawn(|| {
        println!("Here's a vector: {:?}", v);
    });

    handle.join().unwrap();
}
```

リスト 16-3: 別のスレッドでメインスレッドによって作成されたベクトルを使用しようとする

クロージャは `v` を使用するため、`v` をキャプチャしてクロージャの環境の一部にします。`thread::spawn` はこのクロージャを新しいスレッドで実行するため、その新しいスレッド内で `v` にアクセスできるはずです。しかし、この例をコンパイルすると、次のエラーが表示されます。

```bash
error[E0373]: closure may outlive the current function, but it borrows `v`,
which is owned by the current function
 --> src/main.rs:6:32
  |
6 |     let handle = thread::spawn(|| {
  |                                ^^ may outlive borrowed value `v`
7 |         println!("Here's a vector: {:?}", v);
  |                                           - `v` is borrowed here
  |
note: function requires argument type to outlive `'static`
 --> src/main.rs:6:18
  |
6 |       let handle = thread::spawn(|| {
  |  __________________^
7 | |         println!("Here's a vector: {:?}", v);
8 | |     });
  | |______^
help: to force the closure to take ownership of `v` (and any other referenced
variables), use the `move` keyword
  |
6 |     let handle = thread::spawn(move || {
  |                                ++++
```

Rust は、どのように `v` をキャプチャするかを推論します。`println!` は `v` への参照のみが必要なため、クロージャは `v` を借用しようとします。しかし、問題があります。Rust は生成されたスレッドがどのくらい実行されるかを知ることができないため、`v` への参照が常に有効であることを保証できません。

リスト 16-4 は、`v` への参照が有効でなくなる可能性があるより現実的なシナリオを提供しています。

ファイル名：`src/main.rs`

```rust
use std::thread;

fn main() {
    let v = vec![1, 2, 3];

    let handle = thread::spawn(|| {
        println!("Here's a vector: {:?}", v);
    });

    drop(v); // oh no!

    handle.join().unwrap();
}
```

リスト 16-4: メインスレッドが `v` を破棄する生成されたスレッドによって `v` への参照をキャプチャしようとするクロージャを持つスレッド

Rust がこのコードを実行させる場合、生成されたスレッドがまったく実行されずに即座にバックグラウンドに置かれる可能性があります。生成されたスレッドは内部で `v` への参照を持っていますが、メインスレッドは第 15 章で説明した `drop` 関数を使用してすぐに `v` を破棄します。その後、生成されたスレッドが実行を開始すると、`v` はもはや有効ではなくなるため、それへの参照も無効になります。ああ、まずい！

リスト 16-3 のコンパイラエラーを修正するには、エラーメッセージのアドバイスを使用できます。

    help: to force the closure to take ownership of `v` (and any other referenced
    variables), use the `move` keyword
      |
    6 |     let handle = thread::spawn(move || {
      |                                ++++

クロージャの前に `move` キーワードを追加することで、クロージャに値の所有権を取得させるように強制し、Rust が値を借用するように推論するのを許さなくなります。リスト 16-5 に示すように、リスト 16-3 を修正すると、意図通りにコンパイルされて実行されます。

ファイル名：`src/main.rs`

```rust
use std::thread;

fn main() {
    let v = vec![1, 2, 3];

    let handle = thread::spawn(move || {
        println!("Here's a vector: {:?}", v);
    });

    handle.join().unwrap();
}
```

リスト 16-5: `move` キーワードを使用して、クロージャに使用する値の所有権を取得させる

リスト 16-4 のコードを修正するために、メインスレッドが `drop` を呼び出した場合と同じことを試してみたくなるかもしれません。しかし、この修正は機能しません。なぜなら、リスト 16-4 が試していることは、別の理由で禁止されているからです。クロージャに `move` を追加すると、`v` がクロージャの環境に移動し、メインスレッドではもはや `drop` を呼び出せなくなります。代わりに、次のコンパイラエラーが表示されます。

```bash
error[E0382]: use of moved value: `v`
  --> src/main.rs:10:10
   |
4  |     let v = vec![1, 2, 3];
   |         - move occurs because `v` has type `Vec<i32>`, which does not
implement the `Copy` trait
5  |
6  |     let handle = thread::spawn(move || {
   |                                ------- value moved into closure here
7  |         println!("Here's a vector: {:?}", v);
   |                                           - variable moved due to use in
closure
...
10 |     drop(v); // oh no!
   |          ^ value used here after move
```

Rust の所有権ルールが再び助けてくれました！リスト 16-3 のコードでエラーが表示されたのは、Rust が保守的で、スレッドに対して `v` を借用していたためです。これは、理論的にメインスレッドが生成されたスレッドの参照を無効にする可能性があることを意味します。`v` の所有権を生成されたスレッドに移動するように Rust に指示することで、メインスレッドがもはや `v` を使用しないことを Rust に保証しています。同じ方法でリスト 16-4 を変更すると、メインスレッドで `v` を使用しようとするときに所有権ルールに違反してしまいます。`move` キーワードは、借用する Rust の保守的な既定値を上書きします。所有権ルールを破ることはできません。

ここまでで、スレッドとは何か、およびスレッド API が提供するメソッドについて説明しました。次に、スレッドを使用できる状況をいくつか見てみましょう。
