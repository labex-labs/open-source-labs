# ワークスペース内で外部パッケージに依存する

ワークスペースは、各クレートのディレクトリに`Cargo.lock`があるのではなく、トップレベルに1つだけの`Cargo.lock`ファイルを持っていることに注意してください。これにより、すべてのクレートがすべての依存関係の同じバージョンを使用していることが保証されます。もし`rand`パッケージを`adder/Cargo.toml`と`add_one/Cargo.toml`ファイルに追加すると、Cargoはそれらの両方を`rand`の1つのバージョンに解決し、それを1つの`Cargo.lock`に記録します。ワークスペース内のすべてのクレートが同じ依存関係を使用することは、クレートが常に互換性があることを意味します。`add_one/Cargo.toml`ファイルの`[dependencies]`セクションに`rand`クレートを追加して、`add_one`クレートで`rand`クレートを使用できるようにしましょう。

ファイル名: `add_one/Cargo.toml`

```tomlrust
[dependencies]
rand = "0.8.5"
```

これで、`add_one/src/lib.rs`ファイルに`use rand;`を追加できます。そして、`add`ディレクトリで`cargo build`を実行してワークスペース全体をビルドすると、`rand`クレートが取り込まれてコンパイルされます。スコープ内に持ち込んだ`rand`を参照していないため、1つの警告が表示されます。

```bash
$ cargo build
    Updating crates.io index
  Downloaded rand v0.8.5
   --snip--
   Compiling rand v0.8.5
   Compiling add_one v0.1.0 (file:///projects/add/add_one)
   Compiling adder v0.1.0 (file:///projects/add/adder)
    Finished dev [unoptimized + debuginfo] target(s) in 10.18s
```

トップレベルの`Cargo.lock`には、現在、`add_one`が`rand`に依存する情報が含まれています。ただし、ワークスペース内のどこかで`rand`が使用されている場合でも、他のクレートで使用できるようにするには、それらの`Cargo.toml`ファイルにも`rand`を追加する必要があります。たとえば、`adder`パッケージの`adder/src/main.rs`ファイルに`use rand;`を追加すると、エラーが表示されます。

```bash
$ cargo build
   --snip--
   Compiling adder v0.1.0 (file:///projects/add/adder)
error[E0432]: unresolved import `rand`
 --> adder/src/main.rs:2:5
  |
2 | use rand;
  |     ^^^^ no external crate `rand`
```

これを修正するには、`adder`パッケージの`Cargo.toml`ファイルを編集して、`rand`もその依存関係であることを示します。`adder`パッケージをビルドすると、`Cargo.lock`の`adder`の依存関係のリストに`rand`が追加されますが、`rand`の追加コピーはダウンロードされません。Cargoは、ワークスペース内の各パッケージのすべてのクレートが`rand`パッケージを使用している場合、同じバージョンを使用していることを保証しており、スペースを節約し、ワークスペース内のクレートが互換性があることを保証します。
