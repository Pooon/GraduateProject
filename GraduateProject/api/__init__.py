import homepage
import user
import category
from flask import jsonify

"""Define global error code here"""
G_ERR = {
    '400': {'err': 0, 'msg': 'Bad Request'},
    '401': {'err': 1, 'msg': 'Unauthorized'},
    '403': {'err': 2, 'msg': 'Forbidden'},
    '404': {'err': 3, 'msg': 'Not Found'},
}

"""Define api error handlers"""
@api.errorhandler(400)
def handle_400(e):
    return jsonify(stat=0, **G_ERR['400']), 400


@api.errorhandler(401)
def handle_401(e):
    return jsonify(stat=0, **G_ERR['401']), 401


@api.errorhandler(403)
def handle_403(e):
    return jsonify(stat=0, **G_ERR['403']), 403


@api.errorhandler(404)
def handle_404(e):
    return jsonify(stat=0, **G_ERR['404']), 404