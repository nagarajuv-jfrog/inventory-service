# backend.py
from flask import Flask, jsonify
from flask_cors import CORS

# Initialize the Flask application
app = Flask(__name__)
# Enable Cross-Origin Resource Sharing (CORS) to allow the frontend to make requests
CORS(app)

# In-memory data store for our books. In a real application, this would be a database.
books = [
    { "id": 1, "title": "To Kill a Mockingbird", "author": "Harper Lee", "description": "A classic of modern American literature.", "stock": 5, "price": 12.99, "image": "https://placehold.co/300x450/a3bfb8/ffffff?text=To+Kill+a+Mockingbird" },
    { "id": 2, "title": "1984", "author": "George Orwell", "description": "A dystopian novel set in a totalitarian society.", "stock": 8, "price": 10.99, "image": "https://placehold.co/300x450/f0a3a3/ffffff?text=1984" },
    { "id": 3, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "description": "A story of the fabulously wealthy Jay Gatsby.", "stock": 3, "price": 9.99, "image": "https://placehold.co/300x450/f7e1a3/ffffff?text=The+Great+Gatsby" },
    { "id": 4, "title": "The Hobbit", "author": "J.R.R. Tolkien", "description": "A fantasy novel and prelude to The Lord of the Rings.", "stock": 12, "price": 14.99, "image": "https://placehold.co/300x450/a3f7a3/ffffff?text=The+Hobbit" },
    { "id": 5, "title": "Fahrenheit 451", "author": "Ray Bradbury", "description": "A dystopian novel where books are outlawed.", "stock": 6, "price": 10.00, "image": "https://placehold.co/300x450/f7a3a3/ffffff?text=Fahrenheit+451" }
]

@app.route('/api/books', methods=['GET'])
def get_books():
    """
    API endpoint to get the list of all books.
    """
    return jsonify(books)

if __name__ == '__main__':
    # Run the app on port 5000, accessible from any network interface
    app.run(host='0.0.0.0', port=5000)