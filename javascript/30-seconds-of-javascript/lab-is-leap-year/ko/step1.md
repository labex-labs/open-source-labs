# 윤년을 확인하는 코드

주어진 `year`가 윤년인지 확인하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 엽니다.
2. `node`를 입력하여 코딩을 시작합니다.
3. `Date` 생성자를 사용하고 주어진 `year`의 2 월 29 일로 날짜를 설정합니다.
4. `Date.prototype.getMonth()`를 사용하여 월이 `1`과 같은지 확인합니다.
5. 다음 코드 조각을 사용하여 윤년인지 확인합니다.

```js
const isLeapYear = (year) => new Date(year, 1, 29).getMonth() === 1;
```

다음은 이 코드를 사용하는 예시입니다.

```js
isLeapYear(2019); // false
isLeapYear(2020); // true
```
