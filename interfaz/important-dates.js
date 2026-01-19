document.addEventListener('click', function(e){
    
    if (e.target.classList.contains('anadirIdate')){
        clonarElemento('.idates', '.contenedor-idates', e);
    }

    if (e.target.classList.contains('quitarIdate')){
        eliminarElemento('.idates', '.contenedor-idates', e);
    }

});

function clonarElemento(claseOriginal, claseContenedor, e){
    const padre = e.target.closest(claseContenedor);
    const original = padre.querySelector(claseOriginal);

    if(original){
        const copia = original.cloneNode(true);

        copia.querySelectorAll('input, select, textarea').forEach(n => n.value = '');

        e.target.before(copia)
    }
}

function eliminarElemento(claseOriginal, claseContenedor, e){
    const padre = e.target.closest(claseContenedor);

    if(!padre) return;

    const elementos = padre.querySelectorAll(':scope > ' + claseOriginal);

    if(elementos.length > 1){
        elementos[elementos.length - 1].remove();
    }
}