// Navbar Scroll Effect
document.addEventListener('DOMContentLoaded', function() {
    const navbar = document.querySelector('.navbar');
    
    window.addEventListener('scroll', function() {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    // Set active nav link based on current page
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll('.navbar .nav-link');

    navLinks.forEach(link => {
        const href = link.getAttribute('href');
        if (href && currentPath.includes(href) && href !== '/') {
            link.classList.add('active');
        } else if (href === '/' && currentPath === '/') {
            link.classList.add('active');
        }
    });

    // Add body class for page-specific styling
    if (currentPath === '/' || currentPath === '') {
        document.body.classList.add('home');
    } else if (currentPath.includes('/about/')) {
        document.body.classList.add('about');
    } else if (currentPath.includes('/courses/')) {
        document.body.classList.add('courses');
    } else if (currentPath.includes('/resources/')) {
        document.body.classList.add('resources');
    } else if (currentPath.includes('/contact/')) {
        document.body.classList.add('contact');
    }

    // Contact form enhancements
    const contactForm = document.querySelector('.contact-form form');
    if (contactForm) {
        // Add input highlight spans
        const floatingInputs = contactForm.querySelectorAll('.form-floating');
        floatingInputs.forEach(container => {
            const highlightSpan = document.createElement('span');
            highlightSpan.className = 'input-highlight';
            container.appendChild(highlightSpan);
        });

        // File upload preview
        const fileInput = contactForm.querySelector('input[type="file"]');
        if (fileInput) {
            const previewContainer = document.querySelector('.custom-file-preview');
            const fileLabel = document.querySelector('.custom-file-label');

            fileInput.addEventListener('change', function() {
                previewContainer.innerHTML = '';
                if (this.files.length > 0) {
                    fileLabel.textContent = `${this.files.length} file(s) selected`;

                    Array.from(this.files).forEach(file => {
                        const fileItem = document.createElement('div');
                        fileItem.className = 'file-preview-item';

                        // Choose icon based on file type
                        let iconClass = 'fas fa-file';
                        if (file.type.includes('image')) {
                            iconClass = 'fas fa-file-image';
                        } else if (file.type.includes('pdf')) {
                            iconClass = 'fas fa-file-pdf';
                        } else if (file.type.includes('word')) {
                            iconClass = 'fas fa-file-word';
                        }

                        fileItem.innerHTML = `
                            <i class="${iconClass}"></i>
                            ${file.name}
                            <span class="remove-file"><i class="fas fa-times"></i></span>
                        `;

                        previewContainer.appendChild(fileItem);
                    });

                    // Remove file functionality
                    document.querySelectorAll('.remove-file').forEach(removeBtn => {
                        removeBtn.addEventListener('click', function(e) {
                            e.preventDefault();
                            this.parentElement.remove();
                            if (previewContainer.children.length === 0) {
                                fileLabel.textContent = 'Choose files or drag and drop here';
                                fileInput.value = '';
                            } else {
                                fileLabel.textContent = `${previewContainer.children.length} file(s) selected`;
                            }
                        });
                    });
                } else {
                    fileLabel.textContent = 'Choose files or drag and drop here';
                }
            });
        }
    }
    });

    // Add fade-in animation to elements
    const fadeElements = document.querySelectorAll('.fade-in');
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-fade-in');
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.1
    });

    fadeElements.forEach(element => observer.observe(element));

    // Course card hover effect
    const courseCards = document.querySelectorAll('.course-card');
    courseCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-10px)';
        });

        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });

    // Progress bar animation
    const progressBars = document.querySelectorAll('.progress-bar');
    progressBars.forEach(bar => {
        const targetWidth = bar.getAttribute('aria-valuenow') + '%';
        bar.style.width = '0%';
        setTimeout(() => {
            bar.style.width = targetWidth;
        }, 100);
    });

    // Search form enhancement
    const searchForm = document.querySelector('.search-form');
    if (searchForm) {
        const searchInput = searchForm.querySelector('input[type="text"]');
        let debounceTimer;

        searchInput.addEventListener('input', function() {
            clearTimeout(debounceTimer);
            debounceTimer = setTimeout(() => {
                // Add loading state
                searchForm.classList.add('is-loading');
                
                // Simulate search delay
                setTimeout(() => {
                    searchForm.classList.remove('is-loading');
                }, 500);
            }, 300);
        });
    }

    // Category filter animation
    const categoryPills = document.querySelectorAll('.category-pill');
    categoryPills.forEach(pill => {
        pill.addEventListener('click', function(e) {
            e.preventDefault();
            
            // Remove active class from all pills
            categoryPills.forEach(p => p.classList.remove('active'));
            
            // Add active class to clicked pill
            this.classList.add('active');
            
            // Add loading animation to course grid
            const courseGrid = document.querySelector('.course-grid');
            if (courseGrid) {
                courseGrid.classList.add('loading');
                setTimeout(() => {
                    courseGrid.classList.remove('loading');
                }, 500);
            }
        });
    });

    // Dark mode toggle
    const darkModeToggle = document.querySelector('.dark-mode-toggle');
    if (darkModeToggle) {
        darkModeToggle.addEventListener('click', function() {
            document.documentElement.classList.toggle('dark-mode');
            localStorage.setItem('darkMode', 
                document.documentElement.classList.contains('dark-mode')
            );
        });
    }

    // Initialize dark mode from localStorage
    if (localStorage.getItem('darkMode') === 'true') {
        document.documentElement.classList.add('dark-mode');
    }

    // Smooth scroll to sections
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Form validation enhancement
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            if (!form.checkValidity()) {
                e.preventDefault();
                e.stopPropagation();
                
                // Add shake animation to invalid fields
                const invalidInputs = form.querySelectorAll(':invalid');
                invalidInputs.forEach(input => {
                    input.classList.add('shake');
                    setTimeout(() => {
                        input.classList.remove('shake');
                    }, 600);
                });
            }
            form.classList.add('was-validated');
        });
    });

    // Add loading state to buttons
    const buttons = document.querySelectorAll('.btn');
    buttons.forEach(button => {
        button.addEventListener('click', function() {
            if (this.getAttribute('data-loading') === 'true') {
                this.classList.add('is-loading');
                this.setAttribute('disabled', true);
                
                // Simulate loading state
                setTimeout(() => {
                    this.classList.remove('is-loading');
                    this.removeAttribute('disabled');
                }, 1000);
            }
        });
    });
}); 