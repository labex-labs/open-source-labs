# 범위 제너레이터 (Range Generator)

지정된 단계를 사용하여 값의 범위를 생성하려면 다음 `rangeGenerator` 함수를 사용하십시오. 터미널/SSH 를 열고 `node`를 입력하여 코딩을 시작하십시오.

- `start`에서 시작하여 `end`에서 끝나는 각 값을 반환하기 위해 `while` 루프와 `yield`를 사용합니다.
- 기본 단계 `1`을 사용하려면 세 번째 인수를 생략하십시오.

```js
const rangeGenerator = function* (start, end, step = 1) {
  let i = start;
  while (i < end) {
    yield i;
    i += step;
  }
};
```

다음은 `rangeGenerator` 함수를 사용하는 예입니다.

```js
for (let i of rangeGenerator(6, 10)) console.log(i);
// Logs 6, 7, 8, 9
```
