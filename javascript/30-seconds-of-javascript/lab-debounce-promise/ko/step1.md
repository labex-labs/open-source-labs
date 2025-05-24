# 프로미스 디바운스 (Debounce Promise)

프로미스를 반환하는 디바운스 함수를 생성하려면, 마지막으로 호출된 이후 최소 `ms` 밀리초가 경과할 때까지 제공된 함수 호출을 지연시켜야 합니다. 다음 단계를 사용하십시오.

1. 디바운스 함수가 호출될 때마다 `clearTimeout()`을 사용하여 현재 보류 중인 타임아웃을 지우고, `setTimeout()`을 사용하여 최소 `ms` 밀리초가 경과할 때까지 함수 호출을 지연시키는 새로운 타임아웃을 생성합니다.
2. `Function.prototype.apply()`를 사용하여 `this` 컨텍스트를 함수에 적용하고 필요한 인수를 제공합니다.
3. 새로운 `Promise`를 생성하고 해당 `resolve` 및 `reject` 콜백을 `pending` 프로미스 스택에 추가합니다.
4. `setTimeout()`이 호출되면 현재 스택을 복사 (제공된 함수 호출과 해결 사이에서 변경될 수 있으므로) 하고, 스택을 지운 다음 제공된 함수를 호출합니다.
5. 제공된 함수가 resolve/reject되면, 반환된 데이터를 사용하여 스택의 모든 프로미스 (함수가 호출될 때 복사됨) 를 resolve/reject합니다.
6. 두 번째 인수 `ms`를 생략하여 타임아웃을 기본값인 `0` ms 로 설정합니다.

다음은 `debouncePromise()` 함수의 코드입니다.

```js
const debouncePromise = (fn, ms = 0) => {
  let timeoutId;
  const pending = [];
  return (...args) =>
    new Promise((res, rej) => {
      clearTimeout(timeoutId);
      timeoutId = setTimeout(() => {
        const currentPending = [...pending];
        pending.length = 0;
        Promise.resolve(fn.apply(this, args)).then(
          (data) => {
            currentPending.forEach(({ resolve }) => resolve(data));
          },
          (error) => {
            currentPending.forEach(({ reject }) => reject(error));
          }
        );
      }, ms);
      pending.push({ resolve: res, reject: rej });
    });
};
```

다음은 `debouncePromise()`를 사용하는 예시입니다.

```js
const fn = (arg) =>
  new Promise((resolve) => {
    setTimeout(resolve, 1000, ["resolved", arg]);
  });
const debounced = debouncePromise(fn, 200);
debounced("foo").then(console.log);
debounced("bar").then(console.log);
// Will log ['resolved', 'bar'] both times
```
