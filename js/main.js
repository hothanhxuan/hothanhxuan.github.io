// ========== DARK MODE ==========
const themeToggle = document.getElementById('theme-toggle');
const root = document.documentElement;

function setTheme(theme) {
  root.setAttribute('data-theme', theme);
  localStorage.setItem('theme', theme);
  const icon = themeToggle?.querySelector('.theme-icon');
  if (icon) icon.textContent = theme === 'dark' ? '☀️' : '🌙';
}

// Init theme
const saved = localStorage.getItem('theme');
const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
setTheme(saved || (prefersDark ? 'dark' : 'light'));

themeToggle?.addEventListener('click', () => {
  const current = root.getAttribute('data-theme');
  setTheme(current === 'dark' ? 'light' : 'dark');
});

// ========== MOBILE MENU ==========
const hamburger = document.getElementById('hamburger');
const navLinks = document.getElementById('nav-links');
const navOverlay = document.getElementById('nav-overlay');

function toggleMenu() {
  hamburger?.classList.toggle('active');
  navLinks?.classList.toggle('open');
  navOverlay?.classList.toggle('open');
  document.body.style.overflow = navLinks?.classList.contains('open') ? 'hidden' : '';
}

hamburger?.addEventListener('click', toggleMenu);
navOverlay?.addEventListener('click', toggleMenu);
document.querySelectorAll('.nav-links a').forEach(link => {
  link.addEventListener('click', () => {
    if (navLinks?.classList.contains('open')) toggleMenu();
  });
});

// ========== NAVBAR SCROLL ==========
const navbar = document.querySelector('.navbar');
window.addEventListener('scroll', () => {
  navbar?.classList.toggle('scrolled', window.scrollY > 20);
});

// ========== TYPING ANIMATION ==========
const typingEl = document.getElementById('typing-text');
if (typingEl) {
  const titles = ['Business Analyst', 'Data Analyst', 'BI Specialist', 'Problem Solver'];
  let titleIdx = 0, charIdx = 0, deleting = false;

  function type() {
    const current = titles[titleIdx];
    typingEl.textContent = current.substring(0, charIdx);

    if (!deleting) {
      charIdx++;
      if (charIdx > current.length) {
        deleting = true;
        setTimeout(type, 2000);
        return;
      }
    } else {
      charIdx--;
      if (charIdx === 0) {
        deleting = false;
        titleIdx = (titleIdx + 1) % titles.length;
      }
    }
    setTimeout(type, deleting ? 40 : 80);
  }
  setTimeout(type, 500);
}

// ========== SCROLL REVEAL ==========
const revealElements = document.querySelectorAll('.reveal');
const revealObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('active');
    }
  });
}, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

revealElements.forEach(el => revealObserver.observe(el));

// ========== ANIMATED SKILL BARS ==========
const skillBars = document.querySelectorAll('.skill-fill');
const skillObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const target = entry.target;
      target.style.width = target.dataset.width;
      skillObserver.unobserve(target);
    }
  });
}, { threshold: 0.3 });

skillBars.forEach(bar => skillObserver.observe(bar));

// ========== PROJECT FILTER ==========
const mainFilterBtns = document.querySelectorAll('#main-filter-bar .filter-btn');
const subFilterBar = document.getElementById('sub-filter-bar');
const subFilterBtns = document.querySelectorAll('#sub-filter-bar .filter-btn');
const sectionBusiness = document.getElementById('section-business');
const sectionData = document.getElementById('section-data');

function animateCards(cards) {
  cards.forEach(card => {
    if (card.style.display !== 'none') {
      card.style.opacity = '0';
      card.style.transform = 'translateY(20px)';
      requestAnimationFrame(() => {
        card.style.transition = 'opacity 0.4s ease, transform 0.4s ease';
        card.style.opacity = '1';
        card.style.transform = 'translateY(0)';
      });
    }
  });
}

function showAllCards(section) {
  section.querySelectorAll('.project-card').forEach(card => {
    card.style.display = '';
  });
}

// Main filter logic
if (mainFilterBtns.length) {
  mainFilterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      mainFilterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const filter = btn.dataset.filter;

      if (filter === 'all') {
        // Show both sections, all cards
        if (sectionBusiness) { sectionBusiness.style.display = ''; showAllCards(sectionBusiness); }
        if (sectionData) { sectionData.style.display = ''; showAllCards(sectionData); }
        if (subFilterBar) { subFilterBar.classList.remove('visible'); subFilterBar.classList.add('hidden'); }
        animateCards(document.querySelectorAll('.project-card'));
      } else if (filter === 'business') {
        // Show only business section
        if (sectionBusiness) { sectionBusiness.style.display = ''; showAllCards(sectionBusiness); }
        if (sectionData) sectionData.style.display = 'none';
        if (subFilterBar) { subFilterBar.classList.remove('visible'); subFilterBar.classList.add('hidden'); }
        animateCards(sectionBusiness.querySelectorAll('.project-card'));
      } else if (filter === 'data') {
        // Show only data section, show sub-filters
        if (sectionBusiness) sectionBusiness.style.display = 'none';
        if (sectionData) { sectionData.style.display = ''; showAllCards(sectionData); }
        if (subFilterBar) { subFilterBar.classList.remove('hidden'); subFilterBar.classList.add('visible'); }
        // Reset sub-filter to "All Data"
        subFilterBtns.forEach(b => b.classList.remove('active'));
        const allDataBtn = document.querySelector('[data-subfilter="all-data"]');
        if (allDataBtn) allDataBtn.classList.add('active');
        animateCards(sectionData.querySelectorAll('.project-card'));
      }
    });
  });
}

// Sub-filter logic (within Data section)
if (subFilterBtns.length && sectionData) {
  subFilterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      subFilterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const subfilter = btn.dataset.subfilter;
      const dataCards = sectionData.querySelectorAll('.project-card');

      dataCards.forEach(card => {
        const tags = card.dataset.tags || '';
        const show = subfilter === 'all-data' || tags.includes(subfilter);
        card.style.display = show ? '' : 'none';
      });
      animateCards(dataCards);
    });
  });
}

// ========== BACK TO TOP ==========
const backToTop = document.getElementById('back-to-top');
window.addEventListener('scroll', () => {
  backToTop?.classList.toggle('visible', window.scrollY > 400);
});
backToTop?.addEventListener('click', () => {
  window.scrollTo({ top: 0, behavior: 'smooth' });
});

// ========== ACTIVE NAV LINK ==========
const currentPage = window.location.pathname.split('/').pop() || 'index.html';
document.querySelectorAll('.nav-links a').forEach(link => {
  const href = link.getAttribute('href');
  if (href === currentPage || (currentPage === '' && href === 'index.html')) {
    link.classList.add('active');
  }
});
