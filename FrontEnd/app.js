
function setDutyCycle(dutyCycle) {
    if (dutyCycle > 100) {
        dutyCycle = 100;
    }
    if (dutyCycle < 0) {
        dutyCycle = 0;
    }

    console.log("Duty Cycle Now: " + dutyCycle);

    var dutyCycleElement = document.getElementById("dutyCycle");
    dutyCycleElement.innerHTML = dutyCycle;
    var dutyCycleInputElement = document.getElementById("dutyInput");
    document.getElementById("dutySlider").value = dutyCycle;
    dutyCycleInputElement.value = "";

    //Send Duty Cycle to Server
    const data = { "DutyCycle": dutyCycle };
fetch(url+"DutyCycle", {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify(data),
})
.then(response => response.json())
.then(data => console.log(data))
.catch(error => console.error(error));
    
    
}

function getInputValue() {
    var inputVal = document.getElementById("dutyInput").value;
    if(inputVal == ""){
        return;
    }

    setDutyCycle(inputVal);
}


function updateRPM() {
   
    //Get RPM From Server

    let rpmJSON = httpGet(url+"RPM");
    // console.log(rpmJSON);
    rpm = JSON.parse(rpmJSON).RPM;
    // let rpm = Math.floor(Math.random() * 1000)
    // Update RPM on FrontEnd
    var rpmElement = document.getElementById("fanRPM");
    rpmElement.innerHTML = rpm;
}

function httpGet(theUrl) {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET", theUrl, false); // false for synchronous request
    xmlHttp.send(null);
    return xmlHttp.responseText;
}

function globalKeyListener(e) {
    let dutyCycle = document.getElementById("dutySlider").value;
    console.log(e.key);
    switch (e.key) {
        case 'ArrowRight':
        case '+':
            dutyCycle++;
            setDutyCycle(dutyCycle);
            break;
        case 'ArrowLeft':
        case '-':
            dutyCycle--;
            setDutyCycle(dutyCycle);
            break;
        case 'Enter':
            getInputValue();
            break;
        default:
        // console.log("Other Key");
    }
}

const url = "http://localhost:5000/";
setInterval(updateRPM, 500);
window.addEventListener('keydown', globalKeyListener);

    