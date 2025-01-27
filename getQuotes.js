async function init() {
    try {
        const response = await fetch('http://127.0.0.1:5000/getQuotes');
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        console.log(data);
        document.getElementById("quote").innerHTML = data.text + "<br>-" + data.author;
    } catch (error) {
        console.error('Error:', error);
    }
}

function updateTime() {
    let date = new Date();
    let timeNow = date.toLocaleString();
    // console.log(timeNow.substring(10));
    document.getElementById("time").innerHTML = timeNow.substring(10);
}

setInterval(updateTime, 1000);