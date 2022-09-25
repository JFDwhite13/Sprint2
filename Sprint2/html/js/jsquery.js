const getPatients= 'https://db-hospital-c3g53.herokuapp.com/viewpatients'

var contenido = document.querySelector('#contenido')

function asas(){
  fetch(getPatients)
    .then(res => res.json())
    .then(datos =>{
      //console.log(datos)
      handleCustomers(datos)
      

    })
}

function handleCustomers(datos) {
  contenido.innerHTML=''
  for (let valor of datos){
    contenido.innerHTML +=`
    <tr id=ntdta>
      <td>${valor.patientid}</td>
      <td>${valor.patientfirstname}</td>
      <td>${valor.patientlastname}</td>
      <td>${valor.patientphonenumber}</td>
      <td>${valor.patientgender}</td>
      <td>${valor.patientaddress}</td>
      <td>${valor.patientcity}</td>
      <td>${valor.patientBirthday}</td>
      <td>${valor.patientLatitude}</td>
      <td>${valor.patientLongitude}</td>
    </tr>
    `   
  }
  
}

function handleCustomer(datos) {
  contenido.innerHTML=''
  for (let valor of datos){
    contenido.innerHTML =`
    <tr id=ntdta>
      <td>${valor.patientid}</td>
      <td>${valor.patientfirstname}</td>
      <td>${valor.patientlastname}</td>
      <td>${valor.patientphonenumber}</td>
      <td>${valor.patientgender}</td>
      <td>${valor.patientaddress}</td>
      <td>${valor.patientcity}</td>
      <td>${valor.patientBirthday}</td>
      <td>${valor.patientLatitude}</td>
      <td>${valor.patientLongitude}</td>
    </tr>
    `   
  }
}

function sdata(evt){
  evt.preventDefault();
  const idsearch = document.searchbar.search.value;
  search(idsearch)
}

function search(idsearch){
  fetch(getPatients)
  .then(res => res.json())
  .then(datos =>{
    handleCustomer(datos)
    

  })
}
document.addEventListener("DOMContentLoaded", asas);
document.addEventListener('submit', sdata);