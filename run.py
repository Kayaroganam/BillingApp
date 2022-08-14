from flask import Flask, render_template, redirect, request, url_for
from database_operation import *
import datetime
import database_operation

app = Flask(__name__)   #Creating an flask object

no_of_rows = get_max_row()

@app.route('/')
@app.route('/home')
def home():
    data = select_all()
    total = total_price()
    data2 = select_all_selected()

    return render_template("home.html", data=data, total=total, data2=data2)

@app.route('/add_selected/', methods=['POST','GET'])
def selected_add():
    if request.method == 'POST':
        item_id = request.form.get('select_item_id')
        qty = request.form.get('qty')
        if qty != '':
            qty = float(qty)
        else:
            qty = 0

        total = selected_id(item_id, qty)
    return redirect(url_for('home'))

@app.route('/list')
def list():
    data = select_all()
    return render_template('list.html', data=data)

@app.route('/add')
def add():
    data = select_all()
    return render_template('add.html',data=data)

@app.route('/adding', methods=['POST','GET'])
def adding():
    if request.method == 'POST':
        item_name = request.form.get('item_name')
        item_price = float(request.form.get('item_price'))
        insert_data(item_name, item_price)
    return redirect(url_for('list'))

@app.route('/edit/<int:post_id>')
def edit(post_id):
    data = select_all()
    return render_template('edit.html', data=data, post_id=post_id)

@app.route('/editing/<int:post_id>', methods=['POST','GET'])
def editing(post_id):
    if request.method == 'POST':
        item_name = request.form.get('item_name')
        item_price = request.form.get('item_price')
        edit_data(post_id, item_name, item_price)
    return redirect(url_for('list'))

@app.route('/delete/<int:post_id>')
def delete(post_id):
    delete_data(post_id)
    return redirect(url_for('list'))

@app.route('/delete_selection/<int:post_id>')
def delete_select(post_id):
    delete_selection(post_id)
    return redirect(url_for('home'))

@app.route('/generateBill')
def generate_bill():
    data = select_all_selected()
    total = total_price()
    date_ = datetime.datetime.now()
    return render_template('generate.html', data=data, total=total, date=date_)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
