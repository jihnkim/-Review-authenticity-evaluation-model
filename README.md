### 리뷰의 진정성 평가 모델 구현
****
#### 1. 크롤러 제작(Google Maps Crawler)

- 동적 크롤링이 요구되어 Selenium 패키지 사용
- DOM 구조 파악 및 패키지 인스톨(21.10.23)
- 로직 작성, 크롤러 구현(21.10.24)
- Selenium 사용하지 않고 구현 방법 존재(api 이용, 정말 획기적인 방법!!)
- 개발자 탭>Network>찾고자 하는 docs 검색>해당 file의 curl copy 후 정규식 처리 or json변환(21.10.25)
- 가게 ID와 해당 가게 review를 연결하는 로직 생성(21.10.26)
- 전 코드 함수화(21.10.28)
- store_info.csv 빈 컬럼 채우는 코드 작성(21.10.28)
- store_info_1.csv 구동 확인(본 파일)(21.10.29)
****
#### 2. 리뷰 전처리(Preprocessing)

- gpu 환경설정 : CUDA driver, CUDA toolkit, cuDNN, tensorflow-gpu(21.11.01)
- 전처리 패키지 인스톨, 구동 확인
- hanspell, soynlp, kospacing, punct 처리
- kss 파이참 error
- 패키지 구현 완료

****
#### 3. 워드 임베딩(Word Embedding)

- 전처리 파일 받아서 tokenizer 적용
- 형태소 분석기로 mecap 사용
- twipp 관련 issue >> 모듈 내부에서 class CorpusListener(tweepy.Stream): Listener 수정
- conda 환경에서 jPype1.1.2 설치, java 관련 issue >> 환경변수, jpype 버전확인
- 문서 벡터화 후 평점 tagging(doctag_id로 score 지정)

****
#### 4. DEC(Deep Embedding for Clustering)

- KoBERT 의 분류 성능 향상을 위해 사용
- 비지도 학습으로 AutoEncoder와 Kmeans를 혼합한 모델

****
#### 5. KoBERT

- DEC의 결과 데이터를 받아 KoBERT로 다중 분류 시작
issue >
  1. transformers 버전 문제 > 모델 파라미터 return_dict=False
  2. 모델 load시 HTTPS error? kobert_hf 패키지 참고
  3. ..
- 각 리뷰의 새로운 평점 컬럼 생성
- 리뷰에 해당하는 가게의 새로운 평점 평균 생성 성공!!!!!
  (약 360만개 데이터, accuracy 88%)
- 모델 학습을 하며 데이터의 중요성을 다시 한번 깨달았당..  
fin. 