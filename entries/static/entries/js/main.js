document.addEventListener('DOMContentLoaded', function() {
    // Emoji hover effects
    document.querySelectorAll('.mood-emoji, .display-6').forEach(emoji => {
        emoji.addEventListener('mouseover', function() {
            this.style.transform = `scale(1.3) rotate(${Math.random() * 20 - 10}deg)`;
            this.style.transition = 'transform 0.3s ease';
        });
        
        emoji.addEventListener('mouseout', function() {
            this.style.transform = 'scale(1) rotate(0deg)';
        });
    });

    // Add mood-specific animations to emoji headers
    document.querySelectorAll('.display-4-emoji').forEach(emoji => {
        const moodAnimations = {
            '😊': 'happy-bounce',
            '😢': 'sad-drop',
            '😠': 'angry-shake',
            '😲': 'surprised-pop',
            '😴': 'tired-sway',
            '😃': 'excited-jump',
            '😌': 'peaceful-float'
        };

        emoji.addEventListener('mouseover', function() {
            const mood = this.textContent.trim();
            const animation = moodAnimations[mood] || 'bounce';
            this.style.animation = `${animation} 1s ease infinite`;
        });
        
        emoji.addEventListener('mouseout', function() {
            this.style.animation = '';
        });
    });

    // Card entrance animations
    const cards = document.querySelectorAll('.card');
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '50px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    cards.forEach(card => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        card.style.transition = 'all 0.5s ease-out';
        observer.observe(card);
    });

    // Random background patterns
    const patterns = [
        'repeating-linear-gradient(45deg, #fff5f8 0px, #fff5f8 10px, transparent 10px, transparent 20px)',
        'radial-gradient(circle at 50% 50%, #fff5f8 1px, transparent 1px)',
        'linear-gradient(45deg, #fff5f8 25%, transparent 25%)',
    ];

    document.body.style.backgroundImage = patterns[Math.floor(Math.random() * patterns.length)];
});
