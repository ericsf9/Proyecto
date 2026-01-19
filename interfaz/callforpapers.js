document.addEventListener('click', function(e){
    
    if (e.target.classList.contains('anadirFecha')){
        clonarElemento('.fechas', '.contenedor-fechas', e);
    }
    if (e.target.classList.contains('anadirSeccion')){
        clonarElemento('.secciones', '.contenedor-secciones', e);
    }
    if (e.target.classList.contains('anadirSubseccion')){
        clonarElemento('.subsecciones', '.contenedor-subsecciones', e);
    }

    if (e.target.classList.contains('quitarFecha')){
        eliminarElemento('.fechas', '.contenedor-fechas', e);
    }
    if (e.target.classList.contains('quitarSeccion')){
        eliminarElemento('.secciones', '.contenedor-secciones', e);
    }
    if (e.target.classList.contains('quitarSubseccion')){
        eliminarElemento('.subsecciones', '.contenedor-subsecciones', e);
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