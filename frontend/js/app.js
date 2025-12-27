function handleLogin(e) {
  e.preventDefault();
  showToast("Login successful");
  setTimeout(() => window.location.href = "dashboard.html", 700);
}

function toggleDarkMode() {
  document.documentElement.classList.toggle("dark");
  showToast("Theme updated");
}

function showToast(msg) {
  const t = document.createElement("div");
  t.textContent = msg;
  t.className =
    "fixed bottom-6 right-6 bg-slate-900 text-white px-4 py-3 rounded-lg shadow animate-fade";
  document.body.appendChild(t);
  setTimeout(() => t.remove(), 2500);
}

function allowDrop(e) { e.preventDefault(); }
function drag(e) { e.dataTransfer.setData("id", e.target.id); }
function drop(e) {
  e.preventDefault();
  e.target.appendChild(document.getElementById(e.dataTransfer.getData("id")));
  showToast("Request status updated");
}
