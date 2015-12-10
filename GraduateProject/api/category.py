from GraduateProject import app
from GraduateProject.model import MySQLConnectionWrap
from GraduateProject.model.category import Category

@app.route('/category/detail',methods=['GET'])
def getCategoryDetail():
	
	category_id = request.args['categoryId']

	if category_id is None:
		return jsonify(stat = 0, ''), 400

	return 'category not null'
