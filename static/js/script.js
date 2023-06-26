document.addEventListener('DOMContentLoaded', function() {
    // Get the register form
    var registerForm = document.getElementById('register-form');

    // Add submit event listener to the register form
    registerForm.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent the form from submitting

        // Get the form inputs
        var usernameInput = document.getElementById('username');
        var passwordInput = document.getElementById('password');

        // Prepare the data to send
        var data = {
            username: usernameInput.value,
            password: passwordInput.value
        };

        // Make a POST request to the registration API endpoint
        fetch('/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(function(response) {
            if (response.ok) {
                return response.json();
            } else {
                throw new Error('Registration failed');
            }
        })
        .then(function(data) {
            alert(data.message); // Show success message
            registerForm.reset(); // Reset the form
        })
        .catch(function(error) {
            alert(error.message); // Show error message
        });
    });

    // Get the login form
    var loginForm = document.getElementById('login-form');

    // Add submit event listener to the login form
    loginForm.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent the form from submitting

        // Get the form inputs
        var usernameInput = document.getElementById('username');
        var passwordInput = document.getElementById('password');

        // Prepare the data to send
        var data = {
            username: usernameInput.value,
            password: passwordInput.value
        };

        // Make a POST request to the login API endpoint
        fetch('/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(function(response) {
            if (response.ok) {
                return response.json();
            } else {
                throw new Error('Login failed');
            }
        })
        .then(function(data) {
            alert(data.message); // Show success message
            loginForm.reset(); // Reset the form
        })
        .catch(function(error) {
            alert(error.message); // Show error message
        });
    });
});

