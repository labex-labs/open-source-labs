# 필터 정의

`<defs>` 및 `<filter>` 태그와 `stdDeviation` 속성을 사용하여 가우시안 블러 (Gaussian blur) 에 대한 필터를 정의합니다.

```python
filter_def = """
  <defs xmlns='http://www.w3.org/2000/svg'
        xmlns:xlink='http://www.w3.org/1999/xlink'>
    <filter id='dropshadow' height='1.2' width='1.2'>
      <feGaussianBlur result='blur' stdDeviation='3'/>
    </filter>
  </defs>
"""
```
