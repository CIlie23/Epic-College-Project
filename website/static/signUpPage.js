/*function showForm(formId, clickedTab) {
    document.getElementById('login-form').style.display = 'none';
    document.getElementById('register-form').style.display = 'none';
    document.getElementById(formId).style.display = 'block';

    // Remove 'active' class from all tabs
    var tabs = document.querySelectorAll('.tab');
    tabs.forEach(function(tab) {
        tab.classList.remove('active');
    });

    // Add 'active' class to the clicked tab
    clickedTab.classList.add('active');
}*/

function validateFormLogin() {
    // Obținem valorile introduse în câmpuri
    /*const username = document.getElementById('username').value;*/
    const email = document.getElementById('loginEmail').value;
    const password = document.getElementById('loginPassword').value;

    // Resetăm mesajele de eroare
    resetErrorMessages();

    // Validăm e-mailul
    if (!isValidEmail(email)) {
        displayErrorMessage('emailError', 'E-mailul introdus nu este valid.');
        return;
    }

    // Validăm parola
    if (!isValidPassword(password)) {
        displayErrorMessage('passwordError', 'Parola gresita!');
        return;
    }

    // Dacă toate validările trec, puteți continua cu trimiterea formularului
    console.log('Autentificare:', email, password);
    alert('Formularul este valid! Puteți trimite înregistrarea.');
}

function validateFormRegister() {
    // Obținem valorile introduse în câmpuri
    const email = document.getElementById('registerEmail').value;
    const password = document.getElementById('registerPassword').value;
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
    console.log('Inregistrare:', username, email, password, confirmPassword);
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
