document.addEventListener("DOMContentLoaded", function () {
  const alerts = document.querySelectorAll(".alert");
  alerts.forEach(function (alert) {
    setTimeout(function () {
      alert.style.opacity = "0";
      alert.style.position = "opacity 0.5s";
      setTimeout(() => alert.remove(), 500);
    }, 3000);
  });
});
