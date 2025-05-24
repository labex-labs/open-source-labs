# 2 차원 배열을 CSV 로 변환하기

2 차원 배열을 쉼표로 구분된 값 (CSV) 문자열로 변환하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `Array.prototype.map()`과 `Array.prototype.join()`을 사용하여 제공된 `delimiter`를 사용하여 개별 1 차원 배열 (행) 을 문자열로 결합합니다.
3. `Array.prototype.join()`을 사용하여 모든 행을 CSV 문자열로 결합하고, 각 행을 줄 바꿈 문자 (`\n`) 로 구분합니다.
4. 기본 구분 기호인 `,`를 사용하려면 두 번째 인수 `delimiter`를 생략합니다.

다음은 코드의 예입니다.

```js
const arrayToCSV = (arr, delimiter = ",") =>
  arr
    .map((v) =>
      v
        .map((x) => (isNaN(x) ? `"${x.replace(/"/g, '""')}"` : x))
        .join(delimiter)
    )
    .join("\n");
```

다음 코드 줄을 실행하여 함수를 테스트할 수 있습니다.

```js
arrayToCSV([
  ["a", "b"],
  ["c", "d"]
]); // '"a","b"\n"c","d"'
arrayToCSV(
  [
    ["a", "b"],
    ["c", "d"]
  ],
  ";"
); // '"a";"b"\n"c";"d"'
arrayToCSV([
  ["a", '"b" great'],
  ["c", 3.1415]
]);
// '"a","""b"" great"\n"c",3.1415'
```
