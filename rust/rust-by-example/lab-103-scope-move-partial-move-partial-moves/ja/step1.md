# 部分的なムーブ

単一の変数の\[分解構文\]内では、`by-move` と `by-reference` の両方のパターンバインディングを同時に使用できます。これを行うと、変数の _部分的なムーブ_ が行われます。これは、変数の一部がムーブされる一方で、他の部分は残ることを意味します。この場合、親変数はその後は全体として使用できませんが、参照のみされている（ムーブされていない）部分は依然として使用できます。

```rust
fn main() {
    #[derive(Debug)]
    struct Person {
        name: String,
        age: Box<u8>,
    }

    let person = Person {
        name: String::from("Alice"),
        age: Box::new(20),
    };

    // `name` は person からムーブされますが、`age` は参照されます
    let Person { name, ref age } = person;

    println!("The person's age is {}", age);

    println!("The person's name is {}", name);

    // エラー！部分的にムーブされた値の借用：`person` 部分的なムーブが発生します
    //println!("The person struct is {:?}", person);

    // `person` は使用できませんが、`person.age` はムーブされていないため使用できます
    println!("The person's age from person struct is {}", person.age);
}
```

（この例では、部分的なムーブを示すために `age` 変数をヒープ上に格納しています。上記のコードで `ref` を削除すると、`person.age` の所有権が変数 `age` にムーブされるため、エラーが発生します。もし `Person.age` がスタック上に格納されていた場合、`age` の定義が `person.age` からデータをコピーしてムーブしないため、`ref` は必要ありません。）
