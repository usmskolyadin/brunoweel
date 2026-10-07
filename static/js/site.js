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