/*jslint browser:true */
/*global $, jQuery*/


// This function sets the duty cycle of the fan and sends it to the server
function setDutyCycle(dutyCycle) {
    // Make sure the duty cycle is within the valid range of 0-100
    "use strict";
    if (dutyCycle > 100) {
        dutyCycle = 100;
    }
    if (dutyCycle < 0) {
        dutyCycle = 0;
    }

    // Update the duty cycle value on the front-end
    var dutyCycleElement = document.getElementById("duty_cycle");
    dutyCycleElement.innerHTML = dutyCycle;
    var dutyCycleInputElement = document.getElementById("duty_input");
    document.getElementById("duty_slider").value = dutyCycle;
    dutyCycleInputElement.value = "";

    // Send the duty cycle to the server using a POST request
    var data = { "duty_cycle": dutyCycle };
    fetch(url + "duty_cycle", {
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

// This function gets the duty cycle input value from the front-end and sets the duty cycle
function getInputValue() {
    var inputVal = document.getElementById("duty_input").value;
    if(inputVal == ""){
        return;
    }

    setDutyCycle(inputVal);
}

// This function updates the RPM value of the fan from the server and displays it on the front-end
function updateRPM() {
    // Get the RPM value from the server using a GET request
    let rpmJSON = httpGet(url+"RPM");
    rpm = JSON.parse(rpmJSON).RPM;

    // Update the RPM value on the front-end
    var rpmElement = document.getElementById("fan_rpm");
    rpmElement.innerHTML = rpm;
}

// This function sends a synchronous GET request to the server and returns the response text
function httpGet(theUrl) {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET", theUrl, false);
    xmlHttp.send(null);
    return xmlHttp.responseText;
}

// This function is a global key listener that listens for ArrowRight, ArrowLeft, +, -, and Enter keys
// ArrowRight and + increase the duty cycle by 1, ArrowLeft and - decrease it by 1, and Enter gets the input value and sets the duty cycle
function globalKeyListener(e) {
    let dutyCycle = document.getElementById("duty_slider").value;
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

// The URL for the server
const url = "http://localhost:5000/";

// Set up a timer to update the RPM every 500ms
setInterval(updateRPM, 500);

// Add a global key listener to the window
window.addEventListener('keydown', globalKeyListener);
