// Gentle continuous movement, with a visible pause control and reduced-motion support.
const motionToggle = document.querySelector('.v2 .motion-toggle');
const motionPreference = window.matchMedia('(prefers-reduced-motion: reduce)');
let motionPaused = false;
const eurekaAnimation = document.querySelector('.eureka-animation');
const clipMotionToggle = document.querySelector('.clip-motion-toggle');
let clipPaused = false;
function updateFishingMotion() {
  const reduced = motionPreference.matches;
  document.body.classList.toggle('motion-enabled', !reduced);
  document.body.classList.toggle('motion-paused', motionPaused || reduced);
  if (eurekaAnimation) {
    const paused = motionPaused || clipPaused || reduced;
    const source = paused ? eurekaAnimation.dataset.stillSrc : eurekaAnimation.dataset.motionSrc;
    if (eurekaAnimation.getAttribute('src') !== source) eurekaAnimation.setAttribute('src', source);
    if (clipMotionToggle) {
      clipMotionToggle.hidden = reduced;
      clipMotionToggle.textContent = paused ? 'Resume animation' : 'Pause animation';
      clipMotionToggle.setAttribute('aria-pressed', String(paused));
    }
  }
  if (motionToggle) {
    motionToggle.hidden = reduced;
    motionToggle.textContent = motionPaused ? 'Resume motion' : 'Pause motion';
    motionToggle.setAttribute('aria-pressed', String(motionPaused));
  }
}
if (motionToggle) {
  motionToggle.addEventListener('click', () => {
    motionPaused = !motionPaused;
    updateFishingMotion();
  });
  motionPreference.addEventListener('change', updateFishingMotion);
  updateFishingMotion();
}
if (clipMotionToggle) {
  clipMotionToggle.addEventListener('click', () => {
    if (motionPaused || clipPaused) {
      motionPaused = false;
      clipPaused = false;
    } else {
      clipPaused = true;
    }
    updateFishingMotion();
  });
}
// Keep keyboard and screen-reader navigation with the selected project.
document.querySelectorAll('.v2 .hero-research-floats a, .v2 .hero-cast, .v2 .catalog-floats a').forEach(link => {
  link.addEventListener('click', () => {
    const target = document.getElementById(link.hash.slice(1));
    if (target) target.focus({preventScroll:true});
  });
});
