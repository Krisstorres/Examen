<section class="container fst-italic fw-bold pt-3 border border-5 rounded  w-1  bg-warning ;">
    <div class="col-12 col-lg-12  ">
    <h3 class="fst-italic fw-bold  lead text-center"> Formulario de contacto</h3>
    <h3 class="fst-italic fw-bold lead text-center"> </h3>

    <p class="lead  p-10  fst-italic text-center container">Lorem ipsum dolor sit, amet consectetur adipisicing elit. Placeat, veritatis? Labore repudiandae doloremque </p>
       
      
 

    <form id="validar" class="needs-validation" action="Contacto.php" novalidate>
      
        <div class="row   ">
    <div class="col-12 col-lg-4 mb-3 text-center container">
      <label for="vvalidationDefault01" class="form-label fst-italic fw-bold">Nombres:</label>
      <input type="text" class="form-control" id="nombre" value="" placeholder="ingrese sus nombres" required>
<div class="valid-feedback"> Correcto</div>
<div class="invalid-feedback"> Ingrese Un Nombre ejemplo:(Juan jose)</div>

    </div>
</div>
   
<div class="row">
    <div class="col-12 col-lg-4 mb-3 text-center container">
        <label for="validationDefault02" class="form-label fst-italic fw-bold">Apellidos</label>
        <input type="text" class="form-control" id="apellido" value="" placeholder="ingrese sus apellidos" required>
        <div class="valid-feedback"> Correcto</div>
        <div class="invalid-feedback"> Ingrese Un Apellido ejemplo:(Soto Riveras)</div>
      </div>
</div>  

<div class="row">
        <div class="col-12 col-lg-4 mb-3 text-center container">
            <label for="validationDefault04" class="form-label fst-italic fw-bold" id="region">Region</label>
            <select class="form-select" id="validationDefault04" name="provincia" onchange="changeFunc(value);" required>
              <option>Seleccione una Region</option>
        
            </select>
          </div>
        </div>


        <div class="row">
          <div class="col-12 col-lg-4 mb-3 text-center container">
              <label for="validationDefault04" class="form-label fst-italic fw-bold" id="comuna">Comuna</label>
              <select class="form-select" id="validationDefault04" name="comunaa" required>
                <option>Seleccione una comuna</option>
          
              </select>
            </div>
          </div>

<div class="row">
<div class="col-12 col-lg-4 mb-3 text-center container">
    <label for="validationDefault05" class="form-label fst-italic fw-bold">Direccion</label  >
    <input type="text" class="form-control" id="Direccion" placeholder="ingrese su direccion" required>
    <div class="valid-feedback"> Correcto</div>
    <div class="invalid-feedback"> Ingrese Una Direccion ejemplo:(Heroes titan 432)</div>
  </div>
</div>

<div class="row">
<div class="col-12 col-lg-4 mb-3 text-center container">
    <label for="validationDefaultUsername" class="form-label fst-italic fw-bold">Email</label>
    <div class="input-group">

      <input type="text" class="form-control" id="validationDefaultUsername"  aria-describedby="inputGroupPrepend2" required>
      <div class="valid-feedback"> Correcto</div>
    <div class="invalid-feedback"> Ingrese Una Direccion ejemplo:(example@email.com)</div>
    </div>
  </div>
</div>

<div class="col-12 col-lg-4 mb-3  container">
    <div class="form-check">
      <input class="form-check-input" type="checkbox" value="" id="invalidCheck2" required>
      <label class="form-check-label fst-italic fw-bold" for="invalidCheck2" >Agree to terms and conditions
      </label>
    </div>
  </div>

<div class="col-12 text-center container">
    <button class="btn btn-warning mb-5  fw-bold text-black widi" type="submit">  Enviar <img  class="w-25" src="img/paw3.png"></button>
  </div>
  <section class="container">
    <div class="row">
      <div class="col-12 col-lg-12 text-center container">
        <h3 class="fst-italic fw-bold lead text-center">Terminos y condiciones </h3>
        <p class="fst-italic fw-bold  text-center lh-base p-4">
       Lorem, ipsum dolor sit amet consectetur adipisicing elit. Earum fuga eius quasi. Sint sunt rem molestias tempore non ab voluptates ipsum. Id sapiente consequatur ex voluptatibus, necessitatibus quasi mollitia voluptatum!
       Cumque voluptatum voluptatem, vitae ducimus accusantium debitis dolore vel recusandae omnis? Amet ex, cum quaerat vitae id culpa facere mollitia nam officia quod expedita commodi iste harum esse consectetur ipsum!
     </p>
      </div>
    </div>
  </section>
</form>
</section>
</div>


<script>
    (function () {
       'use strict'
       var forms = document.querySelectorAll('.needs-validation')

       Array.prototype.slice.call(forms)
        .forEach(function(form){
            form.addEventListener('submit', function (event){
            if(!form.checkValidity()){
                event.preventDefault()
                event.stopPropagation()
            }
            form.classList.add('was-validated')
            },false)
        })
    })()

    const promises = [];
for (let i = 0 ; i <= 16; i++) {
    if (i <= 9) {
          const url = `https://apis.digital.gob.cl/dpa/regiones/0${i}`;
          promises.push(fetch(url).then(res => res.json()));
    }if (i > 9) {
        const url = `https://apis.digital.gob.cl/dpa/regiones/${i}`;
        promises.push(fetch(url).then(res => res.json()));
    }

  console.log(promises[i])
}

Promise.all(promises).then(results => {
    //MODIFICAMOS LA LISTA CON MAP AÑADEMOS FORMATO
    const regionees = results.map(data => ({
      codigo: data.codigo,
      nombre: data.nombre,
    }));
    console.log(regionees);
    sendData(regionees);
  });



  function sendData(jsonData) {
    //RECORREMOS Y AÑADEMOS A LA TABLA HTML
  for (let i = 1; i < jsonData.length; i++) {
      const regiones = [];
      const nmbre = []
      regiones.push(jsonData[i].nombre)
      nmbre.push(jsonData[i].codigo)
      regiones.sort();
      addOptions("provincia", regiones, nmbre)
  }
}



// Rutina para agregar opciones a un <select>
function addOptions(domElement, array, codigoo) {
    var select = document.getElementsByName(domElement)[0];

    for (value in array) {
    for (val in codigoo) {
     var option = document.createElement("option");
     option.text = array[value];
     option.id = codigoo[val];
     option.value = codigoo[val];
     select.add(option);
    
    }} 

 console.log(document.getElementById("15"))
   }




function changeFunc(el) {


    let cod = el
    const api = `https://apis.digital.gob.cl/dpa/regiones/${el}/comunas`;
   
    var list = document.getElementsByClassName("deletea");
    for(var i = list.length - 1; 0 <= i; i--)
    if(list[i] && list[i].parentElement)
    list[i].parentElement.removeChild(list[i]);

   (async function(){
    const res = await fetch(api).then(res => res.json());




Promise.all(res).then(results => {
    //MODIFICAMOS LA LISTA CON MAP AÑADEMOS FORMATO
    const comunass = results.map(data => ({
      nombre: data.nombre,
    }));
console.log(comunass)   
//addOptionsC("comunaa", comunass) 
 sendComuna(comunass)
  });
  })();
    }

 
    


function sendComuna(datos){

    for (let i = 0; i < datos.length; i++) {
        const comuna = [];
        comuna.push(datos[i].nombre)
        comuna.sort();
        addOptionsC("comunaa", comuna)
    }
        
}


// Rutina para agregar opciones a un <select>
function addOptionsC(domElement, array) {
  
  var select = document.getElementsByName(domElement)[0];
  console.log(array)
  for (value in array) {
    let comun = array[value]
   var option = document.createElement("option");
   option.text = comun;
   option.className = "deletea";
   select.add(option);
  } 
 }






























</script>