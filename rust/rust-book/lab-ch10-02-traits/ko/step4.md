# 기본 구현

때로는 모든 타입의 모든 메서드에 대한 구현을 요구하는 대신, 트레이트의 일부 또는 모든 메서드에 대한 기본 동작을 갖는 것이 유용합니다. 그런 다음, 특정 타입에 트레이트를 구현할 때 각 메서드의 기본 동작을 유지하거나 재정의할 수 있습니다.

Listing 10-14 에서, Listing 10-12 에서 했던 것처럼 메서드 시그니처만 정의하는 대신, `Summary` 트레이트의 `summarize` 메서드에 대한 기본 문자열을 지정합니다.

파일 이름: `src/lib.rs`

```rust
pub trait Summary {
    fn summarize(&self) -> String {
        String::from("(Read more...)")
    }
}
```

Listing 10-14: `summarize` 메서드의 기본 구현이 있는 `Summary` 트레이트 정의

`NewsArticle`의 인스턴스를 요약하기 위해 기본 구현을 사용하려면, `impl Summary for NewsArticle {}`로 빈 `impl` 블록을 지정합니다.

더 이상 `NewsArticle`에서 `summarize` 메서드를 직접 정의하지 않더라도, 기본 구현을 제공하고 `NewsArticle`이 `Summary` 트레이트를 구현하도록 지정했습니다. 결과적으로, 다음과 같이 `NewsArticle`의 인스턴스에서 `summarize` 메서드를 계속 호출할 수 있습니다.

```rust
let article = NewsArticle {
    headline: String::from(
        "Penguins win the Stanley Cup Championship!"
    ),
    location: String::from("Pittsburgh, PA, USA"),
    author: String::from("Iceburgh"),
    content: String::from(
        "The Pittsburgh Penguins once again are the best \
         hockey team in the NHL.",
    ),
};

println!("New article available! {}", article.summarize());
```

이 코드는 `New article available! (Read more...)`를 출력합니다.

기본 구현을 생성하는 것은 Listing 10-13 에서 `Tweet`에 대한 `Summary`의 구현에 대해 아무것도 변경할 필요가 없습니다. 그 이유는 기본 구현을 재정의하는 구문이 기본 구현이 없는 트레이트 메서드를 구현하는 구문과 동일하기 때문입니다.

기본 구현은 동일한 트레이트의 다른 메서드를 호출할 수 있으며, 해당 다른 메서드가 기본 구현을 갖지 않더라도 마찬가지입니다. 이러한 방식으로, 트레이트는 많은 유용한 기능을 제공하고 구현자가 그 중 작은 부분만 지정하도록 요구할 수 있습니다. 예를 들어, 구현이 필요한 `summarize_author` 메서드를 갖도록 `Summary` 트레이트를 정의한 다음, `summarize_author` 메서드를 호출하는 기본 구현이 있는 `summarize` 메서드를 정의할 수 있습니다.

```rust
pub trait Summary {
    fn summarize_author(&self) -> String;

    fn summarize(&self) -> String {
        format!(
            "(Read more from {}...)",
            self.summarize_author()
        )
    }
}
```

이 버전의 `Summary`를 사용하려면, 타입에 트레이트를 구현할 때 `summarize_author`만 정의하면 됩니다.

```rust
impl Summary for Tweet {
    fn summarize_author(&self) -> String {
        format!("@{}", self.username)
    }
}
```

`summarize_author`를 정의한 후, `Tweet` 구조체의 인스턴스에서 `summarize`를 호출할 수 있으며, `summarize`의 기본 구현은 우리가 제공한 `summarize_author`의 정의를 호출합니다. `summarize_author`를 구현했으므로, `Summary` 트레이트는 더 이상 코드를 작성할 필요 없이 `summarize` 메서드의 동작을 제공했습니다. 다음은 그 모습입니다.

```rust
let tweet = Tweet {
    username: String::from("horse_ebooks"),
    content: String::from(
        "of course, as you probably already know, people",
    ),
    reply: false,
    retweet: false,
};

println!("1 new tweet: {}", tweet.summarize());
```

이 코드는 `1 new tweet: (Read more from @horse_ebooks...)`를 출력합니다.

해당 메서드의 재정의 구현에서 기본 구현을 호출하는 것은 불가능하다는 점에 유의하십시오.
