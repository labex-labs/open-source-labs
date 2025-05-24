# 지속 시간 형식 지정

주어진 밀리초 숫자를 사람이 읽을 수 있는 형식으로 얻으려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `ms`를 적절한 값으로 나누어 `day`, `hour`, `minute`, `second`, `millisecond`에 대한 적절한 값을 얻습니다.
3. `Object.entries()`와 `Array.prototype.filter()`를 사용하여 0 이 아닌 값만 유지합니다.
4. `Array.prototype.map()`을 사용하여 각 값에 대한 문자열을 생성하고 적절하게 복수형으로 만듭니다.
5. `Array.prototype.join()`을 사용하여 값을 문자열로 결합합니다.

다음은 코드입니다.

```js
const formatDuration = (ms) => {
  if (ms < 0) ms = -ms;
  const time = {
    day: Math.floor(ms / 86400000),
    hour: Math.floor(ms / 3600000) % 24,
    minute: Math.floor(ms / 60000) % 60,
    second: Math.floor(ms / 1000) % 60,
    millisecond: Math.floor(ms) % 1000
  };
  return Object.entries(time)
    .filter((val) => val[1] !== 0)
    .map(([key, val]) => `${val} ${key}${val !== 1 ? "s" : ""}`)
    .join(", ");
};
```

다음은 몇 가지 예입니다.

```js
formatDuration(1001); // '1 second, 1 millisecond'
formatDuration(34325055574);
// '397 days, 6 hours, 44 minutes, 15 seconds, 574 milliseconds'
```
