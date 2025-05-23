# 날짜가 평일인지 확인하기

주어진 날짜가 평일인지 확인하려면 다음 코드 스니펫을 사용할 수 있습니다.

```js
const isWeekday = (date = new Date()) => date.getDay() % 6 !== 0;
```

- 이 함수는 `Date.prototype.getDay()`를 사용하여 요일을 숫자로 (0-6) 가져옵니다. 여기서 일요일은 0 이고 토요일은 6 입니다.
- 그런 다음 요일이 0 (일요일) 또는 6 (토요일) 과 같지 않은지 확인합니다. 이는 평일임을 의미합니다.
- 인수로 날짜가 제공되지 않으면 현재 날짜가 기본값으로 사용됩니다.

사용 예시:

```js
isWeekday(); // true (현재 날짜가 평일인 경우)
isWeekday(new Date(2021, 5, 28)); // true (날짜가 평일인 경우)
```
