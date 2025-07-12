from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# In-memory data store for our books. In a real application, this would be a database.
books = [
    { "id": 1, "title": "To Kill a Mockingbird", "author": "Harper Lee", "description": "A classic of modern American literature.", "stock": 5, "price": 12.99, "image": "https://upload.wikimedia.org/wikipedia/commons/4/4f/To_Kill_a_Mockingbird_%28first_edition_cover%29.jpg" },
    { "id": 2, "title": "Neuromancer", "author": "William Gibson", "description": "The definitive cyberpunk novel, a story of a washed-up computer hacker.", "stock": 8, "price": 11.99, "image": "https://upload.wikimedia.org/wikipedia/en/4/4b/Neuromancer_%28Book%29.jpg" },
    { "id": 3, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "description": "A story of the fabulously wealthy Jay Gatsby.", "stock": 3, "price": 9.99, "image": "https://upload.wikimedia.org/wikipedia/commons/7/7a/The_Great_Gatsby_Cover_1925_Retouched.jpg" },
    { "id": 4, "title": "The Hobbit", "author": "J.R.R. Tolkien", "description": "A fantasy novel and prelude to The Lord of the Rings.", "stock": 12, "price": 14.99, "image": "https://upload.wikimedia.org/wikipedia/en/4/4a/TheHobbit_FirstEdition.jpg" },
    { "id": 5, "title": "Fahrenheit 451", "author": "Ray Bradbury", "description": "A dystopian novel where books are outlawed.", "stock": 6, "price": 10.00, "image": "https://upload.wikimedia.org/wikipedia/en/d/db/Fahrenheit_451_1st_ed_cover.jpg" },
    { "id": 6, "title": "Pride and Prejudice", "author": "Jane Austen", "description": "A romantic novel of manners written in 1813.", "stock": 10, "price": 8.99, "image": "https://upload.wikimedia.org/wikipedia/commons/1/17/PrideAndPrejudiceTitlePage.jpg" },
    { "id": 7, "title": "The Catcher in the Rye", "author": "J.D. Salinger", "description": "A story about adolescent alienation and loss of innocence.", "stock": 2, "price": 11.50, "image": "https://upload.wikimedia.org/wikipedia/commons/8/89/The_Catcher_in_the_Rye_%281951%2C_first_edition_cover%29.jpg" },
    { "id": 8, "title": "The Lord of the Rings", "author": "J.R.R. Tolkien", "description": "An epic high-fantasy novel and the sequel to The Hobbit.", "stock": 7, "price": 25.00, "image": "https://upload.wikimedia.org/wikipedia/en/e/e9/First_Single_Volume_Edition_of_The_Lord_of_the_Rings.gif" },
    { "id": 9, "title": "Brave New World", "author": "Aldous Huxley", "description": "A dystopian novel about a future World State.", "stock": 5, "price": 11.99, "image": "https://upload.wikimedia.org/wikipedia/en/6/62/BraveNewWorld_FirstEdition.jpg" },
    { "id": 10, "title": "Moby Dick", "author": "Herman Melville", "description": "The saga of Captain Ahab and his obsession with a giant whale.", "stock": 4, "price": 13.50, "image": "https://upload.wikimedia.org/wikipedia/commons/3/36/Moby-Dick_FE_title_page.jpg" },
    { "id": 11, "title": "War and Peace", "author": "Leo Tolstoy", "description": "An epic novel that intertwines the lives of private and public individuals.", "stock": 3, "price": 18.99, "image": "https://upload.wikimedia.org/wikipedia/commons/a/af/Tolstoy_-_War_and_Peace_-_first_edition%2C_1869.jpg" },
    { "id": 12, "title": "A Wizard of Earthsea", "author": "Ursula K. Le Guin", "description": "A fantasy novel about a young mage named Ged in the fictional archipelago of Earthsea.", "stock": 7, "price": 14.00, "image": "https://upload.wikimedia.org/wikipedia/en/b/b4/A_Wizard_of_Earthsea_%281968_edition%29.jpg" },
    { "id": 13, "title": "The Left Hand of Darkness", "author": "Ursula K. Le Guin", "description": "A science fiction novel set on the planet Gethen, whose inhabitants are ambisexual.", "stock": 6, "price": 13.50, "image": "https://upload.wikimedia.org/wikipedia/en/9/91/Lhanddark.jpg" },
    { "id": 14, "title": "Crime and Punishment", "author": "Fyodor Dostoevsky", "description": "A novel about the mental anguish and moral dilemmas of a poor ex-student.", "stock": 6, "price": 12.50, "image": "https://upload.wikimedia.org/wikipedia/en/4/4b/Crimeandpunishmentcover.png" },
    { "id": 15, "title": "The Hitchhiker's Guide to the Galaxy", "author": "Douglas Adams", "description": "A comedic science fiction series following the adventures of Arthur Dent.", "stock": 18, "price": 9.99, "image": "https://upload.wikimedia.org/wikipedia/en/b/bd/H2G2_UK_front_cover.jpg" },
    { "id": 16, "title": "Frankenstein", "author": "Mary Shelley", "description": "A young science student creates a sapient creature in an unorthodox experiment.", "stock": 5, "price": 10.75, "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f7/Frankenstein_1818_edition_title_page.jpg/800px-Frankenstein_1818_edition_title_page.jpg" },
    { "id": 17, "title": "Foundation", "author": "Isaac Asimov", "description": "A science fiction series about the fall of the Galactic Empire and the rise of a new one.", "stock": 9, "price": 15.50, "image": "https://upload.wikimedia.org/wikipedia/en/2/25/Foundation_gnome.jpg" },
    { "id": 18, "title": "Dune", "author": "Frank Herbert", "description": "A science fiction novel set in a distant future amidst a feudal interstellar society.", "stock": 11, "price": 16.50, "image": "https://upload.wikimedia.org/wikipedia/en/d/de/Dune-Frank_Herbert_%281965%29_First_edition.jpg" },
    { "id": 19, "title": "Hyperion", "author": "Dan Simmons", "description": "A science fiction novel, the first of four in the Hyperion Cantos.", "stock": 4, "price": 14.50, "image": "https://upload.wikimedia.org/wikipedia/en/7/73/Hyperion_cover.jpg" },
    { "id": 20, "title": "The Name of the Wind", "author": "Patrick Rothfuss", "description": "A fantasy novel, the first book in The Kingkiller Chronicle series.", "stock": 15, "price": 17.00, "image": "https://upload.wikimedia.org/wikipedia/en/5/56/TheNameoftheWind_cover.jpg" }
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
