BASE_BACKEND_URL = 'http://localhost:8000/urlshortner/'

function timepass() {
    btn = document.querySelector("#submit-btn")

    console.log("hiii")
    console.log(btn)
    btn.addEventListener('click',modifyText)
}
setTimeout(timepass,1000)

console.log("hello")



async function modifyText() {
    try {
        console.log("in url ");
        input_url = document.querySelector("#url-input").value
        payload = {
            "long_url":input_url
        }
        headers = {
            'Content-Type': 'application/json',
        }
      const response = await axios.post(BASE_BACKEND_URL,payload);
      console.log(response);
    } catch (error) {
      console.error(error);
    }
  }

// btn.addEventListener('click',modifyText)