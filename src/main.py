from flask import Flask
app = Flask(__name__)



@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/testServo')
def testServo():
    from controllers.lock import lock
    
    lock = lock()

    lock.test()

    return 'testing'

@app.route('/unlock')
def unlock():
    return 'unlocking'
    
@app.route('/ring')
def ring():
    return 'ringing'

    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
