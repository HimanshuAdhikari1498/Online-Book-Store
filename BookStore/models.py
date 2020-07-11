from datetime import datetime
from BookStore import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    address=db.Column(db.Text, nullable=True)
    state=db.Column(db.String(60), nullable=True)
    pincode=db.Column(db.Integer, nullable=True)
    cart=db.relationship('Cart', backref='reader', lazy=True)
    order=db.relationship('Order', backref='buyer', lazy=True)
    orderbook=db.relationship('OrderBook', backref='orderby', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"
        
        
class Admin(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"Admin('{self.email}')"
        

class Book(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    publication = db.Column(db.String(100), nullable=False)
    ISBN = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    piece=db.Column(db.Integer, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    cart=db.relationship('Cart', backref='cartbook', lazy=True)
    orderbook=db.relationship('OrderBook', backref='orderbook', lazy=True)

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', '{self.publication}', '{self.ISBN}', '{self.price}', '{self.image_file}')"
        

class Cart(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    

    def __repr__(self):
        return f"Cart('{self.id}', '{self.user_id}', '{self.book_id}')" 


class Order(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    order_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    orderbook=db.relationship('OrderBook', backref='orderdetail', lazy=True)
    

    def __repr__(self):
        return f"Order('{self.id}', '{self.user_id}','{self.amount}','{self.order_date}')" 


class OrderBook(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    order_id= db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    

    def __repr__(self):
        return f"OrderBook('{self.id}', '{self.user_id}','{self.book_id}','{self.order_id}')"        