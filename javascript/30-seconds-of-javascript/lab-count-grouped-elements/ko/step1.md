# JavaScript 를 사용하여 배열의 요소를 그룹화하고 계산하는 방법

JavaScript 를 사용하여 배열의 요소를 그룹화하고 계산하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `Array.prototype.map()` 메서드를 사용하여 배열의 값을 함수 또는 속성 이름에 매핑합니다.
3. `Array.prototype.reduce()` 메서드를 사용하여 키가 매핑된 결과에서 생성되는 객체를 만듭니다.
4. 배열과 함수를 인수로 사용하는 `countBy`라는 함수를 만듭니다.
5. `countBy` 함수 내부에서 삼항 연산자를 사용하여 전달된 인수가 함수인지 속성 이름인지 확인합니다. 함수인 경우 매핑 함수로 사용합니다. 속성 이름인 경우 배열 요소의 해당 속성에 접근합니다.
6. `reduce()` 메서드를 사용하여 각 키가 배열의 고유한 요소를 나타내고 해당 값이 배열에 나타나는 횟수인 객체를 만듭니다.

다음은 코드입니다.

```js
const countBy = (arr, fn) =>
  arr
    .map(typeof fn === "function" ? fn : (val) => val[fn])
    .reduce((acc, val) => {
      acc[val] = (acc[val] || 0) + 1;
      return acc;
    }, {});
```

다음 예제를 사용하여 `countBy` 함수를 테스트할 수 있습니다.

```js
countBy([6.1, 4.2, 6.3], Math.floor); // {4: 1, 6: 2}
countBy(["one", "two", "three"], "length"); // {3: 2, 5: 1}
countBy([{ count: 5 }, { count: 10 }, { count: 5 }], (x) => x.count); // {5: 2, 10: 1}
```
