from flask import Flask, request, render_template, session
import json

app = Flask(__name__, template_folder= 'interfaz', static_folder='interfaz')
app.secret_key = 'mi_clave_segura'


@app.route('/')
def inicio():
    session['callforpapers']=''
    session['program']=''
    session['registration']=''
    session['sponsors']=''
    session['proceedings']=''
    session['awards']=''
    session['keynotes']=''
    session['venue']=''
    session['committees']=''
    session['history']=''
    session['importantdates']=''
    return render_template('home.html')

@app.route('/pestanas', methods=['GET'])
def pestanas():
    return render_template('caracteristicas-pestañas.html')

    
@app.route('/home',methods=['GET','POST'])
def chome():
    if request.method == 'POST':
        pestanas = request.form.getlist('pestañas')
        
        print(pestanas)
        
        
    return render_template('caracteristicas-home.html')


@app.route('/callforpapers',methods=['GET','POST'])
def ccallforpapers():
    if request.method == 'POST':
        print("Funciona")
        
        session['home']=json.loads(json.dumps(request.form.to_dict(), indent=4))
        
    return render_template('caracteristicas-callforpapers.html')


@app.route('/program',methods=['GET','POST'])
def cprogram():
    if request.method == 'POST':
        print("Funciona")
        
        session['callforpapers']=json.loads(json.dumps(request.form.to_dict(), indent=4))
        
    return render_template('caracteristicas-program.html')

@app.route('/registration',methods=['GET','POST'])
def cregistration():
    if request.method == 'POST':
        print("Funciona")
        
        session['program']=json.loads(json.dumps(request.form.to_dict(), indent=4))
        
    return render_template('caracteristicas-registration.html')

@app.route('/sponsors',methods=['GET','POST'])
def csponsors():
    if request.method == 'POST':
        print("Funciona")
        
        session['registration']=json.loads(json.dumps(request.form.to_dict(), indent=4))
        
    return render_template('caracteristicas-sponsors.html')

@app.route('/proceedings',methods=['GET','POST'])
def cproceedings():
    if request.method == 'POST':
        print("Funciona")
        
        session['sponsors']=json.loads(json.dumps(request.form.to_dict(), indent=4))
        
    return render_template('caracteristicas-proceedings.html')

@app.route('/awards',methods=['GET','POST'])
def cawards():
    if request.method == 'POST':
        print("Funciona")
        
        session['proceedings']=json.loads(json.dumps(request.form.to_dict(), indent=4))
        
    return render_template('caracteristicas-awards.html')

@app.route('/keynotes',methods=['GET','POST'])
def ckeynotes():
    if request.method == 'POST':
        print("Funciona")
        
        session['awards']=json.loads(json.dumps(request.form.to_dict(), indent=4))
        
    return render_template('caracteristicas-keynotes.html')

@app.route('/venue',methods=['GET','POST'])
def cvenue():
    if request.method == 'POST':
        print("Funciona")
        
        session['keynotes']=json.loads(json.dumps(request.form.to_dict(), indent=4))
        
    return render_template('caracteristicas-venue.html')

@app.route('/committees',methods=['GET','POST'])
def ccommittees():
    if request.method == 'POST':
        print("Funciona")
        
        session['venue']=json.loads(json.dumps(request.form.to_dict(), indent=4))
        
    return render_template('caracteristicas-committees.html')

@app.route('/history',methods=['GET','POST'])
def chistory():
    if request.method == 'POST':
        print("Funciona")
        
        session['committees']=json.loads(json.dumps(request.form.to_dict(), indent=4))
        
    return render_template('caracteristicas-history.html')

@app.route('/important-dates',methods=['GET','POST'])
def cimportantdates():
    if request.method == 'POST':
        print("Funciona")
        
        session['history']=json.loads(json.dumps(request.form.to_dict(), indent=4))
        
    return render_template('caracteristicas-important-dates.html')

@app.route('/resumen-final',methods=['GET','POST'])
def cresumenfinal():
    if request.method == 'POST':
        session['important-dates']=json.loads(json.dumps(request.form.to_dict(), indent=4))
        
        with open('user-configuration.json', 'w', encoding='utf-8') as fichero:
            fichero.write('{\n\t\"file\": \"web_fm.uvl\",\n\t\"config\": \n\t')
            
            fichero.write(json.dumps(dict(session.items()),indent=4)+'\n')
            
            fichero.write('}')
        print("Funciona")
        print(type(session['home']))
        
    return render_template('resumen-final.html')

@app.route('/hosting',methods=['GET','POST'])
def chosting():
    if request.method == 'POST':
        print("Funciona")
        
    return render_template('hosting.html')
    
if __name__ == '__main__':
    app.run(debug=True)