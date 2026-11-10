# Leaf & Loan — Community Book Exchange

**Leaf & Loan** is a full-stack web application built with **Python (Flask)** and **SQLite** that enables communities to share, discover, and exchange physical books. Designed with a warm editorial aesthetic, it allows readers to list books from their personal shelves, browse available titles by category or keyword, and coordinate book swaps through a built-in request management system.

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Key Features](#key-features)
3. [Tech Stack & Architecture](#tech-stack--architecture)
4. [Project Structure](#project-structure)
5. [Database Schema](#database-schema)
6. [How to Run in VS Code (Step-by-Step)](#how-to-run-in-vs-code-step-by-step)
7. [Demo Accounts & Testing](#demo-accounts--testing)
8. [Troubleshooting](#troubleshooting)

---

## Project Overview
Many readers have finished books sitting on their shelves while others in their neighborhood are looking for those exact titles. **Leaf & Loan** solves this by providing a centralized community shelf where:
- **Book Owners** can list books, specify their physical condition (`Like new`, `Good`, `Acceptable`), edit details, or temporarily hide listings.
- **Readers** can search the catalog, filter by genre/category, and send an exchange request with a personalized note.
- **Direct Coordination** happens safely: a book owner's or requester's email address is only revealed once an exchange request is **Accepted**.

---

## Key Features
- **Instant Auto-Seeded Catalog:** Automatically creates `books.db` and populates 6 starter books and 2 community demo accounts on first launch so the shelf is immediately interactive.
- **Search & Category Filtering:** Real-time SQLite filtering across book titles, authors, descriptions, and 9 distinct categories (`Fiction`, `Non-fiction`, `Education`, `Science`, `Technology`, `History`, `Biography`, `Children`, `Other`).
- **Complete User Authentication:** Secure account registration and login powered by Werkzeug password hashing (`scrypt`/`pbkdf2`) and HTTP-only session cookies.
- **Personal Shelf Management (`My Shelf`):** View all your listed books, see live pending request counts per book, edit metadata, or toggle availability (`Hide` / `Relist`) with a single click.
- **Two-Way Exchange Workflow:**
  - **Incoming Requests:** Review notes from interested readers and click **Accept** or **Decline**. Accepting a request automatically marks the book as unavailable and declines competing pending requests.
  - **Outgoing Requests:** Track the status (`Pending`, `Accepted`, `Declined`) of books you have requested from other members.
- **Security & Performance:**
  - Custom **CSRF token verification** on every `POST` request.
  - **SQLite WAL (Write-Ahead Logging)** mode enabled for concurrent read/write performance.
  - **Per-request database connection pooling** via Flask's `g` context and indexed foreign keys.

---

## Tech Stack & Architecture
| Layer | Technology | Purpose |
| :--- | :--- | :--- |
| **Backend** | Python 3.8+, Flask 3.x | Routing, session management, CSRF protection, business logic |
| **Database** | SQLite 3 (WAL mode) | Relational storage for users, books, and exchange requests |
| **Frontend** | HTML5, Jinja2 Templates | Server-side rendered views with template inheritance |
| **Styling** | Custom CSS3 (`style.css`) | Responsive grid layout, custom CSS book illustrations, mobile-ready |
| **Security** | Werkzeug Security, `secrets` | Password hashing, cryptographically strong CSRF tokens |

---

## Project Structure

```text
book_exchange/
├── app.py                  # Main Flask application, routes, DB init & auto-seeder
├── books.db                # SQLite database (auto-generated on first run)
├── requirements.txt        # Python package dependencies
├── README.md               # Project documentation and setup guide
├── static/
│   └── style.css           # Global stylesheet and responsive layout rules
└── templates/
    ├── base.html           # Base layout (navbar, flash messages, footer)
    ├── index.html          # Explore shelf, My Shelf, Auth forms, and Error views
    ├── add_book.html       # Create & Edit book listing form
    └── requests.html       # Incoming and Outgoing exchange request dashboard