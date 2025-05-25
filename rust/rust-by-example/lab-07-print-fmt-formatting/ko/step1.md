# 형식 지정 (Formatting)

형식 지정은 *형식 문자열 (format string)*을 통해 지정됩니다.

- `format!("{}", foo)` -\> `"3735928559"`
- `format!("0x{:X}", foo)` -\> `"0xDEADBEEF"`
- `format!("0o{:o}", foo)` -\> `"0o33653337357"`

동일한 변수 (`foo`) 는 어떤 *인수 유형 (argument type)*이 사용되는지에 따라 다르게 형식 지정될 수 있습니다: `X` vs `o` vs _지정되지 않음_.

이 형식 지정 기능은 트레이트 (traits) 를 통해 구현되며, 각 인수 유형에 대해 하나의 트레이트가 있습니다. 가장 일반적인 형식 지정 트레이트는 `Display`로, 인수 유형이 지정되지 않은 경우, 예를 들어 `{}`를 처리합니다.

```rust
use std::fmt::{self, Formatter, Display};

struct City {
    name: &'static str,
    // Latitude
    lat: f32,
    // Longitude
    lon: f32,
}

impl Display for City {
    // `f` is a buffer, and this method must write the formatted string into it.
    fn fmt(&self, f: &mut Formatter) -> fmt::Result {
        let lat_c = if self.lat >= 0.0 { 'N' } else { 'S' };
        let lon_c = if self.lon >= 0.0 { 'E' } else { 'W' };

        // `write!` is like `format!`, but it will write the formatted string
        // into a buffer (the first argument).
        write!(f, "{}: {:.3}°{} {:.3}°{}",
               self.name, self.lat.abs(), lat_c, self.lon.abs(), lon_c)
    }
}

#[derive(Debug)]
struct Color {
    red: u8,
    green: u8,
    blue: u8,
}

fn main() {
    for city in [
        City { name: "Dublin", lat: 53.347778, lon: -6.259722 },
        City { name: "Oslo", lat: 59.95, lon: 10.75 },
        City { name: "Vancouver", lat: 49.25, lon: -123.1 },
    ] {
        println!("{}", city);
    }
    for color in [
        Color { red: 128, green: 255, blue: 90 },
        Color { red: 0, green: 3, blue: 254 },
        Color { red: 0, green: 0, blue: 0 },
    ] {
        // Switch this to use {} once you've added an implementation
        // for fmt::Display.
        println!("{:?}", color);
    }
}
```

`std::fmt` 문서에서 형식 지정 트레이트와 해당 인수 유형의 전체 목록을 볼 수 있습니다.

## 활동

위의 `Color` 구조체에 대해 `fmt::Display` 트레이트의 구현을 추가하여 출력이 다음과 같이 표시되도록 하십시오.

```plaintext
RGB (128, 255, 90) 0x80FF5A
RGB (0, 3, 254) 0x0003FE
RGB (0, 0, 0) 0x000000
```

막히는 경우 세 가지 힌트:

- RGB 색상 공간에서 색상을 계산하는 공식은 다음과 같습니다: `RGB = (R*65536)+(G*256)+B , (when R is RED, G is GREEN and B is BLUE)`. 자세한 내용은 RGB 색상 형식 및 계산을 참조하십시오.
- 각 색상을 두 번 이상 나열해야 할 수 있습니다.
- `:0>2`를 사용하여 너비 2 로 0 을 채울 수 있습니다.
