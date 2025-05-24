# Array.prototype.filter() 를 사용하여 컴팩트 배열 생성 방법

JavaScript 에서 컴팩트 배열을 생성하려면 `Array.prototype.filter()` 메서드를 사용하여 배열에서 falsy 값을 제거할 수 있습니다. Falsy 값에는 `false`, `null`, `0`, `""`, `undefined`, 그리고 `NaN`이 포함됩니다.

다음은 `Array.prototype.filter()`를 사용하여 컴팩트 배열을 생성하는 방법을 보여주는 코드 예시입니다.

```js
const compact = (arr) => arr.filter(Boolean);
```

그런 다음 `compact` 함수를 사용하여 배열을 인수로 전달하여 컴팩트 배열을 생성할 수 있습니다. 예를 들어:

```js
compact([0, 1, false, 2, "", 3, "a", "e" * 23, NaN, "s", 34]);
// Output: [ 1, 2, 3, 'a', 's', 34 ]
```

이러한 방식으로 `Array.prototype.filter()`를 사용하면 truthy 값만 포함하는 컴팩트 배열을 쉽게 생성할 수 있습니다.
