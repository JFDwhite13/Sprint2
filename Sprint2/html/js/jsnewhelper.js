const newHelperurl = 'https://db-hospital-c3g53.herokuapp.com/newhelper';

function validar_nombre_apellido(val) {
    const letters = /^[A-Z a-zÁÉÍÓÚáéíóúñ]+$/;
    if (val.match(letters)){
        return true;
    }else{
        return false;
    }
}


function validar_contrasena(val) {
    if (val.length >= 5)
        return true;
    else
        return false;
}

function Collectdata(evt){
    evt.preventDefault();

    const hid = document.registro.id.value;
    const hfirstname = document.registro.firstname.value;
    const hlastname  = document.registro.lastname.value;
    const hphoneNumber = document.registro.phonenumber.value;
    const hgender = document.registro.gender.value;
    const hidpatient = document.registro.patientid.value;
    const hkinship = document.registro.parents.value;
    const hemail = document.registro.email.value;


    let result = validar_nombre_apellido(hfirstname);
    if (!result) {
        alert('Nombre no válido');
        return;
    }
    result = validar_nombre_apellido(hlastname);
    if (!result) {
        alert('Apellido no válido');
        return;
    }
 
    
    const customer ={
        hid : hid,
        hfirstname : hfirstname,
        hlastname :hlastname,
        hphoneNumber : hphoneNumber,
        hgender :hgender,
        hidpatient : hidpatient,
        hkinship :hkinship,
        hemail :hemail
    
    }
    /*
    alert(`Usuario registrado con los siguientes datos:
        ${customer.patientfirstname} ${customer.patientlastname} ${customer.patientid}`);*/
    console.log(customer);
    const dataToSend = JSON.stringify(customer);
    sendData(dataToSend);
}

function sendData(data) {
    fetch(newHelperurl, {
        method: "POST",
        headers: {
            "Content-Type": "text/json"
        },
        body: data
    })
        .then(response => {
            if (response.ok) {
                return response.text()
            } else {
                throw new Error(response.status)
            }
        })
        .then(data => {
            console.log(data);
            handleSuccess();
        })
        .catch(err => {
            console.log("Error: " + err);
            handleError();
        });
}

function handleSuccess() {
    document.getElementById("formData").remove();
    const message = document.createElement("p");
    message.innerHTML = "Familiar creado exitosamente.";
    const info = document.getElementById("info");
    info.appendChild(message);
}

function handleError() {
    document.getElementById("formData").remove();
    const message = document.createElement("p");
    message.innerHTML = "No se pudo crear el familiar. Intente luego.";
    const info = document.getElementById("info");
    info.appendChild(message);
}

document.registro.addEventListener('submit', Collectdata);