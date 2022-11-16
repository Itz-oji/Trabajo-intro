const username = document.getElementById('username')
const password = document.getElementById('password')
const mail= document.getElementById('mail')
const button = document.getElementById('button')

button.addEventListener ('click', (e) => {
    e.preventDefault ()
    const data = {
        mail: mail.value,
        username: username.value,
        password: password.value,
    }

    console.log(data)
})
const API_URL= 'http://localhost:8000/login';
const getUser = () => {
    fetch(API_URL)
    .then(response => response.json() )
    .then(data => {
    console.log(data)
    })
    .catch(err=> console.log(err))
}