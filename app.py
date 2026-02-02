from flask import Flask, request, render_template, session, redirect, url_for, flash, send_file
import json
import main
import subprocess
import os
from github import Github, GithubException
import shutil
import stat
from glom import glom, T
import re
import requests

app = Flask(__name__, template_folder= 'interfaz', static_folder='interfaz')
app.secret_key = 'mi_clave_segura'


@app.route('/', methods=['GET','POST'])
def inicio():
    session.clear()
    session['ultima_pestana']='registration'
    return render_template('home.html')

@app.route('/pestanas', methods=['GET'])
def pestanas():
    return render_template('caracteristicas-pestañas.html')

    
@app.route('/home',methods=['GET','POST'])
def chome():
    if request.method == 'POST':
        pestanas = request.form.getlist('pestañas')
        session['pestanas'] = pestanas
        print(pestanas)
        
        
    return render_template('caracteristicas-home.html')


@app.route('/callforpapers',methods=['GET','POST'])
def ccallforpapers():
    if request.method == 'POST':
        print("Funciona")
        
        json_esp = json.loads(json.dumps(request.form.to_dict(), indent=4))
        
        target = {
            "Conference name": "Conference name",
            "Conference date": "Conference date",
            "Conference venue": "Conference venue",
            "Conference format": "Conference format",
            "headerimage": "headerimage",
            "logoimage": "logoimage",
            "aims": {
                "aimscontent": "aimscontent"
            }
        }
        
        session['home'] = glom(json_esp, target)
        
    return render_template('caracteristicas-callforpapers.html')


@app.route('/program',methods=['GET','POST'])
def cprogram():
    if request.method == 'POST':
        print("Funciona")
        
        json_esp = json.loads(json.dumps(request.form.to_dict(flat=False), indent=4))
        
        campos = ["sectitle","seccontent","seccontentp","subsectitle","subseccontent"]
        
        target = { 
            "cimportantdates" : (
              lambda t: zip(t['description'], t['cdate']),  
                [
            {
                "description": T[0],
                "cdate": T[1]
            }
            ]),
            "sections": (
                lambda t: lista_dinamica(t, campos),
                [
            {
            "sectitle": "sectitle",
            "seccontent": "seccontent",
            "subsections": (
                lambda x: list(zip(x.get("subsectitle", []),x.get("subseccontent", []))),  
                [
                {
                    "subsectitle": T[0],
                    "subseccontent": T[1]
                }
            ]),
            "seccontentp": "seccontentp"
        }
        ])}
        
        
        session['callforpapers'] = glom(limpieza(json_esp), target)
        
        
    return render_template('caracteristicas-program.html')

@app.route('/registration',methods=['GET','POST'])
def cregistration():
    if request.method == 'POST':
        print("Funciona")
        
        
        json_esp = json.loads(json.dumps(request.form.to_dict(flat=False), indent=4))
        
        campos = ["Day information", "timelapse", "eventscontent"]
        
        target = {
            "Program information":"Program information",
            "Days of the conference": (
                    lambda t: lista_dinamica(t, campos),
                [
                {
                    "Day information":"Day information",
                    "events": (
                        lambda x: list(zip(x.get("timelapse", []),x.get("eventscontent", []))),
                        [
                        {
                            "timelapse":T[0],
                            "eventscontent":T[1]
                        }
                    ])
                }
            ]),
            "Further program information":{
                "Further program information title":"Further program information title",
                "Further program information content":"Further program information content"
            }
        }
        
        session['program'] = glom(limpieza(json_esp), target)
        
    return render_template('caracteristicas-registration.html')

@app.route('/procesar', methods=['GET', 'POST'])
def procesar_pestanas():
    if request.method == 'POST':
        pestanas = session['pestanas']
        
        
        json_esp = json.loads(json.dumps(request.form.to_dict(flat=False), indent=4))
    
        if session['ultima_pestana'] == 'registration':
            
            json_arreglado = adaptar_registration(json_esp)
        
            if len(pestanas) == 0:
                session[session['ultima_pestana']]=json_arreglado
                return redirect(url_for('cresumenfinal'))
        
        elif session['ultima_pestana'] == "sponsors":
            
            target = {
            "Conference sponsors":(
                lambda t: zip(t['Sponsor url'], t['Sponsor logo'], t['Sponsor name']),
                [
                {
                    "Sponsor url":T[0],
                    "Sponsor logo":T[1],
                    "Sponsor name":T[2]
                }
            ])
            }        
            
            json_arreglado = glom(limpieza(json_esp), target)
            
        elif session['ultima_pestana'] == "proceedings":
            
            json_arreglado = limpieza(json_esp)
            
        elif session['ultima_pestana'] == "awards":
            
            target = {
            "Awards information":"Awards information",
            "Conference awards":(
                lambda t: zip(t['Award title'], t['Award content']),
                [
                {
                    "Award title":T[0],
                    "Award content":T[1]
                }
            ])
            }
            
            json_arreglado = glom(limpieza(json_esp), target)
            
        elif session['ultima_pestana'] == "keynotes":
            
            json_arreglado = limpieza(json_esp)
            
        elif session['ultima_pestana'] == "venue":
            
            target = {
            "Exact location": "Exact location",
            "Street location": "Street location",
            "Venue information": "Venue information"
            }
            
            json_arreglado = glom(limpieza(json_esp), target)
            
        elif session['ultima_pestana'] == "committees":
            
            campos = ["Committee title", "Committee content"]
            
            target = {
            "Workshop chairs":(
            lambda t: t.get('Workshop chair content', []),
                [
                {
                    "Workshop chair content":T
                }
            ]),
            "Program committee":(
                lambda t: t.get('Program chair content', []),
                [
                {
                    "Program chair content":T
                }
            ]),
            "Other committees":(
                lambda t: lista_dinamica(t, campos),
                [
                {
                    "Committee title": "Committee title",
                    "Committee chairs":(
                        lambda x: list(x.get("Committee content", [])),
                        [
                        {
                            "Committee content":T
                        }
                    ])
                }
            ])
            }
            
            json_arreglado = glom(limpieza(json_esp), target)
            
        elif session['ultima_pestana'] == "history":
            
            target = {
            "History information": "History information",
            "History events":(
                lambda t: zip(t['History event title'], t['History event venue'], t['History event content']),
                [
                {
                    "History event title":T[0],
                    "History event venue":T[1],
                    "History event content":T[2]
                }
            ])
            }
            
            json_arreglado = glom(limpieza(json_esp), target)
            
        elif session['ultima_pestana'] == "importantdates":
            
            target = {
            "idates":(
                lambda t: zip(t['Important date action'], t['Important date date']),
                [
                {
                    "Important date action":T[0],
                    "Important date date":T[1]
                }
            ])
            }
            
            json_arreglado = glom(limpieza(json_esp), target)
            

        
        if len(pestanas) == 0:
            session[session['ultima_pestana']] = json_arreglado
            return redirect(url_for('cresumenfinal'))
            
        pestana = pestanas[0]
        pestanas.pop(0)
        session['pestanas'] = pestanas
        
        
            
        if pestana == "sponsors":        
            
            session[session['ultima_pestana']] = json_arreglado
            
            return redirect(url_for('csponsors'))
        elif pestana == "proceedings":
            
            session[session['ultima_pestana']] = json_arreglado
            
            return redirect(url_for('cproceedings'))
        elif pestana == "awards":
            
            session[session['ultima_pestana']] = json_arreglado
            
            return redirect(url_for('cawards'))
        elif pestana == "keynotes":
            
            session[session['ultima_pestana']] = json_arreglado
            
            return redirect(url_for('ckeynotes'))
        elif pestana == "venue":
            
            session[session['ultima_pestana']] = json_arreglado
            
            return redirect(url_for('cvenue'))
        elif pestana == "committees":
            
            session[session['ultima_pestana']] = json_arreglado
            
            return redirect(url_for('ccommittees'))
        elif pestana == "history":
            
            session[session['ultima_pestana']] = json_arreglado
            
            return redirect(url_for('chistory'))
        elif pestana == "importantdates":
            
            session[session['ultima_pestana']] = json_arreglado
            
            return redirect(url_for('cimportantdates'))

@app.route('/sponsors',methods=['GET','POST'])
def csponsors():
    
    session['ultima_pestana'] = "sponsors"
        
    return render_template('caracteristicas-sponsors.html')

@app.route('/proceedings',methods=['GET','POST'])
def cproceedings():
    print("Funciona")
    
    session['ultima_pestana'] = "proceedings"
        
    return render_template('caracteristicas-proceedings.html')

@app.route('/awards',methods=['GET','POST'])
def cawards():
    print("Funciona")
    
    session['ultima_pestana'] = "awards"
        
    return render_template('caracteristicas-awards.html')

@app.route('/keynotes',methods=['GET','POST'])
def ckeynotes():
    print("Funciona")
    
    session['ultima_pestana'] = "keynotes"
        
    return render_template('caracteristicas-keynotes.html')

@app.route('/venue',methods=['GET','POST'])
def cvenue():
    print("Funciona")
    
    session['ultima_pestana'] = "venue"
        
    return render_template('caracteristicas-venue.html')

@app.route('/committees',methods=['GET','POST'])
def ccommittees():
    print("Funciona")
    
    session['ultima_pestana'] = "committees"
        
    return render_template('caracteristicas-committees.html')

@app.route('/history',methods=['GET','POST'])
def chistory():
    print("Funciona")
    
    session['ultima_pestana'] = "history"
        
    return render_template('caracteristicas-history.html')

@app.route('/important-dates',methods=['GET','POST'])
def cimportantdates():
    print("Funciona")
    
    session['ultima_pestana'] = "importantdates"
        
    return render_template('caracteristicas-important-dates.html')

@app.route('/resumen-final',methods=['GET','POST'])
def cresumenfinal():
    session.pop('ultima_pestana', None)
    session.pop('pestanas', None)
    session.pop('s', None)
    
    
    elimina = []
    
    for k, v in session.items():
        if v == "":
            elimina.append(k)
            
    for k in elimina:
        session.pop(k, None)
        
    with open('user-configuration.json', 'w', encoding='utf-8') as fichero:
        fichero.write('{\n\t\"file\": \"web_fm.uvl\",\n\t\"config\": \n\t')
            
        fichero.write(json.dumps(dict(session.items()),indent=4)+'\n')
            
        fichero.write('}')
        
        
    with open('user-configuration.json', 'r', encoding='utf-8') as f:
        json_sin_adaptar = json.load(f)
        
    
    
    with open('user-configuration.json', 'w', encoding='utf-8') as f:
        json.dump(json_sin_adaptar, f, indent=4)
    
    print("Funciona")
    items = []
    
    for item in session.keys():
        if item == "home":
            items.append("Home")
        elif item == "callforpapers":
            items.append("Call for Papers")
        elif item == "program":
            items.append("Program")
        elif item == "registration":
            items.append("Registration")
        elif item == "sponsors":
            items.append("Sponsors")
        elif item == "awards":
            items.append("Awards")
        elif item == "committees":
            items.append("Committees")
        elif item == "history":
            items.append("History")
        elif item == "keynotes":
            items.append("Keynotes")
        elif item == "proceedings":
            items.append("Proceedings")
        elif item == "venue":
            items.append("Venue")
        elif item == "importantdates":
            items.append("Important Dates")    
    
    return render_template('resumen-final.html', items=items)

@app.route('/hosting',methods=['GET','POST'])
def chosting():
    if request.method == 'POST':
        print("Funciona")
        carpeta_actual = os.path.basename(os.getcwd())
        
        if carpeta_actual == "producto":
            os.chdir("..")
        main.main()
        
    return render_template('hosting.html')


@app.route('/instrucciones-hosting',methods=['GET','POST'])
def chosting2():
    if request.method == 'POST':
        print("Funciona")        
        
    return render_template('hosting2.html')


@app.route('/sin-hosting',methods=['GET','POST'])
def sinhosting():
    if request.method == 'POST':
        print("Funciona")        
        
    return render_template('sin-hosting.html')


@app.route('/descarga',methods=['GET','POST'])
def descarga():
    
    print("Funciona")
    shutil.make_archive("tu_web", 'zip', "producto")
        
    return send_file("tu_web.zip", as_attachment=True)


@app.route('/informacion-final',methods=['GET','POST'])
def cfinal():
    if request.method == 'POST':
        print("Funciona")
        
        token = request.form.get("token").strip()
        nombre_repositorio = request.form.get("nombre_repositorio").strip()
        carpeta_base = os.path.dirname(os.path.abspath(__file__))
        carpeta_web = os.path.join(carpeta_base, "producto")
        
        print("ESTE ES EL TOKEN:")
        print(token)
        print("ESTE ES EL NOMBRE DEL REPOSITORIO: ")
        print(nombre_repositorio)
        
        try:
            git = Github(token)
        except Exception as e:
            flash("ERROR: debes introducir un token GitHub válido.")
            return redirect(url_for('chosting2'))
        
        usuario = git.get_user()
        
        if usuario.login != nombre_repositorio:
            flash("ERROR: El usuario proporcionado no coincide con el dueño del token.")
            return redirect(url_for('chosting2'))
        
        nombre_repositorio = f"{usuario.login}.github.io"
        
        try:
            repositorio = usuario.create_repo(nombre_repositorio)
            
            subir_elementos(carpeta_web, nombre_repositorio, usuario.login,token)
            
            saltar_paso(usuario.login, nombre_repositorio, token)
            
        except GithubException as e:
            if e.status == 422:
                flash("ERROR: Ya existe un repositorio enlazado con GitHub Pages en este usuario.\nElimina este repositorio iniciando sesion con tu cuenta en GitHub y eliminandolo desde el apartado mis repositorios.\nNOTA: Solo puedes tener un repositorio de este estilo en GitHub por usuario.")
            else:
                flash(f"ERROR: Se ha producido un error con la conexión con GitHub.\n{e.data.get('message')}")
            return redirect(url_for('chosting2'))
        
    return render_template('final.html', usuario=usuario.login)
    
    
def subir_elementos(carpeta, repositorio, usuario, token):
    url = f"https://{token}@github.com/{usuario}/{repositorio}.git"
    
    try:
        rutagit = os.path.join(carpeta, ".git")
        
        if os.path.exists(rutagit):
            shutil.rmtree(rutagit, onerror=borrar)
        
        os.chdir(carpeta)
        
        print(f"La carpeta: {os.getcwd()}")
        
        comandos = [
            ["git", "init"],
            ["git", "add", "."],
            ["git", "commit", "-m", "Proyecto completo"],
            ["git", "branch", "-M", "main"],
            ["git", "remote", "add", "origin", url],
            ["git", "push", "origin", "main", "--force"],
        ]
        
        for comando in comandos:
            result = subprocess.run(comando, capture_output=True, text=True, shell=True)
            print(f"Mensaje error: {result.stderr}")
            
    except Exception as e:
        print(f"ERROR: {e}")
        
        
def borrar(action, name, exc):
    os.chmod(name, stat.S_IWRITE)
    os.remove(name)
    
    
def lista_dinamica(datos, campos):
    patron = "|" .join(map(re.escape, campos))
    reobj = re.compile(rf"^({patron})(\d+)?$")
    
    agraupacion = {}
    for k in datos.keys():
        coincidencia = reobj.match(k)
        if coincidencia:
            campo = coincidencia.group(1)
            indice = coincidencia.group(2) if coincidencia.group(2) else "1"
            
            if indice not in agraupacion:
                agraupacion[indice] = {}
            
            agraupacion[indice][campo] = datos.get(k)
            
    return [agraupacion[i] for i in sorted(agraupacion.keys(), key=int)]

def lista_jerarquica(datos, campos):
    
    niveles = {
        0: ["Package name"],
        1: ["Category name", "Registration cost"],
    }
    
    patron = "|" .join(map(re.escape, campos))
    reobj = re.compile(rf"^({patron})(\d[\d_]*)?$")
    
    agraupacion = {}
    for k in datos.keys():
        coincidencia = reobj.match(k)
        if coincidencia:
            campo = coincidencia.group(1)
            ruta = coincidencia.group(2) if coincidencia.group(2) else "1"
            indice = ruta.split('_')
            profundidad = len(indice) - 1
            
            nivel_actual = agraupacion
            
            for i, idx in enumerate(indice):
                if idx not in nivel_actual:
                    nivel_actual[idx] = {"_data": {}, "_hijos": {}}
                    
                if i == len(indice) - 1 and campo in niveles.get(i, []):
                    if campo == "Registration cost" and isinstance(datos.get(k), list):
                        nivel_actual[idx]["_data"]["Registration deadlines table"] = [{"Registration cost": c} for c in datos.get(k)]
                    else:
                        nivel_actual[idx]["_data"][campo] = datos.get(k)
                        
                
                if i < len(indice) - 1:
                    nivel_actual = nivel_actual[idx]["_hijos"]
            
    return procesado_final(agraupacion, nivel=0)

def procesado_final(diccionario, nivel=0):
    if not diccionario: return []
    
    llaves = ["Registration category"]
    
    ordenado = sorted(diccionario.keys(), key=lambda x: [int(c) for c in x.split('_')])
    producto = []
    
    for k in ordenado:
        item = diccionario[k]["_data"]
        
        if diccionario[k]["_hijos"]:
            if nivel < len(llaves):
                hijo = llaves[nivel]
                item[hijo] = procesado_final(diccionario[k]["_hijos"], nivel + 1)
        producto.append(item)
        
    return producto

def limpieza(datos):
    if isinstance(datos, dict):
        return {k: limpieza(v) for k, v in datos.items()}
    elif isinstance(datos, list):
        if len(datos) == 1:
            return limpieza(datos[0])
        else:
            return [limpieza(i) for i in datos]
    
    return datos

def adaptar_registration(json_esp):
    
    
    campos = ["Package name", "Category name", "Registration cost"]
        
    target = {
        "Registration deadlines": (
                lambda t: zip(t['Deadline title'], t['Deadline timelapse']),
                [
                {
                    "Deadline title":T[0],
                    "Deadline timelapse":T[1]
                }
            ]),
            "Registration link":"Registration link",
            "Registration fees": {
                "Registration packages": lambda t: lista_jerarquica(t, campos),
                "Registration fees info": "Registration fees info"
            },
            "Registration status":"Registration status",
            "Registration further info":{
                "Registration further info title":"Registration further info title",
                "Registration further info content":"Registration further info content"
            }
        }
    
    return glom(limpieza(json_esp), target)


def saltar_paso(usuario, repo, token):
    url = f"https://api.github.com/repos/{usuario}/{repo}/actions/workflows/deploy.yml/dispatches"
    
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}"
    }
    
    data = {
        "ref": "main"
    }
    
    response = requests.post(url, headers=headers, json=data)
    
        
    if response.status_code in [204]:
        print("Web establecida con exito, espere unos 30 segundos")
    else:
        print(f"ERROR: {response.status_code}")
        print(response.json())

    
if __name__ == '__main__':
    app.run(debug=True)