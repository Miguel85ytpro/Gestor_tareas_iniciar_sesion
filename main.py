from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'steam_secret_key'

USUARIO_VALIDAR = "admin"
PASSWORD_VALIDAR = "1234"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form.get('usuario')
        password = request.form.get('password')

        if usuario == USUARIO_VALIDAR and password == PASSWORD_VALIDAR:
            session['user'] = usuario
            return redirect(url_for('index'))
        else:
            return redirect(url_for('login'))
            
    return render_template("iniciar_sesion.html")

@app.route("/logout")
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

@app.route("/registro", methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        return redirect(url_for('login'))
    return render_template("formulario.html")

@app.route("/recuperar", methods=['GET', 'POST'])
def recuperar():
    if request.method == 'POST':
        return redirect(url_for('login'))
    return render_template("recuperar_contraseña.html")

@app.route("/tareas")
def tareas():
    return render_template("gestor_tareas.html")

if __name__ == "__main__":
    app.run(debug=True)