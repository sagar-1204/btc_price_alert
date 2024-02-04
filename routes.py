from flask import Blueprint, request, jsonify
from models import Alert, db

alerts_blueprint = Blueprint('alerts', __name__)

@alerts_blueprint.route('/create/', methods=['POST'])
def create_alert():
    data = request.json
    new_alert = Alert(
        user_email=data['email'],
        cryptocurrency=data['crypto'],
        target_price=data['target_price']
    )
    db.session.add(new_alert)
    db.session.commit()
    return jsonify({'message': 'Alert created successfully'}), 201

@alerts_blueprint.route('/delete/<int:alert_id>/', methods=['DELETE'])
def delete_alert(alert_id):
    alert = Alert.query.get(alert_id)
    if alert:
        alert.status = 'deleted'  # Mark as deleted or use db.session.delete(alert) to remove
        db.session.commit()
        return jsonify({'message': 'Alert deleted successfully'}), 200
    return jsonify({'message': 'Alert not found'}), 404

@alerts_blueprint.route('/', methods=['GET'])
def get_alerts():
    page = request.args.get('page', 1, type=int)
    status_filter = request.args.get('status')
    user_email = request.args.get('email')

    query = Alert.query.filter_by(user_email=user_email)
    if status_filter:
        query = query.filter_by(status=status_filter)

    pagination = query.paginate(page, per_page=10, error_out=False)
    alerts = pagination.items
    return jsonify([{
        'id': alert.id,
        'cryptocurrency': alert.cryptocurrency,
        'target_price': alert.target_price,
        'status': alert.status
    } for alert in alerts]), 200
