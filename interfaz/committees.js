document.addEventListener('click', function(e){
    
    if (e.target.classList.contains('anadirWchair')){
        clonarElemento('.wchairs', '.contenedor-wchairs', e);
    }
    if (e.target.classList.contains('anadirPchair')){
        clonarElemento('.pchairs', '.contenedor-pchairs', e);
    }
    if (e.target.classList.contains('anadirChair')){
        clonarElemento('.cchairs', '.contenedor-cchairs', e);
    }
    if (e.target.classList.contains('anadirComite')){
        clonarElemento('.comites', '.contenedor-comites', e);
    }

    if (e.target.classList.contains('quitarWchair')){
        eliminarElemento('.wchairs', '.contenedor-wchairs', e);
    }
    if (e.target.classList.contains('quitarPchair')){
        eliminarElemento('.pchairs', '.contenedor-pchairs', e);
    }
    if (e.target.classList.contains('quitarChair')){
        eliminarElemento('.cchairs', '.contenedor-cchairs', e);
    }
    if (e.target.classList.contains('quitarComite')){
        eliminarElemento('.comites', '.contenedor-comites', e);
    }

});

function clonarElemento(claseOriginal, claseContenedor, e){
    const padre = e.target.closest(claseContenedor);
    const original = padre.querySelector(claseOriginal);

    if(original){
        const copia = original.cloneNode(true);

        copia.querySelectorAll('input, select, textarea').forEach(n => n.value = '');

        e.target.before(copia)

        if (claseOriginal == '.comites'){
            renombrar(padre, claseOriginal)
        }
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

function renombrar(contenedor, elementoC){
    const elementos = contenedor.querySelectorAll(':scope > ' + elementoC)

    elementos.forEach((elemento, indice) => {
        
        elemento.querySelectorAll('input, select, textarea').forEach(input => {
            const nombreBase = input.name.split('[')[0];

            if (indice == 0){
                input.name = nombreBase
            }else{
                input.name = `${nombreBase}${indice + 1}`
            }
            
        })

    })
}