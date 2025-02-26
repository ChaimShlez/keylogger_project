


async function login(event) {
    event.preventDefault();
    

    let email = document.getElementById("email").value;
    let password = document.getElementById("password").value;

    // if (!email || !password) {
    //     alert("Both email and password are required.");
    //     return;
    // }

    try {
        const url = "http://localhost:5000/login/";
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ username: email, password: password })
        });
        if (!response.ok) {
            throw new Error("Login failed, check credentials.");
        }

        const data = await response.json();


        sessionStorage.setItem("token", "Bearer " + data.token);
        console.log("Token saved:", sessionStorage.getItem("token"));
        window.location.href = "../home-page/home-page.html";


    } catch (error) {
        console.error(error);
        alert("Login failed, try again later.");
    }
}
