function login(){

    console.log('google from login')

    var password = document.getElementById("password").value
    var username = document.getElementById("username").value

    if(username == "" || password == "" || username == null || password == null){
        alert("Enter valid username and passeword")
    }
    else{
        const data = {
            username: username,
            password : password
        }

        const header = {
                    "content-type" : "application/json; charset=UTF-8",
                    'Access-Control-Allow-Origin': 'no-cors',
                    'Accept' : '*/*'
                }

         const params = {
            headers: header,
            body : JSON.stringify(data),
            method: 'POST'
        }

        const url = "http://localhost:5000/login/user"

        fetch(url , params)
            .then(response => response.json())
            .then( response => {
                console.log(response)
            })     
            .catch(error=>console.log(error))
    }
}