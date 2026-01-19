document.addEventListener('click', function(e){
    
    if (e.target.classList.contains('anadirFecha')){
        clonarElemento('.fechas', '.contenedor-fechas', e);
    }
    if (e.target.classList.contains('anadirPaquete')){
        clonarElemento('.paquetes', '.contenedor-paquetes', e);
    }
    if (e.target.classList.contains('anadirCategoria')){
        clonarElemento('.categorias', '.contenedor-categorias', e);
    }
    if (e.target.classList.contains('anadirPrecio')){
        clonarElemento('.precios', '.contenedor-precios', e);
    }

    if (e.target.classList.contains('quitarFecha')){
        eliminarElemento('.fechas', '.contenedor-fechas', e);
    }
    if (e.target.classList.contains('quitarPaquete')){
        eliminarElemento('.paquetes', '.contenedor-paquetes', e);
    }
    if (e.target.classList.contains('quitarCategoria')){
        eliminarElemento('.categorias', '.contenedor-categorias', e);
    }
    if (e.target.classList.contains('quitarPrecio')){
        eliminarElemento('.precios', '.contenedor-precios', e);
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