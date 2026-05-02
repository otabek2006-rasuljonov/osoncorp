// Navbar mobile toggle
document.addEventListener('DOMContentLoaded', function () {
  const toggle = document.getElementById('navbarToggle');
  const menu   = document.getElementById('navbarMenu');

  if (toggle && menu) {
    toggle.addEventListener('click', function () {
      menu.classList.toggle('open');
      const isOpen = menu.classList.contains('open');
      toggle.setAttribute('aria-expanded', isOpen);
      const icon = toggle.querySelector('i');
      if (icon) {
        icon.className = isOpen ? 'fas fa-times' : 'fas fa-bars';
      }
    });

    // Close menu when clicking outside
    document.addEventListener('click', function (e) {
      if (!toggle.contains(e.target) && !menu.contains(e.target)) {
        menu.classList.remove('open');
        toggle.setAttribute('aria-expanded', false);
        const icon = toggle.querySelector('i');
        if (icon) icon.className = 'fas fa-bars';
      }
    });
  }

  // Auto-dismiss messages after 5s
  const messages = document.querySelectorAll('.messages li');
  messages.forEach(function (msg) {
    setTimeout(function () {
      msg.style.transition = 'opacity 0.5s';
      msg.style.opacity = '0';
      setTimeout(function () { msg.remove(); }, 500);
    }, 5000);
  });
});
