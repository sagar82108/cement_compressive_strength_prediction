from flask import Flask, request, render_template
from src.pipelines.prediction_pipeline import customdata, predictpipeline

application = Flask(__name__)
app = application

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        try:
            data = customdata(
                cement=float(request.form.get('cement')),
                blast_furnace_slag=float(request.form.get('blast_furnace_slag')),
                fly_ash=float(request.form.get('fly_ash')),
                water=float(request.form.get('water')),
                superplasticizer=float(request.form.get('superplasticizer')),
                coarse_aggregate=float(request.form.get('coarse_aggregate')),
                fine_aggregate=float(request.form.get('fine_aggregate')),
                age=float(request.form.get('age'))
            )
            final_new_data = data.get_data_as_dataframe()
            predict_pipeline = predictpipeline()
            pred = predict_pipeline.predict(final_new_data)

            result = round(pred[0], 2)

            return render_template('form.html', final_result=result)
        except Exception as e:
            return render_template('form.html', error_message=str(e))

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
