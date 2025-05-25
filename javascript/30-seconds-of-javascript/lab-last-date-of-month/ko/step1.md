# 달의 마지막 날짜를 반환하는 함수

코딩을 시작하려면 터미널/SSH 를 열고 `node`를 입력하세요.

이 함수는 주어진 날짜에 대한 해당 달의 마지막 날짜를 반환합니다.

이를 위해 다음 단계를 따르세요:

1. `Date.prototype.getFullYear()` 및 `Date.prototype.getMonth()`를 사용하여 주어진 날짜에서 현재 연도와 월을 가져옵니다.
2. 주어진 연도와 월을 `1`만큼 증가시키고, 일을 `0`으로 설정하여 (이전 달의 마지막 날) 새로운 날짜를 생성합니다. 이 목적으로 `Date` 생성자를 사용할 수 있습니다.
3. 함수에 인수가 전달되지 않으면 기본적으로 현재 날짜를 사용합니다.
4. 달의 마지막 날짜를 날짜의 문자열 표현 형식으로 반환합니다.

다음은 해당 함수의 코드입니다:

```js
const getLastDateOfMonth = (date = new Date()) => {
  let lastDate = new Date(date.getFullYear(), date.getMonth() + 1, 0);
  return lastDate.toISOString().split("T")[0];
};
```

다음과 같이 날짜 객체로 함수를 호출하여 테스트할 수 있습니다:

```js
getLastDateOfMonth(new Date("2015-08-11")); // '2015-08-30'
```
