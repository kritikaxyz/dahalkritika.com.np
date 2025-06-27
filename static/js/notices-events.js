// Notice and Event functionality
document.addEventListener('DOMContentLoaded', function() {
    // Add animation to notices when they appear in viewport
    const noticeItems = document.querySelectorAll('.list-group-item');
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

    noticeItems.forEach(item => {
        item.style.opacity = '0';
        item.style.transform = 'translateY(20px)';
        item.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
        observer.observe(item);
    });

    // Initialize tooltips for event details
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Add hover effect to important notices
    const importantNotices = document.querySelectorAll('.border-danger');
    importantNotices.forEach(notice => {
        notice.addEventListener('mouseenter', function() {
            this.style.borderColor = '#ef4444';
        });

        notice.addEventListener('mouseleave', function() {
            this.style.borderColor = '#dc2626';
        });
    });

    // Notice read more functionality
    const readMoreButtons = document.querySelectorAll('.btn-link');
    readMoreButtons.forEach(button => {
        button.addEventListener('click', function() {
            // Add loading state
            const originalText = this.innerHTML;
            this.innerHTML = '<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Loading...';

            // Simulate loading (in real app, this would be fetching data)
            setTimeout(() => {
                this.innerHTML = originalText;
            }, 500);
        });
    });

    // Calendar view toggle for events (if implemented)
    const viewToggleButtons = document.querySelectorAll('.view-toggle');
    viewToggleButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();

            const view = this.getAttribute('data-view');
            const eventsContainer = document.querySelector('.events-container');

            // Toggle active class
            viewToggleButtons.forEach(btn => btn.classList.remove('active'));
            this.classList.add('active');

            // Toggle view
            if (view === 'list') {
                eventsContainer.classList.remove('calendar-view');
                eventsContainer.classList.add('list-view');
            } else {
                eventsContainer.classList.remove('list-view');
                eventsContainer.classList.add('calendar-view');
            }
        });
    });
});
