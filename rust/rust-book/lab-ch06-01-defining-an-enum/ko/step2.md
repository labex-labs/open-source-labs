# Enum 값

`IpAddrKind`의 두 가지 변형 각각의 인스턴스를 다음과 같이 생성할 수 있습니다.

```rust
let four = IpAddrKind::V4;
let six = IpAddrKind::V6;
```

enum 의 변형은 해당 식별자 아래에 네임스페이스화되며, 두 값을 구분하기 위해 이중 콜론을 사용합니다. 이는 `IpAddrKind::V4`와 `IpAddrKind::V6`의 두 값 모두 동일한 유형인 `IpAddrKind`이기 때문에 유용합니다. 예를 들어, 모든 `IpAddrKind`를 받는 함수를 정의할 수 있습니다.

```rust
fn route(ip_kind: IpAddrKind) {}
```

그리고 이 함수를 두 변형 중 하나로 호출할 수 있습니다.

```rust
route(IpAddrKind::V4);
route(IpAddrKind::V6);
```

enum 을 사용하면 더 많은 이점이 있습니다. IP 주소 유형에 대해 더 생각해보면, 현재 실제 IP 주소 *데이터*를 저장할 방법이 없습니다. 우리는 단지 그것이 어떤 *종류*인지 알고 있을 뿐입니다. 5 장에서 구조체에 대해 배웠다는 점을 감안할 때, Listing 6-1 에 표시된 것처럼 구조체로 이 문제를 해결하고 싶을 수 있습니다.

```rust
1 enum IpAddrKind {
    V4,
    V6,
}

2 struct IpAddr {
  3 kind: IpAddrKind,
  4 address: String,
}

5 let home = IpAddr {
    kind: IpAddrKind::V4,
    address: String::from("127.0.0.1"),
};

6 let loopback = IpAddr {
    kind: IpAddrKind::V6,
    address: String::from("::1"),
};
```

Listing 6-1: `struct`를 사용하여 IP 주소의 데이터와 `IpAddrKind` 변형을 저장

여기서, 두 개의 필드를 가진 구조체 `IpAddr` \[2]를 정의했습니다. `IpAddrKind` 유형 (이전에 정의한 enum \[1]) 의 `kind` 필드 \[3]와 `String` 유형의 `address` 필드 \[4]입니다. 이 구조체의 두 인스턴스가 있습니다. 첫 번째는 `home` \[5]이며, `127.0.0.1`의 관련 주소 데이터와 함께 `IpAddrKind::V4` 값을 `kind`로 갖습니다. 두 번째 인스턴스는 `loopback` \[6]입니다. `kind` 값으로 `IpAddrKind`의 다른 변형인 `V6`을 가지며, `::1` 주소가 연결되어 있습니다. `kind`와 `address` 값을 함께 묶기 위해 구조체를 사용했으므로 이제 변형이 값과 연결됩니다.

그러나 enum 만 사용하여 동일한 개념을 표현하는 것이 더 간결합니다. 구조체 내부의 enum 대신, 각 enum 변형에 직접 데이터를 넣을 수 있습니다. `IpAddr` enum 의 이 새로운 정의는 `V4`와 `V6` 변형 모두 관련 `String` 값을 갖는다고 말합니다.

```rust
enum IpAddr {
    V4(String),
    V6(String),
}

let home = IpAddr::V4(String::from("127.0.0.1"));

let loopback = IpAddr::V6(String::from("::1"));
```

enum 의 각 변형에 데이터를 직접 연결하므로 추가 구조체가 필요하지 않습니다. 여기서 enum 이 작동하는 방식의 또 다른 세부 사항을 쉽게 볼 수 있습니다. 우리가 정의하는 각 enum 변형의 이름은 enum 의 인스턴스를 생성하는 함수가 됩니다. 즉, `IpAddr::V4()`는 `String` 인수를 받아 `IpAddr` 유형의 인스턴스를 반환하는 함수 호출입니다. enum 을 정의한 결과로 이 생성자 함수를 자동으로 얻습니다.

구조체 대신 enum 을 사용하는 또 다른 장점이 있습니다. 각 변형은 서로 다른 유형과 양의 관련 데이터를 가질 수 있습니다. 버전 4 IP 주소는 항상 0 에서 255 사이의 값을 갖는 4 개의 숫자 구성 요소를 갖습니다. `V4` 주소를 4 개의 `u8` 값으로 저장하고 `V6` 주소를 하나의 `String` 값으로 표현하고 싶다면, 구조체로는 할 수 없습니다. enum 은 이 경우를 쉽게 처리합니다.

```rust
enum IpAddr {
    V4(u8, u8, u8, u8),
    V6(String),
}

let home = IpAddr::V4(127, 0, 0, 1);

let loopback = IpAddr::V6(String::from("::1"));
```

버전 4 및 버전 6 IP 주소를 저장하기 위해 데이터 구조를 정의하는 몇 가지 다른 방법을 보여주었습니다. 그러나, IP 주소를 저장하고 어떤 종류인지 인코딩하려는 것은 매우 일반적이어서 표준 라이브러리에 사용할 수 있는 정의가 있습니다! 표준 라이브러리가 `IpAddr`를 정의하는 방식을 살펴보겠습니다. 우리가 정의하고 사용한 정확한 enum 과 변형을 가지고 있지만, 각 변형에 대해 다르게 정의된 두 개의 다른 구조체 형태로 변형 내부에 주소 데이터를 포함합니다.

```rust
struct Ipv4Addr {
    --snip--
}

struct Ipv6Addr {
    --snip--
}

enum IpAddr {
    V4(Ipv4Addr),
    V6(Ipv6Addr),
}
```

이 코드는 문자열, 숫자 유형 또는 구조체와 같이 enum 변형 내부에 모든 종류의 데이터를 넣을 수 있음을 보여줍니다. 다른 enum 을 포함할 수도 있습니다! 또한 표준 라이브러리 유형은 여러분이 생각해낼 수 있는 것보다 훨씬 더 복잡하지 않은 경우가 많습니다.

표준 라이브러리에 `IpAddr`에 대한 정의가 포함되어 있더라도, 표준 라이브러리의 정의를 범위로 가져오지 않았으므로 충돌 없이 자체 정의를 만들고 사용할 수 있습니다. 7 장에서 유형을 범위로 가져오는 것에 대해 더 자세히 이야기하겠습니다.

Listing 6-2 에서 enum 의 또 다른 예를 살펴보겠습니다. 이 예는 변형에 다양한 유형이 포함되어 있습니다.

```rust
enum Message {
    Quit,
    Move { x: i32, y: i32 },
    Write(String),
    ChangeColor(i32, i32, i32),
}
```

Listing 6-2: 각 변형이 서로 다른 양과 유형의 값을 저장하는 `Message` enum

이 enum 에는 서로 다른 유형의 네 가지 변형이 있습니다.

- `Quit`에는 관련 데이터가 전혀 없습니다.
- `Move`는 구조체와 같이 명명된 필드를 갖습니다.
- `Write`는 단일 `String`을 포함합니다.
- `ChangeColor`는 세 개의 `i32` 값을 포함합니다.

Listing 6-2 와 같은 변형으로 enum 을 정의하는 것은 서로 다른 종류의 구조체 정의를 정의하는 것과 유사하지만, enum 은 `struct` 키워드를 사용하지 않고 모든 변형이 `Message` 유형 아래에 함께 그룹화됩니다. 다음 구조체는 앞의 enum 변형이 보유하는 것과 동일한 데이터를 보유할 수 있습니다.

```rust
struct QuitMessage; // unit struct
struct MoveMessage {
    x: i32,
    y: i32,
}
struct WriteMessage(String); // tuple struct
struct ChangeColorMessage(i32, i32, i32); // tuple struct
```

그러나 서로 다른 구조체를 사용하면 각 구조체는 자체 유형을 가지므로, 단일 유형인 Listing 6-2 에 정의된 `Message` enum 을 사용했을 때만큼 쉽게 이러한 종류의 메시지를 모두 받을 함수를 정의할 수 없습니다.

enum 과 구조체 사이에는 한 가지 더 유사점이 있습니다. `impl`을 사용하여 구조체에 메서드를 정의할 수 있는 것처럼, enum 에도 메서드를 정의할 수 있습니다. 다음은 `Message` enum 에 정의할 수 있는 `call`이라는 메서드입니다.

```rust
impl Message {
    fn call(&self) {
      1 // method body would be defined here
    }
}

2 let m = Message::Write(String::from("hello"));
m.call();
```

메서드의 본문은 `self`를 사용하여 메서드를 호출한 값을 가져옵니다. 이 예에서는 `Message::Write(String::from("hello"))` 값을 갖는 변수 `m` \[2]을 만들었으며, `m.call()`이 실행될 때 `call` 메서드 \[1]의 본문에서 `self`가 됩니다.

표준 라이브러리에서 매우 일반적이고 유용한 또 다른 enum 인 `Option`을 살펴보겠습니다.
