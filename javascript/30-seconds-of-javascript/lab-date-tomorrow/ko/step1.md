# 내일 날짜 얻기

코딩 연습을 위해, 터미널/SSH 를 열고 `node`를 입력하여 시작할 수 있습니다. 이렇게 하면 다음 단계에 따라 내일의 날짜를 얻을 수 있습니다.

1. `Date` 생성자 (constructor) 를 사용하여 현재 날짜를 가져옵니다.
2. `Date.prototype.getDate()`를 사용하여 하루를 더합니다.
3. `Date.prototype.setDate()`를 사용하여 결과를 설정합니다.
4. `Date.prototype.toISOString()`를 사용하여 `yyyy-mm-dd` 형식의 문자열을 반환합니다.

다음은 사용할 수 있는 코드입니다.

```js
const tomorrow = () => {
  let currentDate = new Date();
  currentDate.setDate(currentDate.getDate() + 1);
  return currentDate.toISOString().split("T")[0];
};
```

이 코드를 입력한 후, `tomorrow()` 함수를 호출하여 내일의 날짜를 얻을 수 있습니다. 예를 들어, 오늘 날짜가 2018-10-18 인 경우, 출력은 `2018-10-19`가 됩니다.
