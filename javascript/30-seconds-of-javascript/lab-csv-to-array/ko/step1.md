# CSV 를 배열로 변환하기

쉼표로 구분된 값 (CSV) 문자열을 2 차원 배열로 변환하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩을 시작합니다.
2. `Array.prototype.indexOf()`를 사용하여 첫 번째 줄 바꿈 문자 (`\n`) 를 찾습니다.
3. `omitFirstRow`가 `true`로 설정된 경우 `Array.prototype.slice()`를 사용하여 첫 번째 행 (제목 행) 을 제거합니다.
4. 각 행에 대한 문자열을 생성하기 위해 `String.prototype.split()`을 사용합니다.
5. 제공된 `delimiter`를 사용하여 각 행의 값을 분리하기 위해 `String.prototype.split()`을 사용합니다.
6. 두 번째 인수 `delimiter`를 제공하지 않으면 기본 구분 기호인 `','`가 사용됩니다.
7. 세 번째 인수 `omitFirstRow`를 제공하지 않으면 CSV 문자열의 첫 번째 행 (제목 행) 이 포함됩니다.

다음은 CSV 를 배열로 변환하는 코드입니다.

```js
const CSVToArray = (data, delimiter = ",", omitFirstRow = false) =>
  data
    .slice(omitFirstRow ? data.indexOf("\n") + 1 : 0)
    .split("\n")
    .map((v) => v.split(delimiter));
```

다음 예제를 사용하여 함수를 테스트할 수 있습니다.

```js
CSVToArray("a,b\nc,d"); // [['a', 'b'], ['c', 'd']];
CSVToArray("a;b\nc;d", ";"); // [['a', 'b'], ['c', 'd']];
CSVToArray("col1,col2\na,b\nc,d", ",", true); // [['a', 'b'], ['c', 'd']];
```
