# 関連付けられた関数とメソッド

一部の関数は特定の型に関連付けられています。これらは 2 つの形式があります。関連付けられた関数とメソッドです。関連付けられた関数は、一般的に型に定義された関数であり、メソッドは型の特定のインスタンスに対して呼び出される関連付けられた関数です。

```rust
struct Point {
    x: f64,
    y: f64,
}

// 実装ブロック、すべての `Point` 関連付けられた関数とメソッドはここに入ります
impl Point {
    // これは「関連付けられた関数」です。この関数は特定の型、つまり `Point` に関連付けられています。
    //
    // 関連付けられた関数はインスタンスで呼び出す必要はありません。
    // これらの関数は一般的にコンストラクタのように使われます。
    fn origin() -> Point {
        Point { x: 0.0, y: 0.0 }
    }

    // もう一つの関連付けられた関数で、2 つの引数を取ります。
    fn new(x: f64, y: f64) -> Point {
        Point { x: x, y: y }
    }
}

struct Rectangle {
    p1: Point,
    p2: Point,
}

impl Rectangle {
    // これはメソッドです
    // `&self` は `self: &Self` のシュガーで、`Self` は呼び出し元オブジェクトの型です。この場合 `Self` = `Rectangle`
    fn area(&self) -> f64 {
        // `self` を使ってドット演算子で構造体のフィールドにアクセスできます
        let Point { x: x1, y: y1 } = self.p1;
        let Point { x: x2, y: y2 } = self.p2;

        // `abs` は `f64` のメソッドで、呼び出し元の絶対値を返します
        ((x1 - x2) * (y1 - y2)).abs()
    }

    fn perimeter(&self) -> f64 {
        let Point { x: x1, y: y1 } = self.p1;
        let Point { x: x2, y: y2 } = self.p2;

        2.0 * ((x1 - x2).abs() + (y1 - y2).abs())
    }

    // このメソッドは呼び出し元オブジェクトが可変である必要があります
    // `&mut self` は `self: &mut Self` に展開されます
    fn translate(&mut self, x: f64, y: f64) {
        self.p1.x += x;
        self.p2.x += x;

        self.p1.y += y;
        self.p2.y += y;
    }
}

// `Pair` はリソースを所有しています。ヒープ上に割り当てられた 2 つの整数
struct Pair(Box<i32>, Box<i32>);

impl Pair {
    // このメソッドは呼び出し元オブジェクトのリソースを「消費」します
    // `self` は `self: Self` に展開されます
    fn destroy(self) {
        // `self` を分解します
        let Pair(first, second) = self;

        println!("Destroying Pair({}, {})", first, second);

        // `first` と `second` はスコープ外になり、解放されます
    }
}

fn main() {
    let rectangle = Rectangle {
        // 関連付けられた関数はダブルコロンを使って呼び出されます
        p1: Point::origin(),
        p2: Point::new(3.0, 4.0),
    };

    // メソッドはドット演算子を使って呼び出されます
    // 最初の引数 `&self` は暗黙的に渡されます。つまり、
    // `rectangle.perimeter()` === `Rectangle::perimeter(&rectangle)`
    println!("Rectangle perimeter: {}", rectangle.perimeter());
    println!("Rectangle area: {}", rectangle.area());

    let mut square = Rectangle {
        p1: Point::origin(),
        p2: Point::new(1.0, 1.0),
    };

    // エラー！`rectangle` は不変ですが、このメソッドは可変オブジェクトが必要です
    //rectangle.translate(1.0, 0.0);
    // TODO ^ この行のコメントを外してみてください

    // 大丈夫！可変オブジェクトは可変メソッドを呼び出せます
    square.translate(1.0, 1.0);

    let pair = Pair(Box::new(1), Box::new(2));

    pair.destroy();

    // エラー！前の `destroy` 呼び出しで `pair` が「消費」されました
    //pair.destroy();
    // TODO ^ この行のコメントを外してみてください
}
```
