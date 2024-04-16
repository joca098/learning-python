from flask import Flask, render_template, request
import pickle
from modelo import ModeloOrange

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/formulario', methods=['GET'])
def formulario():
    return render_template('formulario.html')

@app.route('/procesar', methods=['POST'])
def procesar():
    if request.method == 'POST':
        # Mapeo de las entradas del formulario a valores numéricos
        features = [
    1 if request.form['disability_babies'] == 's' else 0,
    1 if request.form['water_project_cost_sharing'] == 's' else 0,
    1 if request.form['budget_resolution_adoptation'] == 's' else 0,
    1 if request.form['medical_fees_freezing'] == 's' else 0,
    1 if request.form['aid_el_salvador'] == 's' else 0,
    1 if request.form['religious_groups_in_schools'] == 's' else 0,
    1 if request.form['anti_satellite_test_ban'] == 's' else 0,
    1 if request.form['aid_nicaraguan_contras'] == 's' else 0,
    1 if request.form['missile_mx'] == 's' else 0,
    1 if request.form['immigration'] == 's' else 0,
    1 if request.form['synfuels_corporation_cutback'] == 's' else 0,
    1 if request.form['education_spending'] == 's' else 0,
    1 if request.form['superfund_right_to_sue'] == 's' else 0,
    1 if request.form['crime'] == 's' else 0,
    1 if request.form['duty_free_exports'] == 's' else 0,
    1 if request.form['export_administration_act_south_africa'] == 's' else 0
]

        # Cargar el modelo y hacer la predicción
        modelo = ModeloOrange()
        result = modelo.predict(features)
        result = int(result[0])
        resultt = str(type((result)))
        if result == 0 :
            resultt = "democrat"
        else:
            resultt = "republican" 
        return render_template('resultado.html', prediction=resultt)

@app.route('/resultado')
def resultado():
    return render_template('resultado.html')

if __name__ == '__main__':
    app.run(debug=True)
