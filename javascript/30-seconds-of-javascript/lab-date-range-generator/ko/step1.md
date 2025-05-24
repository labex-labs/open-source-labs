# 날짜 범위 생성기

주어진 간격을 사용하여 지정된 범위 내의 모든 날짜를 생성하려면 터미널/SSH 에서 다음 코드를 사용하고 `node`를 입력하십시오.

```js
const dateRangeGenerator = function* (start, end, step = 1) {
  let d = start;
  while (d < end) {
    yield new Date(d);
    d.setDate(d.getDate() + step);
  }
};
```

이 코드는 `while` 루프를 사용하여 `start`에서 `end`까지 반복하고, `Date` 생성자를 사용하여 범위 내의 각 날짜를 반환하며, `Date.prototype.getDate()` 및 `Date.prototype.setDate()`를 사용하여 `step`일씩 증가시키는 생성기를 생성합니다.

`step`의 기본값으로 `1`을 사용하려면 세 번째 인수를 생략하십시오.

다음은 `dateRangeGenerator`를 사용하는 예입니다.

```js
[...dateRangeGenerator(new Date("2021-06-01"), new Date("2021-06-04"))];
// [ 2021-06-01, 2021-06-02, 2021-06-03 ]
```
