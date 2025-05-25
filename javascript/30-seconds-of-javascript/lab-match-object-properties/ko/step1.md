# JavaScript 에서 객체 속성 비교 방법

두 객체를 비교하고 동일한 속성 값을 갖는지 확인하려면 `matches` 함수를 사용하십시오. 사용 방법은 다음과 같습니다.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩을 시작합니다.
2. `matches` 함수 코드를 복사하여 JavaScript 파일에 붙여넣습니다.
3. 함수를 호출하고 두 객체를 인수로 전달합니다. 첫 번째 객체는 비교하려는 객체이고, 두 번째 객체는 비교할 객체입니다.

```js
matches({ age: 25, hair: "long", beard: true }, { hair: "long", beard: true });
// true
matches({ hair: "long", beard: true }, { age: 25, hair: "long", beard: true });
// false
```

`matches` 함수는 `Object.keys()`를 사용하여 두 번째 객체의 모든 키를 가져온 다음, `Array.prototype.every()`, `Object.prototype.hasOwnProperty()` 및 엄격한 비교를 사용하여 모든 키가 첫 번째 객체에 존재하고 동일한 값을 갖는지 확인합니다.
