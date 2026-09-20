// Example starter JavaScript for disabling form submissions if there are invalid fields
(() => {
  'use strict'

  // Fetch all the forms we want to apply custom Bootstrap validation styles to
  const forms = document.querySelectorAll(".needs-validation")

  // Loop over them and prevent submission
  Array.from(forms).forEach(form => {
    form.addEventListener("submit", event => {
      if (!form.checkValidity()) {
        event.preventDefault()
        event.stopPropagation()
      }

      form.classList.add("was-validated");
    }, false)
  })
})();

// Minimalist Fast Splash Screen with Strict Session Control
document.addEventListener("DOMContentLoaded", () => {
  const splash = document.getElementById("splash-screen");
  if (!splash) return;

  // Check if user has already seen splash in this session
  if (sessionStorage.getItem("hasSeenSplash")) {
    splash.style.display = "none";
    document.body.classList.remove("splash-active");
    return;
  }

  // Mark as seen immediately for subsequent page loads / subpages
  sessionStorage.setItem("hasSeenSplash", "true");

  // Lock scroll temporarily for 1.5 seconds max
  document.body.classList.add("splash-active");

  // Automatic Fade-Out after 1.5 seconds (1500ms)
  setTimeout(() => {
    splash.classList.add("fade-out");
    document.body.classList.remove("splash-active");

    // Unmount from layout after fade transition (500ms)
    setTimeout(() => {
      splash.style.display = "none";
    }, 500);
  }, 1500);
});