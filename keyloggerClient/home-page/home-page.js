
document.addEventListener('DOMContentLoaded', () => {
    loadComputers();
});


async function loadComputers() {

    const token = sessionStorage.getItem("token");
    console.log("token",token)
    try {
        const url = "http://localhost:5000/getComputers/";
        const response = await fetch(url, { method: 'GET',
            headers: { Authorization: token } });
        

        if (!response.ok) {
            throw new Error('Failed to fetch computers');
        }
        const data = await response.json();
        console.log(data);
        const dropdown = document.getElementById("computerDropdown");

        dropdown.innerHTML = "";

        const defaultOption = document.createElement("option");
        defaultOption.text = "Select a computer";
        defaultOption.value = "";
        dropdown.appendChild(defaultOption);

        data.computers.forEach(computer => {
            const option = document.createElement("option");
            option.value = computer;
            option.text = computer;
            dropdown.appendChild(option);
        });

    } catch (error) {
        console.error(error);
        alert("Failed to load computers, try again later.");
    }
}

async function selectedComputer(event) {
    const token = sessionStorage.getItem("token");
    const computer = event.target.value
    window.selectedComputerName = event.target.value;
    console.log(computer)
    try {
        const url = `http://localhost:5000/getDataByComputer/${computer}`;
        console.log(url)
        const response = await fetch(url, { method: 'GET',
            headers: { Authorization: token } });
        console.log(response)
        if (!response) {
            throw new Error('failed to display data')
        }
        const data = await response.json();
        console.log("Received Data:", data)
        console.log(data)
        
        const table = document.getElementById("table-body");


        
        table.innerHTML = "";

        Object.entries(data).forEach(([date, computerDataArray]) => {
            computerDataArray.forEach(([platform, input]) => { 
                const row = `<tr>
                    <td>${date}</td>
                    <td>${platform}</td>
                    <td>${input}</td>
                </tr>`;
                table.innerHTML += row;
            });
        });


        
        document.querySelector(".button").style.display = "block";

        document.querySelector(".table-data").style.display = "block";


    } catch (error) {
        console.error(error);
        alert("Failed to get data.");

    }


}

window.onload = loadComputers;

