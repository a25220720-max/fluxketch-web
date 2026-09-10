/* Fluxketch site v3 — motion system (one orchestrated set; reduced-motion respected) */
(function(){
  const rm = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const nav = document.querySelector('.nav');
  const onScroll = () => nav.classList.toggle('solid', window.scrollY > 8);
  onScroll(); addEventListener('scroll', onScroll, {passive:true});
  const burger = nav.querySelector('.burger');
  burger && burger.addEventListener('click', () => { const o = nav.classList.toggle('open'); burger.setAttribute('aria-expanded', o); });
  nav.querySelectorAll('.menu a').forEach(a => a.addEventListener('click', () => nav.classList.remove('open')));

  // reveal on enter (once)
  const io = new IntersectionObserver((es) => { es.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } }); }, {rootMargin:'0px 0px -12% 0px', threshold:0.12});
  document.querySelectorAll('.reveal').forEach(el => io.observe(el));
  const hero = document.querySelector('.hero'); if (hero) requestAnimationFrame(() => hero.classList.add('in'));

  // hero device tilt (desktop, pointer fine)
  const dev = document.querySelector('.hero .device');
  if (dev && !rm && matchMedia('(pointer:fine)').matches) {
    const stage = document.querySelector('.hero .stage');
    let raf = 0, tx = 0, ty = 0;
    stage.addEventListener('pointermove', (e) => {
      const r = stage.getBoundingClientRect();
      tx = ((e.clientX - r.left) / r.width - .5) * 6; ty = -((e.clientY - r.top) / r.height - .5) * 6;
      if (!raf) raf = requestAnimationFrame(() => { dev.style.transform = `rotateY(${tx}deg) rotateX(${ty}deg)`; raf = 0; });
    });
    stage.addEventListener('pointerleave', () => { dev.style.transition = 'transform .6s cubic-bezier(.2,.7,.2,1)'; dev.style.transform = ''; setTimeout(() => dev.style.transition = '', 600); });
  }

  // feature tabs: auto-advance with progress bar, click to switch, hover pauses
  document.querySelectorAll('.tabs').forEach(tabs => {
    const btns = [...tabs.querySelectorAll('.tab')], panes = [...tabs.querySelectorAll('.pane')];
    const ms = parseInt(tabs.dataset.interval || '6000', 10); tabs.style.setProperty('--tab-ms', ms + 'ms');
    let i = 0, timer = 0, started = false;
    const show = (n) => { i = n; btns.forEach((b, k) => { b.classList.toggle('active', k === n); b.setAttribute('aria-selected', k === n); }); panes.forEach((p, k) => p.classList.toggle('active', k === n)); restart(); };
    const restart = () => { clearInterval(timer); if (!rm) timer = setInterval(() => show((i + 1) % btns.length), ms); };
    btns.forEach((b, k) => { b.addEventListener('click', () => show(k)); b.addEventListener('keydown', e => { if (e.key === 'ArrowDown' || e.key === 'ArrowRight') { e.preventDefault(); show((k + 1) % btns.length); btns[i].focus(); } if (e.key === 'ArrowUp' || e.key === 'ArrowLeft') { e.preventDefault(); show((k - 1 + btns.length) % btns.length); btns[i].focus(); } }); });
    tabs.addEventListener('pointerenter', () => { tabs.classList.add('paused'); clearInterval(timer); });
    tabs.addEventListener('pointerleave', () => { tabs.classList.remove('paused'); restart(); });
    // 첫 탭은 즉시 보인다(관찰자가 못 깨어나도 화면이 비지 않게); 자동 진행만 화면에 들어올 때 시작.
    btns.forEach((b, k) => { b.classList.toggle('active', k === 0); b.setAttribute('aria-selected', k === 0); }); panes.forEach((p, k) => p.classList.toggle('active', k === 0));
    const tio = new IntersectionObserver(es => { es.forEach(e => { if (e.isIntersecting && !started) { started = true; restart(); } }); }, {threshold:0.3});
    tio.observe(tabs);
  });

  // count-up numbers (inline)
  const cio = new IntersectionObserver(es => { es.forEach(e => { if (!e.isIntersecting) return; const el = e.target; cio.unobserve(el); const end = parseFloat(el.dataset.count), dec = (el.dataset.count.split('.')[1] || '').length; if (rm) { el.textContent = end.toLocaleString(undefined,{minimumFractionDigits:dec,maximumFractionDigits:dec}); return; } const t0 = performance.now(), dur = 1400; const step = (t) => { const p = Math.min(1, (t - t0) / dur), v = end * (1 - Math.pow(1 - p, 3)); el.textContent = v.toLocaleString(undefined,{minimumFractionDigits:dec,maximumFractionDigits:dec}); if (p < 1) requestAnimationFrame(step); }; requestAnimationFrame(step); }); }, {threshold:0.6});
  document.querySelectorAll('[data-count]').forEach(el => cio.observe(el));

  // FAQ: close others when one opens (accordion)
  document.querySelectorAll('.faq details').forEach(d => d.addEventListener('toggle', () => { if (d.open) d.parentElement.querySelectorAll('details[open]').forEach(o => { if (o !== d) o.open = false; }); }));
})();
