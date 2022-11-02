from saleapp.models import Category, Product
from saleapp import  db, app
from flask_admin import  Admin, BaseView
from flask_admin.contrib.sqla import ModelView

class ProductView (ModelView):
    column_searchable_list = ['name', 'description']
    column_filters = ['name', 'price']
    can_view_details = True
    can_export = True
    column_export_list = ['image']
    column_labels = {
        'name': 'Tên sản phẩm',
        'description': 'Mô tả',
        'price': 'Giá'
    }

class StatsView (BaseView):
    @expose('/')
    def index(self):
        return  self.render("admin/stats.html")

admin = Admin (app=app, name="Quản trị Shopee", template_mode="bootstrap4")
admin.add_view(ModelView(Category, db.session))
admin.add_view(ModelView(Product, db.session))