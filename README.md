```
The first version of this document was written by
@author: sanghyunlim,sangmoklee
@date: 2022-NOV
```

## **Objectives**
* made platform for cafeteria

## **etc.**
* 디비 : RDS? 상현님 의견 
* backend : python-flask
* frontend : react native? 

## **Folder tree**
```
---- folder
- file

 flask
    |
    |---- data                      : 데이터 저장 폴더, config의 DATA_PATH
    |---- result                    : weight, json, csv 등의 부산물 저장 폴더, config의 RESULT_PATH
    |
    |---- properties
    |- config.properties            : Path, model parameter option settings
    |                                 각종 옵션 조정
    |- db.properties                : DB option settings
    |                                 옵션 조정
    |- logger.json                  : log record
    |
    |- plan.json                    : 데이터 입력 기본형태
    |                                 traindata명,testdata명,file명,model명,option명,scale여부
    |- data_preprocess.py           : functions that can preprocess data
    | 
    |---- query
    |- query.json                   : query                   
    |----
    |
    |- main.py                      : model_run
    |                                 기본 정보 read후 모델 실행
    |- dbconnecter.py               : DB연결
    |                                 (정보는 db.properties에서 가져와서 사용, pem_키(암호화 복호화) 파일은 보안상 삭제) 
    |- data_sql.py                  : sqls to extract MariaDB data are here
    |                                 데이터를 추출하기 위한 쿼리는 여기서 수정
    |- functions.py                 : data_information, model_read
    |                                 데이터 경로, 결측치, 모델 등 정보확인 
    |- models.py                    : SVM, LR, RF, XGB, DNN, CNN, LSTM, AE
    |                                 학습하고자 하는 모형을 models.py에서 불러서 학습 
    |- cut_off.py                   : 컷오프별 결과값 정리, Plot이미지 생성
    |
    |- timedifferent.py             : 바로 전 결제와의 시간차 구하는 함수(시계열 모형에 사용계획)
    |                                 컬럼명은 보안상의 이유로 임의로 변경 
    |- test.ipynb                   : TO BE UPDATED'
    |
    |---- 시계열 분석(폴더 안에 README.md 참고)
    |
    |---- Bithumb_트레이딩 봇(폴더 안에 README.md 참고)
    |          
    |----
```


