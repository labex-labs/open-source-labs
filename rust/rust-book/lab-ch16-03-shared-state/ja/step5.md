# 複数のスレッドによる複数所有権

第15章では、スマートポインタ`Rc<T>`を使って参照カウント付きの値を作成することで、1つの値を複数の所有者に与えました。ここでも同じことをして、何が起こるか見てみましょう。リスト16-14では、`Mutex<T>`を`Rc<T>`でラップし、所有権をスレッドに移動する前に`Rc<T>`をクローンします。

ファイル名: `src/main.rs`

```rust
use std::rc::Rc;
use std::sync::Mutex;
use std::thread;

fn main() {
    let counter = Rc::new(Mutex::new(0));
    let mut handles = vec![];

    for _ in 0..10 {
        let counter = Rc::clone(&counter);
        let handle = thread::spawn(move || {
            let mut num = counter.lock().unwrap();

            *num += 1;
        });
        handles.push(handle);
    }

    for handle in handles {
        handle.join().unwrap();
    }

    println!("Result: {}", *counter.lock().unwrap());
}
```

リスト16-14: `Rc<T>`を使って複数のスレッドが`Mutex<T>`を所有できるようにする試み

再びコンパイルすると、違うエラーが出ます！コンパイラがたくさん教えてくれています。

```bash
error[E0277]: `Rc<Mutex<i32>>` cannot be sent between threads safely 1
   --> src/main.rs:11:22
    |
11  |           let handle = thread::spawn(move || {
    |  ______________________^^^^^^^^^^^^^_-
    | |                      |
    | |                      `Rc<Mutex<i32>>` cannot be sent between threads
safely
12  | |             let mut num = counter.lock().unwrap();
13  | |
14  | |             *num += 1;
15  | |         });
    | |_________- within this `[closure@src/main.rs:11:36: 15:10]`
    |
= help: within `[closure@src/main.rs:11:36: 15:10]`, the trait `Send` is not
implemented for `Rc<Mutex<i32>>` 2
    = note: required because it appears within the type
`[closure@src/main.rs:11:36: 15:10]`
note: required by a bound in `spawn`
```

えらーメッセージがとても長いです！注目すべき重要な部分はここです：「`Rc<Mutex<i32>>` cannot be sent between threads safely」\[1\]。コンパイラはまた、その理由も教えてくれています：「the trait `Send` is not implemented for `Rc<Mutex<i32>>`」\[2\]。次のセクションで`Send`について話します。これは、スレッドで使う型が並列状況で使うことができるようにするためのトレイトの1つです。

残念ながら、`Rc<T>`はスレッド間で共有するのが安全ではありません。`Rc<T>`が参照カウントを管理するとき、`clone`の各呼び出しでカウントが増え、各クローンが破棄されるときにカウントが減ります。しかし、参照カウントの変更が他のスレッドによって中断されないようにするための並列処理プリミティブを使っていません。これは誤ったカウントにつながる可能性があります。つまり、細かいバグがあり、それがメモリリークにつながったり、使い終わる前に値が破棄されたりする可能性があります。必要なのは、`Rc<T>`とまったく同じ型でありながら、参照カウントの変更をスレッドセーフな方法で行う型です。
