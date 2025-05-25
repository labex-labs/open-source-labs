# 타입에 트레이트 구현하기

이제 `Summary` 트레이트의 메서드에 대한 원하는 시그니처를 정의했으므로, 미디어 집계기에 있는 타입에 이를 구현할 수 있습니다. Listing 10-13 은 헤드라인, 작성자 및 위치를 사용하여 `summarize`의 반환 값을 생성하는 `NewsArticle` 구조체에 대한 `Summary` 트레이트의 구현을 보여줍니다. `Tweet` 구조체의 경우, 트윗 내용이 이미 280 자로 제한되어 있다고 가정하여 `summarize`를 사용자 이름과 트윗의 전체 텍스트로 정의합니다.

파일 이름: `src/lib.rs`

```rust
pub struct NewsArticle {
    pub headline: String,
    pub location: String,
    pub author: String,
    pub content: String,
}

impl Summary for NewsArticle {
    fn summarize(&self) -> String {
        format!(
            "{}, by {} ({})",
            self.headline,
            self.author,
            self.location
        )
    }
}

pub struct Tweet {
    pub username: String,
    pub content: String,
    pub reply: bool,
    pub retweet: bool,
}

impl Summary for Tweet {
    fn summarize(&self) -> String {
        format!("{}: {}", self.username, self.content)
    }
}
```

Listing 10-13: `NewsArticle` 및 `Tweet` 타입에 `Summary` 트레이트 구현하기

타입에 트레이트를 구현하는 것은 일반 메서드를 구현하는 것과 유사합니다. 차이점은 `impl` 뒤에 구현하려는 트레이트 이름을 넣고, `for` 키워드를 사용한 다음, 트레이트를 구현하려는 타입의 이름을 지정한다는 것입니다. `impl` 블록 내에서 트레이트 정의가 정의한 메서드 시그니처를 넣습니다. 각 시그니처 뒤에 세미콜론을 추가하는 대신, 중괄호를 사용하고 트레이트의 메서드가 특정 타입에 대해 갖기를 원하는 특정 동작으로 메서드 본문을 채웁니다.

이제 라이브러리가 `NewsArticle` 및 `Tweet`에 `Summary` 트레이트를 구현했으므로, 크레이트 사용자는 일반 메서드를 호출하는 것과 동일한 방식으로 `NewsArticle` 및 `Tweet`의 인스턴스에서 트레이트 메서드를 호출할 수 있습니다. 유일한 차이점은 사용자가 트레이트와 타입을 모두 범위 내로 가져와야 한다는 것입니다. 다음은 바이너리 크레이트가 `aggregator` 라이브러리 크레이트를 사용하는 방법의 예입니다.

```rust
use aggregator::{Summary, Tweet};

fn main() {
    let tweet = Tweet {
        username: String::from("horse_ebooks"),
        content: String::from(
            "of course, as you probably already know, people",
        ),
        reply: false,
        retweet: false,
    };

    println!("1 new tweet: {}", tweet.summarize());
}
```

이 코드는 `1 new tweet: horse_ebooks: of course, as you probably already know, people`을 출력합니다.

`aggregator` 크레이트에 의존하는 다른 크레이트도 `Summary` 트레이트를 범위 내로 가져와 자체 타입에 `Summary`를 구현할 수 있습니다. 주목해야 할 한 가지 제한 사항은 트레이트 또는 타입, 또는 둘 다가 우리 크레이트에 로컬인 경우에만 타입에 트레이트를 구현할 수 있다는 것입니다. 예를 들어, `Tweet` 타입이 `aggregator` 크레이트에 로컬이기 때문에 `aggregator` 크레이트 기능의 일부로 `Tweet`과 같은 사용자 지정 타입에 `Display`와 같은 표준 라이브러리 트레이트를 구현할 수 있습니다. 또한 `Summary` 트레이트가 `aggregator` 크레이트에 로컬이기 때문에 `aggregator` 크레이트에서 `Vec<T>`에 `Summary`를 구현할 수 있습니다.

그러나 외부 타입에 외부 트레이트를 구현할 수는 없습니다. 예를 들어, `Display`와 `Vec<T>`가 모두 표준 라이브러리에 정의되어 있고 `aggregator` 크레이트에 로컬이 아니기 때문에 `aggregator` 크레이트 내에서 `Vec<T>`에 `Display` 트레이트를 구현할 수 없습니다. 이 제한 사항은 _coherence_(일관성) 라고 하는 속성의 일부이며, 더 구체적으로는 _orphan rule_(고아 규칙) 이라고 합니다. 이는 부모 타입이 존재하지 않기 때문에 그렇게 명명되었습니다. 이 규칙은 다른 사람의 코드가 여러분의 코드를 망가뜨릴 수 없고 그 반대의 경우도 마찬가지임을 보장합니다. 이 규칙이 없으면 두 크레이트가 동일한 타입에 대해 동일한 트레이트를 구현할 수 있으며, Rust 는 어떤 구현을 사용해야 할지 알 수 없습니다.
