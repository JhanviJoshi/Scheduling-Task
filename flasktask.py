from flask import Flask, redirect, url_for, request, render_template
import scheduletask

app = Flask(__name__)

@app.route('/enterDetails', methods=['GET','POST'])
def hello_name():
   return render_template('enterDetails.html')


@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      print(result)
      new_profile = request.form['profile']
      startdate = request.form['startdate']
      enddate = request.form['enddate']
      user = request.form['user']
      data = scheduletask.schedule(new_profile,startdate,enddate,user)
      print(data)
      return render_template("result.html", result=data)

@app.route('/alldata',methods = ['POST', 'GET'])
def all_data():
   dataset = scheduletask.all_user()
   return render_template("alldata.html", result=dataset)



if __name__ == '__main__':
   app.run(debug = True)

# from flask import Flask, render_template, request, flash, url_for
# from forms import ContactForm
# from werkzeug.utils import redirect
#
# app = Flask(__name__)
# app.secret_key = 'development key'
#
#
# @app.route('/contact', methods=['GET', 'POST'])
# def contact():
#    form = ContactForm()
#    if form.validate_on_submit():
#       print("here")
#       flash('All fields are required.')
#       return redirect("/success")
#    return render_template('contact.html', form = form)
#
#
# @app.route('/success', methods=['GET', 'POST'])
# def success():
#    return render_template("success.html")
#
#
# if __name__ == '__main__':
#    app.run(debug=True)