# 초를 ISO 시간 형식으로 변환하는 함수

이 코드를 사용하려면 터미널/SSH 를 열고 `node`를 입력하십시오. 이 함수는 초 (seconds) 를 인수로 받아 ISO 시간 형식을 반환합니다. 작동 방식은 다음과 같습니다.

- 초를 적절한 값으로 나누어 `hour`, `minute`, `second`에 해당하는 값을 얻습니다.
- 결과 앞에 붙일 부호 (sign) 를 변수에 저장합니다.
- `Array.prototype.map()`을 `Math.floor()` 및 `String.prototype.padStart()`와 함께 사용하여 각 세그먼트를 문자열로 변환하고 형식화합니다.
- `Array.prototype.join()`을 사용하여 값을 문자열로 결합합니다.

다음은 코드입니다.

```js
const formatSeconds = (s) => {
  const [hour, minute, second, sign] =
    s > 0
      ? [s / 3600, (s / 60) % 60, s % 60, ""]
      : [-s / 3600, (-s / 60) % 60, -s % 60, "-"];

  return (
    sign +
    [hour, minute, second]
      .map((v) => `${Math.floor(v)}`.padStart(2, "0"))
      .join(":")
  );
};
```

다음 예제를 사용하여 함수를 테스트할 수 있습니다.

```js
formatSeconds(200); // '00:03:20'
formatSeconds(-200); // '-00:03:20'
formatSeconds(99999); // '27:46:39'
```
