let lista = document.getElementById('materias');
let count = true;

function show() {
  if (count) {
    lista.style.display = 'block';
    count = false;
  } else {
      lista.style.display = 'none';
      count = true;
    }
}


let phone = document.getElementById('phone');
let textoAtual = phone.textContent; // numero que vem da base de dados
let telefone;

if(true) {
  let textoAjustado = textoAtual.replace(/(\d{2})(\d{5})(\d{4})/,
                  function( regex, arg0, arg1, arg2) {
                  return '(' + arg0 + ')' + ' '  +arg1 + '-' + arg2 ;
                  });
  telefone = textoAjustado;
}

phone.innerHTML = telefone;
