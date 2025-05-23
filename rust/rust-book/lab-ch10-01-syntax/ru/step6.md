# В определениях методов

Мы можем реализовывать методы на структурах и перечислениях (как мы это делали в главе 5), и также использовать обобщенные типы в их определениях. Listing 10-9 показывает структуру `Point<T>`, которую мы определили в Listing 10-6, с методом под названием `x`, реализованным на ней.

Filename: `src/main.rs`

```rust
struct Point<T> {
    x: T,
    y: T,
}

impl<T> Point<T> {
    fn x(&self) -> &T {
        &self.x
    }
}

fn main() {
    let p = Point { x: 5, y: 10 };

    println!("p.x = {}", p.x());
}
```

Listing 10-9: Реализация метода под названием `x` на структуре `Point<T>`, который возвращает ссылку на поле `x` типа `T`

Здесь мы определили метод с именем `x` на `Point<T>`, который возвращает ссылку на данные в поле `x`.

Обратите внимание, что мы должны объявить `T` сразу после `impl`, чтобы мы могли использовать `T` для указания того, что мы реализуем методы для типа `Point<T>`. Объявляя `T` как обобщенный тип после `impl`, Rust может определить, что тип в угловых скобках в `Point` является обобщенным типом, а не конкретным типом. Мы могли бы выбрать другое имя для этого обобщенного параметра, чем обобщенный параметр, объявленный в определении структуры, но использование одного и того же имени является стандартным. Методы, написанные внутри `impl`, который объявляет обобщенный тип, будут определены для любого экземпляра типа, независимо от того, какой конкретный тип окажется подстановкой для обобщенного типа.

Мы также можем задавать ограничения для обобщенных типов при определении методов для типа. Например, мы могли бы реализовать методы только для экземпляров `Point<f32>`, а не для экземпляров `Point<T>` с любым обобщенным типом. В Listing 10-10 мы используем конкретный тип `f32`, что означает, что мы не объявляем никаких типов после `impl`.

Filename: `src/main.rs`

```rust
impl Point<f32> {
    fn distance_from_origin(&self) -> f32 {
        (self.x.powi(2) + self.y.powi(2)).sqrt()
    }
}
```

Listing 10-10: Блок `impl`, который применяется только к структуре с конкретным типом для обобщенного параметра типа `T`

Этот код означает, что тип `Point<f32>` будет иметь метод `distance_from_origin`; другие экземпляры `Point<T>`, где `T` не является типом `f32`, не будут иметь этого метода определённого. Метод измеряет расстояние от нашей точки до точки с координатами (0.0, 0.0) и использует математические операции, доступные только для вещественных типов.

Обобщенные параметры типа в определении структуры не всегда совпадают с теми, которые вы используете в сигнатурах методов той же структуры. Listing 10-11 использует обобщенные типы `X1` и `Y1` для структуры `Point` и `X2` `Y2` для сигнатуры метода `mixup`, чтобы сделать пример более понятным. Метод создает новый экземпляр `Point` с значением `x` из `self` `Point` (типа `X1`) и значением `y` из переданного `Point` (типа `Y2`).

Filename: `src/main.rs`

```rust
struct Point<X1, Y1> {
    x: X1,
    y: Y1,
}

1 impl<X1, Y1> Point<X1, Y1> {
  2 fn mixup<X2, Y2>(
        self,
        other: Point<X2, Y2>,
    ) -> Point<X1, Y2> {
        Point {
            x: self.x,
            y: other.y,
        }
    }
}

fn main() {
  3 let p1 = Point { x: 5, y: 10.4 };
  4 let p2 = Point { x: "Hello", y: 'c' };

  5 let p3 = p1.mixup(p2);

  6 println!("p3.x = {}, p3.y = {}", p3.x, p3.y);
}
```

Listing 10-11: Метод, который использует обобщенные типы, отличающиеся от определения его структуры

В `main` мы определили `Point`, который имеет `i32` для `x` (со значением `5`) и `f64` для `y` (со значением `10.4` \[3\]). Переменная `p2` является структурой `Point`, которая имеет строку - срез для `x` (со значением `"Hello"`) и `char` для `y` (со значением `c` \[4\]). Вызов `mixup` для `p1` с аргументом `p2` даёт нам `p3` \[5\], который будет иметь `i32` для `x`, потому что `x` взялось из `p1`. Переменная `p3` будет иметь `char` для `y`, потому что `y` взялось из `p2`. Вызов макроса `println!` \[6\] выведет `p3.x = 5, p3.y = c`.

Цель этого примера — показать ситуацию, в которой некоторые обобщенные параметры объявляются с `impl`, а некоторые с определением метода. Здесь обобщенные параметры `X1` и `Y1` объявляются после `impl` \[1\], потому что они связаны с определением структуры. Обобщенные параметры `X2` и `Y2` объявляются после `fn mixup` \[2\], потому что они имеют отношение только к методу.
