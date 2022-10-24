document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("formulario").addEventListener('submit', validarFormulario); 
  });
  
  function validarFormulario(evento) {
    evento.preventDefault();
    let email = document.getElementById('email').value;
    if(usuario.length == 0) {
      alert('No has escrito nada en el email');
      return;
    }
    var contraseña = document.getElementById('contraseña').value;
    if(usuario.length == 0) {
        alert('No has escrito nada en la contraseña');
        return;
    }

    this.submit();
  }