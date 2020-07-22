from flask import Flask, request
app = Flask(__name__)

# Generate the opening, index, webpage.
def index():
  return ('Simple web server')

# End-point for a simple web-service. 
def service():
  myArg = request.args.get('myarg')
  return f'''The value of myarg is:{myArg}'''


app.add_url_rule('/', 'index', index) 

app.add_url_rule('/service', 'service', service) 

# Start the web sever - be patient, it takes time.
app.run(host='0.0.0.0')