# `itertools` 모듈

`itertools`는 이터레이터 (iterators) / 제너레이터 (generators) 를 돕도록 설계된 다양한 함수를 포함하는 라이브러리 모듈입니다.

```python
itertools.chain(s1,s2)
itertools.count(n)
itertools.cycle(s)
itertools.dropwhile(predicate, s)
itertools.groupby(s)
itertools.ifilter(predicate, s)
itertools.imap(function, s1, ... sN)
itertools.repeat(s, n)
itertools.tee(s, ncopies)
itertools.izip(s1, ... , sN)
```

모든 함수는 데이터를 반복적으로 처리합니다. 다양한 종류의 반복 패턴을 구현합니다.

자세한 내용은 PyCon '08 의 [Generator Tricks for Systems Programmers](http://www.dabeaz.com/generators/) 튜토리얼을 참조하십시오.

이전 연습에서 로그 파일에 기록되는 줄을 따라가서 이를 일련의 행으로 구문 분석하는 코드를 작성했습니다. 이 연습은 이를 기반으로 계속 진행됩니다. `stocksim.py`가 여전히 실행 중인지 확인하십시오.
