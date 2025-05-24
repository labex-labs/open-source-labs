# JavaScript 함수를 사용하여 해당 월의 날짜 수 구하기

JavaScript 를 사용하여 주어진 연도의 특정 달에 며칠이 있는지 찾으려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `year`와 `month`의 두 가지 매개변수를 사용하는 `daysInMonth`라는 함수를 만듭니다.
3. `daysInMonth` 함수 내부에서 `Date` 생성자를 사용하여 주어진 `year`와 `month`로부터 날짜 객체를 생성합니다.
4. 월이 0 부터 시작하므로, 이전 달의 마지막 날짜를 얻기 위해 날짜 매개변수를 `0`으로 설정합니다.
5. `Date.prototype.getDate()`를 사용하여 주어진 `month`의 날짜 수를 반환합니다.
6. `daysInMonth` 함수에서 날짜 수를 반환합니다.

다음은 `daysInMonth` 함수에 대한 JavaScript 코드입니다.

```js
const daysInMonth = (year, month) => new Date(year, month, 0).getDate();
```

다음 예제와 같이 `daysInMonth` 함수를 사용하여 모든 연도의 모든 달의 날짜 수를 얻을 수 있습니다.

```js
daysInMonth(2020, 12); // 31
daysInMonth(2024, 2); // 29
```
