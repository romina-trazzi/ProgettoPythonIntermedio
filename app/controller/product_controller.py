from app.models.product import Product
from app.utilis.database import db

class ProductController:
    def get_all_products(self, session):
        products = session.query(Product).all()
        return [self.serialize_product(p) for p in products]

    def get_product_by_id(self, product_id, session):
        product = session.query(Product).filter_by(id=product_id).first()
        return self.serialize_product(product) if product else {}

    def create_product(self, product_data, session):
        product = Product(
            name=product_data.get('name'),
            description=product_data.get('description'),
            price=product_data.get('price')
        )
        session.add(product)
        session.commit()
        return self.serialize_product(product)

    def serialize_product(self, product):
        if not product:
            return {}
        return {
            "id": product.id,
            "name": product.name,
            "description": product.description,
            "price": product.price
        }