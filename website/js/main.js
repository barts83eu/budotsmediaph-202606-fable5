// BUDOTS MEDIA PH — parallax, particles, scroll indicators
(() => {
  // ---- scroll progress bar ----
  const bar = document.getElementById('progress');
  const onScrollProgress = () => {
    if (!bar) return;
    const h = document.documentElement;
    const p = h.scrollTop / (h.scrollHeight - h.clientHeight);
    bar.style.width = (p * 100) + '%';
  };

  // ---- parallax backgrounds (rAF, mobile-friendly) ----
  const layers = [...document.querySelectorAll('[data-parallax]')];
  let ticking = false;
  const parallax = () => {
    const vh = window.innerHeight;
    layers.forEach(el => {
      const speed = parseFloat(el.dataset.parallax) || 0.3;
      const r = el.parentElement.getBoundingClientRect();
      if (r.bottom < 0 || r.top > vh) return;
      const offset = (r.top + r.height / 2 - vh / 2) * speed;
      el.style.transform = `translate3d(0, ${offset}px, 0)`;
    });
    ticking = false;
  };
  const requestTick = () => {
    if (!ticking) { requestAnimationFrame(() => { parallax(); onScrollProgress(); updateDots(); }); ticking = true; }
  };
  addEventListener('scroll', requestTick, { passive: true });
  addEventListener('resize', requestTick);

  // ---- section dots ----
  const sections = [...document.querySelectorAll('[data-dot]')];
  const dotsWrap = document.querySelector('.dots');
  if (dotsWrap && sections.length) {
    sections.forEach((s, i) => {
      const a = document.createElement('a');
      a.href = '#' + s.id;
      a.setAttribute('aria-label', s.dataset.dot);
      dotsWrap.appendChild(a);
    });
  }
  const updateDots = () => {
    if (!dotsWrap) return;
    const links = dotsWrap.querySelectorAll('a');
    let active = 0;
    sections.forEach((s, i) => {
      if (s.getBoundingClientRect().top <= innerHeight * 0.45) active = i;
    });
    links.forEach((l, i) => l.classList.toggle('active', i === active));
  };

  // ---- reveal on scroll ----
  const io = new IntersectionObserver(es =>
    es.forEach(e => e.isIntersecting && e.target.classList.add('visible')),
    { threshold: 0.12 });
  document.querySelectorAll('.reveal').forEach(el => io.observe(el));

  // ---- sophisticated particles ----
  const canvas = document.getElementById('particles');
  if (canvas) {
    const ctx = canvas.getContext('2d');
    let W, H, pts = [];
    const N = Math.min(90, Math.floor(innerWidth / 14));
    const resize = () => {
      W = canvas.width = innerWidth * devicePixelRatio;
      H = canvas.height = innerHeight * devicePixelRatio;
      canvas.style.width = innerWidth + 'px';
      canvas.style.height = innerHeight + 'px';
    };
    resize(); addEventListener('resize', resize);

    class P {
      constructor() { this.reset(true); }
      reset(init) {
        this.x = Math.random() * W;
        this.y = init ? Math.random() * H : (Math.random() < .5 ? -10 : H + 10);
        this.vx = (Math.random() - .5) * .35 * devicePixelRatio;
        this.vy = (Math.random() - .5) * .35 * devicePixelRatio;
        this.r = (Math.random() * 1.6 + .4) * devicePixelRatio;
        this.ph = Math.random() * Math.PI * 2;
      }
      step(t) {
        // drift + gentle sine sway = "sophisticated" motion
        this.x += this.vx + Math.sin(t / 2400 + this.ph) * .18 * devicePixelRatio;
        this.y += this.vy + Math.cos(t / 3100 + this.ph) * .12 * devicePixelRatio;
        if (this.x < -20 || this.x > W + 20 || this.y < -20 || this.y > H + 20) this.reset(false);
      }
    }
    for (let i = 0; i < N; i++) pts.push(new P());

    const LINK = 110 * devicePixelRatio;
    const draw = (t) => {
      ctx.clearRect(0, 0, W, H);
      // fade particles out toward the white bottom of the page
      const pageP = document.documentElement.scrollTop /
        (document.documentElement.scrollHeight - innerHeight || 1);
      const alpha = Math.max(0, 0.9 - pageP * 1.1);
      if (alpha > 0.02) {
        pts.forEach(p => {
          p.step(t);
          ctx.beginPath();
          ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
          ctx.fillStyle = `rgba(255,255,255,${alpha * .8})`;
          ctx.fill();
        });
        for (let i = 0; i < pts.length; i++)
          for (let j = i + 1; j < pts.length; j++) {
            const a = pts[i], b = pts[j];
            const d = Math.hypot(a.x - b.x, a.y - b.y);
            if (d < LINK) {
              ctx.strokeStyle = `rgba(255,212,0,${(1 - d / LINK) * alpha * .25})`;
              ctx.lineWidth = devicePixelRatio * .5;
              ctx.beginPath(); ctx.moveTo(a.x, a.y); ctx.lineTo(b.x, b.y); ctx.stroke();
            }
          }
      }
      requestAnimationFrame(draw);
    };
    requestAnimationFrame(draw);
  }

  // ---- animated counters ----
  const counters = document.querySelectorAll('[data-count]');
  const cio = new IntersectionObserver(es => es.forEach(e => {
    if (!e.isIntersecting || e.target.dataset.done) return;
    e.target.dataset.done = 1;
    const end = parseInt(e.target.dataset.count, 10);
    const t0 = performance.now(), dur = 1600;
    const tick = now => {
      const p = Math.min(1, (now - t0) / dur);
      e.target.textContent = Math.round(end * (1 - Math.pow(1 - p, 3))).toLocaleString();
      if (p < 1) requestAnimationFrame(tick);
    };
    requestAnimationFrame(tick);
  }), { threshold: .5 });
  counters.forEach(el => cio.observe(el));

  requestTick();
})();
