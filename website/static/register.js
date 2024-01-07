function validateFormRegister() {
    // Obținem valorile introduse în câmpuri
    /*const username = document.getElementById('username').value;*/
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirmPassword').value;

    // Resetăm mesajele de eroare
    resetErrorMessages();

    // Validăm e-mailul
    if (!isValidEmail(email)) {
        displayErrorMessage('emailError', 'E-mailul introdus nu este valid.');
        return;
    }

    // Validăm parola
    if (!isValidPassword(password)) {
        displayErrorMessage('passwordError', 'Parola trebuie să conțină cel puțin 8 caractere și să includă cel puțin o literă și o cifră.');
        return;
    }

    // Validăm confirmarea parolei
    if (password !== confirmPassword) {
        displayErrorMessage('confirmPasswordError', 'Parola introdusă nu se potrivește.');
        return;
    }

    // Dacă toate validările trec, puteți continua cu trimiterea formularului
    alert('Formularul este valid! Puteți trimite înregistrarea.');
}

function isValidEmail(email) {
    // Simplu - verificăm dacă este o adresă de e-mail validă
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

function isValidPassword(password) {
    // Complexitate minimă a parolei: cel puțin 8 caractere, cel puțin o literă și o cifră
    const passwordRegex = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/;
    return passwordRegex.test(password);
}

function resetErrorMessages() {
    // Resetăm mesajele de eroare
    document.getElementById('emailError').innerText = '';
    document.getElementById('passwordError').innerText = '';
    document.getElementById('confirmPasswordError').innerText = '';
}

function displayErrorMessage(elementId, message) {
    // Afișăm mesajul de eroare în elementul specificat
    document.getElementById(elementId).innerText = message;
}