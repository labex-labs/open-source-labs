# 날짜에 분 추가 함수

주어진 날짜에 특정 분을 추가하려면 다음 함수를 사용하십시오.

```js
const addMinutesToDate = (date, n) => {
  // 주어진 날짜로부터 Date 객체 생성
  const d = new Date(date);
  // Date 객체에 n 분 추가
  d.setTime(d.getTime() + n * 60000);
  // 새로운 날짜의 문자열 표현을 yyyy-mm-dd HH:MM:SS 형식으로 반환
  return d.toISOString().split(".")[0].replace("T", " ");
};
```

이 함수를 사용하려면 날짜의 문자열 표현을 첫 번째 인수로, 추가할 분 (음수일 경우 빼기) 을 두 번째 인수로 전달합니다. 예를 들어:

```js
addMinutesToDate("2020-10-19 12:00:00", 10); // '2020-10-19 12:10:00'
addMinutesToDate("2020-10-19", -10); // '2020-10-18 23:50:00'
```

이 함수는 새로운 날짜를 `yyyy-mm-dd HH:MM:SS` 형식의 문자열로 반환합니다.
