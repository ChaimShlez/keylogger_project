
async function getData() {
    try {
        const url = "http://localhost:5000/";  
        const response = await fetch(url);   
        const data = await response.json();  
        console.log(data);                   
    } catch (error) {
        console.error("Failed to get data", error);
    }
}

async function login(event){
    event.preventDefault();
    console.log("Login function triggered");

    let email = document.getElementById("email").value;
    let password = document.getElementById("password").value;

    if (!email || !password) {
        alert("Both email and password are required.");
        return;
    }

    try {
        const url = "http://localhost:5000/login/";
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({username: email, password: password})
        });

        if (!response.ok) {
            throw new Error('Login failed');
        }

        const data = await response.json();  
        console.log(data);
        
        if (data.status === "success") {
            console.log("Login successful");
            window.location.href = "../home-page/home-page.html";
        } else {
            alert("Invalid credentials");
        }

    } catch (error) {
        console.error(error);
        alert("Login failed, try again later.");
    }
}
