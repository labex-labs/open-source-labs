# 戻り値とスコープ

戻り値も所有権を移転することができます。リスト 4-4 は、戻り値を持つ関数の例を示しており、リスト 4-3 と同様の注釈が付いています。

    // src/main.rs
    fn main() {
        let s1 = gives_ownership();         // gives_ownershipはその戻り値を
                                            // s1にムーブします

        let s2 = String::from("hello");     // s2がスコープ内に入ります

        let s3 = takes_and_gives_back(s2);  // s2がtakes_and_gives_backに
                                            // ムーブされ、それが戻り値を
                                            // s3にムーブします
    } // ここでは、s3がスコープ外に出て破棄されます。s2はムーブされているので、
      // 何も起こりません。s1がスコープ外に出て破棄されます

    fn gives_ownership() -> String {             // gives_ownershipはその戻り値を
                                                 // 呼び出す関数にムーブします

        let some_string = String::from("yours"); // some_stringがスコープ内に入ります

        some_string                              // some_stringが返され、
                                                 // 呼び出し元の関数にムーブされます
    }

    // この関数はStringを受け取り、Stringを返します
    fn takes_and_gives_back(a_string: String) -> String { // a_stringが
                                                          // スコープ内に入ります

        a_string  // a_stringが返され、呼び出し元の関数にムーブされます
    }

リスト 4-4: 戻り値の所有権の移転

変数の所有権は、毎回同じパターンに従います。値を別の変数に代入すると、それがムーブされます。ヒープ上のデータを含む変数がスコープ外になると、データの所有権が別の変数に移されていない限り、値は`drop`によってクリーンアップされます。

これは機能しますが、すべての関数で所有権を取得してから所有権を返すのは少々面倒です。関数に値を使用させたいが所有権を取得したくない場合どうすればよいでしょうか。関数の本体から返したいデータに加えて、再利用したい場合は何を渡しても再度渡さなければならないのは非常に面倒です。

Rust は、タプルを使って複数の値を返すことができます。リスト 4-5 に示すようにです。

ファイル名：`src/main.rs`

```rust
fn main() {
    let s1 = String::from("hello");

    let (s2, len) = calculate_length(s1);

    println!("The length of '{s2}' is {len}.");
}

fn calculate_length(s: String) -> (String, usize) {
    let length = s.len(); // len() は String の長さを返します

    (s, length)
}
```

リスト 4-5: パラメータの所有権の返却

しかし、これはあまりにも形式的で、一般的な概念にとっては多くの作業が必要です。幸いなことに、Rust には所有権を移転することなく値を使用する機能があり、これを「参照」と呼びます。
