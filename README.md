# 편모아 (Pyeon-Mo-A)
국내 3대 편의점(CU, GS25, 세븐일레븐)의 1+1 행사 정보를 한 곳에 모아 제공하는 페이지 입니다.



## 🖥 개발 환경
- **Language :** Python `3.10`
- **Web Framework :** Django `4.0.4`
- **Framework :** Selenium `4.1.5`
- **Database :** SQLite
- **ORM :** Django ORM
- **FrontEnd :** Bootstrap `4.5`

## 👥 개발 구성원
**2인 팀 프로젝트**
  - **팀장 :** [l22hs](https://github.com/l22hs2) - `FrontEnd` `BackEnd` `데이터 수집`
  - **팀원 :** husky - `FrontEnd`

## ⚙️ 동작 과정

## 📌 페이지 소개
- ### 메인 페이지
  ![image](https://github.com/l22hs2/Pyeon-Mo-A/assets/90748701/7da8eb45-4cec-432b-9461-d0eb7d72db87)
  ℹ **검색 :** 검색한 상품명을 3사 편의점 행사 목록에서 조회합니다.
  
  ℹ **최근 작성된 댓글 :** 상품 상세 페이지에 작성된 최근 5개의 댓글을 보여줍니다.
  
  ℹ **편의점 별 BEST 3 :** 각 편의점 별 추천수가 높은 상품 TOP 3를 보여줍니다.

- ### 상품 목록
  ![image](https://github.com/l22hs2/Pyeon-Mo-A/assets/90748701/2730afbf-4867-4598-90b0-4bb51e53852d)
  ℹ **헤더 :** 편의점 상표와 행사 상품 개수를 보여줍니다.
  
  ℹ **정렬 :** 행사 상품들을 추천 순, 가격 순으로 정렬하여 보여줍니다.
  
  ℹ **상품 :** 상품에 대한 정보를 표시합니다. 클릭 시 상세 페이지로 이동합니다.

- ### 상품 상세 페이지
  ![image](https://github.com/l22hs2/Pyeon-Mo-A/assets/90748701/574af884-b0ca-4e7c-a016-113e33dcb450)
  ℹ **상품 추천하기 :** 해당 상품을 추천 합니다. 추천 수가 높으면 메인 페이지에 상품을 노출시킵니다.
  
  ℹ **댓글 :** 상품에 대한 정보를 공유할 수 있습니다. 최근 작성 된 댓글은 메인 페이지에 노출됩니다.
