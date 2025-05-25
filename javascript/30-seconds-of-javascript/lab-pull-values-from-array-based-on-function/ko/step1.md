# 주어진 함수를 기반으로 배열에서 값 빼내기

코딩 연습을 시작하려면 터미널/SSH 를 열고 `node`를 입력하세요.

`pullBy` 함수는 주어진 이터레이터 함수를 기반으로 지정된 값을 필터링하여 원래 배열을 변경합니다. 작동 방식은 다음과 같습니다.

1. 제공된 마지막 인수가 함수인지 확인합니다.
2. `Array.prototype.map()`을 사용하여 이터레이터 함수 `fn`을 모든 배열 요소에 적용합니다.
3. `Array.prototype.filter()` 및 `Array.prototype.includes()`를 사용하여 필요 없는 값을 빼냅니다.
4. `Array.prototype.length`를 설정하여 전달된 배열의 길이를 `0`으로 재설정합니다.
5. `Array.prototype.push()`를 사용하여 빼낸 값만으로 다시 채웁니다.

다음은 코드입니다.

```js
const pullBy = (arr, ...args) => {
  const length = args.length;
  let fn = length > 1 ? args[length - 1] : undefined;
  fn = typeof fn == "function" ? (args.pop(), fn) : undefined;
  let argState = (Array.isArray(args[0]) ? args[0] : args).map((val) =>
    fn(val)
  );
  let pulled = arr.filter((v, i) => !argState.includes(fn(v)));
  arr.length = 0;
  pulled.forEach((v) => arr.push(v));
};
```

다음은 사용 예시입니다.

```js
var myArray = [{ x: 1 }, { x: 2 }, { x: 3 }, { x: 1 }];
pullBy(myArray, [{ x: 1 }, { x: 3 }], (o) => o.x); // myArray = [{ x: 2 }]
```

이 예제에서는 `x` 속성이 `1` 또는 `3`인 모든 요소를 빼내고 있습니다. 결과 `myArray`에는 `x` 속성이 `2`인 요소만 포함됩니다.
