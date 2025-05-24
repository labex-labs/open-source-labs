# Date 객체에서 콜론으로 구분된 시간을 얻는 방법

코딩 연습을 하고 싶다면 터미널/SSH 를 열고 `node`를 입력하여 시작할 수 있습니다.

이 함수는 주어진 `Date` 객체에서 `HH:MM:SS` 형식의 문자열을 반환합니다.

이를 위해 `Date.prototype.toTimeString()` 및 `String.prototype.slice()` 메서드를 사용하여 `Date` 객체의 `HH:MM:SS` 부분을 추출합니다.

다음은 해당 함수의 코드입니다.

```js
const getColonTimeFromDate = (date) => date.toTimeString().slice(0, 8);
```

다음은 사용 예시입니다.

```js
getColonTimeFromDate(new Date()); // '08:38:00'
```
