```
The first version of this document was written by
@author: sanghyunlim,sangmoklee
@date: 2022-NOV
```

## **Objectives**
* made platform for cafeteria

## **etc.**
* 디비 : edgeDB
* backend : python-flask
* frontend : react native? 

## **Folder tree**
```
---- folder
- file

 flask
    |
    |---- app.py                    : flask 메인 실행 파일 
    |
    |---- templates                 : flask는 app.py에서 render_template 내장함수로 templates폴더 내 html파일을 읽을 수 있음
    |- index.html                   : app.py 라우터로 보이는 파일들 (html)
    | 
    |---- static                    : html 파일에 추가하여 css 사용가능 <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
    |- main.css                     : css,js 파일 저장공간으로 메인 css 저장
    |
    |---- api                       : 외부 api 파일 연결
    |
    |---- 그 외 (폴더 안에 README.md 참고)
    |      
```


