from flask import Flask
from flask import request
import subprocess


app = Flask('flaskshell')
ip_whitelist = ['192.168.1.2', '192.168.1.3', '127.0.0.1']

def valid_ip():
    client = request.remote_addr
    if client in ip_whitelist:
        return True
    else:
        return False

@app.route('/dir/')
def get_status():
    if valid_ip():
        command_success = "ls -la /tmp"(query_success)
        command_pending = "ls -la /root"(query_pending)
        command_failed = "ls -la /"(query_failed)

        try:
            result_success = subprocess.check_output(
                [command_success], shell=True)
            result_pending = subprocess.check_output(
                [command_pending], shell=True)
            result_failed = subprocess.check_output(
                [command_failed], shell=True)
        except subprocess.CalledProcessError as e:
            return "An error occurred while trying to fetch task status updates."

        return 'Success %s, Pending %s, Failed %s' % (result_success, result_pending, result_failed)
    else:
        return """<title>404 Not Found</title>
               <h1>Not Found</h1>
               <p>The requested URL was not found on the server.
               If you entered the URL manually please check your
               spelling and try again.</p>""", 404

if __name__ == '__main__':
    app.run()
