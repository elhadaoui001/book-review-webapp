# 📚 Book Review Web Application

A web application that allows users to register, submit reviews for books, and browse reviews by others. This project demonstrates full-stack development skills, including backend API creation, database design, and frontend integration.

## 🚀 Tech Stack
- **Backend:** Django + Django REST Framework
- **Frontend:** Bootstrap + JavaScript
- **Database:** PostgreSQL
- **API Integration:** Google Books API

## 🗂️ Features
- User registration and login
- Submit and view book reviews
- Like and comment on reviews
- Search and filter books by title, author, or genre
- User profile page showing activity and reviews

## 📊 Database Design
The Entity Relationship Diagram (ERD) is located in the `/docs` folder:
- `docs/ERD.png`

### Entities:
- **User:** username, email, password, profile_image, created_at
- **Book:** title, author, ISBN, cover_image, genre
- **Review:** book_id, user_id, rating, comment, created_at, likes_count
- **Comment:** review_id, user_id, comment_text, created_at
- **Like:** review_id, user_id, created_at

## 📡 API Endpoints
A detailed list of all backend endpoints is available in:
- `docs/api_endpoints.md`

### Example Endpoints
**User Endpoints**
- `POST /api/users/register` – Register a new user
- `POST /api/users/login` – Authenticate and log in a user
- `GET /api/users/:id` – Get user profile
- `GET /api/users/:id/reviews` – Get all reviews by a user

**Book Endpoints**
- `POST /api/books` – Add a new book (manual or via Google Books API)
- `GET /api/books` – List all books with search/filter options
- `GET /api/books/:id` – Get book details
- `GET /api/books/:id/reviews` – Get all reviews for a book

**Review Endpoints**
- `POST /api/reviews` – Submit a review
- `GET /api/reviews/:id` – Get review details
- `PUT /api/reviews/:id` – Update a review (author only)
- `DELETE /api/reviews/:id` – Delete a review (author only)
- `POST /api/reviews/:id/like` – Like a review
- `DELETE /api/reviews/:id/like` – Remove a like

**Comment Endpoints**
- `POST /api/comments` – Submit a comment
- `GET /api/reviews/:id/comments` – Get all comments for a review
- `DELETE /api/comments/:id` – Delete a comment (author only)

## 🧠 Setup Instructions
```bash
# Clone the repository
git clone https://github.com/elhadaoui001/book-review-webapp.git
cd book-review-webapp

# Create virtual environment and install dependencies
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
pip install -r backend/requirements.txt

# Apply migrations and start the server
cd backend
python manage.py migrate
python manage.py runserver

# Frontend
# Open frontend/index.html in your browser
