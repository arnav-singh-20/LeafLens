<script>
    const form = document.querySelector('form');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        const formData = {
            first_name : document.querySelector('input[name="first_name"]').value,
            last_name : document.querySelector('input[name="last_name"]').value,
            email: document.querySelector('input[name="email"]').value,
            message: document.querySelector('textarea[name="message"]').value,
        };

        const response = await fetch('http://localhost:5000/submit', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData),
        });

        if (response.ok) {
            alert('Contact information saved successfully!');
            form.reset();
        } else {
            const error = await response.json();
            alert(`Error: ${error.error}`);
        }
    });
</script>
