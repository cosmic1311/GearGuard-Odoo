// ========== AUTHENTICATION ==========

// Handle login form submission
function handleLogin(e) {
  e.preventDefault();
  showToast("Login successful");
  
  // Redirect to dashboard after short delay
  setTimeout(() => {
    window.location.href = "dashboard.html";
  }, 700);
}


// Load dark mode preference on page load
document.addEventListener("DOMContentLoaded", function() {
  const darkMode = localStorage.getItem("darkMode");
  if (darkMode === "true") {
    document.documentElement.classList.add("dark");
  }
});

// ========== NOTIFICATIONS ==========

// Show toast notification
function showToast(msg) {
  const toast = document.createElement("div");
  toast.textContent = msg;
  toast.className =
    "fixed bottom-6 right-6 bg-slate-900 text-white px-4 py-3 rounded-lg shadow-lg z-50 animate-fade";
  document.body.appendChild(toast);
  
  // Remove after 2.5 seconds
  setTimeout(() => toast.remove(), 2500);
}

// ========== DRAG AND DROP (Kanban) ==========

// Allow dropping
function allowDrop(e) {
  e.preventDefault();
}

// Start dragging
function drag(e) {
  e.dataTransfer.setData("taskId", e.target.id);
}

// Handle drop
function drop(e, newStage) {
  e.preventDefault();
  
  const taskId = e.dataTransfer.getData("taskId");
  const draggedElement = document.getElementById(taskId);
  
  // Find the drop zone column
  let dropZone = e.target;
  while (!dropZone.hasAttribute('ondrop')) {
    dropZone = dropZone.parentElement;
  }
  
  // Move the card to new column
  dropZone.appendChild(draggedElement);
  
  // Show feedback
  showToast(`Request moved to ${newStage.replace('_', ' ')}`);
  
  // In production: Update backend
  // const requestId = taskId.split('-')[1];
  // fetch(`/api/requests/${requestId}/update_stage`, {
  //   method: 'POST',
  //   headers: {'Content-Type': 'application/json'},
  //   body: JSON.stringify({stage: newStage})
  // });
  
  console.log(`Task ${taskId} moved to ${newStage}`);
}

// ========== CALENDAR FUNCTIONS ==========

// Open modal to create maintenance request
function openModal(dateStr) {
  const modal = document.getElementById("requestModal");
  if (modal) {
    modal.classList.remove("hidden");
    const dateInput = document.getElementById("scheduledDate");
    if (dateInput) {
      dateInput.value = dateStr;
    }
  }
}

// Close modal
function closeModal() {
  const modal = document.getElementById("requestModal");
  if (modal) {
    modal.classList.add("hidden");
    const form = document.getElementById("maintenanceForm");
    if (form) {
      form.reset();
    }
  }
}