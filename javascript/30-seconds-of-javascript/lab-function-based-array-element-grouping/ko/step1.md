# 배열 요소 그룹화 방법

코딩 연습을 하고 싶다면, 터미널/SSH 를 열고 `node`를 입력하여 시작할 수 있습니다. 준비가 되면 다음 단계를 사용하여 주어진 함수를 기반으로 배열의 요소를 그룹화할 수 있습니다.

1. `Array.prototype.map()`을 사용하여 배열의 값을 함수 또는 속성 이름에 매핑합니다.
2. `Array.prototype.reduce()`를 사용하여 키가 매핑된 결과에서 생성되는 객체를 만듭니다.

다음은 코드 스니펫 예시입니다.

```js
const groupBy = (arr, fn) =>
  arr
    .map(typeof fn === "function" ? fn : (val) => val[fn])
    .reduce((acc, val, i) => {
      acc[val] = (acc[val] || []).concat(arr[i]);
      return acc;
    }, {});
```

코드를 테스트하려면 다음 예시를 사용할 수 있습니다.

```js
groupBy([6.1, 4.2, 6.3], Math.floor); // {4: [4.2], 6: [6.1, 6.3]}
groupBy(["one", "two", "three"], "length"); // {3: ['one', 'two'], 5: ['three']}
```

이 예시들은 지정된 함수를 기반으로 하는 키와 해당 함수와 일치하는 원래 요소의 배열인 값을 가진 객체를 반환합니다.
