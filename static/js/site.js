const menuToggle = document.querySelector(".menu-toggle");
const mobileNav = document.querySelector(".mobile-nav");

menuToggle.addEventListener("click", () => {
  const isExpanded = menuToggle.getAttribute("aria-expanded") === "true";
  menuToggle.setAttribute("aria-expanded", String(!isExpanded));
  mobileNav.classList.toggle("hidden", isExpanded);
});

mobileNav.querySelectorAll("a").forEach((link) => {
  link.addEventListener("click", () => {
    mobileNav.classList.add("hidden");
    menuToggle.setAttribute("aria-expanded", "false");
  });
});

const lightbox = document.createElement("div");
lightbox.className = "lightbox-overlay";
lightbox.innerHTML = '<button class="lightbox-close" type="button" aria-label="Закрыть">✕</button><img alt="">';
document.body.appendChild(lightbox);
const lightboxImage = lightbox.querySelector("img");

function openLightbox(src, alt) {
  lightboxImage.src = src;
  lightboxImage.alt = alt || "";
  lightbox.classList.add("is-open");
  document.body.classList.add("lightbox-locked");
}

function closeLightbox() {
  lightbox.classList.remove("is-open");
  document.body.classList.remove("lightbox-locked");
  lightboxImage.src = "";
}

document.querySelectorAll(".js-zoomable").forEach((img) => {
  img.addEventListener("click", () => openLightbox(img.currentSrc || img.src, img.alt));
});

lightbox.addEventListener("click", (event) => {
  if (event.target === lightbox) closeLightbox();
});
lightbox.querySelector(".lightbox-close").addEventListener("click", closeLightbox);
document.addEventListener("keydown", (event) => {
  if (event.key === "Escape") closeLightbox();
});

function carouselStep(track) {
  const card = track.querySelector(":scope > *");
  const gap = parseFloat(getComputedStyle(track).columnGap || getComputedStyle(track).gap || "16") || 16;
  return card ? card.getBoundingClientRect().width + gap : track.clientWidth * 0.8;
}

function scrollCarousel(track, direction) {
  const atEnd = direction > 0 && track.scrollLeft + track.clientWidth >= track.scrollWidth - 4;
  if (atEnd) {
    track.scrollTo({ left: 0, behavior: "smooth" });
    return;
  }
  const atStart = direction < 0 && track.scrollLeft <= 4;
  if (atStart) {
    track.scrollTo({ left: track.scrollWidth, behavior: "smooth" });
    return;
  }
  track.scrollBy({ left: direction * carouselStep(track), behavior: "smooth" });
}

document.querySelectorAll("[data-carousel-target]").forEach((button) => {
  const track = document.getElementById(button.dataset.carouselTarget);
  if (!track) return;
  button.addEventListener("click", () => {
    scrollCarousel(track, button.classList.contains("carousel-prev") ? -1 : 1);
    pauseAutoCarousel(track);
  });
});

const autoCarouselPauses = new WeakMap();

function pauseAutoCarousel(track) {
  const pause = autoCarouselPauses.get(track);
  if (pause) pause();
}

document.querySelectorAll(".auto-carousel").forEach((track) => {
  if (track.children.length < 2) return;
  const interval = 4200;
  let timer = null;
  let paused = false;
  let resumeTimeout = null;

  function tick() {
    if (!paused) scrollCarousel(track, 1);
  }

  function start() {
    stop();
    timer = window.setInterval(tick, interval);
  }

  function stop() {
    if (timer) window.clearInterval(timer);
    timer = null;
  }

  function pauseAndResumeLater() {
    paused = true;
    window.clearTimeout(resumeTimeout);
    resumeTimeout = window.setTimeout(() => { paused = false; }, interval * 2);
  }

  autoCarouselPauses.set(track, pauseAndResumeLater);

  track.addEventListener("mouseenter", () => { paused = true; });
  track.addEventListener("mouseleave", () => { paused = false; });
  track.addEventListener("touchstart", pauseAndResumeLater, { passive: true });
  track.addEventListener("pointerdown", pauseAndResumeLater);

  if (!window.matchMedia("(prefers-reduced-motion: reduce)").matches) start();
});