# Box-Muller 변환을 사용하여 가우시안 난수 생성하기

Box-Muller 변환을 사용하여 가우시안 (정규 분포) 난수를 생성하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. Box-Muller 변환을 활용하여 가우시안 분포를 가진 난수를 생성하는 제공된 코드 조각을 사용합니다.
3. 코드 조각에 제공된 `randomGauss()` 함수는 가우시안 분포를 가진 난수를 생성합니다.
4. `randomGauss()` 함수의 출력은 0 과 1 사이의 숫자입니다.
5. 이 출력은 통계 시뮬레이션, 데이터 분석 및 머신 러닝과 같은 다양한 응용 분야에 사용될 수 있습니다.

```js
const randomGauss = () => {
  const theta = 2 * Math.PI * Math.random();
  const rho = Math.sqrt(-2 * Math.log(1 - Math.random()));
  return (rho * Math.cos(theta)) / 10.0 + 0.5;
};
```

예시 사용법:

```js
randomGauss(); // 0.5
```
