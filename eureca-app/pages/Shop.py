import streamlit as st
import pandas as pd

#타이틀 & 이모티콘
st.markdown("<h1 style='text-align: center;'>Shop</h1>", unsafe_allow_html=True)

#구분선
st.divider()

#데이터 삽입
def create_streamlit_app():
    # Sidebar for category selection
    category = st.sidebar.selectbox("Shop", ["Lens-me", "O-lens", "Idol-lens", "HapaKristin"])

    #이미지 첨부
    img_url = {
        "Lens-me": "https://i.ytimg.com/vi/aRrlD-9WIbk/maxresdefault.jpg",
        "O-lens": "https://o-lens.com/images/share_image.png",
        "Idol-lens": "https://www.lensgogo.biz/wp-content/uploads/2021/08/%EC%95%84%EC%9D%B4%EB%8F%8C%EB%B0%B0%EB%84%88.jpg",
        "HapaKristin": "https://cdn.winc.app/uploads/ppb/file/file/7926/KR_2023%EB%B8%94%ED%94%84_pcbn-44a881.jpg"
    }
    
    if category in img_url:
        st.header(f"{category} Products")
        st.image(img_url[category])


    # Setting the title based on the selected category
    if category == "Lens-me":
        st.header("Lens-me Product")
        # Data and DataFrame for Lens-me
        lens_me_data = [
    ("유스 원데이 블랙", "13.0mm", "18,000"),
    ("유스 원데이 쵸코", "13.0mm", "18,000"),
    ("유스 원데이 그레이", "13.0mm", "18,000"),
    ("오리지널 원데이 시리즈 베이블리 그레이(10P)", "13.4mm", "18,000"),
    ("악마 원데이 러버블 쵸코", "13.0mm", "55,000"),
    ("악마 원데이 러버블 그레이", "13.0mm", "55,000"),
    ("오리지널 원데이 시리즈 베이블리 브라운(10P)", "13.4mm", "18,000"),
    ("오리지널 원데이 시리즈 아이듀 톤업브라운(10P)", "13.0mm", "18,000"),
    ("메이크오버 원데이 베이블리 브라운(20P)", "13.4mm", "32,000"),
    ("악마 원데이 클로링 브라운", "13.2mm", "55,000"),
    ("악마 원데이 리얼핏 3칼라 브라운", "13.5mm", "55,000"),
    ("오리지널 원데이 시리즈 릴문스킨 브라운(10P)", "13.2mm", "18,000"),
    ("메이크오버 원데이 홀리브 브라운(20P)", "13.8mm", "32,000"),
    ("메이크오버 원데이 위키 브라운(20P)", "13.8mm", "32,000"),
    ("오리지널 원데이 시리즈 블론티 브라운(10P)", "13.3mm", "18,000"),
    ("오리지널 원데이 시리즈 아이듀 톤업브라운(30P)", "13.0mm", "36,000"),
    ("리얼썸 3칼라 원데이 브라운", "13.7mm", "36,000"),
    ("노블미스틱 원데이 리얼썸 브라운 (30p)", "12.9mm", "36,000"),
    ("악마 원데이 홀로리스 진저브라운", "13.2mm", "55,000"),
    ("메이크오버 원데이 위키 브라운(4P)", "13.8mm", "9,000"),
    ("메이크오버 원데이 이브니티 브라운(4P)", "13.0mm", "9,000"),
    ("악마 원데이 리얼핏 홍채 브라운", "12.1mm", "55,000"),
    ("메이크오버 원데이 베이블리 브라운(4P)", "13.4mm", "9,000"),
    ("메이크오버 원데이 홀리브 브라운(4P)", "13.8mm", "9,000"),
    ("노블미스틱 원데이 리얼썸 브라운 (10p)", "12.9mm", "18,000"),
    ("악마 원데이 클로링 그레이", "13.2mm", "55,000"),
    ("악마 원데이 리얼핏 홍채 그레이", "12.1mm", "55,000"),
    ("악마 원데이 그란데 그레이", "13.9mm", "55,000"),
    ("메이크오버 원데이 폴리탄 그레이(4P)", "13.9mm", "9,000"),
    ("메이크오버 원데이 홀리브 그레이(4P)", "13.8mm", "9,000"),
    ("메이크오버 원데이 폴리탄 그레이(20P)", "13.9mm", "32,000"),
    ("리얼썸 3칼라 원데이 그레이", "13.7mm", "36,000"),
    ("메이크오버 원데이 홀리브 그레이(20P)", "13.8mm", "32,000"),
    ("악마 원데이 홀로리스 마일드그레이", "13.2mm", "55,000"),
    ("메이크오버 원데이 밀킨 그레이(20P)", "13.7mm", "32,000"),
    ("악마 원데이 리얼핏 3칼라 그레이", "13.5mm", "55,000"),
    ("메이크오버 원데이 베스니티 그레이(4P)", "13.5mm", "9,000"),
    ("메이크오버 원데이 유럽퀸 그레이(4P)", "13.0mm", "9,000"),
    ("오리지널 원데이 시리즈 프리니 쵸코(10P)", "13.2mm", "18,000"),
    ("칵테일 원데이 애쉬 그레이 (20p)", "13.1mm", "15,000"),
    ("악마 원데이 그란데 쵸코브라운", "13.9mm", "55,000"),
    ("오리지널 원데이 시리즈 블론티 밀크쵸코(30P)", "13.3mm", "36,000"),
    ("악마 원데이 리얼핏 홍채 쵸코", "12.1mm", "55,000"),
    ("메이크오버 원데이 윈블 쵸코(4P)", "13.2mm", "9,000"),
    ("악마 원데이 홀로리스 무스쵸코", "13.1mm", "55,000"),
    ("오리지널 원데이 시리즈 블론티 밀크쵸코(10P)", "13.3mm", "18,000"),
    ("노블미스틱 원데이 리얼썸 쵸코 (10p)", "12.9mm", "18,000"),
    ("리얼썸 원데이 다크쵸코", "13.5mm", "36,000"),
    ("메이크오버 원데이 밀킨 그레이(4P)", "13.7mm", "9,000"),
    ("노블미스틱 원데이 리얼썸 쵸코 (30p)", "12.9mm", "36,000"),
    ("퍼스핏 원데이 에어클리어(10P)", "", "13,000"),
    ("프레쉬콘 데일리 워터핏", "", "36,000"),
    ("트루핏 클리어 원데이", "", "55,000"),
    ("악마 원데이 홀로리스 클래식블랙", "13.0mm", "55,000"),
    ("악마 원데이 클로링 블랙", "13.2mm", "55,000"),
    ("리얼썸 블랙(10P)", "12.7mm", "18,000"),
    ("악마 원데이 홀로리스 핑크", "13.2mm", "55,000"),
    ("칵테일 원데이 셔벗 브라운 (20p)", "13.1mm", "15,000"),
    ("칵테일 원데이 애쉬 그레이 (10p)", "13.1mm", "10,000"),
    ("칵테일 원데이 드라이 그레이 (20p)", "13.1mm", "15,000"),
    ("악마 원데이 그란데 쵸코브라운", "13.9mm", "55,000"),
    ("오리지널 원데이 시리즈 블론티 밀크쵸코(30P)", "13.3mm", "36,000"),
    ("악마 원데이 리얼핏 홍채 쵸코", "12.1mm", "55,000"),
    ("메이크오버 원데이 윈블 쵸코(4P)", "13.2mm", "9,000"),
    ("악마 원데이 홀로리스 무스쵸코", "13.1mm", "55,000"),
    ("오리지널 원데이 시리즈 블론티 밀크쵸코(10P)", "13.3mm", "18,000"),
    ("노블미스틱 원데이 리얼썸 쵸코 (10p)", "12.9mm", "18,000"),
    ("리얼썸 원데이 다크쵸코", "13.5mm", "36,000"),
    ("메이크오버 원데이 밀킨 그레이(4P)", "13.7mm", "9,000"),
    ("노블미스틱 원데이 리얼썸 쵸코 (30p)", "12.9mm", "36,000"),
    ("퍼스핏 원데이 에어클리어(10P)", "", "13,000"),
    ("프레쉬콘 데일리 워터핏", "", "36,000"),
    ("트루핏 클리어 원데이", "", "55,000"),
    ("악마 원데이 홀로리스 클래식블랙", "13.0mm", "55,000"),
    ("악마 원데이 클로링 블랙", "13.2mm", "55,000"),
    ("리얼썸 블랙(10P)", "12.7mm", "18,000"),
    ("악마 원데이 홀로리스 핑크", "13.2mm", "55,000"),
    ("칵테일 원데이 셔벗 브라운 (20p)", "13.1mm", "15,000"),
    ("칵테일 원데이 애쉬 그레이 (10p)", "13.1mm", "10,000"),
    ("칵테일 원데이 드라이 그레이 (20p)", "13.1mm", "15,000"),
    ("[한국알콘] 데일리스 뉴 아쿠아", "25,000", ""),
    ("[인터로조] 클라렌 오투오투 원데이 블렌딩 로즈", "13.0mm", "39,000"),
    ("[인터로조] 클라렌 아이리스 재즈블랙", "12.9mm", "15,000"),
    ("칵테일 원데이 스위트 브라운 (20p)", "13.1mm", "15,000"),
    ("칵테일 원데이 셔벗 브라운 (10p)", "13.1mm", "10,000"),
    ("칵테일 원데이 드라이 그레이 (10p)", "13.1mm", "10,000"),
    ("[한국알콘]데일리스 토탈원(워터렌즈)", "", "57,000"),
    ("[바슈롬] 레이셀 스파클링 블랙", "12.7mm", "17,000"),
    ("[인터로조] 클라렌 1Day", "", "30,000"),
    ("[아큐브] 모이스트 원데이", "", "102,000"),
    ("칵테일 원데이 스위트 브라운 (10p)", "13.1mm", "10,000"),
    ("[쿠퍼비젼] 클래리티 원데이", "", "40,000"),
    ("[바슈롬] 내츄렐 (퓨어 블랙)", "12.6mm", "49,000"),
    ("[바슈롬] 레이셀 컬러스 애쉬 바이올렛", "12.9mm", "49,000"),
    ("[쿠퍼비젼] 프로클리어 원데이", "", "30,000"),
    ("[한국알콘]데일리스 토탈원(워터렌즈)", "", "153,000"),
    ("노블샤인 프로즌 원데이 그레이", "13.5mm", "15,000"),
    ("[아큐브] 디파인 래디언트 브라이트 쵸코", "12.7mm", "49,000"),
    ("노블샤인 멜팅 원데이 브라운", "13.5mm", "15,000"),
    ("[바슈롬] 레이셀 컬러스 마르살라 핑크", "12.9mm", "49,000"),
    ("[한국알콘] 프리시전원", "", "45,000"),
    ("[아큐브] 디파인 액센트 스타일 블랙", "12.5mm", "136,000"),
    ("[아큐브] 디파인 액센트 스타일 블랙", "12.5mm", "53,000"),
    ("[인터로조] 클라렌 프리덤380", "", "32,000"),
    ("[인터로조] 아스트라 글리터", "12.7mm", "45,000"),
    ("[인터로조] 클라렌 원데이", "", "76,000"),
    ("[바슈롬] 레이셀 스파클링 블랙", "12.7mm", "49,000"),
    ("[아큐브] 디파인 비비드 스타일 쵸코", "12.8mm", "53,000"),
    ("[한국알콘] 프리시전원", "", "45,000"),
    ("[아큐브] 디파인 액센트 스타일 블랙", "12.5mm", "136,000"),
    ("[아큐브] 디파인 액센트 스타일 블랙", "12.5mm", "53,000"),
    ("[인터로조] 클라렌 프리덤380", "", "32,000"),
    ("[인터로조] 아스트라 글리터", "12.7mm", "45,000"),
    ("[인터로조] 클라렌 원데이", "", "76,000"),
    ("[바슈롬] 레이셀 스파클링 블랙", "12.7mm", "49,000"),
    ("[아큐브] 디파인 비비드 스타일 쵸코", "12.8mm", "53,000"),
    ("[바슈롬] 내츄렐 (퓨어 블랙)", "12.6mm", "125,000"),
    ("[인터로조] 클라렌 아이리스 재즈블랙", "12.9mm", "48,000"),
    ("[바슈롬] 레이셀 스파클링 블랙", "12.7mm", "50,000"),
    ("[바슈롬] 울트라 원데이", "", "140,000"),
    ("[쿠퍼비젼] 클래리티 원데이", "", "96,000"),
    ("[쿠퍼비젼] 프로클리어 원데이", "", "69,000"),
    ("[바슈롬] 울트라 원데이", "", "55,000"),
    ("[바슈롬] 소프렌 데일리 (30P)", "", "39,000"),
    ("[쿠퍼비젼] 프로클리어 원데이 멀티포컬", "", "49,000"),
    ("[바슈롬] 바이오트루 (30P)", "", "48,000"),
    ("[바슈롬] 바이오트루 (90P)", "", "116,000"),
    ("[쿠퍼비젼] 마이데이(30P)", "", "49,000"),
    ("[쿠퍼비젼] 마이데이(90P)", "", "125,000"),
    ("[인터로조] 클라렌 오투오투 원데이 세피아 쵸코", "12.9mm", "39,000"),
    ("[인터로조] 클라렌 오투오투 원데이 애쉬 그레이", "12.9mm", "39,000"),
    ("[인터로조] 클라렌 오투오투 원데이 애쉬 브라운", "12.9mm", "39,000"),
    ("[인터로조] 클라렌 오투오투 원데이 블렌딩 헤이즐", "13.0mm", "39,000"),
    ("[인터로조] 클라렌 수지그레이 (30P)", "12.9mm", "48,000"),
    ("[인터로조] 클라렌 수지그레이 (90P)", "12.9mm", "118,000"),
    ("[한국알콘] 후레쉬룩 얼루어 그레이", "13.2mm", "45,000"),
    ("바슈롬 레이셀 글리터링 그레이", "12.9mm", "49,000"),
    ("[인터로조] 아스트라 에스텔 그레이", "13.0mm", "50,000"),
    ("바슈롬 레이셀 미스틱 그레이", "12.9mm", "49,000"),
    ("[인터로조] 아스트라 에스텔 브라운", "13.0mm", "50,000"),
    ("[인터로조] 클라렌 아이리스 소울브라운", "", "15,000"),
    ("[바슈롬] 레이셀 베이비 브라운", "12.2mm", "49,000"),
    ("[한국알콘] 후레쉬룩 그레이", "12.7mm", "30,000"),
    ("[바슈롬] 레이셀 트윙클 브라운", "12.7mm", "17,000"),
    ("[인터로조] 클라렌 아이리스 랩소디", "12.7mm", "15,000"),
    ("[인터로조] 클라렌 수지브라운 (30P)", "12.9mm", "48,000"),
    ("[인터로조] 클라렌 아이리스 라틴", "12.7mm", "15,000"),
    ("[바슈롬] 내츄렐 (시크 브라운)", "12.8mm", "49,000"),
    ("[한국알콘] 후레쉬룩 퓨어 헤이즐", "12.7mm", "30,000"),
    ("[바슈롬] 레이셀 쉬머링 골드", "12.9mm", "17,000"),
    ("[한국알콘] 후레쉬룩 일루미네이트 리치브라운", "12.8mm", "45,000"),
    ("[인터로조] 클라렌 아이리스 소울브라운", "", "97,000"),
    ("[바슈롬] 레이셀 밤비 브라운", "12.7mm", "49,000"),
    ("[한국알콘] 후레쉬룩 얼루어 헤이즐", "13.2mm", "45,000"),
    ("[인터로조] 클라렌 아이리스 랩소디", "12.7mm", "97,000"),
    ("[인터로조] 클라렌 수지브라운 (90P)", "12.9mm", "118,000"),
    ("[인터로조] 클라렌 아이리스 소울브라운", "", "48,000"),
    ("[바슈롬] 레이셀 트윙클 브라운", "12.7mm", "29,000"),
    ("[바슈롬] 레이셀 디어 브라운", "12.9mm", "49,000"),
    ("바슈롬 레이셀 멜로우 브라운", "12.9mm", "49,000"),
    ("[바슈롬] 내츄렐 (시크 브라운)", "12.8mm", "125,000"),
    ("알리샤브라운", "12.7mm", "48,000"),
    ("[바슈롬] 레이셀 쉬머링 골드", "12.9mm", "49,000"),
    ("[인터로조] 클라렌 블루문 블루그레이", "12.9mm", "48,000"),
    ("[한국알콘] 후레쉬룩 얼루어 블루", "13.2mm", "45,000"),
    ("[바슈롬] 레이셀 크리스탈 브라운", "12.7mm", "17,000"),
    ("[아큐브] 디파인 래디언트 차밍 그레이", "12.7mm", "49,000"),
    ("[아큐브] 디파인 래디언트 브라이트 쵸코", "12.7mm", "132,000"),
    ("[아큐브] 디파인 래디언트 차밍 그레이", "12.7mm", "132,000"),
    ("[아큐브] 디파인 래디언트 시크 브라운", "12.7mm", "49,000"),
    ("[아큐브] 디파인 샤인 브라운", "12.7mm", "53,000"),
    ("[아큐브] 디파인 래디언트 스윗 브라운", "12.7mm", "132,000"),
    ("[인터로조] 클라렌 아이리스 랩소디", "12.7mm", "48,000"),
    ("[아큐브] 디파인 비비드 스타일 쵸코", "12.8mm", "136,000"),
    ("[아큐브] 디파인 래디언트 스윗 브라운", "12.7mm", "49,000"),
    ("[바슈롬] 레이셀 크리스탈 브라운", "12.7mm", "49,000"),
    ("[인터로조] 클라렌 아이리스 라틴", "12.7mm", "48,000"),
    ("[아큐브] 디파인 래디언트 시크 브라운", "12.7mm", "132,000"),
    ("[아큐브] 디파인 샤인 브라운", "12.7mm", "136,000")
        ]
        df = pd.DataFrame(lens_me_data, columns=["Product Name", "Lens Size", "Product Price"])
    
    elif category == "O-lens":
        st.header("O-lens Product")
        # Data and DataFrame for O-lens
        O_lens_data = [
("워터파인","(40P)","40,000","14.0mm (1Day 권장)"),
("샤인터치 밀키브라운","(20P)","34,000","12.7mm (1Day 권장)"),
("샤인터치 밀키그레이","(20P)","34,000","12.7mm (1Day 권장)"),
("샤인터치 밀키초코","(20P)","34,000","12.7mm (1Day 권장)"),
("미스티 애쉬초코","(20P)","34,000","13.1mm (1Day 권장)"),
("미스티 골드민트","(20P)","34,000","13.1mm (1Day 권장)"),
("에버샤인 모카","(20P)","34,000","13.8mm (1Day 권장)"),
("샤인블랙","(20P)","34,000","13.0mm (1Day 권장)"),
("엔딩 브라운","(20P)","34,000","13.2mm (1Day 권장)"),
("엔딩 그레이","(20P)","34,000","13.2mm (1Day 권장)"),
("에버샤인 그레이","(20P)","34,000","13.8mm (1Day 권장)"),
("에버샤인 브라운","(20P)","34,000","13.8mm (1Day 권장)"),
("닐스 브라운","(20P)","34,000","13.5mm (1Day 권장)"),
("닐스 그레이","(20P)","34,000","13.5mm (1Day 권장)"),
("글로이 내츄럴 원데이 라떼브라운","(20P)","34,000","13.0mm (1Day 권장)"),
("글로이 내츄럴 원데이 모카브라운","(20P)","34,000","13.0mm (1Day 권장)"),
("프렌치샤인 원데이 헤이즐","(20P)","34,000","13.2mm (1Day 권장)"),
("프렌치샤인 원데이 그레이","(20P)","34,000","13.2mm (1Day 권장)"),
("더블틴트 원데이 그레이","(20P)","34,000","12.9mm (1Day 권장)"),
("더블틴트 원데이 브라운","(20P)","34,000","12.9mm (1Day 권장)"),
("리얼링 원데이 브라운","(20P)","34,000","12.5mm (1Day 권장)"),
("리얼링 원데이 그레이","(20P)","34,000","12.5mm (1Day 권장)"),
("무드나잇 원데이 무드그레이","(20P)","34,000","13.3mm (1Day 권장)"),
("무드나잇 원데이 무드브라운","(20P)","34,000","13.3mm (1Day 권장)"),
("글로이 원데이 브라운","(20P)","34,000","13.1mm (1Day 권장)"),
("글로이 원데이 블랙","(20P)","34,000","13.1mm (1Day 권장)"),
("비비링 원데이 그레이","(20P)","34,000","13.0mm (1Day 권장)"),
("시크리스 3콘 코랄 브라운","(20P)","34,000","13.5mm (1Day 권장)"),
("위드썸 브라운","(20P)","34,000","13.8mm (1Day 권장)"),
("시크리스 3콘 코랄 그레이","(20P)","34,000","13.5mm (1Day 권장)"),
("미스티 로맨틱헤이즐","(20P)","34,000","13.5mm (1Day 권장)"),
("비비링 원데이 브라운(20P)","(10P)","18,000","13.0mm (1Day 권장)"),
("미스티 로맨틱초코","(20P)","34,000","13.2mm (1Day 권장)"),
("스칸디 원데이 헤이즐","(20P)","34,000","11.9mm (1Day 권장)"),
("스칸디 원데이 그레이","(20P)","34,000","11.9mm (1Day 권장)"),
("비비링 원데이 초코(20P)","(10P)","18,000","13.0mm (1Day 권장)"),
("오투에디션","(10P)","12,000","14.2mm (1Day 권장)"),
("스칼렛(10P)","(10P)","25,000","14.5mm (1Day 권장)"),
("엔딩 올리브(10P)","(10P)","18,000","13.2mm (1Day 권장)"),
("오션벨벳 원데이 헤이즐","(10P)","18,000","13.0mm (1Day 권장)"),
("오션벨벳 원데이 그레이","(10P)","18,000","13.0mm (1Day 권장)"),
("오션벨벳 원데이 그린","(10P)","18,000","13.0mm (1Day 권장)"),
("비비링 원데이 스모크(20P)","(10P)","18,000","13.0mm (1Day 권장)"),
("마스터안 그레이(10P)","(10P)","22,000","13.3mm (1Day 권장)"),
("비비링 원데이 그린(20P)","(10P)","18,000","13.0mm (1Day 권장)"),
("스카이레벨 브라운(10P)","(10P)","18,000","13.2mm (1Day 권장)"),
("에버샤인 모카(10P)","(10P)","18,000","13.8mm (1Day 권장)"),
("오션벨벳 원데이 브라운","(10P)","18,000","13.0mm (1Day 권장)"),
("미스티 베이비핑크(10P)","(10P)","25,000","13.5mm (1Day 권장)"),
("무드나잇 원데이 무드브라운","(10P)","18,000","13.3mm (1Day 권장)"),
("그라마 그레이(10P)","(10P)","18,000","13.0mm (1Day 권장)"),
("미스티 베이비핑크(20P)","(10P)","25,000","13.5mm (1Day 권장)"),
("위드썸 브라운(10P)","(10P)","18,000","13.8mm (1Day 권장)"),
("에버샤인 그레이(10P)","(10P)","18,000","13.8mm (1Day 권장)"),
("글로이 원데이 블랙(20P)","(10P)","18,000","13.1mm (1Day 권장)"),
("비비링 원데이 블랙(20P)","(10P)","18,000","13.0mm (1Day 권장)"),
("샤인터치 밀키브라운(10P)","(10P)","18,000","12.7mm (1Day 권장)"),
("스카이레벨 블랙(10P)","(10P)","18,000","13.2mm (1Day 권장)"),
("미스티 베이비브라운(10P)","(10P)","25,000","13.5mm (1Day 권장)"),
("닐스 브라운(10P)","(10P)","18,000","13.5mm (1Day 권장)"),
("글로이 내츄럴 원데이 라떼브라운","(10P)","18,000","13.0mm (1Day 권장)"),
("프렌치샤인 원데이 그레이(20P)","(10P)","18,000","13.2mm (1Day 권장)"),
("리얼링 원데이 그레이(20P)","(10P)","18,000","12.5mm (1Day 권장)"),
("시크리스 3콘 코랄 브라운(20P)","(10P)","22,000","13.5mm (1Day 권장)"),
("스칸디 원데이 헤이즐(20P)","(10P)","22,000","11.9mm (1Day 권장)"),
("위드썸 브라운(20P)","(10P)","22,000","13.8mm (1Day 권장)"),
("닐스 그레이(10P)","(10P)","18,000","13.5mm (1Day 권장)"),
("프렌치샤인 원데이 헤이즐(20P)","(10P)","22,000","13.2mm (1Day 권장)"),
("프렌치샤인 원데이 그레이(10P)","(10P)","18,000","13.2mm (1Day 권장)"),
("비비링 원데이 그레이(20P)","(10P)","18,000","13.0mm (1Day 권장)"),
("글로이 내츄럴 원데이 라떼브라운(20P)","(10P)","18,000","13.0mm (1Day 권장)"),
("위드썸 브라운(20P)","(10P)","22,000","13.8mm (1Day 권장)"),
("엔딩 브라운(10P)","(10P)","18,000","13.2mm (1Day 권장)"),
("미스티 골드민트(10P)","(10P)","18,000","13.1mm (1Day 권장)"),
("샤인터치 밀키초코(10P)","(10P)","18,000","12.7mm (1Day 권장)"),
("미스티 애쉬초코(10P)","(10P)","18,000","13.1mm (1Day 권장)"),
("글로이 내츄럴 원데이 라떼브라운(20P)","(10P)","18,000","13.0mm (1Day 권장)"),
("비비링 원데이 초코(10P)","(10P)","18,000","13.0mm (1Day 권장)"),
("더블틴트 원데이 그레이(20P)","(10P)","22,000","12.9mm (1Day 권장)"),
("더블틴트 원데이 브라운(20P)","(10P)","22,000","12.9mm (1Day 권장)"),
("프렌치샤인 원데이 그레이(10P)","(10P)","18,000","13.2mm (1Day 권장)"),
("미스티 로맨틱초코","(20P)","34,000","13.2mm (1Day 권장)")
        ]
        df = pd.DataFrame(O_lens_data, columns=["Product Name", "Product composition", "Product Price", "Lens Size"])

    elif category == "Idol-lens":
        st.header("Idol-lens Product")
        # Data and DataFrame for Idol-lens
        idol_lens_data = [
            ("YURIAL MAX - EARL GRAY 예약수령", "26,000원", "BC : 8.7mm / DIA : 14.2mm / G.SIZE : 13.3mm / Water : 43%", " 사용기간 : 1개월"),
("YURIAL MAX - WATER BROWN 예약수령", "26,000원", "BC : 8.7mm / DIA : 14.2mm / G.SIZE : 13.3mm / Water : 43%", " 사용기간 : 1개월"),
("EURORING - WATERY GRAY 예약수령", "30,000원", "DIA:14.0mm / GRAPHIC SIZE:13.0mm", " 6~12months"),
("EURORING - MINERAL GRAY 예약수령", "30,000원", "DIA:14.0mm / GRAPHIC SIZE:13.0mm", " 6~12months"),
("EURORING - MEL BEIGE 예약수령", "30,000원", "DIA:14.0mm / GRAPHIC SIZE:13.0mm", " 6~12months"),
("유리알 원데이 얼그레이 2팩 할인 이벤트", "33,000원", "DIA:14.2mm/GRAPHIC SIZE:13.2mm/1Day/1팩 10p", ""),
("유리알 원데이 맑은브라운 2팩 할인 이벤트", "33,000원", "DIA:14.2mm/GRAPHIC SIZE:13.2mm/1Day/1팩 10p", ""),
("칸나로제 원데이 베이지브라운 2팩 할인 이벤트", "33,000원", "DIA:14.2mm/GRAPHIC SIZE:13.2mm/1Day/1팩 10p", ""),
("칸나로제 원데이 누드브라운 2팩 할인 이벤트", "33,000원", "DIA:14.2mm/GRAPHIC SIZE:13.2mm/1Day/1팩 10p", ""),
("2세트 할인 이벤트(12개월)", "48,000원", "", ""),
("YURIAL 1DAY - EARL GRAY 예약수령", "20,000원", "DIA:14.2mm/GRAPHIC SIZE:13.2mm/1Day/1팩 10p", ""),
("YURIAL 1DAY - WATER BROWN 예약수령", "20,000원", "DIA:14.2mm/GRAPHIC SIZE:13.2mm/1Day/1팩 10p", ""),
("YURIAL - MUL GRAY 예약수령", "30,000원", "DIA:14.0mm / GRAPHIC SIZE:12.8mm", " 6~12months"),
("YURIAL - SERUM BROWN 예약수령", "30,000원", "DIA:14.0mm / GRAPHIC SIZE:12.8mm", " 6~12months"),
("YURIAL - ROYAL BROWN 예약수령", "30,000원", "DIA:14.0mm / GRAPHIC SIZE:12.8mm", " 6~12months"),
("YURIAL - WATER BROWN 예약수령", "30,000원", "DIA:14.0mm / GRAPHIC SIZE:12.8mm", " 6~12months"),
("YURIAL - EARL GRAY 예약수령", "30,000원", "DIA:14.0mm / GRAPHIC SIZE:12.8mm", " 6~12months"),
("CANNA ROZE 1DAY - NUDE BROWN 예약수령", "20,000원", "DIA:14.2mm/GRAPHIC SIZE:13.2mm/1Day/1팩 10p", ""),
("CANNA ROZE 1DAY - BEIGE BROWN 예약수령", "20,000원", "DIA:14.2mm/GRAPHIC SIZE:13.2mm/1Day/1팩 10p", ""),
("PRO1.5 - CARAMEL BROWN 예약수령", "32,000원", "DIA:14.0mm/GRAPHIC SIZE:13.1mm", " 6~12months"),
("PRO1.5 - CHARCOAL GRAY 예약수령", "32,000원", "DIA:14.0mm/GRAPHIC SIZE:13.1mm", " 6~12months"),
("PRO1.5 - PEACH BROWN 예약수령", "32,000원", "DIA:14.0mm/GRAPHIC SIZE:13.1mm", " 6~12months"),
("ROZE AIRY - BLUE BLACK 예약수령", "26,000원", "DIA:14.2mm GRAPHIC:13.2mm 실리콘폴리머렌즈", " 권장 사용:1개월"),
("ROZE AIRY - BABY BROWN 예약수령", "26,000원", "DIA:14.2mm GRAPHIC:13.2mm 실리콘폴리머렌즈", " 권장 사용:1개월"),
("ROZE AIRY - OLIVE GREEN 예약수령", "26,000원", "DIA:14.2mm GRAPHIC:13.2mm 실리콘폴리머렌즈", " 권장 사용:1개월")
        ]
        df = pd.DataFrame(idol_lens_data, columns=["Product Name", "Product Price", "Lens Size", "Use period"])

    elif category == "HapaKristin":
        st.header("HapaKristin Product")
        # Data and DataFrame for HapaKristin
        hapa_kristin_data = [
            ("쇼퍼홀릭 크리스틴 - 미드나잇 그레이", "한달용", "13mm(14.2mm)", ""),
    ("웨이크업 크리스틴 원데이 - 던 브라운", "원데이", "12.7mm(14.2mm)", "19,000원"),
    ("[포카증정] 쇼퍼홀릭&웨이크업 세트 기획", "한달용", "전 직경", "50,000원"),
    ("원앤온리 크리스틴 원데이 - 그레이", "원데이", "13mm(14.2mm)", "19,000원"),
    ("슈거하이 크리스틴 원데이 - 애쉬 초코", "원데이", "13mm(14.2mm)", "19,000원"),
    ("쇼퍼홀릭 크리스틴 원데이 - 미드나잇 그레이", "원데이", "13mm(14.2mm)", ""),
    ("비터스윗 크리스틴 - 올리브 브라운", "한달용", "12.4mm(14.2mm)", "25,000원"),
    ("웨이크업 크리스틴 - 페일 그레이", "한달용", "12.7mm(14.2mm)", "25,000원"),
    ("본투비 크리스틴 - 그레이", "한달용", "12.4mm(14.2mm)", "25,000원"),
    ("하파 트라이얼 미니 세트 - 시그니처 세트", "원데이", "전 직경", ""),
    ("본투비 크리스틴 - 브라운", "한달용", "12.4mm(14.2mm)", "25,000원"),
    ("하파 트라이얼 미니 세트 - 내추럴 톤업 세트", "원데이", "전 직경", ""),
    ("퍼스트러브 크리스틴 원데이 - 브라운", "원데이", "12.5mm(14.2mm)", "19,000원"),
    ("비터스윗 크리스틴 원데이 - 올리브 브라운", "원데이", "12.4mm(14.2mm)", "19,000원"),
    ("원앤온리 크리스틴 원데이 - 브라운", "원데이", "13mm(14.2mm)", "19,000원"),
    ("하파 트라이얼 세트 - AtoZ 직경 스펙트럼 세트", "원데이", "전 직경", ""),
    ("글레이즈드 크리스틴 한달용 - 초코", "한달용", "12.9mm(14.2mm)", "25,000원"),
    ("퍼스트러브 크리스틴 한달용 - 브라운", "한달용", "12.5mm(14.2mm)", "25,000원"),
    ("하파 트라이얼 미니 세트 - 브라운 러버 세트 Vol.2", "원데이", "전 직경", ""),
    ("비터스윗 크리스틴 원데이 - 앰버 브라운", "원데이", "12.4mm(14.2mm)", "19,000원"),
    ("비터스윗 크리스틴 - 앰버 브라운", "25,000원", "한달용", "12.4mm(14.2mm)"),
    ("글레이즈드 크리스틴 난시용 원데이 - 초코", "30,000원", "원데이", "12.9mm(14.2mm)"),
    ("블러 크리스틴 원데이 - 블랙", "19,000원", "원데이", "12.8mm(14.2mm)"),
    ("듀이 크리스틴 베이직 - 그레이", "25,000원", "한달용", "12mm(14mm)"),
    ("원앤온리 크리스틴 - 베이지", "25,000원", "한달용", "13mm(14.2mm)"),
    ("그레이 러버 세트", "", "원데이", "13mm(14.2mm)"),
    ("원앤온리 크리스틴 원데이 - 베이지", "19,000원", "원데이", "13mm(14.2mm)"),
    ("시스루 크리스틴 원데이 - 초코", "19,000원", "원데이", "13mm(14.2mm)"),
    ("오엠지 크리스틴 - 그레이", "19,000원", "원데이", "13.2mm(14.2mm)"),
    ("시크리티브 크리스틴 - 브라운", "25,000원", "한달용", "13mm(14.2mm)"),
    ("시크리티브 크리스틴 원데이 - 앤티크 브라운", "19,000원", "원데이", "13mm(14.2mm)"),
    ("듀이 크리스틴 원데이 - 브라운", "19,000원", "원데이", "11.8mm(14.2mm)"),
    ("듀이 크리스틴 베이직 - 브라운", "25,000원", "한달용", "12mm(14mm)"),
    ("원앤온리 크리스틴 - 그레이", "25,000원", "한달용", "13mm(14.2mm)"),
    ("원앤온리 크리스틴 플러스 - 브라운", "25,000원", "한달용", "13.5mm(14.2mm)"),
    ("글레이즈드 크리스틴 난시용 원데이 - 초코", "30,000원", "원데이", "12.9mm(14.2mm)"),
    ("시크리티브 크리스틴 원데이 - 더스크 브라운", "19,000원", "원데이", "13mm(14.2mm)"),
    ("글레이즈드 크리스틴 원데이 - 초코", "19,000원", "원데이", "12.9mm(14.2mm)"),
    ("피스풀 크리스틴 - 헤이즐", "25,000원", "한달용", "13.3mm(14mm)"),
    ("시크리티브 크리스틴 - 블랙", "25,000원", "한달용", "13mm(14.2mm)"),
    ("오엠지 크리스틴 - 헤이즐", "원데이", "13.2mm(14.2mm)", "19,000원"),
    ("시크리티브 크리스틴 원데이 - 크러시 브라운", "원데이", "13mm(14.2mm)", "19,000원"),
    ("시스루 크리스틴 원데이 - 애쉬 브라운", "원데이", "13mm(14.2mm)", "19,000원"),
    ("시크리티브 크리스틴 - 그레이", "한달용", "13mm(14.2mm)", "25,000원"),
    ("시크리티브 크리스틴 플러스 원데이 - 올리브", "원데이", "13.5mm(14.2mm)", "19,000원"),
    ("피스풀 크리스틴 - 브라운", "한달용", "13.3mm(14mm)", "25,000원"),
    ("어도러블 크리스틴 - 그레이", "원데이", "13.4mm(14.2mm)", "19,000원"),
    ("슈거하이 크리스틴 - 베이지", "한달용", "13mm(14mm)", "25,000원"),
    ("욜로 크리스틴 - 그린", "원데이", "13.4mm(14.2mm)", "19,000원"),
    ("시크리티브 크리스틴 원데이 - 크렘 브라운", "원데이", "13mm(14.2mm)", "19,000원"),
    ("시크리티브 크리스틴 - 올리브", "한달용", "13mm(14.2mm)", "25,000원"),
    ("티타임 크리스틴 - 브라운", "한달용", "13.1mm(14.2mm)", "25,000원"),
    ("에이투지 크리스틴 원데이 - 브라운 (12.7)", "원데이", "12.7mm(14.2mm)", "19,000원"),
    ("에이투지 크리스틴 - 브라운 (13.0)", "한달용", "13mm(14.2mm)", "25,000원"),
    ("시크리티브 크리스틴 - 베이지", "한달용", "13mm(14.2mm)", "25,000원"),
    ("시크리티브 크리스틴 플러스(13.5) - 브라운", "한달용", "13.5mm(14.2mm)", "25,000원"),
    ("시스루 크리스틴 - 초코", "한달용", "13mm(14.2mm)", "25,000원"),
    ("시스루 크리스틴 플러스 원데이 - 초코", "원데이", "13.5mm(14.2mm)", "19,000원"),
    ("시크리티브 크리스틴 플러스 - 블랙", "한달용", "13.5mm(14.2mm)", "25,000원"),
    ("시크리티브 크리스틴 플러스(13.8) - 브라운", "한달용", "13.8mm(14.2mm)", "25,000원"),
    ("원앤온리 크리스틴 - 브라운", "한달용", "13mm(14.2mm)", "25,000원"),
    ("시스루 크리스틴 - 애쉬 브라운", "한달용", "13mm(14.2mm)", "25,000원"),
    ("시크리티브 크리스틴 베이직 - 올리브", "한달용", "11.6mm(14.2mm)", "25,000원"),
    ("시스루 크리스틴 - 브라운", "한달용", "13mm(14.2mm)", "25,000원"),
    ("시스루 크리스틴 - 올리브 브라운", "한달용", "13mm(14.2mm)", "25,000원"),
    ("어도러블 크리스틴 - 브라운", "원데이", "13.4mm(14.2mm)", ""),
    ("시크리티브 크리스틴 플러스 - 올리브", "한달용", "13.5mm(14.2mm)", "25,000원"),
    ("피스풀 크리스틴 - 차콜 그레이", "한달용", "13.3mm(14mm)", "25,000원"),
    ("시크리티브 크리스틴 베이직 - 브라운", "한달용", "11.6mm(14.2mm)", "25,000원"),
    ("그루비 크리스틴 - 올리브 브라운", "한달용", "12.9mm(14.2mm)", "25,000원"),
    ("돌리 크리스틴 - 그레이", "한달용", "13.6mm(14.2mm)", "25,000원"),
    ("시크리티브 크리스틴 플러스 - 그레이", "한달용", "13.5mm(14.2mm)", "25,000원"),
    ("오커 크리스틴 - 브라운", "원데이", "13.4mm(14.2mm)", "19,000원"),
    ("멜로 크리스틴 - 브라운", "한달용", "12.9mm(14.2mm)", "25,000원"),
    ("클라우디 크리스틴 - 그레이", "한달용", "13.4mm(14.2mm)", "25,000원"),
    ("피스풀 크리스틴 - 애쉬 브라운", "한달용", "13.3mm(14mm)", "25,000원"),
    ("피스풀 크리스틴 - 블루", "한달용", "13.3mm(14mm)", "25,000원"),
    ("피스풀 크리스틴 - 그린", "한달용", "13.3mm(14mm)", "25,000원"),
    ("에이투지 크리스틴 원데이 - 브라운 (12.4)", "원데이", "12.4mm(14.2mm)", "19,000원"),
    ("에이투지 크리스틴 원데이 - 브라운 (13.0)", "원데이", "13mm(14.2mm)", "19,000원"),
    ("에이투지 크리스틴 원데이 - 브라운 (13.3)", "원데이", "13.3mm(14.2mm)", "19,000원"),
    ("에이투지 크리스틴 원데이 - 브라운 (13.6)", "원데이", "13.6mm(14.2mm)", "19,000원"),
    ("에이투지 크리스틴 원데이 - 브라운 (13.9)", "원데이", "13.9mm(14.2mm)", "19,000원"),
    ("락앤롤 크리스틴 - 블루", "한달용", "12.2mm(14.2mm)", "25,000원"),
    ("블라제 크리스틴 - 그린", "한달용", "13.2mm(14.2mm)", "25,000원"),
    ("솔리터리 크리스틴 - 헤이즐", "원데이", "12.6mm(14.2mm)", "19,000원"),
    ("크리스틴 클리어", "원데이", "14.2mm(14.2mm)", "17,000원"),
    ("치어풀 크리스틴 - 브라운", "한달용", "13.3mm(14.2mm)", "25,000원"),
    ("퓨밍 크리스틴 - 블루", "한달용", "13.4mm(14.2mm)", "25,000원"),
    ("락앤롤 크리스틴 - 브라운", "한달용", "12.2mm(14.2mm)", "25,000원"),
    ("타다 크리스틴 - 그레이", "한달용", "13.1mm(14.2mm)", "25,000원"),
    ("치어풀 크리스틴 - 그린", "한달용", "13.3mm(14.2mm)", "25,000원"),
    ("실리 크리스틴 - 그레이", "한달용", "13.4mm(14.2mm)", "25,000원"),
    ("스킵더비트 크리스틴 - 그레이", "한달용", "13.8mm(14.2mm)", "25,000원"),
    ("치어풀 크리스틴 - 블루", "한달용", "13.3mm(14.2mm)", "25,000원"),
    ("고트 크리스틴 - 그린", "한달용", "12.9mm(14.2mm)", "25,000원"),
    ("고트 크리스틴 - 블루", "한달용", "12.9mm(14.2mm)", "25,000원"),
    ("러브미 크리스틴 - 브라운", "한달용", "13.2mm(14.2mm)", "25,000원"),
    ("아아! 크리스틴 - 그레이", "한달용", "12.9mm(14.2mm)", "25,000원"),
    ("아아! 크리스틴 - 브라운", "한달용", "12.9mm(14.2mm)", "25,000원"),
    ("블라제 크리스틴 - 브라운", "한달용", "13.2mm(14.2mm)", "25,000원"),
    ("아아! 크리스틴 - 바이올렛", "한달용", "12.9mm(14.2mm)", "25,000원")
        ]
        df = pd.DataFrame(hapa_kristin_data, columns=["Product Name", "Use period", "Lens Size", "Product Price"])

    # Displaying the DataFrame
    st.write(df)

if __name__ == '__main__':
    create_streamlit_app()


#프로필
st.markdown("---")
# 전체 배경색을 흰색으로 설정
st.write("""
<style>
    body {
        background-color: white;
    }
    .btn-container {
        display: flex;
        justify-content: center;  # 가운데 정렬
        align-items: center;  # 수직 가운데 정렬
        gap: 10px;  # 버튼간의 간격 조절
    }
    .btn-link {
        font-size: 14px;
        text-align: center;
        color: black !important;  # 글씨 색을 검정색으로 강제로 설정
        background-color: transparent;  # 배경색을 투명하게 설정
        border: 1px solid black;  # 테두리 추가
        padding: 5px 10px;  # 버튼 내 여백 조절
        text-decoration: none;  # 밑줄 제거
    }
</style>
""", unsafe_allow_html=True)

# 세 개의 버튼 생성 (버튼 텍스트 사이에 공백 추가)
st.markdown("""
<div class="btn-container">
    <a href='https://www.instagram.com/lensingray.official/' 
       class='btn-link'>INSTAGRAM</a>
    <span>&nbsp;</span>  <!-- 공백 추가 -->
    <span>&nbsp;</span>  <!-- 공백 추가 -->
    <span>&nbsp;</span>  <!-- 공백 추가 -->
    <span>&nbsp;</span>  <!-- 공백 추가 -->
    <span>&nbsp;</span>  <!-- 공백 추가 -->
    <a href='https://blog.naver.com/lens_in_gray' 
       class='btn-link'>BLOG</a>
    <span>&nbsp;</span>  <!-- 공백 추가 -->
    <span>&nbsp;</span>  <!-- 공백 추가 -->
    <span>&nbsp;</span>  <!-- 공백 추가 -->
    <span>&nbsp;</span>  <!-- 공백 추가 -->
    <span>&nbsp;</span>  <!-- 공백 추가 -->
    <a href='http://pf.kakao.com/_xblxexjG' 
       class='btn-link'>KAKAO CHANNEL</a>
</div>
""", unsafe_allow_html=True)


st.write(" ")
st.write("<p style='text-align: center; margin: 5px; line-height: 0.8;'><span style='font-size: 15px;'>Lens in Gray</span> <span style='font-size: 15px;'>Co.</span> <span style='font-size: 12px;'>Owner</span> <span style='font-size: 15px;'>Uquahanuqui</span> </p>", unsafe_allow_html=True)
st.write("<p style='text-align: center; margin: 5px; line-height: 0.8;'><span style='font-size: 12px;'>Business Number</span> <span style='font-size: 15px;'>20230922</span> </p>", unsafe_allow_html=True)
st.write(" ")
st.write("<p style='text-align: center; margin: 5px; line-height: 0.8;'><span style='font-size: 15px;'>CUSTOMER CARE</span></p>", unsafe_allow_html=True)
st.caption("<p style='text-align: center; margin: 5px; line-height: 0.8;'><span style='font-size: 14px;'>Phone</span> <span style='margin-right: 7px;'> </span> <span style='font-size: 14px;'>+82 10-4536-6713</span></p>", unsafe_allow_html=True)
st.caption("<p style='text-align: center; margin: 5px; line-height: 0.8;'><span style='font-size: 14px;'>Email</span> <span style='margin-right: 7px;'> </span> <span style='font-size: 14px;'>hyb0320@kookmin.ac.kr</span></p>", unsafe_allow_html=True)
st.write(" ")
st.write("<p style='text-align: center; margin: 5px; line-height: 0.8;'><span style='font-size: 15px;'>OFFICE</span></p>", unsafe_allow_html=True)
st.caption("<p style='text-align: center; margin: 5px; line-height: 0.8;'>#77 Kookmin University Management Hall, Jeongneung-ro, Seongbuk-gu, Seoul</p>", unsafe_allow_html=True)
st.caption("<p style='text-align: center; margin: 5px; line-height: 0.8;'>서울특별시 성북구 정릉로 77 국민대학교 경영관 (02707)</p>", unsafe_allow_html=True)
st.divider()
