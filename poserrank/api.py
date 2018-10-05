from flask import Blueprint, request, jsonify
from poserrank.models import User, Group

api = Blueprint('api', __name__)

@api.route('/users/search', methods=['POST'])
def search_users():
	"""
	this function may not scale -- I highly doubt this will ever be a problem
	"""
	if 'query' in request.form:
		if 'group' in request.form:
			group = Group.query.filter(Group.id == request.form['group'])[0]
			users = [m.user for m in group.memberships]
		else:
			users = User.query.all()
		all_usernames = [user.username for user in users]
		#all_fullnames = [user.full_name for user in all_users]
		suggestions = list(filter(lambda x: request.form['query'].lower() in x.lower(), all_usernames))
		#suggestions += list(filter(lambda x: request.form['query'].lower() in x.lower(), all_usernames))

		return jsonify(suggestions)

	else:
		return "Request must contain 'query' field", 400