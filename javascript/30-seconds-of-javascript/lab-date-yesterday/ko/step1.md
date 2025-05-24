# yyyy-mm-dd 형식으로 어제의 날짜 가져오기

`yyyy-mm-dd` 형식으로 어제의 날짜를 가져오려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `Date` 생성자 (constructor) 를 사용하여 현재 날짜를 가져옵니다.
3. `Date.prototype.getDate()`를 사용하여 날짜를 하루 줄입니다.
4. `Date.prototype.setDate()`를 사용하여 줄어든 날짜를 설정합니다.
5. `Date.prototype.toISOString()`를 사용하여 `yyyy-mm-dd` 형식의 문자열을 반환합니다.
6. `yesterday()` 함수를 호출하여 어제의 날짜를 가져옵니다.

```js
const yesterday = () => {
  let d = new Date();
  d.setDate(d.getDate() - 1);
  return d.toISOString().split("T")[0];
};

yesterday(); // returns "2018-10-17" (if current date is 2018-10-18)
```

이 단계를 따르면 어제의 날짜를 명확하고 간결하게 검색할 수 있습니다.
