# 비동기 함수 연결하기

비동기 함수를 연결하려면 터미널/SSH 를 열고 `node`를 입력합니다. 그런 다음, 비동기 이벤트를 포함하는 함수 배열을 반복 처리하고 각 비동기 이벤트가 완료되면 `next` 함수를 호출합니다.

다음은 비동기 함수를 연결하는 방법을 보여주는 코드 조각입니다.

```js
const chainAsync = (fns) => {
  let curr = 0;
  const last = fns[fns.length - 1];
  const next = () => {
    const fn = fns[curr++];
    fn === last ? fn() : fn(next);
  };
  next();
};

chainAsync([
  (next) => {
    console.log("0 seconds");
    setTimeout(next, 1000);
  },
  (next) => {
    console.log("1 second");
    setTimeout(next, 1000);
  },
  () => {
    console.log("2 second");
  }
]);
```
