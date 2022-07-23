let usernameInput = document.getElementById('username-input');
let passwordInput = document.getElementById('password-input');
let loginButton = document.getElementById('login-btn');

console.log('test1');

loginButton.addEventListener('click', async (e) => {
    e.preventDefault()
    console.log(usernameInput.value, passwordInput.value)

    let res = await fetch(`http://127.0.0.1:8082/login`, {
        'credentials': 'include',
        'method': 'POST',
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': JSON.stringify({
            "username": usernameInput.value,
            "password": passwordInput.value
        })
    })
    let data = await res.json()

    if (res.status == 200) {
        console.log(data)
        window.location.href = '/employee.html'

    }
    
    
});