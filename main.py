#pip install flask
#pip install pandas
#pip install numpy
#pip install scikit-learn
#pip install joblib


from flask import Flask,render_template,request,json,jsonify
import predict_performance

#app=Flask(__name__)
app = Flask(__name__)
app.secret_key="secure"
data =0

@app.route('/',methods=["post","get"])
def first_page():
    if request.method=="POST":
        global data
        data=json.loads(request.data)
        print('Form Data:', data)
        return jsonify(dict(msg="success"))
    else:
        return render_template("form_page.html")
    


@app.route("/data_page/",methods=["get"])
def data_page():
    res = predict_performance.get_performance(data["late_days"], data["engagement"], data["salary"],
                                              data["date_of_hire"], data["absents"], data["date_of_birth"],
                                              data["satisfaction"])
    print("ML", res)
    return render_template("data_page.html",message=data, result = res)
    
app.run(host="0.0.0.0", debug=True)
