# 잠재 디리클레 할당 (LDA)

#### 주제 모델링을 위한 LDA

잠재 디리클레 할당 (LDA) 는 문서 모음에서 추상적인 주제를 발견하기 위해 사용되는 생성적 확률 모델입니다. LDA 는 문서가 여러 주제의 혼합이며 단어가 이러한 주제에 의해 생성된다고 가정합니다. LDA 는 scikit-learn 의 `LatentDirichletAllocation` 클래스를 사용하여 구현할 수 있습니다.

```python
from sklearn.decomposition import LatentDirichletAllocation

# 원하는 주제의 수를 n_components 로 설정한 LDA 객체 생성
lda = LatentDirichletAllocation(n_components=5)

# 문서 - 용어 행렬에 LDA 모델을 맞춤
lda.fit(document_term_matrix)

# 주제 - 용어 행렬과 문서 - 주제 행렬 가져오기
topic_term_matrix = lda.components_
document_topic_matrix = lda.transform(document_term_matrix)
```
