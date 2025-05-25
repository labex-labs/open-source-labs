# 특징 순위 지정

RFE 객체에 데이터를 적용한 후, 특징의 중요도에 따라 특징을 순위화할 수 있습니다. RFE 객체의 `ranking_` 속성을 사용하여 특징 순위를 얻을 것입니다. 또한, 순위를 원본 이미지의 모양과 일치하도록 변형할 것입니다.

```python
ranking = rfe.ranking_.reshape(digits.images[0].shape)
```
