// Wait for the DOM to fully load before executing the script
document.addEventListener('DOMContentLoaded', function () {
    // Get references to the input fields and feedback elements
    const usernameInput = document.getElementById('id_username');
    const emailInput = document.getElementById('id_email');
    const usernameFeedback = document.getElementById('username-feedback');
    const emailFeedback = document.getElementById('email-feedback');

    // Add an event listener to the username input field to handle real-time validation
    usernameInput.addEventListener('input', function () {
        const username = usernameInput.value;

        // Check if the username field is not empty
        if (username) {
            // Make an AJAX request to check if the username is already taken
            fetch(`/accounts/ajax/check_username/?username=${username}`)
                .then(response => response.json())
                .then(data => {
                    // If the username is taken, show an error message and apply invalid styles
                    if (data.is_taken) {
                        usernameFeedback.textContent = 'A user with that username already exists.';
                        usernameFeedback.classList.add('d-block');
                        usernameInput.classList.add('is-invalid');
                    } else {
                        // If the username is available, show a success message and apply valid styles
                        usernameFeedback.textContent = 'Username is available.';
                        usernameFeedback.classList.add('d-block');
                        usernameFeedback.classList.remove('invalid-feedback');
                        usernameFeedback.classList.add('valid-feedback');
                        usernameInput.classList.remove('is-invalid');
                        usernameInput.classList.add('is-valid');
                    }
                });
        } else {
            // Clear the feedback and remove validation styles if the input is empty
            usernameFeedback.textContent = '';
            usernameFeedback.classList.remove('d-block');
            usernameInput.classList.remove('is-invalid');
            usernameInput.classList.remove('is-valid');
        }
    });

    // Add an event listener to the email input field to handle real-time validation
    emailInput.addEventListener('input', function () {
        const email = emailInput.value;

        // Check if the email field is not empty
        if (email) {
            // Make an AJAX request to check if the email is already taken
            fetch(`/accounts/ajax/check_email/?email=${email}`)
                .then(response => response.json())
                .then(data => {
                    // If the email is taken, show an error message and apply invalid styles
                    if (data.is_taken) {
                        emailFeedback.textContent = 'This email address is already in use.';
                        emailFeedback.classList.add('d-block');
                        emailInput.classList.add('is-invalid');
                    } else {
                        // If the email is available, show a success message and apply valid styles
                        emailFeedback.textContent = 'Email is available.';
                        emailFeedback.classList.add('d-block');
                        emailFeedback.classList.remove('invalid-feedback');
                        emailFeedback.classList.add('valid-feedback');
                        emailInput.classList.remove('is-invalid');
                        emailInput.classList.add('is-valid');
                    }
                });
        } else {
            // Clear the feedback and remove validation styles if the input is empty
            emailFeedback.textContent = '';
            emailFeedback.classList.remove('d-block');
            emailInput.classList.remove('is-invalid');
            emailInput.classList.remove('is-valid');
        }
    });
});
