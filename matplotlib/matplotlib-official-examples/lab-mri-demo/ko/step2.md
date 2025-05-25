# MRI 이미지 데이터 로드

`matplotlib`의 `get_sample_data` 함수를 사용하여 샘플 MRI 이미지를 로드합니다. 이미지는 256x256 16 비트 정수 형식입니다.

```python
with cbook.get_sample_data('s1045.ima.gz') as dfile:
    im = np.frombuffer(dfile.read(), np.uint16).reshape((256, 256))
```
