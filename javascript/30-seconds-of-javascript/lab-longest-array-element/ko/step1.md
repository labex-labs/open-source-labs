# 배열에서 가장 긴 항목을 찾는 방법

배열에서 가장 긴 항목을 찾으려면 터미널/SSH 를 열고 `node`를 입력합니다. 이 함수는 임의의 수의 반복 가능한 객체 (iterable objects) 또는 `length` 속성을 가진 객체를 인수로 받아 가장 긴 객체를 반환합니다. `Array.prototype.reduce()`를 사용하여 객체의 길이를 비교하고 가장 긴 객체를 찾습니다. 여러 객체가 동일한 길이를 갖는 경우, 함수는 첫 번째 객체를 반환합니다. 인수가 제공되지 않으면 `undefined`를 반환합니다.

다음은 코드입니다.

```js
const longestItem = (...vals) =>
  vals.reduce((a, x) => (x.length > a.length ? x : a));
```

이 함수는 다음과 같이 사용할 수 있습니다.

```js
longestItem("this", "is", "a", "testcase"); // 'testcase'
longestItem(...["a", "ab", "abc"]); // 'abc'
longestItem(...["a", "ab", "abc"], "abcd"); // 'abcd'
longestItem([1, 2, 3], [1, 2], [1, 2, 3, 4, 5]); // [1, 2, 3, 4, 5]
longestItem([1, 2, 3], "foobar"); // 'foobar'
```
