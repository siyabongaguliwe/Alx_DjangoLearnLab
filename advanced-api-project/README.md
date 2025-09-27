## API Views Overview

- `GET /api/books/` — List all books.
- `GET /api/books/<id>/` — Retrieve a specific book.
- `POST /api/books/create/` — Create a new book (auth required).
- `PUT /api/books/<id>/update/` — Update a book (auth required).
- `DELETE /api/books/<id>/delete/` — Delete a book (auth required).

### Permissions
- Read-only access for unauthenticated users.
- Write access restricted to authenticated users.

### Custom Behavior
- Validation prevents future publication years.
- Views use DRF generic classes for clean, efficient logic.
