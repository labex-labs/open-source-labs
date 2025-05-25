# 트레이트를 구현하는 타입 반환하기

또한 반환 위치에서 `impl Trait` 구문을 사용하여 트레이트를 구현하는 특정 타입의 값을 반환할 수 있습니다. 다음은 그 예입니다.

```rust
fn returns_summarizable() -> impl Summary {
    Tweet {
        username: String::from("horse_ebooks"),
        content: String::from(
            "of course, as you probably already know, people",
        ),
        reply: false,
        retweet: false,
    }
}
```

반환 타입으로 `impl Summary`를 사용함으로써, `returns_summarizable` 함수가 구체적인 타입을 명시하지 않고 `Summary` 트레이트를 구현하는 어떤 타입을 반환한다고 지정합니다. 이 경우, `returns_summarizable`는 `Tweet`을 반환하지만, 이 함수를 호출하는 코드는 그것을 알 필요가 없습니다.

트레이트만으로 반환 타입을 지정하는 기능은 13 장에서 다루는 클로저 (closures) 와 이터레이터 (iterators) 의 맥락에서 특히 유용합니다. 클로저와 이터레이터는 컴파일러만 알고 있거나, 지정하기에 매우 긴 타입을 생성합니다. `impl Trait` 구문을 사용하면 매우 긴 타입을 작성할 필요 없이 함수가 `Iterator` 트레이트를 구현하는 어떤 타입을 반환한다고 간결하게 지정할 수 있습니다.

그러나, 단일 타입만 반환하는 경우에만 `impl Trait`를 사용할 수 있습니다. 예를 들어, `NewsArticle` 또는 `Tweet` 중 하나를 반환하고 반환 타입을 `impl Summary`로 지정하는 다음 코드는 작동하지 않습니다.

```rust
fn returns_summarizable(switch: bool) -> impl Summary {
    if switch {
        NewsArticle {
            headline: String::from(
                "Penguins win the Stanley Cup Championship!",
            ),
            location: String::from("Pittsburgh, PA, USA"),
            author: String::from("Iceburgh"),
            content: String::from(
                "The Pittsburgh Penguins once again are the best \
                 hockey team in the NHL.",
            ),
        }
    } else {
        Tweet {
            username: String::from("horse_ebooks"),
            content: String::from(
                "of course, as you probably already know, people",
            ),
            reply: false,
            retweet: false,
        }
    }
}
```

`NewsArticle` 또는 `Tweet` 중 하나를 반환하는 것은 `impl Trait` 구문이 컴파일러에서 구현되는 방식과 관련된 제한 사항 때문에 허용되지 않습니다. "다양한 타입의 값을 허용하는 트레이트 객체 사용하기"에서 이 동작을 가진 함수를 작성하는 방법을 다룰 것입니다.
