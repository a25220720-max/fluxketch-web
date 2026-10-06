# 홈 v5 문구·요금 사전 (2026-10-06). 렌더 = build_site.render_home → tools/home.html
import html
from urllib.parse import quote

MAIL = "flux0720@fluxketch.com"

def mailto(subject, body=""):
    u = f"mailto:{MAIL}?subject={quote(subject)}"
    return u + (f"&amp;body={quote(body)}" if body else "")

# 요금제별 기능 — 순서 = ROWS 순서. 1 = 포함
HAS = {"free": [1, 0, 0, 0, 0, 0], "lite": [1, 1, 1, 1, 0, 0], "markup": [1, 0, 0, 1, 1, 1], "pro": [1, 1, 1, 1, 1, 1]}

CHECK = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#2FB56A" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>'
DASH = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#3A3F46" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M7 12h10"/></svg>'

KO = dict(
 brand_sub="플럭스케치", hm_swipe="옆으로 넘겨 보기", hm_nav_office="사무소 도입",
 notice='<div class="notice" data-until="2026-10-14T00:00:00+09:00">베타 무료 이용은 <b>10월 13일(화)</b>까지 · 지금 Pro 월 <b>12,900원</b> (정가 16,900원)</div>',
 hm_chip="현장용 모바일 캐드 · 1.1.1", hm_dim="100% 자체 개발 CAD 엔진",
 hm_h1="현장 도면,<br><em>패드 하나로</em> 끝.",
 hm_lead="DWG·DXF·PDF를 그대로 열고, 그 자리에서 고치고, 표시하고,<br>축척 맞춰 PDF·DXF로 꺼냅니다.",
 hm_cta2="요금제 보기",
 proof=[("약 700명", "베타 테스터"), ("약 620명", "앱스토어 이용자"), ("30곳+", "건축·인테리어 사무소"), ("140만", "개체 도면까지 열림")],
 hm_f_eyebrow="A-101 · 기능", hm_f_h2="열고, 고치고, 표시하고, 꺼낸다.", hm_f_sub="사무실 도면을 그대로 들고 나가, 현장에서 손댄 것을 그대로 사무실로 돌려보냅니다.",
 cards=[("01 열기", "도면을 그대로", "DWG·DXF·PDF를 레이어·색·블록·해치까지 그대로 엽니다. 140만 개체 도면도 손에서 부드럽게.", "granada-topo-dark", "그라나다 지형도 전체를 연 화면"),
        ("02 고치기", "현장에서 바로 작도", "선·원·호·치수 등 CAD 도구 12종, 끝점·직교 스냅, 수치 키패드. 아는 캐드 문법 그대로.", "app-detail-dark", "레이어 팔레트와 CAD 도구가 열린 평면도"),
        ("03 표시하기", "마크업과 사진 핀", "펜슬 필압 그대로 도면 좌표에 붙는 손글씨, 사진과 메모가 달린 핀, 노트 페이지.", "app-markup", "단면도 위 손글씨 마크업"),
        ("04 꺼내기", "축척 맞춰 내보내기", "플롯 PDF·DXF 내보내기·리포트·시트 발행. 현장에서 사무실로 바로.", "menu-report", "핀 로그·리포트·플롯 메뉴")],
 hm_new_tag="1.1.1 NEW", news=["공정 일정 달력과 날짜별 노트", "iCloud로 프로젝트 통째로 옮기기", "마크업·핀 사진을 PDF 한 장으로 공유"],
 hm_p_eyebrow="A-201 · 요금제", hm_p_h2="필요한 만큼만 고르세요.", hm_p_sub="월간 요금제는 <b>3일 무료 체험</b>으로 시작합니다.",
 hm_cycle_label="결제 주기", hm_monthly="월간", hm_yearly="연간", hm_yearly_save="2개월 무료",
 rows=["도면 열기·보기 (DWG·DXF·PDF)", "작도·편집 · CAD 도구 12종", "블록·배치 · DXF 내보내기", "축척 맞춘 플롯 PDF", "마크업·사진 핀·노트", "리포트 · 마크업 PDF 공유"],
 per_m="/ 월", per_y="/ 년", included="포함", not_included="미포함",
 plans=[dict(k="free", name="Free", m="₩0", y="₩0", free=True, tag="도면을 열어 보기만 할 때.", cta_m="무료로 받기", cta_y="무료로 받기"),
        dict(k="lite", name="Lite", m="₩4,900", y="₩49,000", tag="사무실처럼 그리고 고칠 때.", cta_m="3일 무료로 시작", cta_y="Lite 시작"),
        dict(k="markup", name="Markup", badge="신규", m="₩8,900", y="₩89,000", tag="현장에서 표시하고 기록할 때.", cta_m="3일 무료로 시작", cta_y="Markup 시작"),
        dict(k="pro", name="Pro", badge="할인 중", hi=True, m="₩12,900", y="₩129,000", was_m="₩16,900", was_y="₩169,000", tag="전부 다. 앞으로 나올 아이폰 버전 포함.", cta_m="3일 무료로 시작", cta_y="Pro 시작")],
 hm_p_note="가격은 대한민국 App Store 기준(부가세 포함)입니다. 구독은 기간 종료 24시간 전까지 해지하지 않으면 자동 갱신되며, 설정 › Apple 계정 › 구독에서 언제든 해지할 수 있습니다. 무료 체험은 끝나기 24시간 전에 해지하면 요금이 청구되지 않습니다.",
 hm_o_h="사무소·팀 단위로 도입하시나요?", hm_o_p="여러 대를 함께 쓰실 사무소는 메일로 알려 주세요. 인원과 쓰임에 맞춰 도입 상담과 견적을 드립니다.", hm_o_btn="도입 문의 메일 보내기",
 o_subject="[사무소 도입 문의] ", o_body="사무소명:\n담당자·연락처:\n사용 인원(태블릿 대수):\n관심 플랜(Lite / Markup / Pro):\n문의 내용:\n",
 mail_subject="[플럭스케치 문의] ", hm_ft_mail="문의 메일",
 hm_end_h="다음 현장부터, 플럭스케치로.", hm_end_p="App Store에서 받아 바로 쓰실 수 있습니다.",
 hm_biz1="상호 플럭스케치(Fluxketch) · 대표 김준서 · 사업자등록번호 102-14-97190 · 통신판매업 신고번호 제2026-서울강남-05411호",
 hm_biz2="주소 서울특별시 강남구 언주로134길 18, 5층 S35호(논현동, 신승빌딩) · 전화 010-7179-0722 · 이메일 flux0720@fluxketch.com",
 ft_tag_home="플럭스케치 — 현장용 모바일 캐드.<br>현장에서 끝냅니다.",
)

EN = dict(
 brand_sub="", hm_swipe="Swipe for more", hm_nav_office="For teams",
 notice="",
 hm_chip="Field CAD · 1.1.1", hm_dim="Our own CAD engine, built from scratch",
 hm_h1="Site drawings,<br><em>done on one tablet.</em>",
 hm_lead="Open DWG, DXF and PDF as they are, fix them on the spot, mark them up,<br>and export scale-true PDF and DXF.",
 hm_cta2="See pricing",
 proof=[("~700", "beta testers"), ("~620", "App Store users"), ("30+", "architecture & interior offices"), ("1.4M", "entities in one drawing")],
 hm_f_eyebrow="A-101 · Features", hm_f_h2="Open. Fix. Mark up. Export.", hm_f_sub="Take office drawings out as they are, and send what you touched on site straight back.",
 cards=[("01 Open", "Drawings as they are", "DWG, DXF and PDF with layers, colors, blocks and hatches intact. Smooth even at 1.4M entities.", "granada-topo-dark", "Full Granada topographic map opened in Fluxketch"),
        ("02 Fix", "Draft right on site", "12 CAD tools — line, circle, arc, dimension and more — with endpoint and ortho snaps and a numeric keypad.", "app-detail-dark", "Floor plan with layer palette and CAD tools"),
        ("03 Mark up", "Markup and photo pins", "Handwriting locked to drawing coordinates with pencil pressure, pins with photos and notes, note pages.", "app-markup", "Handwritten markup on a section drawing"),
        ("04 Export", "Out at true scale", "Plot PDF, DXF export, reports and sheet issue. From site to office, right away.", "menu-report", "Pin log, report and plot menu")],
 hm_new_tag="1.1.1 NEW", news=["Schedule calendar with daily notes", "Move whole projects via iCloud", "Share markup and pin photos as one PDF"],
 hm_p_eyebrow="A-201 · Pricing", hm_p_h2="Pick only what you need.", hm_p_sub="Monthly plans start with a <b>3-day free trial</b>.",
 hm_cycle_label="Billing period", hm_monthly="Monthly", hm_yearly="Yearly", hm_yearly_save="2 months free",
 rows=["Open and view DWG, DXF, PDF", "Draft and edit · 12 CAD tools", "Blocks, layouts · DXF export", "Scale-true plot PDF", "Markup, photo pins, notes", "Reports · markup PDF sharing"],
 per_m="/ mo", per_y="/ yr", included="Included", not_included="Not included",
 plans=[dict(k="free", name="Free", m="$0", y="$0", free=True, tag="Just open and view drawings.", cta_m="Get it free", cta_y="Get it free"),
        dict(k="lite", name="Lite", m="$2.99", y="$29.99", tag="Draw and edit like at the office.", cta_m="Start 3-day free trial", cta_y="Start Lite"),
        dict(k="markup", name="Markup", badge="New", m="$4.99", y="$49.99", tag="Mark up and record on site.", cta_m="Start 3-day free trial", cta_y="Start Markup"),
        dict(k="pro", name="Pro", badge="Best value", hi=True, m="$7.99", y="$79.99", tag="Everything. Includes the upcoming iPhone version.", cta_m="Start 3-day free trial", cta_y="Start Pro")],
 hm_p_note="Prices shown are for the U.S. App Store; your local price is set by Apple and may differ. Subscriptions renew automatically unless cancelled at least 24 hours before the period ends, and you can cancel anytime in Settings › Apple Account › Subscriptions. Cancel a free trial at least 24 hours before it ends and you won't be charged.",
 hm_o_h="Rolling out to a whole office?", hm_o_p="If your team will use several tablets, email us. We'll help you set up and quote for your headcount and use.", hm_o_btn="Email us about teams",
 o_subject="[Team inquiry] ", o_body="Company:\nContact name & phone:\nNumber of users (tablets):\nPlan of interest (Lite / Markup / Pro):\nQuestion:\n",
 mail_subject="[Fluxketch] ", hm_ft_mail="Email us",
 hm_end_h="Take Fluxketch to your next site.", hm_end_p="Download it from the App Store and start today.",
 hm_biz1="Fluxketch · Owner Junseo Kim · Business Registration No. 102-14-97190 · Mail-Order Business Registration No. 2026-Seoul Gangnam-05411",
 hm_biz2="5F S35, 18 Eonju-ro 134-gil, Gangnam-gu, Seoul, Republic of Korea · +82 10-7179-0722 · flux0720@fluxketch.com",
 ft_tag_home="Field CAD for tablets.<br>Finish it on site.",
)

def _e(s): return html.escape(s)

def build(c, store_url):
    """홈 사전 c → 템플릿 키 dict."""
    d = {k: v for k, v in c.items() if isinstance(v, str)}
    d["hm_proof"] = "\n".join(f'      <div><dt>{_e(t)}</dt><dd>{_e(n)}</dd></div>' for n, t in c["proof"])
    d["hm_cards"] = "\n".join(
        f'      <article class="card"><div class="shot"><img src="/assets/img/v3/{img}-sm.jpg" alt="{_e(alt)}" loading="lazy" width="900" height="625"></div>'
        f'<div class="tx"><span class="n">{_e(n)}</span><h3>{_e(t)}</h3><p>{_e(b)}</p></div></article>'
        for n, t, b, img, alt in c["cards"])
    d["hm_new"] = '<span class="sep" aria-hidden="true">·</span>'.join(f"<span>{_e(x)}</span>" for x in c["news"])
    plans = []
    for p in c["plans"]:
        hi = p.get("hi")
        badge = f'<span class="badge">{_e(p["badge"])}</span>' if p.get("badge") else ""
        def amt(cyc):
            was = p.get("was_" + cyc)
            per = "" if p.get("free") else f'<span>{_e(c["per_" + cyc])}</span>'
            return (f'<div class="pr {cyc}">' + (f'<span class="was">{_e(was)}</span>' if was else "")
                    + f'<div class="amt"><b>{_e(p[cyc])}</b>{per}</div></div>')
        rows = "".join(
            (f'<li>{CHECK}<span class="sr">{_e(c["included"])}: </span>{_e(r)}</li>' if HAS[p["k"]][i]
             else f'<li class="off">{DASH}<span class="sr">{_e(c["not_included"])}: </span>{_e(r)}</li>')
            for i, r in enumerate(c["rows"]))
        cta = (f'<a class="go m" href="{store_url}" target="_blank" rel="noopener noreferrer">{_e(p["cta_m"])}</a>'
               f'<a class="go y" href="{store_url}" target="_blank" rel="noopener noreferrer">{_e(p["cta_y"])}</a>')
        plans.append(f'      <div class="plan{" hi" if hi else ""}"><div class="top"><span class="nm">{_e(p["name"])}</span>{badge}</div>'
                     f'{amt("m")}{amt("y")}<p class="tg">{_e(p["tag"])}</p><ul>{rows}</ul>{cta}</div>')
    d["hm_plans"] = "\n".join(plans)
    d["hm_o_mail"] = mailto(c["o_subject"], c["o_body"])
    d["hm_mail"] = mailto(c["mail_subject"])
    d["ft_tag"] = c["ft_tag_home"]
    return d
