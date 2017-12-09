from flask import Flask
from flask import jsonify
from flask import request
app = Flask(__name__)
DeptDB=[
{'id':'1','title':'Department of Aerospace Engineering'},
{ 'id':'2' , 'title':'Department of Agricultural and Food Engineering' },
{ 'id':'3' , 'title':'Department of Biotechnology' },
{ 'id':'4' , 'title':'Department of Civil Engineering' },
{ 'id':'5' , 'title':'Department of Computer Science & Engineering' },
{ 'id':'6' , 'title':'Department of Electrical Engineering' },
{ 'id':'7' , 'title':'Department of Mathematics' },
{ 'id':'8' , 'title':'Department of Mechanical Engennering' },
{ 'id':'9' , 'title':'Department of Mechanical Engineering' },
{ 'id':'10' , 'title':'Department of Metallurgical & Materials Engineering' },
{ 'id':'11' , 'title':'Department of Metallurgical and Materials Engineering' },
{ 'id':'12' , 'title':'Department Of Mining' },
{ 'id':'13' , 'title':'Department of Ocean Engineering & Naval Architecture' },
{ 'id':'14' , 'title':'Department of Rural Development Centre' }
]
@app.route("/DeptDB/Departments",methods=['GET'])
def getDeptList():
    return jsonify({'Dpt':DeptDB})
@app.route("/DeptDB/Departments/<sno>",methods=['GET'])
def getDepName(sno):
    dept = [ Dpt for Dpt in DeptDB if (Dpt['id']==sno)]
    return jsonify({'Dpt':dept})
@app.route("/DeptDB/Departments/<sno>",methods=['PUT'])
def updateDB(sno):
    dept = [ Dpt for Dpt in DeptDB if (Dpt['id']==sno)]
    if 'name' in request.json:
        dept[0]['name'] = request.json['name']
    return jsonify({'Dpt':dept[0]})
@app.route("/DeptDB/Departments/",methods=['POST'])
def addDept():
    add = {
    'id':request.json['id'],
    'name':request.json['name']
    }
    DeptDB.append(add)
    return jsonify(add)

if __name__=='__main__':
    app.run()
