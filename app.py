
from flask import Flask,render_template,request,jsonify
from src.pipeline.predict_pipeline import PredictPipeline,CustomData
from src.exception import CustomException


application = Flask(__name__)
app = application

@app.route("/",methods = ["GET","POST"])
def predict_datapoint():
    if request.method == "GET":
        return render_template("index.html")

    else:
        data = CustomData(
        age=int(request.form.get("age") or 0),
        workclass=int(request.form.get("workclass") or 0),
        education=int(request.form.get("education") or 0),
        marital_status=int(request.form.get("marital-status") or 0),
        occupation=int(request.form.get("occupation") or 0),
        relationship=int(request.form.get("relationship") or 0),
        race=int(request.form.get("race") or 0),
        sex=int(request.form.get("sex") or 0),
        hours_per_week=int(request.form.get("hours_per_week") or 0),
        native_country=int(request.form.get("native_country") or 0)
)



        final_new_data=data.get_data_as_data_frame()
        predict_pipeline=predict_pipeline()
        pred=predict_pipeline.predict(final_new_data)

        results=round(pred[0],2)

        return render_template('index.html',final_result=results)


    if result == 0:
            return render_template("form.html",final_result = "Your Income is Less Then Equal To 50K: {}".format(result))

    elif result == 1:
            return  render_template("form.html",final_result = "Your Income is More Then 50K: {}".format(result))


if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)