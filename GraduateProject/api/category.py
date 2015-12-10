from GraduateProject import app
from GraduateProject.model import MySQLConnectionWrap
from GraduateProject.model.category import Category

class Error(object):
    CATEGORY_ERROR = {'err': 1001,
                      'msg': 'Categories is illegal'}

@app.route('/category/detail',methods=['GET'])
def getCategoryDetail():
	
	category_id = request.args['categoryId']

	if category_id is None:
		return jsonify(stat = 0, **Error.CATEGORY_ERROR), 400

	return 'category not null'
