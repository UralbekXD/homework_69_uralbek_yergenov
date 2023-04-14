const xhr = new XMLHttpRequest()
const buttons = document.querySelectorAll(".button")

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


xhr.onreadystatechange = function () {
    if (this.readyState === 4 && this.status === 200) {
        let parsedResponse = JSON.parse(this.response)
        let result = document.querySelector(".result")

        if (parsedResponse.hasOwnProperty("answer")) {
            result.textContent = parsedResponse['answer']
        } else {
            result.textContent = parsedResponse['error']
        }

    }
}

const handleCalcOperation = (event) => {
    let a = Number(document.querySelector("#a").value)
    let b = Number(document.querySelector("#b").value)
    let operation = event.target.dataset.operation
    xhr.open("POST", `http://localhost:8000/api/${operation}/`)
    xhr.setRequestHeader("Content-Type", "application/json")
    xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"))
    xhr.send(
        JSON.stringify(
            {
                "A": a,
                "B": b
            }
        )
    )
}

for (let button of buttons) {
    button.addEventListener("click", handleCalcOperation)
}