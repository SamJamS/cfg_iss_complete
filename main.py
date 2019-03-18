from flask import Flask, render_template, request
import iss

app = Flask('MyApp')

@app.route('/')
def hello():
    return 'Hello World'

@app.route('/iss', methods=['GET','POST'])
def iss_main():
    current_location = iss.get_iss_location()
    pass_time = None
    postcode = None

    if request.method == 'POST':
        postcode = request.form.get('postcode')
        pass_time = iss.get_iss_pass_time_from_postcode(postcode)

    return render_template(
        'iss.html',
        current_location=current_location,
        pass_time=pass_time,
        postcode=postcode
    )


app.run(debug=True)
