# JavaScript 에서 날짜로부터 Unix 타임스탬프 얻는 방법

코딩을 시작하려면 터미널/SSH 를 열고 `node`를 입력하십시오.

JavaScript 에서 `Date` 객체로부터 Unix 타임스탬프를 얻으려면 다음 단계를 사용할 수 있습니다.

1. `Date.prototype.getTime()`을 사용하여 밀리초 단위의 타임스탬프를 얻습니다.
2. 타임스탬프를 `1000`으로 나누어 초 단위의 타임스탬프를 얻습니다.
3. `Math.floor()`를 사용하여 결과 타임스탬프를 정수로 반올림합니다.
4. `date` 인수를 생략하면 현재 날짜가 사용됩니다.

다음은 예제 코드 조각입니다.

```js
const getTimestamp = (date = new Date()) => Math.floor(date.getTime() / 1000);
```

`getTimestamp()` 함수를 호출하여 Unix 타임스탬프를 얻을 수 있습니다. 예를 들어:

```js
getTimestamp(); // 1602162242
```
