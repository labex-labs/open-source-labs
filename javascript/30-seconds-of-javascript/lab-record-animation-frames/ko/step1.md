# 애니메이션 프레임 기록 가이드

애니메이션 프레임을 기록하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. 재귀 (recursion) 를 사용하여 각 애니메이션 프레임에서 제공된 콜백 (callback) 을 호출합니다.
3. `running`이 `true`이면, 제공된 콜백을 호출하는 `Window.requestAnimationFrame()`을 계속 호출합니다.
4. 기록을 수동으로 제어할 수 있도록 `start`와 `stop`의 두 가지 메서드를 가진 객체를 반환합니다.
5. 함수가 호출될 때 `start`를 암시적으로 호출하려면 두 번째 인수 `autoStart`를 생략합니다.

애니메이션 프레임을 기록하려면 다음 코드를 사용하세요.

```js
const recordAnimationFrames = (callback, autoStart = true) => {
  let running = false,
    raf;
  const stop = () => {
    if (!running) return;
    running = false;
    cancelAnimationFrame(raf);
  };
  const start = () => {
    if (running) return;
    running = true;
    run();
  };
  const run = () => {
    raf = requestAnimationFrame(() => {
      callback();
      if (running) run();
    });
  };
  if (autoStart) start();
  return { start, stop };
};
```

코드 사용 예시:

```js
const cb = () => console.log("Animation frame fired");
const recorder = recordAnimationFrames(cb);
// logs 'Animation frame fired' on each animation frame
recorder.stop(); // stops logging
recorder.start(); // starts again
const recorder2 = recordAnimationFrames(cb, false);
// `start` needs to be explicitly called to begin recording frames
```
