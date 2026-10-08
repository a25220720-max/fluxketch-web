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
 brand_sub="플럭스케치", og_desc="도면을 열고, 고치고, 표시하고, 보낸다. 현장에서 바로.", hm_v_eyebrow="A-102 · 작동 영상", hm_v_h2="실제 화면 그대로.", hm_v_sub="작도부터 수치 입력, 마크업까지 — 앱에서 바로 녹화한 화면입니다.", hm_v_label="플럭스케치 작동 영상", hm_swipe="옆으로 넘겨 보기", hm_nav_office="사무소 도입",
 notice='<div class="notice" data-until="2026-10-14T00:00:00+09:00">베타 무료 이용은 <b>10월 13일(화)</b>까지 · 지금 Pro 월 <b>12,900원</b> (정가 16,900원)</div>',
 hm_chip="현장용 모바일 캐드 · 1.1.1", hm_dim="100% 자체 개발 CAD 엔진",
 hm_h1="현장 도면,<br><em>패드 하나로</em> 끝.",
 hm_lead="DWG·DXF·PDF를 그대로 열고, 그 자리에서 고치고, 표시하고,<br>축척 맞춰 PDF·DXF로 보냅니다.",
 hm_cta2="요금제 보기",
 proof=[("700명+", "베타 테스터"), ("1,000명+", "앱스토어 이용자"), ("30곳+", "건축·인테리어 사무소"), ("140만", "개체 도면까지 열림")],
 hm_f_eyebrow="A-101 · 기능", hm_f_h2="열고, 고치고, 표시하고, 보낸다.", hm_f_sub="사무실 도면을 그대로 들고 나가, 현장에서 손댄 것을 그대로 사무실로 돌려보냅니다.",
 cards=[("01 열기", "도면을 그대로", "DWG·DXF·PDF를 레이어·색·블록·해치까지 그대로 엽니다. 140만 개체 도면도 손에서 부드럽게.", "granada-topo-dark", "그라나다 지형도 전체를 연 화면"),
        ("02 고치기", "현장에서 바로 작도", "선·원·호·치수 등 CAD 도구 12종, 끝점·직교 스냅, 수치 키패드. 아는 캐드 문법 그대로.", "app-detail-dark", "레이어 팔레트와 CAD 도구가 열린 평면도"),
        ("03 표시하기", "마크업과 사진 핀", "펜슬 필압 그대로 도면 좌표에 붙는 손글씨, 사진과 메모가 달린 핀, 노트 페이지.", "app-markup", "단면도 위 손글씨 마크업"),
        ("04 보내기", "축척 맞춰 보내기", "플롯 PDF·DXF 내보내기·리포트·시트 발행. 현장에서 사무실로 바로.", "menu-report", "핀 로그·리포트·플롯 메뉴")],
 hm_new_tag="1.1.1 NEW", news=["공정 일정 달력과 날짜별 노트", "iCloud로 프로젝트 통째로 옮기기", "마크업·핀 사진을 PDF 한 장으로 공유"],
 hm_p_eyebrow="A-201 · 요금제", hm_p_h2="필요한 만큼만 고르세요.", hm_p_sub="월간 요금제는 <b>3일 무료 체험</b>으로 시작합니다.",
 hm_cycle_label="결제 주기", hm_monthly="월간", hm_yearly="연간", hm_yearly_save="2개월 무료",
 rows=["도면 열기·보기 (DWG·DXF·PDF)", "작도·편집 · CAD 도구 12종", "블록·배치 · DXF 내보내기", "축척 맞춘 플롯 PDF", "마크업·사진 핀·노트", "리포트 · 마크업 PDF 공유"],
 per_m="/ 월", per_y="/ 년", billed_y="연 {} 결제", alt_m="월간 결제 시 월 {}", included="포함", not_included="미포함",
 plans=[dict(k="free", name="Free", m="₩0", y="₩0", free=True, tag="도면 3개까지 무료로 불러와 볼 때.", row0="도면 불러오기 3회 무료", cta_m="무료로 받기", cta_y="무료로 받기"),
        dict(k="lite", name="Lite", m="₩4,900", y="₩49,000", tag="사무실처럼 그리고 고칠 때.", cta_m="3일 무료로 시작", cta_y="Lite 시작"),
        dict(k="markup", name="Markup", badge="신규", m="₩8,900", y="₩89,000", tag="현장에서 표시하고 기록할 때.", cta_m="3일 무료로 시작", cta_y="Markup 시작"),
        dict(k="pro", name="Pro", badge="할인 중", hi=True, m="₩12,900", y="₩129,000", was_m="₩16,900", was_y="₩169,000", tag="전부 다. 아이폰 지원 예정.", cta_m="3일 무료로 시작", cta_y="Pro 시작")],
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
 brand_sub="", og_desc="Open, fix, mark up, send. Right on site.", hm_v_eyebrow="A-102 · In action", hm_v_h2="The real app, as it is.", hm_v_sub="Drafting, numeric input and markup — recorded straight from the app.", hm_v_label="Fluxketch in action", hm_swipe="Swipe for more", hm_nav_office="For teams",
 notice="",
 hm_chip="Field CAD · 1.1.1", hm_dim="Our own CAD engine, built from scratch",
 hm_h1="Site drawings,<br><em>done on one tablet.</em>",
 hm_lead="Open DWG, DXF and PDF as they are, fix them on the spot, mark them up,<br>and send scale-true PDF and DXF.",
 hm_cta2="See pricing",
 proof=[("700+", "beta testers"), ("1,000+", "App Store users"), ("30+", "architecture & interior offices"), ("1.4M", "entities in one drawing")],
 hm_f_eyebrow="A-101 · Features", hm_f_h2="Open. Fix. Mark up. Send.", hm_f_sub="Take office drawings out as they are, and send what you touched on site straight back.",
 cards=[("01 Open", "Drawings as they are", "DWG, DXF and PDF with layers, colors, blocks and hatches intact. Smooth even at 1.4M entities.", "granada-topo-dark", "Full Granada topographic map opened in Fluxketch"),
        ("02 Fix", "Draft right on site", "12 CAD tools — line, circle, arc, dimension and more — with endpoint and ortho snaps and a numeric keypad.", "app-detail-dark", "Floor plan with layer palette and CAD tools"),
        ("03 Mark up", "Markup and photo pins", "Handwriting locked to drawing coordinates with pencil pressure, pins with photos and notes, note pages.", "app-markup", "Handwritten markup on a section drawing"),
        ("04 Send", "Send at true scale", "Plot PDF, DXF export, reports and sheet issue. From site to office, right away.", "menu-report", "Pin log, report and plot menu")],
 hm_new_tag="1.1.1 NEW", news=["Schedule calendar with daily notes", "Move whole projects via iCloud", "Share markup and pin photos as one PDF"],
 hm_p_eyebrow="A-201 · Pricing", hm_p_h2="Pick only what you need.", hm_p_sub="Monthly plans start with a <b>3-day free trial</b>.",
 hm_cycle_label="Billing period", hm_monthly="Monthly", hm_yearly="Yearly", hm_yearly_save="2 months free",
 rows=["Open and view DWG, DXF, PDF", "Draft and edit · 12 CAD tools", "Blocks, layouts · DXF export", "Scale-true plot PDF", "Markup, photo pins, notes", "Reports · markup PDF sharing"],
 per_m="/ mo", per_y="/ yr", billed_y="billed {} yearly", alt_m="or {} billed monthly", included="Included", not_included="Not included",
 plans=[dict(k="free", name="Free", m="$0", y="$0", free=True, tag="Import up to 3 drawings free.", row0="3 free drawing imports", cta_m="Get it free", cta_y="Get it free"),
        dict(k="lite", name="Lite", m="$2.99", y="$29.99", tag="Draw and edit like at the office.", cta_m="Start 3-day free trial", cta_y="Start Lite"),
        dict(k="markup", name="Markup", badge="New", m="$5.99", y="$59.99", tag="Mark up and record on site.", cta_m="Start 3-day free trial", cta_y="Start Markup"),
        dict(k="pro", name="Pro", badge="Best value", hi=True, m="$7.99", y="$79.99", tag="Everything. iPhone support coming soon.", cta_m="Start 3-day free trial", cta_y="Start Pro")],
 hm_p_note="Prices shown are for the U.S. App Store; your local price is set by Apple and may differ. Subscriptions renew automatically unless cancelled at least 24 hours before the period ends, and you can cancel anytime in Settings › Apple Account › Subscriptions. Cancel a free trial at least 24 hours before it ends and you won't be charged.",
 hm_o_h="Rolling out to a whole office?", hm_o_p="If your team will use several tablets, email us. We'll help you set up and quote for your headcount and use.", hm_o_btn="Email us about teams",
 o_subject="[Team inquiry] ", o_body="Company:\nContact name & phone:\nNumber of users (tablets):\nPlan of interest (Lite / Markup / Pro):\nQuestion:\n",
 mail_subject="[Fluxketch] ", hm_ft_mail="Email us",
 hm_end_h="Take Fluxketch to your next site.", hm_end_p="Download it from the App Store and start today.",
 hm_biz1="Fluxketch · Owner Junseo Kim · Business Registration No. 102-14-97190 · Mail-Order Business Registration No. 2026-Seoul Gangnam-05411",
 hm_biz2="5F S35, 18 Eonju-ro 134-gil, Gangnam-gu, Seoul, Republic of Korea · +82 10-7179-0722 · flux0720@fluxketch.com",
 ft_tag_home="Field CAD for tablets.<br>Finish it on site.",
)

KO["hm_q_eyebrow"] = "A-301 · 질문"
KO["hm_q_h2"] = "자주 묻는 질문"
KO["hm_q_sub"] = "더 궁금한 점은 flux0720@fluxketch.com으로 보내 주세요."
KO["faq"] = [
 ("플럭스케치(Fluxketch)는 어떤 앱인가요?", "플럭스케치는 현장용 모바일 캐드(CAD) 앱입니다. 사무실의 DWG·DXF 도면을 아이패드에서 그대로 열어 선·원·치수를 CAD 문법으로 그리고 고치고, 펜슬로 마크업하고, 축척 맞춘 PDF와 DXF로 돌려보냅니다. 뷰어가 아니라 편집기입니다."),
 ("무료로 쓸 수 있나요?", "Free는 도면 불러오기 3회까지 무료입니다. 작도·편집과 DXF 내보내기는 Lite(연간 결제 시 월 4,083원·연 49,000원, 월간 결제 시 월 4,900원), 마크업·사진 핀·노트·리포트는 Markup(연간 결제 시 월 7,417원·연 89,000원, 월간 결제 시 월 8,900원), 전부 다 쓰려면 Pro(연간 결제 시 월 10,750원·연 129,000원, 월간 결제 시 월 12,900원)입니다. 월간 요금제는 3일 무료 체험으로 시작합니다."),
 ("Lite·Markup·Pro는 어떻게 다른가요?", "Lite는 사무실처럼 그리고 고치는 작도·편집용, Markup은 현장에서 표시하고 기록하는 마크업·핀·노트·리포트용입니다. Pro는 둘을 한 도면에서 모두 쓰고, 아이폰 지원 예정입니다. 축척 맞춘 플롯 PDF는 Lite·Markup·Pro 모두 됩니다."),
 ("어떤 파일을 열 수 있나요?", "DXF와 DWG(서버 변환), PDF(밑그림)를 엽니다. 레이어·색·굵기·선종류·블록·해치·다중선·3D면·지시선을 가져오고, 가져오지 못한 요소는 리포트에 개수로 표시됩니다."),
 ("인터넷 없이도 되나요?", "DXF·PDF는 완전히 오프라인으로 동작합니다. DWG만 변환 서버가 필요해 인터넷이 필요합니다(PC에서 DXF로 저장하면 오프라인 가능)."),
 ("어떤 기기가 필요한가요?", "아이패드와 펜슬입니다. 큰 도면은 M 시리즈 아이패드에서 가장 쾌적하지만, 9세대·A16 기종에서도 검증했습니다. App Store에서 '플럭스케치' 또는 'Fluxketch'로 검색해 받으실 수 있습니다."),
 ("마크업은 도면과 함께 저장되나요?", "네. 마크업·핀·노트는 도면 파일 안에 도면 좌표로 저장됩니다. 플롯 PDF에 잉크와 핀이 그대로 나가고, 마크업·핀 사진을 PDF 한 장으로 공유할 수도 있습니다."),
 ("사무소 단위로 도입할 수 있나요?", "네. 여러 대를 함께 쓰실 사무소는 flux0720@fluxketch.com으로 사무소명·인원·관심 플랜을 알려 주세요. 도입 상담과 견적을 드립니다."),
 ("구독은 어떻게 해지하나요?", "설정 > Apple 계정 > 구독에서 언제든 해지할 수 있습니다. 기간이 끝날 때까지는 그대로 쓰실 수 있고, 무료 체험은 끝나기 24시간 전에 해지하면 요금이 청구되지 않습니다."),
 ("문제가 있으면 어디로 알리나요?", "앱 첫 화면의 '오류 즉시 문의' 또는 flux0720@fluxketch.com으로 파일과 함께 보내 주세요. 인스타그램 @fluxketch_official으로도 받습니다."),
]
EN["hm_q_eyebrow"] = "A-301 · FAQ"
EN["hm_q_h2"] = "Frequently asked questions"
EN["hm_q_sub"] = "Anything else? Email flux0720@fluxketch.com."
EN["faq"] = [
 ("What is Fluxketch?", "Fluxketch is field CAD for tablets. Open office DWG and DXF drawings as they are, draw and fix them with real CAD tools, mark them up with a pencil, and send back scale-true PDF and DXF. It is an editor, not a viewer."),
 ("Is it free?", "Free includes 3 drawing imports. Drafting, editing and DXF export are Lite ($2.50/mo billed yearly at $29.99, or $2.99 billed monthly); markup, photo pins, notes and reports are Markup ($5.00/mo billed yearly at $59.99, or $5.99 billed monthly); everything is Pro ($6.67/mo billed yearly at $79.99, or $7.99 billed monthly). Monthly plans start with a 3-day free trial."),
 ("How do Lite, Markup and Pro differ?", "Lite is for drafting and editing like at the office. Markup is for marking up and recording on site — markup, pins, notes and reports. Pro gives you both on the same drawing, with iPhone support coming soon. Scale-true plot PDF is in Lite, Markup and Pro."),
 ("Which files can it open?", "DXF, DWG (server conversion) and PDF (underlay). Layers, colors, weights, linetypes, blocks, hatches, multilines, 3D faces and leaders are imported; anything that isn't gets counted in the import report."),
 ("Does it work offline?", "DXF and PDF work fully offline. Only DWG needs the conversion server, so it needs a connection (save as DXF on a PC to work offline)."),
 ("What hardware do I need?", "A tablet and a pencil. Large drawings are most comfortable on M-series models, and we also verify on 9th-gen and A16 models. Search the App Store for \"Fluxketch\" to download."),
 ("Are markups saved with the drawing?", "Yes. Markup, pins and notes are stored inside the drawing file in drawing coordinates. Plot PDFs carry the ink and pins, and you can share markup and pin photos as one PDF."),
 ("Can my whole office use it?", "Yes. Email flux0720@fluxketch.com with your company, headcount and plan of interest, and we'll help you set up and send a quote."),
 ("How do I cancel?", "In Settings > Apple Account > Subscriptions, anytime. You keep access until the period ends, and cancelling a free trial at least 24 hours before it ends means no charge."),
 ("Where do I report a problem?", "Use the app's 'Report a bug now' card or email flux0720@fluxketch.com with the file. Instagram @fluxketch_official works too."),
]

def _e(s): return html.escape(s)

def per_month(yearly):
    """연 금액 문자열(₩49,000 / $29.99) → 월 환산(÷12). 원화 = 정수, 달러 = 소수 둘째 자리(사사오입)."""
    from decimal import Decimal, ROUND_HALF_UP
    sym, num = yearly[0], Decimal(yearly[1:].replace(",", ""))
    if sym == "₩":
        return f"₩{int((num / 12).quantize(Decimal('1'), ROUND_HALF_UP)):,}"
    return f"{sym}{(num / 12).quantize(Decimal('0.01'), ROUND_HALF_UP):,}"

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
            if cyc == "y" and not p.get("free"):
                # 연간 = 기본 표시: 크게 = 연 금액 ÷ 12(월 환산), 옆에 작게 = 연 합산, 아래 = 월간 결제 금액
                billed = (f'<s>{_e(was)}</s> ' if was else "") + _e(p["y"])
                return (f'<div class="pr y"><div class="amt"><b>{_e(per_month(p["y"]))}</b><span>{_e(c["per_m"])}</span>'
                        f'<em class="yr">{c["billed_y"].format(billed)}</em></div>'
                        f'<span class="alt">{_e(c["alt_m"].format(p["m"]))}</span></div>')
            per = "" if p.get("free") else f'<span>{_e(c["per_" + cyc])}</span>'
            return (f'<div class="pr {cyc}">' + (f'<span class="was">{_e(was)}</span>' if was else "")
                    + f'<div class="amt"><b>{_e(p[cyc])}</b>{per}</div></div>')
        rows = "".join(
            (f'<li>{CHECK}<span class="sr">{_e(c["included"])}: </span>{_e(r)}</li>' if HAS[p["k"]][i]
             else f'<li class="off">{DASH}<span class="sr">{_e(c["not_included"])}: </span>{_e(r)}</li>')
            for i, r in enumerate([p.get("row0", c["rows"][0])] + c["rows"][1:]))
        cta = (f'<a class="go m" href="{store_url}" target="_blank" rel="noopener noreferrer">{_e(p["cta_m"])}</a>'
               f'<a class="go y" href="{store_url}" target="_blank" rel="noopener noreferrer">{_e(p["cta_y"])}</a>')
        plans.append(f'      <div class="plan{" hi" if hi else ""}"><div class="top"><span class="nm">{_e(p["name"])}</span>{badge}</div>'
                     f'{amt("m")}{amt("y")}<p class="tg">{_e(p["tag"])}</p><ul>{rows}</ul>{cta}</div>')
    d["hm_plans"] = "\n".join(plans)
    d["hm_o_mail"] = mailto(c["o_subject"], c["o_body"])
    d["hm_mail"] = mailto(c["mail_subject"])
    d["ft_tag"] = c["ft_tag_home"]
    d["hm_faq"] = "\n".join(f'      <details><summary>{_e(q)}<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M12 5v14"/><path d="M5 12h14"/></svg></summary><p>{_e(a)}</p></details>' for q, a in c["faq"])
    return d
