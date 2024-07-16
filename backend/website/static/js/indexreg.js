// Función para hacer scroll hacia arriba
function scrollToTop() {
    window.scrollTo({top: 0, behavior: 'smooth'});
}

// Función para mostrar u ocultar el botón
function toggleButtonVisibility() {
    const button = document.getElementById('volver-arriba');
    const footer = document.querySelector('footer');
    const footerRect = footer.getBoundingClientRect();
    const footerVisible = footerRect.top <= window.innerHeight;

    if (footerVisible) {
        button.classList.add('visible');
    } else {
        button.classList.remove('visible');
    }
}

// Añadir el evento scroll para verificar la visibilidad del botón
window.addEventListener('scroll', toggleButtonVisibility);

/* validaciones*/
const nombre = document.getElementById("name")
const email = document.getElementById("email")
const pass = document.getElementById("password")
const form = document.getElementById("form")
const parrafo = document.getElementById("warnings")
const rut = document.getElementById("rut")

form.addEventListener("submit", e=>{
    e.preventDefault()
    let warnings = ""
    let entrar = false
    let regexRut = /^[0-9]+[-|‐]{1}[0-9kK]{1}$/
    let regexEmail = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/
    parrafo.innerHTML = ""

    if(nombre.value.length <4){
        warnings += `El nombre es muy corto <br>`
        entrar = true
    }
    if(!regexEmail.test(email.value)){
        warnings += `El email no es valido <br>`
        entrar = true
    }
    if(pass.value.length < 8){
        warnings += `La contraseña es muy corta <br>`
        entrar = true
    }
    if(!regexRut.test(rut.value)){
        warnings += `El rut no es valido <br>`
        entrar = true
    }

    if(entrar){
        parrafo.innerHTML = warnings
    }else{
        parrafo.innerHTML = "Enviado"
    }
})