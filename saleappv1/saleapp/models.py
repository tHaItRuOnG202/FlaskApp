from flask import Flask
from sqlalchemy import Column, Integer, String, Text, Float, Boolean, ForeignKey
from saleapp import app, db

class BaseModel(db.Model):
    __abstract__ = True
    id = Column(Integer, primary_key = True, autoincrement = True)

class Category(BaseModel):
    __tablename__ = 'category'
    name = Column(String(50), nullable = False)

class Product(BaseModel):
    __tablename__ = 'category'
    name = Column(String(50), nullable = False)
    description = Column(Text)
    price = Column(Float, default = 0)
    image = Column(String(100))
    active = Column(Boolean, default = True)
    category_id = Column(Integer, ForeignKey(Category.id), nullable = False)

if __name__ == '__main__':
    with app.app_context():
        # c1 = Category(name = 'Điện thoại')
        # c2 = Category(name = 'Máy tính bảng')
        # c3 = Category(name = 'Máy tính bàn')
        #
        # db.session.add_all([c1, c2, c3])

        p1 = Product (name = "Iphone 13 Promax", desciption = "Apple A12, 1TB", price = 25000000, image = 'https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729569/fi9v6vdljyfmiltegh7k.jpg', category_id = 1)
        p2 = Product (name = "Iphone 13 Promax", desciption = "Apple A12, 1TB", price = 25000000, image = 'https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729569/fi9v6vdljyfmiltegh7k.jpg', category_id = 1)
        p3 = Product (name = "Iphone 13 Promax", desciption = "Apple A12, 1TB", price = 25000000, image = 'https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729569/fi9v6vdljyfmiltegh7k.jpg', category_id = 1)
        p4 = Product (name = "Iphone 13 Promax", desciption = "Apple A12, 1TB", price = 25000000, image = 'https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729569/fi9v6vdljyfmiltegh7k.jpg', category_id = 1)
        p5 = Product (name = "Iphone 13 Promax", desciption = "Apple A12, 1TB", price = 25000000, image = 'https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729569/fi9v6vdljyfmiltegh7k.jpg', category_id = 1)
        db.session.commit()
        db.create_all()
