from flask import Flask, render_template, request
from src.pipeline.predict_pipeline import PredictPipeline, CustomData
from src.exception import CustomException
from src.pipeline.train_pipeline import train_model

application = Flask(__name__)
app = application

@app.route("/", methods=["GET", "POST"])
def predict_datapoint():
    if request.method == "GET":
        return render_template("form.html")
    else:
        data = CustomData(
            age=int(request.form.get("age") or 0),
            workclass=int(request.form.get("workclass") or 0),
            education_num=int(request.form.get("education_num") or 0),
            marital_status=int(request.form.get("marital_status") or 0),
            occupation=int(request.form.get("occupation") or 0),
            relationship=int(request.form.get("relationship") or 0),
            race=int(request.form.get("race") or 0),
            sex=int(request.form.get("sex") or 0),
            hours_per_week=int(request.form.get("hours_per_week") or 0),
            native_country=int(request.form.get("native_country") or 0)
        )

    final_new_data = data.get_data_as_data_frame()
    predict_pipeline = PredictPipeline()
    pred = predict_pipeline.predict(final_new_data)

    # Clean up the prediction result
    pred_cleaned = pred[0].strip()

    if pred_cleaned == '>50K':
        result_text = "Your Income is More Than 50K"
    else:
        result_text = "Your Income is Less Than or Equal to 50K"

    return render_template("form.html", final_result=result_text)




if __name__=="__main__":
    app.run(host="0.0.0.0")
    