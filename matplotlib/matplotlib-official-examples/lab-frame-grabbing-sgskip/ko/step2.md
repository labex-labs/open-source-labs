# Writer 설정

프레임을 파일에 쓰는 데 사용될 writer 를 설정해야 합니다. 초당 프레임 수 (fps) 를 설정하고 제목, 아티스트, 코멘트와 같은 메타데이터를 추가합니다.

```python
metadata = dict(title='Movie Test', artist='Matplotlib',
                comment='Movie support!')
writer = FFMpegWriter(fps=15, metadata=metadata)
```
