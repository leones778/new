from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cartridges.db'
db.init_app(app)

# Создаем таблицу в базе данных
class Сartridges(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(50))
    printer = db.Column(db.String(100))
    status = db.Column(db.String(5000))

    def __init__(self, model, printer, status):
        self.model = model
        self.printer = printer
        self.status = status


with app.app_context():
    db.create_all()


# Метод для добавления картриджа
@app.route('/add_cartridges', methods=['POST'])
def add_cartridges():
    model = request.form['model']
    printer = request.form['printer']
    status = request.form['status']
    rep = Сartridges(model, printer, status)
    db.session.add(rep)
    db.session.commit()
    return jsonify({'message': 'cartridg added successfully'})


# Метод для получения картриджей по id
@app.route('/viewing_cartridges_fitler_id/<int:id>')
def viewing_cartridges_filter_id(id):
    report = Сartridges.query.get(id)
    if report:
        return jsonify({
            'id': report.id,
            'model': report.model,
            'printer': report.printer,
            'status': report.status
        })
    else:
        return {'error': 'There is no such ID in the list of cartridg'}


# Метод для получения кртриджей определенной модели
@app.route('/viewing_cartridges_filter_model/<model>')
def viewing_cartridges_filter_model(model):
    reports = Сartridges.query.all()
    response = []
    for report in reports:
        if report.model==model:
            response.append({
                'id': report.id,
                'model': report.model,
                'printer': report.printer,
                'status': report.status
            })
    if response:
        return jsonify(response)
    else:
        return {'error': 'There is no such ID in the list of cartridg'}


# Метод для получения кртриджей по статусу

@app.route('/viewing_cartridges_filter_status/<status>')
def viewing_cartridges_filter_status(status):
    reports = Сartridges.query.all()
    response = []
    for report in reports:
        if report.status==status:
            response.append({
                'id': report.id,
                'model': report.model,
                'printer': report.printer,
                'status': report.status
            })
    if response:
        return jsonify(response)
    else:
        return {'error': 'There is no such ID in the list of cartridg'}


# Метод для получения всех картриджей
@app.route('/viewing_cartridges', methods=['GET'])
def viewing_cartridges():
    reports = Сartridges.query.all()
    response = []
    for report in reports:
        response.append({
            'id': report.id,
            'model': report.model,
            'printer': report.printer,
            'status': report.status
        })
    return jsonify(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
