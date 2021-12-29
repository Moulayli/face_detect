from flask import Flask, render_template, Response
from camera import Video

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect_face/')
def detect_face():
    return render_template('detect_face.html')


def gen(camera):
    while True:
        frame=camera.get_frame()
        yield(b'--frame\r\n'
       b'Content-Type:  image/jpeg\r\n\r\n' + frame +
         b'\r\n\r\n')

@app.route('/video')
def video():
    return Response(gen(Video()),
    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

#app.run(debug=True)
if __name__=="__main__":
    app.run(debug=True)
#app.run(host="0.0.0.0",port=5000)