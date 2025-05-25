# 숫자를 서수 접미사로 변환하는 함수

숫자를 서수 접미사로 변환하려면 `toOrdinalSuffix` 함수를 사용하십시오.

- 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
- 이 함수는 숫자를 입력으로 받아 올바른 서수 지시자 접미사가 붙은 문자열로 반환합니다.
- 모듈로 연산자 (`%`) 를 사용하여 일의 자리와 십의 자리 숫자의 값을 찾습니다.
- 어떤 서수 패턴 숫자가 일치하는지 찾습니다.
- 숫자가 10 대 패턴에 있으면 10 대 서수를 사용합니다.

```js
const toOrdinalSuffix = (num) => {
  const int = parseInt(num),
    digits = [int % 10, int % 100],
    ordinals = ["st", "nd", "rd", "th"],
    oPattern = [1, 2, 3, 4],
    tPattern = [11, 12, 13, 14, 15, 16, 17, 18, 19];
  return oPattern.includes(digits[0]) && !tPattern.includes(digits[1])
    ? int + ordinals[digits[0] - 1]
    : int + ordinals[3];
};
```

다음은 `toOrdinalSuffix` 함수를 사용하는 예입니다.

```js
toOrdinalSuffix("123"); // '123rd'
```
