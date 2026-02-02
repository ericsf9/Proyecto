document.addEventListener('click', function(e){
    
    if (e.target.classList.contains('anadirDia')){
        clonarElemento('.dias', '.contenedor-dias', e);
    }
    if (e.target.classList.contains('anadirEvento')){
        clonarElemento('.eventos', '.contenedor-eventos', e);
    }
    

    if (e.target.classList.contains('quitarDia')){
        eliminarElemento('.dias', '.contenedor-dias', e);
    }
    if (e.target.classList.contains('quitarEvento')){
        eliminarElemento('.eventos', '.contenedor-eventos', e);
    }

});

function clonarElemento(claseOriginal, claseContenedor, e){
    const padre = e.target.closest(claseContenedor);
    const original = padre.querySelector(claseOriginal);

    if(original){
        const copia = original.cloneNode(true);

        copia.querySelectorAll('input, select, textarea').forEach(n => n.value = '');

        e.target.before(copia)
        
        if (claseOriginal == '.dias'){
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