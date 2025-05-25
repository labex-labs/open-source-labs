# JavaScript 에서 배열에서 값 가져오는 방법

JavaScript 에서 배열에서 특정 값을 추출하려면 `Array.prototype.filter()` 및 `Array.prototype.includes()` 메서드를 사용할 수 있습니다. 방법은 다음과 같습니다.

```js
const pull = (arr, ...args) => {
  let argState = Array.isArray(args[0]) ? args[0] : args;
  let pulled = arr.filter((v) => !argState.includes(v));
  arr.length = 0;
  pulled.forEach((v) => arr.push(v));
};
```

`pull` 함수는 배열과 제거할 값을 나타내는 하나 이상의 인수를 받습니다. 그런 다음 이 함수는 `Array.prototype.filter()`를 사용하여 지정된 값을 필터링하여 새 배열을 생성합니다. 그런 다음 원래 배열의 길이를 `0`으로 재설정하고 `Array.prototype.push()`를 사용하여 가져온 값만으로 다시 채워 원래 배열을 변경합니다.

다음은 `pull` 함수를 사용하는 예입니다.

```js
let myArray = ["a", "b", "c", "a", "b", "c"];
pull(myArray, "a", "c"); // myArray = [ 'b', 'b' ]
```

이 예에서 `pull` 함수는 `myArray` 배열에서 모든 `'a'`와 `'c'`의 발생을 제거하고 `'b'`와 `'b'` 값만 포함하는 새 배열을 반환합니다.
