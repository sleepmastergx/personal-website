// Gentle continuous movement, with a visible pause control and reduced-motion support.
const motionToggle = document.querySelector('.v2 .motion-toggle');
const motionPreference = window.matchMedia('(prefers-reduced-motion: reduce)');
let motionPaused = false;
function updateFishingMotion() {
  const reduced = motionPreference.matches;
  document.body.classList.toggle('motion-enabled', !reduced);
  document.body.classList.toggle('motion-paused', motionPaused || reduced);
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
// Keep keyboard and screen-reader navigation with the selected project.
document.querySelectorAll('.v2 .hero-research-floats a, .v2 .hero-cast, .v2 .catalog-floats a').forEach(link => {
  link.addEventListener('click', () => {
    const target = document.getElementById(link.hash.slice(1));
    if (target) target.focus({preventScroll:true});
  });
});
