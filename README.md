## v1.0.1
## v1.0.0

<p align="center">
  <img alt="Thumbnail" src="./_github/thumbnail.png" width="100%" />
</p>
<h1 align="center">🐳 고래 키우기</h1>
<h4>항해99 18기 5조 미니프로젝트</h4>
매일매일 고래에게 ‘공부’ 먹이를 주고, 항해 99일간 키우면 성장 완료!

## 💻 preview
배포주소 :[woo3145.pythonanywhere.com](https://woo3145.pythonanywhere.com/)  

[고래키우기 시연 영상](https://youtu.be/D-ZuqNl9Zzk) 

## 👨‍👨‍👧‍👦 팀원
- [김기민](https://github.com/js1171) - 회원가입
- [김진욱](https://github.com/naraspc) - JWT, 로그인 구현, 보안
- [이지선](https://github.com/js1171) - 메인로직
- [이창우](https://github.com/woo3145) - 프로젝트 총괄 관리, 메인페이지

## 기능
<aside>
❓ 미니 프로젝트에 제 실제 비밀번호를 사용해도 괜찮을까요?

</aside>
### 실제 비밀번호를 사용해도 괜찮을까?

<aside>
❓ 미니 프로젝트에 제 실제 비밀번호를 사용해도 괜찮을까요?

</aside>

**⇒ 안심하고 사용해도 괜찮습니다!**

- SQLAlchemy라는 ORM을 사용해 DB와 통신함으로써 SQL Injection에 대해 대비
- 암호화 알고리즘을 적용해 PW DB에 저장
    - DB에 저장되는 PW는 암호화된 값이므로, **PW찾기 기능은 지원하지않습니다.**
- 블라인드 SQL 인젝션, 유니온 베이스 인젝션, 에러 베이스 인젝션 테스트 완료
- 어드민 권한 탈취를 방지하기 위해 프로젝트 기능상 필요없는 권한은 구현하지 않았습니다.

  
<details>
  
<summary>고래의 밥!</summary>

<img alt="Thumbnail" src="./_github/feature1.png" width="100%" />

- 고래에게 줄 밥을 하나 클릭!
- 밥은 하루에 한 번만 줄 수 있음

</details>

<details>
<summary>고래 진화!</summary>

<img alt="Thumbnail" src="./_github/feature2.png" width="100%" />

 **Level 1 : 응애 고래**
    
- 회원 가입 후 나오는 첫 번째 고래
- 먹이를 주면 성장!

</details>

<details>
<summary>진화</summary>

<img alt="Thumbnail" src="./_github/feature3.png" width="100%" />

- 99일의 최종 Level은 Lv5
- 먹이 종류에 따라 성장 형태 변화
- 진화하는 과정은 비밀~

</details> 

<details>
<summary>로그인 / 회원가입</summary>

- JWT토큰을 사용한 인증처리

</details>

## 🛠️ Stack

### Backend
- 언어: `Python`
- 프레임워크: `Flask`
- DB: `SQL3LITE`
- ORM: `SQLALCHEMY`
- 인증: `JWT`
- 배포: `AWS-S3`, `PythonAnyWhere`

### Front
- 언어: `JavaScript`, `HTML`
- CSS: `Bootstrap`
- 템플릿 엔진: `Jinja2`
