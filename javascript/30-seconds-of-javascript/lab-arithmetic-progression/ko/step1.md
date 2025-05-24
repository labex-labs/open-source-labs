# 등차수열 코드 예시

코딩 연습을 위해 터미널/SSH 를 열고 `node`를 입력하세요.

다음은 등차수열의 숫자로 이루어진 배열을 생성하는 코드 예시입니다. 배열은 주어진 양의 정수에서 시작하여 지정된 제한까지 증가합니다.

```js
const arithmeticProgression = (n, lim) =>
  Array.from({ length: Math.ceil(lim / n) }, (_, i) => (i + 1) * n);
```

이 코드를 사용하려면 `arithmeticProgression` 함수를 두 개의 인자, 즉 시작하는 양의 정수와 제한 값으로 호출하면 됩니다. 예를 들어:

```js
arithmeticProgression(5, 25); // [5, 10, 15, 20, 25]
```
