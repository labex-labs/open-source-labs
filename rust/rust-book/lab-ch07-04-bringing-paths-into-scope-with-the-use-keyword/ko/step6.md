# 중첩 경로를 사용하여 큰 `use` 목록 정리하기

동일한 크레이트 또는 동일한 모듈에 정의된 여러 항목을 사용하는 경우, 각 항목을 별도의 줄에 나열하면 파일에서 많은 수직 공간을 차지할 수 있습니다. 예를 들어, Listing 2-4 의 추측 게임에서 사용했던 다음 두 개의 `use` 문은 `std`에서 항목을 범위로 가져옵니다.

파일 이름: `src/main.rs`

```rust
--snip--
use std::cmp::Ordering;
use std::io;
--snip--
```

대신, 중첩 경로를 사용하여 동일한 항목을 한 줄로 범위로 가져올 수 있습니다. 이렇게 하려면 경로의 공통 부분을 지정한 다음 콜론 두 개를 입력하고, Listing 7-18 에 표시된 것처럼 경로의 다른 부분 목록을 중괄호로 묶습니다.

파일 이름: `src/main.rs`

```rust
--snip--
use std::{cmp::Ordering, io};
--snip--
```

Listing 7-18: 동일한 접두사를 가진 여러 항목을 범위로 가져오기 위해 중첩 경로 지정

더 큰 프로그램에서는 중첩 경로를 사용하여 동일한 크레이트 또는 모듈에서 많은 항목을 범위로 가져오면 필요한 별도의 `use` 문의 수를 크게 줄일 수 있습니다!

경로의 모든 수준에서 중첩 경로를 사용할 수 있으며, 이는 하위 경로를 공유하는 두 개의 `use` 문을 결합할 때 유용합니다. 예를 들어, Listing 7-19 는 두 개의 `use` 문을 보여줍니다. 하나는 `std::io`를 범위로 가져오고 다른 하나는 `std::io::Write`를 범위로 가져옵니다.

파일 이름: `src/lib.rs`

```rust
use std::io;
use std::io::Write;
```

Listing 7-19: 하나가 다른 하나의 하위 경로인 두 개의 `use` 문

이 두 경로의 공통 부분은 `std::io`이며, 이는 첫 번째 경로를 완성합니다. 이 두 경로를 하나의 `use` 문으로 병합하려면 Listing 7-20 에 표시된 것처럼 중첩 경로에서 `self`를 사용할 수 있습니다.

파일 이름: `src/lib.rs`

```rust
use std::io::{self, Write};
```

Listing 7-20: Listing 7-19 의 경로를 하나의 `use` 문으로 결합

이 줄은 `std::io`와 `std::io::Write`를 범위로 가져옵니다.
