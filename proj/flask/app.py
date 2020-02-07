from flask import Flask, render_template, request, redirect
import bot1 as Server
commandno1=[1]

app = Flask(__name__)
lstatus=['OFF']
dstatus=['CLOSED']
@app.route('/', methods=['GET', 'POST'])
def index():
    global lstatus
    return render_template('index.html',light_status=lstatus[0],door_status=dstatus[0])



@app.route('/lightaction/<string:even>')
def action(even):
    if even == "on":
        lstatus[0]="ON"
        subject='command'+str(commandno1[0])
        Server.sender(subject,"lighton","NULL","NULL")
        commandno1[0]=commandno1[0]+1
        return render_template('index.html',light_status=lstatus[0],door_status=dstatus[0])
    elif even == "off":
        lstatus[0]="off"
        subject='command'+str(commandno1[0])
        Server.sender(subject, "lightoff", "NULL", "NULL")
        commandno1[0]=commandno1[0]+1
        return render_template('index.html',light_status=lstatus[0],door_status=dstatus[0])
    else:
        return render_template('index.html',light_status=lstatus[0],door_status=dstatus[0])
@app.route('/dooraction/<string:deven>')
def daction(deven):
    if deven == "open":
        dstatus[0]="OPEN"
        subject='command'+str(commandno1[0])
        Server.sender(subject, "dooropen", "NULL", "NULL")
        commandno1[0]=commandno1[0]+1
        return render_template('index.html',door_status=dstatus[0],light_status=lstatus[0])
    elif deven == "close":
        dstatus[0]="CLOSED"
        subject='command'+str(commandno1[0])
        Server.sender(subject, "doorclose", "NULL", "NULL")
        commandno1[0]=commandno1[0]+1
        return render_template('index.html',door_status=dstatus[0],light_status=lstatus[0])
    else:
        return render_template('index.html',door_status=dstatus[0],light_status=lstatus[0])



if __name__ == "__main__":
    app.run('192.168.137.1','80')
