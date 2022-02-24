#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask
app =Flask (__name__)
from flask import request, render_template
import joblib

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        rates = request.form.get("rates")
        request.form.get("rates")
        print(rates)    
        
        model = joblib.load("Equity_Reg")
        pred1 = model.predict([[float(rates)]])
        print (pred1)       
        s1 = "Predicted Equity base on Linear Regression model is : " + str(pred1)
    
        model = joblib.load("Equity_DT")
        pred2 = model.predict([[float(rates)]])
        print (pred2)
        s2 = "Predicted Equity base on Decision Tree model is : " + str(pred2)
    
        model = joblib.load("Equity_NN")
        pred3 = model.predict([[float(rates)]])
        print (pred3)
        s3 = "Predicted Equity base on Neural Network model is : " + str(pred3)
    
        return(render_template("index.html", result1=s1, result2=s2, result3=s3))
    else:
        return(render_template("index.html", result1="2", result2="2", result3="2"))


# In[ ]:


if __name__ == "__main__":
    app.run()

