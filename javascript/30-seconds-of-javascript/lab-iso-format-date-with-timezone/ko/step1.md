# 시간대를 포함한 날짜를 ISO 형식으로 변환하기

시간대 오프셋을 포함하여 날짜를 확장된 ISO 형식 (ISO 8601) 으로 변환하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩을 시작합니다.
2. `Date.prototype.getTimezoneOffset()`을 사용하여 시간대 오프셋을 얻고 반전시킵니다. 부호를 `diff`에 저장합니다.
3. `Math.floor()` 및 `Math.abs()`를 사용하여 전달된 모든 숫자를 정수로 정규화하고 `String.prototype.padStart()`를 사용하여 `2`자리로 채우는 도우미 함수 `pad()`를 정의합니다.
4. `pad()`와 `Date` 프로토타입의 내장 메서드를 사용하여 시간대 오프셋이 있는 ISO 8601 문자열을 구성합니다.

다음은 사용할 수 있는 코드입니다.

```js
const toISOStringWithTimezone = (date) => {
  const tzOffset = -date.getTimezoneOffset();
  const diff = tzOffset >= 0 ? "+" : "-";
  const pad = (n) => `${Math.floor(Math.abs(n))}`.padStart(2, "0");
  return (
    date.getFullYear() +
    "-" +
    pad(date.getMonth() + 1) +
    "-" +
    pad(date.getDate()) +
    "T" +
    pad(date.getHours()) +
    ":" +
    pad(date.getMinutes()) +
    ":" +
    pad(date.getSeconds()) +
    diff +
    pad(tzOffset / 60) +
    ":" +
    pad(tzOffset % 60)
  );
};
```

`toISOStringWithTimezone()` 함수를 `new Date()` 객체를 인수로 사용하여 시간대 오프셋이 있는 ISO 형식으로 날짜를 얻습니다. 예를 들어:

```js
toISOStringWithTimezone(new Date()); // '2020-10-06T20:43:33-04:00'
```
