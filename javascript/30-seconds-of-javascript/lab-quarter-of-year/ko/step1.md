# 연도 분기 결정 함수

연도의 분기를 결정하려면 `quarterOfYear()` 함수를 사용하십시오. 이 함수는 선택적 `date` 인수를 받아 지정된 날짜가 속한 분기와 연도를 포함하는 배열을 반환합니다.

이 함수를 사용하려면 터미널/SSH 를 열고 `node`를 입력하십시오. 그런 다음 다음 코드를 복사하여 붙여넣으십시오.

```js
const quarterOfYear = (date = new Date()) => [
  Math.ceil((date.getMonth() + 1) / 3),
  date.getFullYear()
];
```

`quarterOfYear()` 함수는 다음 단계를 사용하여 분기와 연도를 계산합니다.

- `Date.prototype.getMonth()`를 사용하여 현재 월을 범위 (0, 11) 에서 가져와 `1`을 더하여 범위 (1, 12) 로 매핑합니다.
- `Math.ceil()`을 사용하고 월을 `3`으로 나누어 현재 분기를 구합니다.
- `Date.prototype.getFullYear()`을 사용하여 주어진 `date`에서 연도를 가져옵니다.
- 인수인 `date`를 생략하여 기본적으로 현재 날짜를 사용합니다.

다음은 `quarterOfYear()` 함수를 사용하는 몇 가지 예입니다.

```js
quarterOfYear(new Date("07/10/2018")); // [ 3, 2018 ]
quarterOfYear(); // [ 4, 2020 ]
```
