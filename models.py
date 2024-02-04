from app import db
from datetime import datetime

class Alert(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_email = db.Column(db.String(120), nullable=False) 
    cryptocurrency = db.Column(db.String(50), nullable=False)
    target_price = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), default='created') 
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
