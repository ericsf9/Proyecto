from uvengine import UVEngine

def main():
    
    plantillas_data = [
    'plantilla/_data/navigation.yml'
    ]
    
    plantillas_pages = [
    'plantilla/_pages/about.md',
    'plantilla/_pages/call-for-papers.md',
    'plantilla/_pages/program.md',
    'plantilla/_pages/registration.md',
    'plantilla/_pages/awards.md',
    'plantilla/_pages/venue.md',
    'plantilla/_pages/committees.md',
    'plantilla/_pages/history.md',
    'plantilla/_pages/dates.md',
    'plantilla/_pages/proceedings.md',
    'plantilla/_pages/keynotes.md',
    ]
    
    plantillas_includes = [
    'plantilla/_includes/vsponsors.html'
    ]
    
    uvengine = UVEngine('web_fm.uvl', ['user-configuration.json'], plantillas_data)
    producto = uvengine.resolve_variability()
    for plantilla in plantillas_data:
        salida = plantilla.replace('plantilla/','producto/')
        with open(salida, 'w', encoding='utf-8') as fichero:
            fichero.write(producto.get(plantilla))
            
    uvengine = UVEngine('web_fm.uvl', ['user-configuration.json'], plantillas_pages)
    producto = uvengine.resolve_variability()
    for plantilla in plantillas_pages:
        salida = plantilla.replace('plantilla/','producto/')
        with open(salida, 'w', encoding='utf-8') as fichero:
            fichero.write(producto.get(plantilla))
            
    uvengine = UVEngine('web_fm.uvl', ['user-configuration.json'], plantillas_includes)
    producto = uvengine.resolve_variability()
    for plantilla in plantillas_includes:
        salida = plantilla.replace('plantilla/','producto/')
        with open(salida, 'w', encoding='utf-8') as fichero:
            fichero.write(producto.get(plantilla))
            
    print("WEB GENERADA CORRECTAMENTE")
    

if __name__ == '__main__':
    main()