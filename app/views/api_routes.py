from flask import Blueprint, request, jsonify, current_app
from app.utilis.database import db
from app.models.user import User
from app.controller.user_controller import UserController
from app.controller.product_controller import ProductController
from app.controller.sentiment_controller import SentimentController
from app.controller.recommendation_controller import RecommendationController
from app.controller.data_analysis_controller import DataAnalysisController
user_ctrl = UserController()
product_ctrl = ProductController()
sentiment_ctrl = SentimentController()
recommendation_ctrl = RecommendationController()
data_analysis_ctrl = DataAnalysisController()

api_bp = Blueprint('api_bp', __name__, url_prefix='/api')

# --- Rotte per gli Utenti ---
@api_bp.route('/users/register', methods=['POST'])
def register():
    user_data = request.get_json()
    user = user_ctrl.register_user(user_data, db.session)
    return jsonify(user), 201

@api_bp.route('/users/token', methods=['POST'])
def login_for_access_token():
    data = request.form or request.get_json()
    username = data.get('username')
    password = data.get('password')
    user = user_ctrl.authenticate_user(username, password, db.session)
    if not user:
        return jsonify({"detail": "Credenziali non valide"}), 401
    access_token = user_ctrl.create_access_token(data={"sub": user.username})
    return jsonify({"access_token": access_token, "token_type": "bearer"})

@api_bp.route('/users/me', methods=['GET'])
def read_users_me():
    # Implementa la logica per ottenere l'utente corrente (ad esempio tramite JWT)
    current_user = user_ctrl.get_current_user()
    return jsonify(current_user)

# --- Rotte per i Prodotti ---
@api_bp.route('/products/', methods=['GET'])
def get_products():
    products = product_ctrl.get_all_products(db.session)
    return jsonify(products)

@api_bp.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = product_ctrl.get_product_by_id(product_id, db.session)
    return jsonify(product)

@api_bp.route('/products/', methods=['POST'])
def create_product():
    product_data = request.get_json()
    # Implementa la logica per autenticazione utente se necessario
    product = product_ctrl.create_product(product_data, db.session)
    return jsonify(product), 201

# --- Rotte per le Recensioni ---
@api_bp.route('/reviews/', methods=['POST'])
def add_product_review():
    review_data = request.get_json()
    # Implementa la logica per autenticazione utente se necessario
    review = sentiment_ctrl.add_review(review_data, None, db.session)
    return jsonify(review), 201

@api_bp.route('/products/<int:product_id>/reviews', methods=['GET'])
def get_reviews_for_product_nested(product_id):
    reviews = sentiment_ctrl.get_reviews_for_product(product_id, db.session)
    return jsonify(reviews)

# --- Rotte per le Raccomandazioni ---
@api_bp.route('/recommendations/me', methods=['GET'])
def get_my_recommendations():
    # Implementa la logica per autenticazione utente se necessario
    recommendations = recommendation_ctrl.get_user_recommendations(None, db.session)
    return jsonify(recommendations)

# --- Rotte per l'Analisi Dati ---
@api_bp.route('/data/random-numbers-and-average', methods=['GET'])
def get_random_data():
    result = data_analysis_ctrl.get_random_numbers_and_average()
    return jsonify(result)