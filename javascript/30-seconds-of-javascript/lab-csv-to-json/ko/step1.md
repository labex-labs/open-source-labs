# CSV 를 JSON 으로 변환하기

쉼표로 구분된 값 (CSV) 문자열을 객체의 2 차원 배열로 변환하고 코딩 연습에 사용하려면 터미널/SSH 를 열고 `node`를 입력하십시오. 문자열의 첫 번째 행은 제목 행으로 사용됩니다. CSV 를 JSON 으로 변환하는 단계는 다음과 같습니다.

1. `Array.prototype.indexOf()`를 사용하여 첫 번째 줄 바꿈 문자 (`\n`) 를 찾습니다.
2. `Array.prototype.slice()`를 사용하여 첫 번째 행 (제목 행) 을 제거하고, 제공된 `delimiter`를 사용하여 `String.prototype.split()`으로 값을 분리합니다.
3. `String.prototype.split()`을 사용하여 각 행에 대한 문자열을 생성합니다.
4. 제공된 `delimiter`를 사용하여 `String.prototype.split()`을 사용하여 각 행의 값을 분리합니다.
5. `Array.prototype.reduce()`를 사용하여 제목 행에서 구문 분석된 키를 사용하여 각 행의 값에 대한 객체를 생성합니다.
6. 두 번째 인수 `delimiter`를 생략하여 기본 구분 기호인 `,`를 사용합니다.

다음은 코드입니다.

```js
const CSVToJSON = (data, delimiter = ",") => {
  const titles = data.slice(0, data.indexOf("\n")).split(delimiter);
  return data
    .slice(data.indexOf("\n") + 1)
    .split("\n")
    .map((v) => {
      const values = v.split(delimiter);
      return titles.reduce(
        (obj, title, index) => ((obj[title] = values[index]), obj),
        {}
      );
    });
};
```

함수를 테스트하려면 다음 예제를 사용하십시오.

```js
CSVToJSON("col1,col2\na,b\nc,d");
// [{'col1': 'a', 'col2': 'b'}, {'col1': 'c', 'col2': 'd'}];
CSVToJSON("col1;col2\na;b\nc;d", ";");
// [{'col1': 'a', 'col2': 'b'}, {'col1': 'c', 'col2': 'd'}];
```
