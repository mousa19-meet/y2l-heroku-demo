from flask import Flask,request
from flask import render_template
from database import get_all_cats, query_by_id, create_cat,delete_cat_by_id,update_voter

app = Flask(__name__)
app.config['SECRET_KEY'] = 'YOUR-VERY-SECRET-SHHH'

@app.route('/')
def catbook_home():
    cats = get_all_cats()
    return render_template("home.html", cats=cats)


@app.route('/cats/<int:id>')
def cat_page(id):
    var_name = query_by_id(id)
    return render_template(
        'cat.html', n = var_name,d =id)

@app.route('/delete/<int:id>')
def delete_cat(id):
	delete_cat_by_id(id)
	cats = get_all_cats()
	return render_template("delete.html",cats=cats)

@app.route('/like/<int:id>')
def liked(id):
	update_voter(id)
	var_name = query_by_id(id)
	return render_template('like.html',n = var_name)

@app.route('/create', methods =["GET","POST"])
def make_cat():
	if request.method =="GET":
		return render_template('form.html')
	else:
		name = request.form['firstname']
		create_cat(name,0)
		cats = get_all_cats()
		return render_template('home.html', cats=cats)


if __name__ == '__main__':
   app.run(debug = True)
