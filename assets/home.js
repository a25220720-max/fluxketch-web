// Fluxketch 홈 v5 — 월간/연간 전환 · 공지 띠 자동 종료 · 접는 메뉴 닫기
(function () {
  var plans = document.getElementById('plans-wrap');
  var seg = document.querySelectorAll('.seg button');
  seg.forEach(function (b) {
    b.addEventListener('click', function () {
      if (plans) plans.setAttribute('data-cycle', b.getAttribute('data-cycle'));
      seg.forEach(function (o) { o.setAttribute('aria-pressed', o === b ? 'true' : 'false'); });
    });
  });

  // 공지 띠: data-until(ISO 시각)이 지나면 저절로 숨긴다 — 10/14 수동 작업 없음
  var notice = document.querySelector('.notice[data-until]');
  if (notice && Date.now() >= Date.parse(notice.getAttribute('data-until'))) notice.hidden = true;

  // 접는 메뉴: 항목을 누르면 닫는다
  var menu = document.querySelector('details.menu');
  if (menu) {
    menu.querySelectorAll('a').forEach(function (a) { a.addEventListener('click', function () { menu.open = false; }); });
    document.addEventListener('click', function (e) { if (menu.open && !menu.contains(e.target)) menu.open = false; });
  }

  // 작동 영상: 화면에 들어오면 재생, 벗어나면 멈춤(데이터 절약 — preload none)
  var v = document.querySelector('.vbox video');
  if (v && 'IntersectionObserver' in window && !matchMedia('(prefers-reduced-motion: reduce)').matches) {
    new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { var p = v.play(); if (p && p.catch) p.catch(function () {}); } else v.pause(); });
    }, { threshold: 0.35 }).observe(v);
  }
})();
