# put-stamp
이미지에 본인확인 도장을 찍어주는 프로그램

## 폴더 구조
- python: 도장을 찍는 기능을 수행하는 파이썬 코드 - 실행파일로 만들어 자바에서 호출하도록 하기
  - 실행: `python script.py stamp.jpg doc.jpg 150 255 0 100 0 100 output.jpg 0 0`
  - stamp.jpg: 도장 이미지
  - doc.jpg: 도장을 찍을 이미지
- java: 파이썬 실행파일을 호출하는 자바 코드
