from flask import Flask, render_template, request, redirect, url_for, jsonify
app = Flask(__name__)

list_shopping = ['Milk', 'Eggs', 'Bread', 'Juice']

@app.route('/', methods=['GET', 'POST'])
def index():
    global list_shopping
    if request.method == 'POST':
        list_shopping.append(request.form['item'])
    return render_template('index.html', items=list_shopping)

@app.route('/remove/<name>')
def remove_item(name):
    global list_shopping
    if name in list_shopping:
        list_shopping.remove(name)
    else:
        pass
    return redirect(url_for('index'))

@app.route('/api/items')
def get_items():
    '''
    A simple API that returns a JSON object with the list
    '''
    global list_shopping
    return jsonify({'items': list_shopping})

if __name__ == '__main__':
    app.run(debug=True)
