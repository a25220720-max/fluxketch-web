#!/usr/bin/env python3
# Fluxketch site v3 — ko/en 생성기. 정본 = tools/template.html + 이 파일의 사전. 실행: python3 tools/build_site.py
import os, re, html
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FORM = "https://docs.google.com/forms/d/e/1FAIpQLSdV-CMVpm1hdJ6i37DJ2JRsa_WfrnI2mPNDxfqHYr5mrLZGgg/viewform"
ICO = {
 "learn": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19V5a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v14"/><path d="M4 19a2 2 0 0 0 2 2h14"/><path d="M8 8h8M8 12h5"/></svg>',
 "fast": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M13 2 4 14h7l-1 8 9-12h-7z"/></svg>',
 "export": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M6 9V4h12v5"/><rect x="4" y="9" width="16" height="8" rx="2"/><path d="M8 17v3h8v-3"/></svg>',
 "x": '<svg viewBox="0 0 24 24" fill="none" stroke="#8a919e" stroke-width="2" stroke-linecap="round"><path d="M6 6l12 12M18 6 6 18"/></svg>',
 "check": '<svg viewBox="0 0 24 24" fill="none" stroke="#248f54" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12l5 5L20 7"/></svg>',
}
STRIP = [  # (file, caption-key)
 ("vivienda-dark","s1"),("hotel-sheet-portrait","s2"),("layers-sheet","s3"),("casino-portrait-dark","s4"),
 ("arquitectura-sheet","s5"),("granada-topo-dark","s6"),("vivienda-markup-sheet","s7"),("callejas-sheet","s8"),
]
TABS = [  # (file, title-key)
 ("hotel-parking-sheet","t1"),("vivienda-dark","t2"),("vivienda-markup-dark","t3"),("layers-sheet","t4"),("ruler-popover","t5"),("menu-report","t6"),
]
KO = dict(
 lang="ko", path="/", home="/", alt_href="/en/", alt_lang="en", alt_label="EN", alt_full="English",
 title="Fluxketch — 현장에서 끝내는 iPad CAD", desc="DXF·DWG·PDF 도면을 iPad에서 열고, Apple Pencil로 작도·마크업·핀·노트를 얹어 축척 맞춘 PDF와 DXF로 꺼내는 현장용 CAD. 비공개 베타 진행 중.",
 og_desc="도면을 열고, 그리고, 표시하고, 꺼낸다. 전부 iPad 위에서.",
 og_locale="ko_KR", nav_guides="가이드", p_answers_btn="궁금한 것 보기", qa_eyebrow="질문과 답", steps_eyebrow="순서", rel_h2="함께 보기", crumbs_label="경로", crumb_home="홈", g_h1="현장에서 CAD를 쓰는 사람을 위한 가이드", g_lead="DWG·DXF·축척·마크업처럼 현장에서 매일 부딪히는 것을 정보 위주로 씁니다. 대부분은 어떤 앱을 쓰든 그대로 적용됩니다.", read_min="읽는 시간 약 %d분", updated="업데이트", guide_k="가이드", nav_label="주 메뉴", nav_features="기능", nav_field="현장 기록", nav_perf="성능", nav_drawings="실제 도면", nav_pricing="요금제", nav_faq="자주 묻는 질문",
 cta_short="베타 신청", cta_primary="비공개 베타 신청", cta_secondary="기능 둘러보기", menu_open="메뉴 열기",
 h1="도면에서 현장까지,<br>iPad 하나로.", h1_sub="Fluxketch는 현장 사람을 위한 CAD입니다. DXF·DWG·PDF를 그대로 열어 Apple Pencil로 작도하고, 마크업과 사진 핀을 도면 좌표에 붙이고, 축척 맞춘 PDF와 DXF로 꺼냅니다.",
 platform="iPad · Apple Pencil · TestFlight 비공개 베타", hero_alt="Fluxketch 도면 보기 — 호텔 지하 1층 주차장 평면도, 왼쪽 도구 팔레트, 오른쪽 스냅 레일",
 dim_top="181,422 도형 · 60 Hz", dim_side="CAD 도구 12종",
 v_h2="CAD의 힘. 번거로움은 빼고.", v_sub="사무실 CAD의 도면을 그대로 들고 나가고, 현장에서 손댄 것이 그대로 사무실로 돌아옵니다. 파일 형식을 바꾸거나 다시 그릴 일이 없습니다.",
 v1_t="배우는 시간이 짧습니다", v1_p="선·폴리선·원·호·사각형·문자·이동·복사·모깎기·자르기·지우기·치수 — 12개 도구, 스냅과 직교, 수치 키패드. 이미 아는 CAD 문법 그대로입니다.",
 v2_t="큰 도면도 손에서 부드럽게", v2_p="18만 도형 도면에서도 팬·줌이 60Hz로 따라옵니다. 멈추면 즉시 선명해지고, 레이어 188개도 그대로 다룹니다.",
 v3_t="축척 맞춰 종이로", v3_p="플롯 PDF는 축척과 100mm 검증 눈금을 달고 나갑니다. 마크업 잉크와 핀까지 그대로. DXF로도 돌려보냅니다.",
 strip_label="실제 도면 갤러리",
 s1="주택 5층 · 전기·설비 시트", s2="호텔 기준층 · 도면 보기", s3="레이어 188 · 굵기·선종류", s4="카지노 1층 · CAD 모드", s5="아파트 평면 · 도면 보기", s6="그라나다 지형도 · 등고선 전체", s7="마크업 · 마커", s8="상가 6개 층 · 시트",
 f_eyebrow="기능", f_h2="필요한 CAD 도구가 전부, 그리고 현장 도구.", f_sub="카탈로그에 이름만 있는 도구는 넣지 않았습니다. 아래는 실제 iPad에서 매 라운드 검증된 것들입니다.",
 t1="도면 보기, 인쇄물처럼", t1s="한 번 누르면 검은 선·흰 바탕 시트. 확대해도 벡터라 뭉개지지 않습니다.",
 t2="DXF·DWG·PDF 그대로 열기", t2s="레이어·색·굵기·선종류·블록·해치·다중선까지. 없는 것은 리포트가 개수로 말합니다.",
 t3="마크업은 도면에 붙습니다", t3s="펜·마커·연필·지우개·올가미·자. 획은 도면 좌표에 고정돼 확대·이동 중에도 갈라지지 않습니다.",
 t4="레이어 188개도 그대로", t4s="가시성·잠금·색·굵기·선종류를 팔레트에서 바로. 눈 감긴 레이어는 화면·스냅·플롯이 같은 규칙으로 뺍니다.",
 t5="실척 자와 치수", t5s="화면 밀도를 추정해 1:1부터 1:1,000까지 실척으로. 두 점을 찍으면 실제 길이가 단위와 함께.",
 t6="꺼내기는 7종 문서로", t6s="핀 로그·리포트·시트 발행·플롯 PDF·DXF 내보내기·PDF 언더레이. 현장에서 사무실로 바로.",
 scene1_alt="현장에서 iPad로 도면을 확인하는 감리자", fd_eyebrow="현장 기록", fd_h2="본 것을 도면 위에 남깁니다.", fd_sub="사진이 달린 핀, 손글씨 마크업, 노트 페이지가 한 파일에 삽니다. 모드를 오가도 자리는 그대로이고, 모아서 한 부의 리포트가 됩니다.",
 fd1_alt="더보기 메뉴 — 핀 로그, 리포트, 시트 발행, 플롯, DXF 내보내기, PDF 불러오기, 베타 피드백", fd1_t="핀 로그에서 리포트까지", fd1_p="핀을 찍고 사진과 메모를 답니다. 핀 로그가 곧 목록이고, 리포트는 문서 7종(점검·지시·회의 등) 서식으로 인쇄됩니다.",
 fd1_l1="핀은 언제나 마크업 위에 — 도면 좌표에 고정", fd1_l2="리포트 표 서식과 법령 근거 항목 인쇄", fd1_l3="시트 발행으로 특정 시트만 PDF로",
 fd2_alt="마크업 모드 — 펜·마커·연필·지우개·올가미·자, 색과 굵기 팔레트", fd2_t="손글씨는 손글씨답게", fd2_p="Apple Pencil 필압 그대로. 획이 도면과 갈라지지 않고, 굵기는 도면 단위 기준이라 축척이 바뀌어도 의미가 같습니다.",
 fd2_l1="펜·마커·연필·지우개·올가미·자", fd2_l2="되돌리기·다시 실행, 잉크까지 그대로 플롯", fd2_l3="노트 페이지: 백지·줄·도트·모눈·제도 모눈",
 fd3_alt="실척 자 팝오버 — 1:1부터 1:1,000 축척 선택과 자로 맞추기", fd3_t="실척으로 보고, 자로 잽니다", fd3_p="기종별 화면 밀도를 추정해 1:50이면 1:50으로 보여 줍니다. 종이 위 100mm 눈금으로 프린터 배율까지 검증합니다.",
 fd3_l1="1:1 ~ 1:1,000 축척 · 자로 맞추기(보정)", fd3_l2="DXF는 단위를 묻고 읽는 순간 보정(mm·cm·m·inch·ft)", fd3_l3="PDF 밑그림은 두 점으로 축척을 맞추고 벡터에 스냅",
 pf_eyebrow="성능", pf_h2="큰 도면이 무섭지 않습니다.", pf_sub="Metal 벡터 렌더와 래스터 타일 피라미드가 함께 그립니다. 그라나다 시가지와 산악 등고선 전체를 한 화면에 올려도 손을 따라옵니다.",
 pf_alt="그라나다 지형도 — 시가지와 산악 등고선 전체, CAD 모드", st1="도형을 열어 검증한 도면(TalkFile_18)", st2="18만 도형에서 팬·줌", st3="레이어를 그대로 다루는 도면(호텔 5 ESTRELLAS)",
 flow_label="작업 흐름: 사무실 도면 → Fluxketch(iPad) → 종이·DXF·리포트 → 사무실로 되돌림", flow_in="사무실 CAD에서 그대로", flow_mid="작도 · 마크업 · 핀 · 노트", flow_mid2="iPad · Apple Pencil", flow_report="리포트", flow_out="축척 맞춘 출력 · 회의", flow_back="DXF로 되돌려 사무실 CAD에서 이어 그리기", cp_eyebrow="왜 iPad인가", cp_h2="사무실과 현장 사이의 거리를 없앱니다.",
 cp_before_t="지금까지", cp_b1="현장에선 출력물에 볼펜, 사무실에 돌아와 다시 CAD로 옮겨 그리기", cp_b2="사진은 카메라 롤에, 메모는 수첩에 — 어느 위치였는지는 기억에", cp_b3="확인 회의는 PDF 스크린샷을 메신저로", cp_b4="현장용 앱은 DWG를 못 열거나 레이어를 잃음",
 cp_after_t="Fluxketch", cp_a1="현장에서 바로 도면 좌표에 마크업·치수·핀", cp_a2="사진과 메모가 핀에 달려 위치가 곧 기록", cp_a3="리포트·플롯 PDF 한 부로 회의", cp_a4="DXF·DWG를 레이어·굵기·선종류 그대로 열고 돌려보냄",
 cs_eyebrow="실제 도면", cs_h2="실제 도면으로 검증합니다.", cs_sub="아래는 베타 기간에 실제로 열고 손댄 도면들입니다. 화면은 앱 그대로이며 보정하지 않았습니다.",
 cs1_k="주택 · 5개 층", cs1_t="전기·설비 4개 시트를 한 파일에", cs1_p="시트마다 다른 색 규칙(레이어 색·자기 색)이 그대로 살아 있습니다.",
 cs2_k="상업 건물 · 단면·입면", cs2_t="단면 5장과 지붕 평면", cs2_p="해치·치수·문자까지 벡터로, 확대해도 선이 살아 있습니다.",
 cs3_k="구조 · 배근 상세", cs3_t="배근 상세 수백 개", cs3_p="작은 상세가 빽빽한 도면도 타일로 즉시 선명하게.",
 pr_eyebrow="요금제", pr_h2="베타 기간에는 전부 무료입니다.", pr_sub="요금은 정식 출시 때 공개합니다. 베타에 참여하신 분께는 출시 뒤 별도 프로모션이 있습니다.", pr_tba="추후 공개", pr_promo="베타 참여자 프로모션 예정",
 per_month="/월", pr_free_1="도면 열기·보기·마크업", pr_free_2="기본 내보내기", pr_lite_1="CAD 도구 12종·치수", pr_lite_2="플롯 PDF·DXF 내보내기",
 pr_tag="베타 참여 시 프로모션", pr_pro_1="Lite 전부 + 핀·리포트 7종 문서", pr_pro_2="시트 발행·PDF 언더레이", pr_pro_3="대형 도면 성능(래스터 타일)",
 pr_btn_beta="베타로 시작", pr_note="요금제 구성과 가격은 정식 출시 시 공개되며 변경될 수 있습니다. 베타 기간에는 모든 기능이 무료입니다.",
 cta_h2="다음 현장부터 Fluxketch로.", cta_sub="TestFlight 비공개 베타에 참여하시면 베타 기간 동안 모든 기능을 무료로 쓰고, 개발팀에 바로 피드백할 수 있습니다.", cta_mail="이메일로 문의",
 faq_h2="자주 묻는 질문",
 faq=[("무료로 쓸 수 있나요?","베타 기간에는 모든 기능이 무료입니다. 정식 출시 뒤의 요금제와 가격은 출시 때 공개하며, 베타에 참여하신 분께는 별도 프로모션을 드립니다."),
      ("어떤 파일을 열 수 있나요?","DXF와 DWG(서버 변환), PDF(언더레이)를 엽니다. 레이어·색·굵기·선종류·블록·해치·다중선·3D면·지시선을 가져오고, 가져오지 못한 요소는 리포트에 개수로 표시됩니다."),
      ("인터넷 없이도 되나요?","DXF·PDF는 완전히 오프라인으로 동작합니다. DWG만 변환 서버가 필요해 인터넷이 필요합니다(PC에서 DXF로 저장하면 오프라인 가능)."),
      ("3D 모델링이나 AI 기능이 있나요?","없습니다. Fluxketch는 2D 도면을 현장에서 열고, 그리고, 표시하고, 꺼내는 데 집중합니다."),
      ("어떤 기기가 필요한가요?","iPad와 Apple Pencil입니다. 큰 도면은 M 시리즈 iPad에서 가장 쾌적하지만, 베타에서는 iPad 9세대·A16 기종에서도 검증하고 있습니다."),
      ("마크업은 도면과 함께 저장되나요?","네. 마크업·핀·노트는 도면 파일 안에 도면 좌표로 저장됩니다. 플롯 PDF에 잉크와 핀이 그대로 나가고, DXF 내보내기도 됩니다."),
      ("베타는 어떻게 참여하나요?","위의 '비공개 베타 신청'으로 신청하시면 TestFlight 초대를 보내 드립니다. 문제는 앱 첫 화면의 '오류 즉시 문의' 또는 flux0720@fluxketch.com으로 파일과 함께 보내 주세요.")],
 ft_tag="현장에서 끝내는 iPad CAD.", ft_product="제품", ft_use="쓰임", ft_use1="현장 기록", ft_use2="실제 도면", ft_use3="대형 도면", ft_company="회사", ft_contact="문의 flux0720@fluxketch.com", ft_legal="법적 고지", ft_privacy="개인정보 처리방침", ft_terms="이용약관", ft_licenses="오픈소스 라이선스", ft_fine="베타 기간 안내 문서는 정식 문서로 대체될 예정입니다.",
)
EN = dict(KO)
EN.update(
 lang="en", path="/en/", home="/en/", alt_href="/", alt_lang="ko", alt_label="KO", alt_full="한국어",
 title="Fluxketch — Field CAD for iPad", desc="Open DXF, DWG and PDF drawings on iPad, draft with Apple Pencil, pin markups and photos to drawing coordinates, and export scale-true PDF and DXF. Private beta.",
 og_desc="Open, draw, mark up, export. All on iPad.",
 og_locale="en_US", nav_guides="Guides", p_answers_btn="See the answers", qa_eyebrow="Questions and answers", steps_eyebrow="How it works", rel_h2="See also", crumbs_label="Breadcrumb", crumb_home="Home", g_h1="Guides for people who use CAD on site", g_lead="Practical writing on what the field runs into every day — DWG, DXF, scale, markup. Most of it applies whichever app you use.", read_min="About %d min read", updated="Updated", guide_k="Guide", nav_label="Main menu", nav_features="Features", nav_field="Field notes", nav_perf="Performance", nav_drawings="Real drawings", nav_pricing="Pricing", nav_faq="FAQ",
 cta_short="Join beta", cta_primary="Join the private beta", cta_secondary="Explore features", menu_open="Open menu",
 h1="From the drawing<br>to the site, on one iPad.", h1_sub="Fluxketch is CAD for people who carry drawings. Open DXF, DWG and PDF as they are, draft with Apple Pencil, pin markups and photos to drawing coordinates, and export scale-true PDF and DXF.",
 platform="iPad · Apple Pencil · TestFlight private beta", hero_alt="Fluxketch sheet view — hotel basement parking plan with tool palette and snap rail",
 dim_top="181,422 entities · 60 Hz", dim_side="12 CAD tools",
 v_h2="The power of CAD. None of the pain.", v_sub="Take your office drawings out as they are, and bring what you touched on site straight back. No format juggling, no redrawing.",
 v1_t="Short to learn", v1_p="Line, polyline, circle, arc, rectangle, text, move, copy, fillet, trim, erase, dimension — 12 tools with snaps, ortho and a numeric keypad. The CAD grammar you already know.",
 v2_t="Big drawings stay smooth", v2_p="Pan and zoom at 60 Hz on a 180,000-entity drawing. Sharp the moment you stop, and 188 layers handled as-is.",
 v3_t="Scale-true on paper", v3_p="Plot PDFs carry the scale and a 100 mm check ruler. Markup ink and pins included. Round-trip to DXF too.",
 strip_label="Real drawing gallery",
 s1="5-storey house · MEP sheets", s2="Hotel typical floor · sheet view", s3="188 layers · weights & linetypes", s4="Casino ground floor · CAD mode", s5="Apartment plan · sheet view", s6="Granada terrain · full contours", s7="Markup · marker", s8="6-floor commercial · sheets",
 f_eyebrow="Features", f_h2="Every CAD tool you need. Plus the field ones.", f_sub="No catalog-only tools. Everything below is verified on real iPads every round.",
 t1="Sheet view, like a print", t1s="One tap: black lines on white. Vector all the way — zoom without mush.",
 t2="Open DXF, DWG and PDF as they are", t2s="Layers, colors, weights, linetypes, blocks, hatches, multilines. What can't be imported is reported by count.",
 t3="Markup that sticks to the drawing", t3s="Pen, marker, pencil, eraser, lasso, ruler. Strokes are locked to drawing coordinates — no drift while you zoom or pan.",
 t4="188 layers, untouched", t4s="Visibility, lock, color, weight and linetype right in the palette. Hidden layers leave the screen, snaps and plots by the same rule.",
 t5="True-scale ruler and dimensions", t5s="Screen density is estimated per device, so 1:50 shows as 1:50, from 1:1 to 1:1,000. Two taps give a real length with units.",
 t6="Export as seven document types", t6s="Pin log, report, sheet issue, plot PDF, DXF export, PDF underlay. From the site straight to the office.",
 scene1_alt="A site supervisor checking a plan on iPad in the field", fd_eyebrow="Field notes", fd_h2="What you saw, left on the drawing.", fd_sub="Photo pins, handwritten markup and note pages live in one file. Positions stay put across modes, and they collect into a single report.",
 fd1_alt="More menu — pin log, report, sheet issue, plot, DXF export, PDF underlay, beta feedback", fd1_t="From pin log to report", fd1_p="Drop a pin, attach a photo and a note. The pin log is the list; the report prints in seven document formats (inspection, instruction, meeting and more).",
 fd1_l1="Pins always sit above markup, locked to drawing coordinates", fd1_l2="Table layouts and regulatory reference lines in reports", fd1_l3="Sheet issue exports just the sheets you choose",
 fd2_alt="Markup mode — pen, marker, pencil, eraser, lasso, ruler with color and width palette", fd2_t="Handwriting that stays handwriting", fd2_p="Apple Pencil pressure as-is. Strokes never split from the drawing, and widths are in drawing units, so meaning survives a scale change.",
 fd2_l1="Pen, marker, pencil, eraser, lasso, ruler", fd2_l2="Undo/redo, ink plotted as-is", fd2_l3="Note pages: blank, ruled, dotted, grid, drafting grid",
 fd3_alt="True-scale ruler popover — scale presets from 1:1 to 1:1,000 and ruler calibration", fd3_t="See at true scale, measure with a ruler", fd3_p="Per-device screen density puts 1:50 on screen at 1:50. A 100 mm ruler on paper verifies even the printer's scaling.",
 fd3_l1="1:1 to 1:1,000 · calibrate against a ruler", fd3_l2="DXF asks the unit and corrects on read (mm, cm, m, inch, ft)", fd3_l3="PDF underlays scale with two points and snap to vectors",
 pf_eyebrow="Performance", pf_h2="Big drawings aren't scary.", pf_sub="A Metal vector renderer and a raster tile pyramid draw together. Put all of Granada's streets and mountain contours on one screen and it still follows your hand.",
 pf_alt="Granada terrain map — city and full mountain contours in CAD mode", st1="entities in a verified drawing (TalkFile_18)", st2="pan and zoom on 180k entities", st3="layers handled as-is (Hotel 5 Estrellas)",
 flow_label="Workflow: office drawings → Fluxketch on iPad → paper, DXF and reports → back to the office", flow_in="straight from office CAD", flow_mid="draft · markup · pins · notes", flow_mid2="iPad · Apple Pencil", flow_report="Report", flow_out="scale-true output · meetings", flow_back="Round-trip to DXF and keep drawing in office CAD", cp_eyebrow="Why iPad", cp_h2="Close the gap between the office and the site.",
 cp_before_t="Until now", cp_b1="Ballpoint on a printout on site, redraw it in CAD back at the office", cp_b2="Photos in the camera roll, notes in a pocketbook — the location lives in memory", cp_b3="Review meetings run on PDF screenshots over chat", cp_b4="Field apps that can't open DWG, or drop the layers",
 cp_after_t="Fluxketch", cp_a1="Markup, dimensions and pins on drawing coordinates, on site", cp_a2="Photos and notes hang on pins — the position is the record", cp_a3="One report or plot PDF for the meeting", cp_a4="DXF and DWG in and out with layers, weights and linetypes intact",
 cs_eyebrow="Real drawings", cs_h2="Verified on real drawings.", cs_sub="These were opened and worked on during the beta. Screens are straight from the app, unretouched.",
 cs1_k="House · 5 floors", cs1_t="Four MEP sheets in one file", cs1_p="Each sheet's color rules — by-layer and explicit — survive intact.",
 cs2_k="Commercial · sections & elevations", cs2_t="Five sections and a roof plan", cs2_p="Hatches, dimensions and text stay vector — lines hold at any zoom.",
 cs3_k="Structural · rebar details", cs3_t="Hundreds of rebar details", cs3_p="Dense sheets of small details turn sharp instantly through tiles.",
 pr_eyebrow="Pricing", pr_h2="Everything is free during the beta.", pr_sub="Pricing will be announced at launch. Beta participants get a separate promotion after launch.", pr_tba="To be announced", pr_promo="Promotion for beta participants",
 per_month="/mo", pr_free_1="Open, view and mark up drawings", pr_free_2="Basic export", pr_lite_1="12 CAD tools and dimensions", pr_lite_2="Plot PDF and DXF export",
 pr_tag="Beta promotion", pr_pro_1="Everything in Lite + pins and 7 report types", pr_pro_2="Sheet issue and PDF underlay", pr_pro_3="Large-drawing performance (raster tiles)",
 pr_btn_beta="Start with the beta", pr_note="Plan structure and prices will be announced at launch and may change. Everything is free during the beta.",
 cta_h2="Take Fluxketch to your next site.", cta_sub="Join the TestFlight private beta to use every feature free during the beta and talk directly to the team.", cta_mail="Email us",
 faq_h2="Frequently asked questions",
 faq=[("Is it free?","Everything is free during the beta. Plans and prices will be announced at launch, and beta participants get a separate promotion."),
      ("Which files can it open?","DXF, DWG (server conversion) and PDF (underlay). Layers, colors, weights, linetypes, blocks, hatches, multilines, 3D faces and leaders are imported; anything that isn't gets counted in the import report."),
      ("Does it work offline?","DXF and PDF work fully offline. Only DWG needs the conversion server, so it needs a connection (save as DXF on a PC to work offline)."),
      ("Is there 3D or AI?","No. Fluxketch focuses on opening, drawing, marking up and exporting 2D drawings on site."),
      ("What hardware do I need?","An iPad and an Apple Pencil. Large drawings are most comfortable on M-series iPads, and the beta is also verified on iPad 9th gen and A16 models."),
      ("Are markups saved with the drawing?","Yes. Markup, pins and notes are stored inside the drawing file in drawing coordinates. Plot PDFs carry the ink and pins, and DXF export is available."),
      ("How do I join the beta?","Use 'Join the private beta' above and we'll send a TestFlight invite. Report problems from the app's 'Report a bug now' card or by email to flux0720@fluxketch.com, ideally with the file.")],
 ft_tag="Field CAD for iPad.", ft_product="Product", ft_use="Use cases", ft_use1="Field notes", ft_use2="Real drawings", ft_use3="Large drawings", ft_company="Company", ft_contact="Contact flux0720@fluxketch.com", ft_legal="Legal", ft_privacy="Privacy", ft_terms="Terms", ft_licenses="Open-source licenses", ft_fine="Beta-period notices will be replaced by formal documents.",
)

import json, re
from content_pages import PAGES
from content_guides import GUIDES, DATE

SITE = "https://fluxketch.com"
TOP = open(os.path.join(ROOT, "tools", "_top.html"), encoding="utf-8").read()
BOTTOM = open(os.path.join(ROOT, "tools", "_bottom.html"), encoding="utf-8").read()
BOTTOM = re.sub(r'<section id="faq".*?</section>\n\n', "", BOTTOM, flags=re.S)  # 홈 FAQ는 홈에만

def fill(tpl, d):
    out = tpl
    for k, v in d.items():
        if isinstance(v, (str, int)): out = out.replace("{{" + k + "}}", str(v))
    return out

def sub(base, lang):
    """홈 사전(KO/EN)에서 하위 페이지용 사전을 만든다."""
    d = dict(base); d["form"] = FORM
    for k, v in ICO.items(): d["ico_" + k] = v
    return d

def ld(obj): return json.dumps(obj, ensure_ascii=False, separators=(",", ":"))

ORG = {"@type":"Organization","name":"Fluxketch","url":SITE+"/","logo":SITE+"/assets/img/icon-512.png","email":"flux0720@fluxketch.com"}
def app_ld(lang):
    ko = lang == "ko"
    return {"@context":"https://schema.org","@type":"MobileApplication","name":"Fluxketch",
      "operatingSystem":"iPadOS","applicationCategory":"DesignApplication","applicationSubCategory":"CAD",
      "description": KO["desc"] if ko else EN["desc"], "url": SITE + ("/" if ko else "/en/"),
      "inLanguage":["ko","en"], "screenshot": SITE+"/assets/img/v3/hotel-parking-sheet.jpg",
            "author": ORG, "publisher": ORG}
def faq_ld(pairs):
    return {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":re.sub("<[^>]+>","",a)}} for q,a in pairs]}
def crumbs_ld(items):
    return {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":i+1,"name":n,"item":SITE+u} for i,(n,u) in enumerate(items)]}

def path_for(lang, slug, guide=False):
    p = ("/" if lang == "ko" else "/en/") + ("guides/" if guide else "") + slug + "/"
    return p

def related_cards(lang, exclude=None, guides=False):
    cards = []
    for pg in PAGES:
        if pg["slug"] == exclude: continue
        c = pg[lang]
        cards.append(f'    <a href="{path_for(lang, pg["slug"])}"><span class="k">{html.escape(c["k"])}</span><span class="t">{html.escape(c["short"])}</span><span class="s">{html.escape(c["h1"])}</span></a>\n')
    if guides:
        base = KO if lang == "ko" else EN
        cards.append(f'    <a href="{path_for(lang, "", True)[:-1]}"><span class="k">{html.escape(base["nav_guides"])}</span><span class="t">{html.escape(base["g_h1"])}</span><span class="s">{html.escape(base["g_lead"])}</span></a>\n')
    return "".join(cards)

def guide_cards(lang, exclude=None, limit=None):
    base = KO if lang == "ko" else EN
    cards = []
    for g in GUIDES:
        if g["slug"] == exclude: continue
        c = g[lang]
        cards.append(f'    <a href="{path_for(lang, g["slug"], True)}"><span class="k">{html.escape(base["guide_k"])}</span><span class="t">{html.escape(c["short"])}</span><span class="s">{html.escape(c["desc"])}</span></a>\n')
    return "".join(cards[:limit] if limit else cards)

def footer_use_links(lang):
    return "".join(f'<li><a href="{path_for(lang, pg["slug"])}">{html.escape(pg[lang]["short"])}</a></li>' for pg in PAGES)

URLS = []  # (ko_path, en_path, lastmod, images)
def write(path, content):
    full = os.path.join(ROOT, path.lstrip("/"), "index.html") if path.endswith("/") else os.path.join(ROOT, path.lstrip("/"))
    os.makedirs(os.path.dirname(full), exist_ok=True)
    assert "{{" not in content, (path, re.findall(r"{{[a-z_0-9]+}}", content)[:5])
    with open(full, "w", encoding="utf-8") as f: f.write(content)

def render_page(pg, lang):
    base = KO if lang == "ko" else EN
    c = pg[lang]; d = sub(base, lang)
    d.update(c); d["path"] = path_for(lang, pg["slug"]); d["home"] = "/" if lang == "ko" else "/en/"
    other = "en" if lang == "ko" else "ko"
    d["alt_href"] = path_for(other, pg["slug"])
    d["og_desc"] = c["desc"]; d["img"] = pg["img"]; d["img2"] = pg["img2"]; d["orient"] = pg["orient"]; d["orient2"] = pg["orient2"]
    d["qa_items"] = "".join(f'    <article><h3>{html.escape(q)}</h3><p>{html.escape(a)}</p></article>\n' for q, a in c["qa"])
    d["step_items"] = "".join(f'      <li><h3>{html.escape(t)}</h3><p>{html.escape(p)}</p></li>\n' for t, p in c["steps"])
    d["rel_items"] = related_cards(lang, exclude=pg["slug"], guides=True)
    d["ft_use_links"] = footer_use_links(lang)
    d["jsonld"] = ld([{"@context":"https://schema.org","@type":"WebPage","name":c["title"],"description":c["desc"],"url":SITE+d["path"],"inLanguage":lang,"isPartOf":{"@type":"WebSite","name":"Fluxketch","url":SITE+"/"},"about":app_ld(lang)}, faq_ld(c["qa"]), crumbs_ld([(base["crumb_home"], d["home"]), (c["short"], d["path"])])])
    tpl = open(os.path.join(ROOT, "tools", "page.html"), encoding="utf-8").read().replace("{{_top}}", TOP).replace("{{_bottom}}", BOTTOM)
    tpl = tpl.replace('<link rel="alternate" hreflang="ko" href="https://fluxketch.com/">', f'<link rel="alternate" hreflang="ko" href="{SITE}{path_for("ko", pg["slug"])}">')
    tpl = tpl.replace('<link rel="alternate" hreflang="en" href="https://fluxketch.com/en/">', f'<link rel="alternate" hreflang="en" href="{SITE}{path_for("en", pg["slug"])}">')
    tpl = tpl.replace('<link rel="alternate" hreflang="x-default" href="https://fluxketch.com/">', f'<link rel="alternate" hreflang="x-default" href="{SITE}{path_for("ko", pg["slug"])}">')
    tpl = tpl.replace("/assets/img/v3/hotel-parking-sheet.jpg", f"/assets/img/v3/{pg['img']}.jpg")
    write(d["path"], fill(tpl, d))

def body_html(blocks):
    out = []
    for blk in blocks:
        t = blk[0]
        if t == "h2": out.append(f"<h2>{html.escape(blk[1])}</h2>")
        elif t == "p": out.append(f"<p>{blk[1]}</p>")
        elif t in ("ul", "ol"): out.append(f"<{t}>" + "".join(f"<li>{x}</li>" for x in blk[1]) + f"</{t}>")
        elif t == "note": out.append(f'<div class="note"><p>{blk[1]}</p></div>')
        elif t == "fig": out.append(f'<figure><div class="device land"><div class="screen"><img src="/assets/img/v3/{blk[1]}.jpg" alt="{html.escape(blk[2])}" loading="lazy"></div></div><figcaption>{html.escape(blk[3])}</figcaption></figure>')
        elif t == "table":
            out.append('<div class="tablewrap"><table><thead><tr>' + "".join(f"<th>{html.escape(h)}</th>" for h in blk[1]) + "</tr></thead><tbody>" + "".join("<tr>" + "".join(f"<td>{html.escape(c)}</td>" for c in r) + "</tr>" for r in blk[2]) + "</tbody></table></div>")
    return "\n".join(out)

def words(blocks):
    txt = re.sub("<[^>]+>", "", " ".join(str(x) for b in blocks for x in (b[1:] if b[0] != "table" else [])))
    return len(txt)

def render_guide(g, lang):
    base = KO if lang == "ko" else EN
    c = g[lang]; d = sub(base, lang)
    d.update({k: v for k, v in c.items() if k != "body"})
    d["path"] = path_for(lang, g["slug"], True); d["home"] = "/" if lang == "ko" else "/en/"
    other = "en" if lang == "ko" else "ko"; d["alt_href"] = path_for(other, g["slug"], True)
    d["og_desc"] = c["desc"]
    n = words(c["body"]); mins = max(3, round(n / (500 if lang == "ko" else 1100)))
    d["meta_line"] = f'{base["updated"]} {DATE} · {base["read_min"] % mins}'
    cta = f'<div class="cta-soft"><p>{html.escape(c["cta"])}</p><a class="btn primary small" href="{FORM}" target="_blank" rel="noopener noreferrer">{html.escape(base["cta_primary"])}</a></div>'
    d["body"] = body_html(c["body"]) + "\n" + cta
    d["rel_items"] = guide_cards(lang, exclude=g["slug"], limit=3) + related_cards(lang)[:0]
    d["ft_use_links"] = footer_use_links(lang)
    d["jsonld"] = ld([{"@context":"https://schema.org","@type":"Article","headline":c["h1"],"description":c["desc"],"inLanguage":lang,"datePublished":DATE,"dateModified":DATE,"image":SITE+f"/assets/img/v3/{g['img']}.jpg","author":ORG,"publisher":ORG,"mainEntityOfPage":SITE+d["path"]}, crumbs_ld([(base["crumb_home"], d["home"]), (base["nav_guides"], d["home"]+"guides/"), (c["short"], d["path"])])])
    tpl = open(os.path.join(ROOT, "tools", "article.html"), encoding="utf-8").read().replace("{{_top}}", TOP).replace("{{_bottom}}", BOTTOM)
    tpl = tpl.replace('<link rel="alternate" hreflang="ko" href="https://fluxketch.com/">', f'<link rel="alternate" hreflang="ko" href="{SITE}{path_for("ko", g["slug"], True)}">')
    tpl = tpl.replace('<link rel="alternate" hreflang="en" href="https://fluxketch.com/en/">', f'<link rel="alternate" hreflang="en" href="{SITE}{path_for("en", g["slug"], True)}">')
    tpl = tpl.replace('<link rel="alternate" hreflang="x-default" href="https://fluxketch.com/">', f'<link rel="alternate" hreflang="x-default" href="{SITE}{path_for("ko", g["slug"], True)}">')
    tpl = tpl.replace("/assets/img/v3/hotel-parking-sheet.jpg", f"/assets/img/v3/{g['img']}.jpg")
    tpl = tpl.replace('<meta property="og:type" content="website">', '<meta property="og:type" content="article">')
    write(d["path"], fill(tpl, d))

def render_guides_index(lang):
    base = KO if lang == "ko" else EN
    d = sub(base, lang); d["home"] = "/" if lang == "ko" else "/en/"; d["path"] = d["home"] + "guides/"
    other = "en" if lang == "ko" else "ko"; d["alt_href"] = ("/" if other == "ko" else "/en/") + "guides/"
    d["title"] = f'{base["nav_guides"]} — Fluxketch'; d["desc"] = base["g_lead"]; d["og_desc"] = base["g_lead"]
    items = []
    for g in GUIDES:
        c = g[lang]; n = words(c["body"]); mins = max(3, round(n / (500 if lang == "ko" else 1100)))
        items.append(f'    <a href="{path_for(lang, g["slug"], True)}"><div class="thumb"><img src="/assets/img/v3/{g["img"]}-sm.jpg" alt="" loading="lazy"></div><div><span class="t">{html.escape(c["h1"])}</span><span class="s">{html.escape(c["desc"])}</span><span class="m">{base["read_min"] % mins}</span></div></a>\n')
    d["g_items"] = "".join(items); d["rel_items"] = related_cards(lang); d["ft_use_links"] = footer_use_links(lang)
    d["jsonld"] = ld([{"@context":"https://schema.org","@type":"CollectionPage","name":d["title"],"description":d["desc"],"url":SITE+d["path"],"inLanguage":lang}, crumbs_ld([(base["crumb_home"], d["home"]), (base["nav_guides"], d["path"])])])
    tpl = open(os.path.join(ROOT, "tools", "guides.html"), encoding="utf-8").read().replace("{{_top}}", TOP).replace("{{_bottom}}", BOTTOM)
    tpl = tpl.replace('href="https://fluxketch.com/">', f'href="{SITE}/guides/">').replace('href="https://fluxketch.com/en/">', f'href="{SITE}/en/guides/">')
    write(d["path"], fill(tpl, d))

def render_home(d):
    d = dict(d); d["form"] = FORM
    for k, v in ICO.items(): d["ico_" + k] = v
    d["strip_items"] = "".join(f'  <figure><div class="thumb"><img src="/assets/img/v3/{f}-sm.jpg" alt="" loading="lazy" width="900" height="{626 if "portrait" not in f else 1295}"></div><figcaption><span>{html.escape(d[c])}</span></figcaption></figure>\n' for f, c in STRIP)
    d["f_tabs"] = "".join(f'      <button class="tab" role="tab" id="tab-{i}" aria-controls="pane-{i}" aria-selected="false"><span class="bar" aria-hidden="true"></span><span class="t">{html.escape(d[c])}</span><span class="s"><span>{html.escape(d[c+"s"])}</span></span></button>\n' for i, (f, c) in enumerate(TABS))
    d["f_panes"] = "".join(f'      <div class="pane" role="tabpanel" id="pane-{i}" aria-labelledby="tab-{i}"><div class="device land"><div class="screen"><img src="/assets/img/v3/{f}.jpg" alt="{html.escape(d[c])}" loading="{"eager" if i == 0 else "lazy"}"></div></div></div>\n' for i, (f, c) in enumerate(TABS))
    d["faq_items"] = "".join(f'    <details{" open" if i == 0 else ""}><summary>{html.escape(q)}</summary><div class="a">{html.escape(a)}</div></details>\n' for i, (q, a) in enumerate(d["faq"]))
    d["ft_use_links"] = footer_use_links(d["lang"])
    d["jsonld"] = ld([app_ld(d["lang"]), {"@context":"https://schema.org","@type":"WebSite","name":"Fluxketch","url":SITE+"/","inLanguage":["ko","en"],"publisher":ORG}, faq_ld(d["faq"])])
    tpl = open(os.path.join(ROOT, "tools", "template.html"), encoding="utf-8").read()
    write(d["path"], fill(tpl, d))

def sitemap():
    pairs = [("/", "/en/", ["hotel-parking-sheet"]), ("/guides/", "/en/guides/", [])]
    pairs += [(path_for("ko", p["slug"]), path_for("en", p["slug"]), [p["img"], p["img2"]]) for p in PAGES]
    pairs += [(path_for("ko", g["slug"], True), path_for("en", g["slug"], True), [g["img"]]) for g in GUIDES]
    legal = ["/privacy", "/terms", "/licenses"]
    out = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">']
    for ko, en, imgs in pairs:
        for u, alt in ((ko, en), (en, ko)):
            out.append(f"  <url><loc>{SITE}{u}</loc><lastmod>{DATE}</lastmod>")
            out.append(f'    <xhtml:link rel="alternate" hreflang="ko" href="{SITE}{ko}"/><xhtml:link rel="alternate" hreflang="en" href="{SITE}{en}"/><xhtml:link rel="alternate" hreflang="x-default" href="{SITE}{ko}"/>')
            for im in imgs: out.append(f"    <image:image><image:loc>{SITE}/assets/img/v3/{im}.jpg</image:loc></image:image>")
            out.append("  </url>")
    for u in legal: out.append(f"  <url><loc>{SITE}{u}</loc><lastmod>{DATE}</lastmod></url>")
    out.append("</urlset>")
    open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8").write("\n".join(out) + "\n")
    open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8").write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
    return len(pairs) * 2 + len(legal)

if __name__ == "__main__":
    render_home(KO); render_home(EN)
    for pg in PAGES:
        render_page(pg, "ko"); render_page(pg, "en")
    for g in GUIDES:
        render_guide(g, "ko"); render_guide(g, "en")
    render_guides_index("ko"); render_guides_index("en")
    n = sitemap()
    print(f"built: home 2, landing {len(PAGES)*2}, guides {len(GUIDES)*2} + index 2, sitemap {n} urls")
