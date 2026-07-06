// M/V Dream Keeper — depth gauge, ghost-ship descent, rising bubbles
(() => {
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const doc = document.documentElement;
  const val = document.getElementById('depth-val');
  const ship = document.getElementById('ghost-ship');
  const frac = () => doc.scrollTop / (doc.scrollHeight - innerHeight || 1);

  // the gauge is an impression of the descent, not survey data
  const MAXDEPTH = 120;
  let ticking = false;
  const update = () => {
    const p = frac();
    if (val) val.textContent = Math.round(p * MAXDEPTH);
    if (ship) {
      const a = (p - 0.16) / (0.72 - 0.16); // ship drifts down through the mid-dive
      if (a > 0 && a < 1 && !reduce) {
        const fade = Math.min(1, Math.min(a, 1 - a) * 5);
        ship.style.opacity = (0.38 * fade).toFixed(3);
        ship.style.transform =
          `translate(-50%, ${(12 + a * 58).toFixed(2)}vh) rotate(${(a * 12 - 2).toFixed(2)}deg)`;
      } else {
        ship.style.opacity = 0;
      }
    }
    ticking = false;
  };
  addEventListener('scroll', () => {
    if (!ticking) { requestAnimationFrame(update); ticking = true; }
  }, { passive: true });
  addEventListener('resize', update);
  update();

  // bubbles rise toward the surface; the water dims as the page goes deeper
  const canvas = document.getElementById('bubbles');
  if (canvas && !reduce) {
    const ctx = canvas.getContext('2d');
    let W, H, bs = [];
    const resize = () => {
      W = canvas.width = innerWidth * devicePixelRatio;
      H = canvas.height = innerHeight * devicePixelRatio;
      canvas.style.width = innerWidth + 'px';
      canvas.style.height = innerHeight + 'px';
    };
    resize(); addEventListener('resize', resize);

    const N = Math.min(60, Math.floor(innerWidth / 22));
    class B {
      constructor() { this.reset(true); }
      reset(init) {
        this.x = Math.random() * W;
        this.y = init ? Math.random() * H : H + 12 * devicePixelRatio;
        this.r = (Math.random() * 2.4 + .6) * devicePixelRatio;
        this.v = (Math.random() * .7 + .35) * devicePixelRatio;
        this.ph = Math.random() * Math.PI * 2;
      }
      step(t) {
        this.y -= this.v;
        this.x += Math.sin(t / 1400 + this.ph) * .3 * devicePixelRatio;
        if (this.y < -12) this.reset(false);
      }
    }
    for (let i = 0; i < N; i++) bs.push(new B());

    const draw = (t) => {
      ctx.clearRect(0, 0, W, H);
      const alpha = Math.max(.12, .55 - frac() * .45);
      ctx.strokeStyle = `rgba(255,255,255,${alpha})`;
      ctx.lineWidth = devicePixelRatio * .8;
      bs.forEach(b => {
        b.step(t);
        ctx.beginPath();
        ctx.arc(b.x, b.y, b.r, 0, Math.PI * 2);
        ctx.stroke();
      });
      requestAnimationFrame(draw);
    };
    requestAnimationFrame(draw);
  }
})();
