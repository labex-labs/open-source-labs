# Unix 타임스탬프로부터 Date 객체 생성 방법

Unix 타임스탬프로부터 `Date` 객체를 생성하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. 타임스탬프에 `1000`을 곱하여 밀리초로 변환합니다.
3. `Date` 생성자를 사용하여 새로운 `Date` 객체를 생성합니다.

다음은 예시 코드 조각입니다.

```js
const fromTimestamp = (timestamp) => new Date(timestamp * 1000);
```

이 함수를 사용하여 Unix 타임스탬프를 `Date` 객체로 변환할 수 있습니다.

```js
fromTimestamp(1602162242); // 2020-10-08T13:04:02.000Z
```
