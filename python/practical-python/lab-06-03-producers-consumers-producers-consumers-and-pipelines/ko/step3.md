# 연습 6.8: 간단한 파이프라인 설정

파이프라인 아이디어를 실제로 살펴보겠습니다. 다음 함수를 작성하십시오.

```python
>>> def filematch(lines, substr):
        for line in lines:
            if substr in line:
                yield line

>>>
```

이 함수는 이전 연습의 첫 번째 제너레이터 예제와 거의 동일하지만 더 이상 파일을 열지 않고 인수로 제공된 일련의 라인에서 작동합니다. 이제 다음을 시도해 보십시오.

```python
>>> from follow import follow
>>> lines = follow('stocklog.csv')
>>> goog = filematch(lines, 'GOOG')
>>> for line in goog:
        print(line)

... wait for output ...
```

출력이 나타나기까지 시간이 걸릴 수 있지만, 결국 GOOG 에 대한 데이터를 포함하는 일부 라인을 볼 수 있습니다.

참고: 이 연습은 두 개의 별도 터미널에서 동시에 수행해야 합니다.
