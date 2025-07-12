from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# In-memory data store for our books. In a real application, this would be a database.
books = [
    { "id": 1, "title": "To Kill a Mockingbird", "author": "Harper Lee", "description": "A classic of modern American literature.", "stock": 5, "price": 12.99, "image": "https://placehold.co/300x450/a3bfb8/ffffff?text=To+Kill+a+Mockingbird" },
    { "id": 2, "title": "1984", "author": "George Orwell", "description": "A dystopian novel set in a totalitarian society.", "stock": 8, "price": 10.99, "image": "https://placehold.co/300x450/f0a3a3/ffffff?text=1984" },
    { "id": 3, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "description": "A story of the fabulously wealthy Jay Gatsby.", "stock": 3, "price": 9.99, "image": "https://placehold.co/300x450/f7e1a3/ffffff?text=The+Great+Gatsby" },
    { "id": 4, "title": "The Hobbit", "author": "J.R.R. Tolkien", "description": "A fantasy novel and prelude to The Lord of the Rings.", "stock": 12, "price": 14.99, "image": "https://placehold.co/300x450/a3f7a3/ffffff?text=The+Hobbit" },
    { "id": 5, "title": "Fahrenheit 451", "author": "Ray Bradbury", "description": "A dystopian novel where books are outlawed.", "stock": 6, "price": 10.00, "image": "https://placehold.co/300x450/f7a3a3/ffffff?text=Fahrenheit+451" },
    { "id": 6, "title": "Pride and Prejudice", "author": "Jane Austen", "description": "A romantic novel of manners written in 1813.", "stock": 10, "price": 8.99, "image": "https://placehold.co/300x450/d3a3f7/ffffff?text=Pride+and+Prejudice" },
    { "id": 7, "title": "The Catcher in the Rye", "author": "J.D. Salinger", "description": "A story about adolescent alienation and loss of innocence.", "stock": 2, "price": 11.50, "image": "https://placehold.co/300x450/a3a3f7/ffffff?text=The+Catcher+in+the+Rye" },
    { "id": 8, "title": "The Lord of the Rings", "author": "J.R.R. Tolkien", "description": "An epic high-fantasy novel and the sequel to The Hobbit.", "stock": 7, "price": 25.00, "image": "https://placehold.co/300x450/b0f0b0/ffffff?text=Lord+of+the+Rings" },
    { "id": 9, "title": "Brave New World", "author": "Aldous Huxley", "description": "A dystopian novel about a future World State.", "stock": 5, "price": 11.99, "image": "https://placehold.co/300x450/f0b0f0/ffffff?text=Brave+New+World" },
    { "id": 10, "title": "Moby Dick", "author": "Herman Melville", "description": "The saga of Captain Ahab and his obsession with a giant whale.", "stock": 4, "price": 13.50, "image": "https://placehold.co/300x450/a3c2f7/ffffff?text=Moby+Dick" },
    { "id": 11, "title": "War and Peace", "author": "Leo Tolstoy", "description": "An epic novel that intertwines the lives of private and public individuals.", "stock": 3, "price": 18.99, "image": "https://placehold.co/300x450/e0e0e0/ffffff?text=War+and+Peace" },
    { "id": 12, "title": "Don Quixote", "author": "Miguel de Cervantes", "description": "A Spanish novel about a nobleman who loses his sanity.", "stock": 1, "price": 15.00, "image": "https://placehold.co/300x450/f0e0b0/ffffff?text=Don+Quixote" },
    { "id": 13, "title": "The Odyssey", "author": "Homer", "description": "An ancient Greek epic poem that is a sequel to the Iliad.", "stock": 9, "price": 14.00, "image": "https://placehold.co/300x450/f7c4a3/ffffff?text=The+Odyssey" },
    { "id": 14, "title": "Crime and Punishment", "author": "Fyodor Dostoevsky", "description": "A novel about the mental anguish and moral dilemmas of a poor ex-student.", "stock": 6, "price": 12.50, "image": "https://placehold.co/300x450/c4a3f7/ffffff?text=Crime+and+Punishment" },
    { "id": 15, "title": "Alice's Adventures in Wonderland", "author": "Lewis Carroll", "description": "A young girl falls through a rabbit hole into a fantasy world.", "stock": 15, "price": 9.50, "image": "https://placehold.co/300x450/a3f7c4/ffffff?text=Alice+in+Wonderland" },
    { "id": 16, "title": "Frankenstein", "author": "Mary Shelley", "description": "A young science student creates a sapient creature in an unorthodox experiment.", "stock": 5, "price": 10.75, "image": "https://placehold.co/300x450/c4c4c4/ffffff?text=Frankenstein" },
    { "id": 17, "title": "The Picture of Dorian Gray", "author": "Oscar Wilde", "description": "A novel about a man whose portrait ages while he stays young.", "stock": 4, "price": 11.00, "image": "https://placehold.co/300x450/e0b0e0/ffffff?text=Dorian+Gray" },
    { "id": 18, "title": "Dune", "author": "Frank Herbert", "description": "A science fiction novel set in a distant future amidst a feudal interstellar society.", "stock": 11, "price": 16.50, "image": "https://placehold.co/300x450/d2b48c/ffffff?text=Dune" },
    { "id": 19, "title": "One Hundred Years of Solitude", "author": "Gabriel Garcia Marquez", "description": "A landmark 1967 novel that tells the multi-generational story of the Buendía family.", "stock": 3, "price": 13.00, "image": "https://placehold.co/300x450/ffd700/ffffff?text=One+Hundred+Years" },
    { "id": 20, "title": "The Alchemist", "author": "Paulo Coelho", "description": "An allegorical novel about a young Andalusian shepherd in his journey to the pyramids of Egypt.", "stock": 20, "price": 12.00, "image": "https://placehold.co/300x450/ffc0cb/ffffff?text=The+Alchemist" }
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
