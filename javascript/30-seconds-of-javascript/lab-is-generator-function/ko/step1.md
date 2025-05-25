# 값이 제너레이터 함수인지 확인하기

값이 제너레이터 함수인지 확인하려면 `isGeneratorFunction` 함수를 사용할 수 있습니다. 코딩 연습을 시작하려면 터미널/SSH 를 열고 `node`를 입력하십시오.

`isGeneratorFunction` 함수는 다음과 같이 작동합니다.

- `Object.prototype.toString()` 및 `Function.prototype.call()`을 사용하여 주어진 인수가 제너레이터 함수인지 확인합니다.
- 확인 결과가 `'[object GeneratorFunction]'`이면 해당 값은 제너레이터 함수입니다.

`isGeneratorFunction` 함수의 코드는 다음과 같습니다.

```js
const isGeneratorFunction = (val) =>
  Object.prototype.toString.call(val) === "[object GeneratorFunction]";
```

다음은 이 함수를 사용하는 몇 가지 예입니다.

```js
isGeneratorFunction(function () {}); // false
isGeneratorFunction(function* () {}); // true
```
