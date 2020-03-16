from flask import Flask
import socket,json,psutil,multiprocessing
app = Flask(__name__)


@app.route('/status')
def status_info():

    info = {}
    info['hostname'] = socket.gethostname()
    info['ip_address'] = socket.gethostbyname(socket.gethostname())
    info['cpus'] = multiprocessing.cpu_count()
    info['memory'] = str(round(psutil.virtual_memory().total / (1024.0 ** 3))) + " GB"
    return json.dumps(info, sort_keys=False, indent=4)


if __name__ == '__main__':

    debug = True
    app.run(host='0.0.0.0', port='8080')
