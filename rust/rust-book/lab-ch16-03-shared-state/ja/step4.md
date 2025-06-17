# 複数のスレッド間で Mutex`<T>`を共有する

次に、`Mutex<T>`を使って複数のスレッド間で値を共有してみましょう。10 個のスレッドを起動し、それぞれがカウンター値を 1 増やすようにします。すると、カウンターは 0 から 10 まで増えます。リスト 16-13 の例ではコンパイルエラーが発生します。そのエラーを使って、`Mutex<T>`の使い方と Rust がどのように正しく使うのを助けるかについてもっと学びましょう。

ファイル名：`src/main.rs`

```rust
use std::sync::Mutex;
use std::thread;

fn main() {
  1 let counter = Mutex::new(0);
    let mut handles = vec![];

  2 for _ in 0..10 {
      3 let handle = thread::spawn(move || {
          4 let mut num = counter.lock().unwrap();

          5 *num += 1;
        });
      6 handles.push(handle);
    }

    for handle in handles {
      7 handle.join().unwrap();
    }

  8 println!("Result: {}", *counter.lock().unwrap());
}
```

リスト 16-13: 10 個のスレッドで、それぞれが Mutex`<T>`で保護されたカウンターを 1 増やす

リスト 16-12 と同じように、`Mutex<T>`内に`i32`を保持するための`counter`変数を作成します\[1\]。次に、数値の範囲を反復することで 10 個のスレッドを作成します\[2\]。`thread::spawn`を使って、すべてのスレッドに同じクロージャを与えます。それは、カウンターをスレッドに移動し\[3\]、`lock`メソッドを呼び出すことで`Mutex<T>`のロックを取得し\[4\]、そしてミューテックス内の値に 1 を加えるものです\[5\]。スレッドがそのクロージャの実行を終えると、`num`はスコープ外になり、ロックが解放されて他のスレッドがそれを取得できるようになります。

メインスレッドでは、すべてのジョインハンドルを収集します\[6\]。そして、リスト 16-2 でやったように、各ハンドルに`join`を呼び出してすべてのスレッドが終了することを確認します\[7\]。その時点で、メインスレッドはロックを取得してこのプログラムの結果を表示します\[8\]。

この例がコンパイルされないことをヒントしました。では、なぜか見てみましょう！

```bash
error[E0382]: use of moved value: `counter`
  --> src/main.rs:9:36
   |
5  |     let counter = Mutex::new(0);
   |         ------- move occurs because `counter` has type `Mutex<i32>`, which
does not implement the `Copy` trait
...
9  |         let handle = thread::spawn(move || {
   |                                    ^^^^^^^ value moved into closure here,
in previous iteration of loop
10 |             let mut num = counter.lock().unwrap();
   |                           ------- use occurs due to use in closure
```

エラーメッセージによると、`counter`値はループの前の反復で移動されました。Rust は、ロック`counter`の所有権を複数のスレッドに移動できないことを私たちに伝えています。第 15 章で議論した複数所有権の方法を使って、コンパイラエラーを修正しましょう。
