// Carousel functionality
document.addEventListener('DOMContentLoaded', function() {
    const carousel = document.querySelector('.carousel');
    const prevBtn = document.querySelector('.carousel-prev');
    const nextBtn = document.querySelector('.carousel-next');
    const slides = carousel.querySelectorAll('img');
    
    let currentSlide = 0;
    
    function showSlide(index) {
        slides.forEach((slide, i) => {
            slide.style.opacity = i === index ? '1' : '0';
        });
    }
    
    function nextSlide() {
        currentSlide = (currentSlide + 1) % slides.length;
        showSlide(currentSlide);
    }
    
    function prevSlide() {
        currentSlide = (currentSlide - 1 + slides.length) % slides.length;
        showSlide(currentSlide);
    }
    
    nextBtn.addEventListener('click', nextSlide);
    prevBtn.addEventListener('click', prevSlide);
    
    // Auto-advance carousel every 5 seconds
    setInterval(nextSlide, 5000);
    
    // Show the first slide initially
    showSlide(currentSlide);
});
