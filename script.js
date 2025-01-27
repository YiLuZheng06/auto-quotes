window.onload = function() {
    document.getElementById("submit").addEventListener('click', async function(event) {
        event.preventDefault();
        let email = document.getElementById('email').value;
        let pwd = document.getElementById('pass').value;
        
        try {
            // Send the POST request
            let response = await fetch('http://127.0.0.1:5000/authenticate', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ email: email, pwd: pwd })
            });

            // Checks if the response is okay
            if (!response.ok) {
                throw new Error(`Server error: ${response.status}`);
            }

            // Parse the response JSON
            let data = await response.json();
            if (data.success) {
                window.location.href = '/dailyQuotes.html';
                console.log('Response:', data);
            } else {
                alert("Authentication failed. Please try again.");
            }
        } catch (error) {
            console.error('Error:', error);
        }
    });
};
