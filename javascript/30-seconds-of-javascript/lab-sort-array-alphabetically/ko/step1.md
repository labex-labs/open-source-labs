# JavaScript 에서 주어진 속성을 기준으로 배열을 알파벳순으로 정렬하는 방법

JavaScript 에서 주어진 속성을 기준으로 객체 배열을 알파벳순으로 정렬하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `Array.prototype.sort()`를 사용하여 주어진 속성을 기준으로 배열을 정렬합니다.
3. `String.prototype.localeCompare()`를 사용하여 주어진 속성의 값을 비교합니다.

다음은 사용할 수 있는 예시 코드 조각입니다.

```js
const alphabetical = (arr, getter, order = "asc") =>
  arr.sort(
    order === "desc"
      ? (a, b) => getter(b).localeCompare(getter(a))
      : (a, b) => getter(a).localeCompare(getter(b))
  );
```

객체 배열과 정렬할 속성을 반환하는 getter 함수를 사용하여 `alphabetical` 함수를 호출할 수 있습니다. 다음은 사용 예시입니다.

```js
const people = [{ name: "John" }, { name: "Adam" }, { name: "Mary" }];
alphabetical(people, (g) => g.name);
// [ { name: 'Adam' }, { name: 'John' }, { name: 'Mary' } ]
alphabetical(people, (g) => g.name, "desc");
// [ { name: 'Mary' }, { name: 'John' }, { name: 'Adam' } ]
```
