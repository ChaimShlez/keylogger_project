

async function displayProfile() {
    const token = sessionStorage.getItem("token");
    const computerName = window.selectedComputerName;
    console.log(computerName);

    try {
        const url = `http://localhost:5000/getProfileByComputer/${computerName}`;
        console.log(url);

        const response = await fetch(url, { method: 'GET',
            headers: { Authorization: token } });
        console.log(response);

        if (!response.ok) {
            throw new Error('Failed to display data');
        }

        const data = await response.json();
        console.log("Received Data:", data);


        sessionStorage.setItem("profileData", JSON.stringify(data));



        // window.location.href = "profile.html";
        window.location.href = "../profile/profile.html";

    } catch (error) {
        console.error(error);
        alert("Failed to get data.");
    }
}
