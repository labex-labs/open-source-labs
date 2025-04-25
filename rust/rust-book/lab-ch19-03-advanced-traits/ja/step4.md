# 同名のメソッドの曖昧さの解消

Rust では、あるトレイトが別のトレイトのメソッドと同じ名前のメソッドを持つことを妨げるものはありませんし、Rust はまた、ある型に対して両方のトレイトを実装することも妨げません。また、トレイトのメソッドと同じ名前のメソッドを型に直接実装することも可能です。

同名のメソッドを呼び出す際、どのメソッドを使用したいかを Rust に伝える必要があります。リスト 19-16 のコードを考えてみましょう。ここでは、`Pilot`と`Wizard`の 2 つのトレイトを定義しており、両方とも`fly`という名前のメソッドを持っています。そして、既に`fly`という名前のメソッドが実装されている`Human`型に対して、両方のトレイトを実装しています。各`fly`メソッドは異なることを行います。

ファイル名：`src/main.rs`

```rust
trait Pilot {
    fn fly(&self);
}

trait Wizard {
    fn fly(&self);
}

struct Human;

impl Pilot for Human {
    fn fly(&self) {
        println!("This is your captain speaking.");
    }
}

impl Wizard for Human {
    fn fly(&self) {
        println!("Up!");
    }
}

impl Human {
    fn fly(&self) {
        println!("*waving arms furiously*");
    }
}
```

リスト 19-16：`fly`メソッドを持つ 2 つのトレイトを定義し、`Human`型に実装し、`Human`に直接`fly`メソッドを実装する

`Human`のインスタンスで`fly`を呼び出すと、コンパイラはデフォルトで型に直接実装されているメソッドを呼び出します。リスト 19-17 を参照してください。

ファイル名：`src/main.rs`

```rust
fn main() {
    let person = Human;
    person.fly();
}
```

リスト 19-17：`Human`のインスタンスで`fly`を呼び出す

このコードを実行すると、`*waving arms furiously*`が表示され、Rust が`Human`に直接実装されている`fly`メソッドを呼び出したことがわかります。

`Pilot`トレイトまたは`Wizard`トレイトの`fly`メソッドを呼び出すには、どの`fly`メソッドを意味するのかを指定するために、より明示的な構文を使用する必要があります。リスト 19-18 にこの構文を示します。

ファイル名：`src/main.rs`

```rust
fn main() {
    let person = Human;
    Pilot::fly(&person);
    Wizard::fly(&person);
    person.fly();
}
```

リスト 19-18：どのトレイトの`fly`メソッドを呼び出したいかを指定する

メソッド名の前にトレイト名を指定することで、Rust にどの`fly`の実装を呼び出したいのかを明確にします。また、`Human::fly(&person)`と書くこともできます。これは、リスト 19-18 で使用した`person.fly()`に相当しますが、曖昧さを解消する必要がない場合は、こちらの方が書くのが少し長くなります。

このコードを実行すると、以下が表示されます。

    This is your captain speaking.
    Up!
    *waving arms furiously*

`fly`メソッドは`self`パラメータを取るため、2 つの*型*が両方とも 1 つの*トレイト*を実装している場合、Rust は`self`の型に基づいてどのトレイトの実装を使用するかを判断することができます。

ただし、メソッドではない関連関数には`self`パラメータがありません。同じ関数名を持つ非メソッド関数を定義する複数の型またはトレイトがある場合、Rust は完全修飾構文を使用しない限り、どの型を意味するのかを常に把握できません。たとえば、リスト 19-19 では、すべての子犬に Spot という名前を付ける動物愛護施設用のトレイトを作成しています。`Animal`という名前のトレイトを作成し、関連する非メソッド関数`baby_name`を定義しています。`Animal`トレイトは、`baby_name`という関連非メソッド関数も直接提供する`Dog`構造体に対して実装されています。

ファイル名：`src/main.rs`

```rust
trait Animal {
    fn baby_name() -> String;
}

struct Dog;

impl Dog {
    fn baby_name() -> String {
        String::from("Spot")
    }
}

impl Animal for Dog {
    fn baby_name() -> String {
        String::from("puppy")
    }
}

fn main() {
    println!("A baby dog is called a {}", Dog::baby_name());
}
```

リスト 19-19：関連関数を持つトレイトと、同じ名前の関連関数を持ち、トレイトも実装する型

子犬すべてに Spot という名前を付けるコードは、`Dog`に定義されている`baby_name`関連関数で実装されています。`Dog`型はまた、すべての動物が持つ特性を表す`Animal`トレイトを実装しています。子犬は子犬と呼ばれ、これは`Animal`トレイトの`baby_name`関数における`Dog`に対する`Animal`トレイトの実装で表現されています。

`main`では、`Dog::baby_name`関数を呼び出しており、これは`Dog`に定義されている関連関数を直接呼び出します。このコードは以下を表示します。

```rust
A baby dog is called a Spot
```

この出力は私たちが望んだものではありません。私たちは、`Dog`に対して実装した`Animal`トレイトの一部である`baby_name`関数を呼び出したいので、コードは`A baby dog is called a puppy`を表示するようにしたいと思います。リスト 19-18 で使用したトレイト名を指定する手法はここでは役に立ちません。`main`をリスト 19-20 のコードに変更すると、コンパイルエラーが発生します。

ファイル名：`src/main.rs`

```rust
fn main() {
    println!("A baby dog is called a {}", Animal::baby_name());
}
```

リスト 19-20：`Animal`トレイトの`baby_name`関数を呼び出そうとしますが、Rust はどの実装を使用するかを判断できません

`Animal::baby_name`には`self`パラメータがないため、`Animal`トレイトを実装する他の型がある可能性があり、Rust は`Animal::baby_name`のどの実装を私たちが望んでいるのかを判断することができません。このコンパイラエラーが表示されます。

```bash
error[E0283]: type annotations needed
  --> src/main.rs:20:43
   |
20 |     println!("A baby dog is called a {}", Animal::baby_name());
   |                                           ^^^^^^^^^^^^^^^^^ cannot infer
type
   |
   = note: cannot satisfy `_: Animal`
```

曖昧さを解消し、Rust に、他の型に対する`Animal`の実装とは対照的に、`Dog`に対する`Animal`の実装を使用したいことを伝えるには、完全修飾構文を使用する必要があります。リスト 19-21 に、完全修飾構文の使い方を示します。

ファイル名：`src/main.rs`

```rust
fn main() {
    println!(
        "A baby dog is called a {}",
        <Dog as Animal>::baby_name()
    );
}
```

リスト 19-21：`Dog`に対して実装された`Animal`トレイトの`baby_name`関数を呼び出したいことを指定するための完全修飾構文の使用

角括弧内に型注釈を提供することで、Rust に対して、この関数呼び出しにおいて`Dog`型を`Animal`として扱うことで、`Dog`に対して実装された`Animal`トレイトの`baby_name`メソッドを呼び出したいことを伝えています。このコードは、私たちが望む出力を表示します。

```rust
A baby dog is called a puppy
```

一般的に、完全修飾構文は以下のように定義されます。

```rust
<Type as Trait>::function(receiver_if_method, next_arg,...);
```

メソッドではない関連関数の場合、`receiver`はありません。他の引数のリストのみがあります。関数またはメソッドを呼び出すすべての場所で完全修飾構文を使用することができます。ただし、Rust がプログラムの他の情報から把握できる構文の任意の部分を省略することが許されています。同じ名前を使用する複数の実装があり、Rust がどの実装を呼び出したいのかを特定するのに助けが必要な場合にのみ、このより冗長な構文を使用する必要があります。
