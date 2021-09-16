from flask import Flask

# Create a flask app
app = Flask(
  __name__,
  template_folder='templates',
  static_folder='static'
)

# Index page
@app.route('/')
def hello():
  return "Hello World!"

#Amanda's HTTP Request
@app.route("/number/<input>")
def number(input):
  input = int(input)
  if (input%2==0):
    return "even!"
  else:
    return "odd!"

app.run(host = "0.0.0.0")
