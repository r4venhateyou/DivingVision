document.addEventListener('DOMContentLoaded', function() {
    const modal = document.getElementById('modal');
    const modalTitle = document.getElementById('modal-title');
    const modalImage = document.getElementById('modal-image');
    const modalDescription = document.getElementById('modal-description');
    const closeButton = document.querySelector('.close-button');

    document.querySelectorAll('.marine-card').forEach(card => {
        card.addEventListener('click', function() {
            const lifeId = this.getAttribute('data-id');
            fetch(`/marine_life/${lifeId}`)
                .then(response => response.json())
                .then(data => {
                    modalTitle.innerText = data.name;
                    modalImage.src = `static/images/${data.image}`;
                    modalDescription.innerText = data.description;
                    modal.style.display = 'block';
                })
                .catch(error => console.error('Error:', error));
        });
    });

    closeButton.addEventListener('click', function() {
        modal.style.display = 'none';
    });

    window.addEventListener('click', function(event) {
        if (event.target == modal) {
            modal.style.display = 'none';
        }
    });
});

