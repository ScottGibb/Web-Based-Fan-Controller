

// The URL for the server
const url = 'http://localhost:5000/';


/**
 * Sets the duty cycle of the fan through the back-end
 * @date 31/03/2023 - 12:55:15
 *
 * @param {*} dutyCycle
 */
function setDutyCycle(dutyCycle) {
    // Make sure the duty cycle is within the valid range of 0-100
    'use strict';
    if (dutyCycle > 100) {
        dutyCycle = 100;
    }
    if (dutyCycle < 0) {
        dutyCycle = 0;
    }

    // Update the duty cycle value on the front-end

    // Update the duty cycle value on the front-end
    var dutyCycleElement = document.getElementById("dutyCycle");
    dutyCycleElement.innerHTML = dutyCycle;
    var dutyCycleInputElement = document.getElementById("dutyInput");
    document.getElementById("dutySlider").value = dutyCycle;
    dutyCycleInputElement.value = "";

    // Send the duty cycle to the server using a POST request
    const data = { "DutyCycle": dutyCycle };
    fetch(url + "DutyCycle", {
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


/**
 *  Gets the input from the duty cycle input box and sets the duty cycle
 * @date 31/03/2023 - 12:58:01
 */
function getInputValue() {
    const inputVal = document.getElementById('duty_input').value;
    if (inputVal == '') {
        return;
    }

    setDutyCycle(inputVal);
}

/**
 * Updates the RPM value on the front-end
 * @date 31/03/2023 - 12:58:25
 */
function updateRPM() {
    // Get the RPM value from the server using a GET request
    const rpmJSON = httpGet(url + 'RPM');
    rpm = JSON.parse(rpmJSON).RPM;

    // Update the RPM value on the front-end
    const rpmElement = document.getElementById('fan_rpm');
    rpmElement.innerHTML = rpm;
}


/**
 * Performs a GET request to the specified URL
 * @date 31/03/2023 - 12:58:45
 *
 * @param {*} theUrl
 * @return {*}
 */
function httpGet(theUrl) {
    const xmlHttp = new XMLHttpRequest();
    xmlHttp.open('GET', theUrl, false);
    xmlHttp.send(null);
    return xmlHttp.responseText;
}


/**
 * Key Listener for the Webpage
 * @date 31/03/2023 - 12:59:00
 *
 * @param {*} e
 */
function globalKeyListener(e) {
    let dutyCycle = document.getElementById('duty_slider').value;
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


// Set up a timer to update the RPM every 500ms
setInterval(updateRPM, 500);
// Add a global key listener to the window
window.addEventListener('keydown', globalKeyListener);
