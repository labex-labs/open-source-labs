# 他の反復子を生成するメソッド

_反復子アダプタ_ は、`Iterator` トレイトに定義されたメソッドであり、反復子を消費しません。代わりに、元の反復子のある側面を変更することで、異なる反復子を生成します。

リスト 13-14 は、反復子アダプタメソッドである `map` を呼び出す例を示しています。このメソッドは、要素が反復処理される際に各要素に対して呼び出すクロージャを取ります。`map` メソッドは、変更された要素を生成する新しい反復子を返します。ここでのクロージャは、ベクトルの各要素が 1 増えた新しい反復子を作成します。

ファイル名：`src/main.rs`

```rust
let v1: Vec<i32> = vec![1, 2, 3];

v1.iter().map(|x| x + 1);
```

リスト 13-14: 新しい反復子を作成するために反復子アダプタ `map` を呼び出す

ただし、このコードは警告を生成します。

    warning: unused `Map` that must be used
     --> src/main.rs:4:5
      |
    4 |     v1.iter().map(|x| x + 1);
      |     ^^^^^^^^^^^^^^^^^^^^^^^^^
      |
      = note: `#[warn(unused_must_use)]` on by default
      = note: iterators are lazy and do nothing unless consumed

リスト 13-14 のコードは何も行いません。指定したクロージャは決して呼び出されません。この警告は、なぜそうなるのかを思い出させてくれます。反復子アダプタは遅延評価であり、ここで反復子を消費する必要があります。

この警告を修正して反復子を消費するには、リスト 12-1 で `env::args` と共に使用した `collect` メソッドを使用します。このメソッドは反復子を消費し、結果の値をコレクションデータ型に収集します。

リスト 13-15 では、`map` の呼び出しから返される反復子を反復処理した結果をベクトルに収集しています。このベクトルには、元のベクトルの各要素が 1 増えたものが含まれるようになります。

ファイル名：`src/main.rs`

```rust
let v1: Vec<i32> = vec![1, 2, 3];

let v2: Vec<_> = v1.iter().map(|x| x + 1).collect();

assert_eq!(v2, vec![2, 3, 4]);
```

リスト 13-15: 新しい反復子を作成するために `map` メソッドを呼び出し、その後新しい反復子を消費してベクトルを作成するために `collect` メソッドを呼び出す

`map` はクロージャを取るため、各要素に対して行いたい任意の操作を指定できます。これは、クロージャが `Iterator` トレイトが提供する反復処理の動作を再利用しながら、ある動作をカスタマイズできる素晴らしい例です。

反復子アダプタの複数の呼び出しをチェーン化して、読みやすい方法で複雑な操作を行うことができます。ただし、すべての反復子は遅延評価であるため、反復子アダプタの呼び出しから結果を得るには、消費アダプタメソッドの 1 つを呼び出す必要があります。
