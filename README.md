# Django Blog Application

This is a feature-rich blog application built with the Django framework and PostgreSQL. It includes a complete set of functionalities for creating, managing, and sharing blog content.

## Features Implemented

### Core Blog Functionality
- **Post Management**: Full CRUD (Create, Read, Update, Delete) capabilities for blog posts through the Django admin interface.
- **Draft & Published Status**: Posts can be saved as drafts or published to be publicly visible. A custom model manager provides easy access to published posts only.
- **SEO-Friendly URLs**: Post detail URLs are structured with the publication date and a unique slug (e.g., `/2025/12/29/my-post-title/`) for better search engine optimization.
- **Markdown Support**: Post bodies are written in Markdown and are converted to HTML for display using a custom template filter.

### Content Organization & Discovery
- **Tagging System**: Posts can be categorized with multiple tags using `django-taggit`. Users can browse all posts associated with a specific tag.
- **Full-Text Search**: Integrated PostgreSQL's full-text search capabilities to allow users to search for posts based on keywords in the title and body.
- **Similar Posts**: The post detail page displays a list of similar posts based on shared tags.

### User Interaction
- **Commenting System**: Users can leave comments on individual posts. Comments can be moderated (activated/deactivated) through the admin panel.
- **Share Posts by Email**: A built-in feature allows users to share interesting posts with others via email.

### Custom Template Tags & Reusability
The application includes several custom template tags to display dynamic content across the site:
- `{% total_posts %}`: Shows the total number of published posts.
- `{% show_latest_posts %}`: Renders a list of the most recent posts.
- `{% get_most_commented_posts %}`: Displays a list of the most popular posts based on comment count.

### SEO & Content Syndication
- **Dynamic Sitemap**: A `sitemap.xml` is automatically generated to help search engines discover and index the site's content.
- **RSS Feed**: An RSS feed (`/blog/feed/`) is available for users to subscribe to the latest posts.

### Configuration & Administration
- **Secure Configuration**: Sensitive information like the `SECRET_KEY` and database credentials are kept out of version control using `python-decouple` and a `.env` file.
- **Enhanced Admin Interface**: The Django admin is customized for the `Post` and `Comment` models to provide a more efficient management experience, including filters, search fields, and prepopulated slugs.

## Setup and Installation

1.  **Clone the repository:**
    ```sh
    git clone <your-repository-url>
    cd <repository-folder>
    ```

2.  **Create and activate a virtual environment:**
    ```sh
    python -m venv .venv
    source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4.  **Set up environment variables:**
    Create a `.env` file in the `mysite` directory and add your database credentials and a `SECRET_KEY`.

5.  **Run database migrations and start the server:**
    ```sh
    python manage.py migrate
    python manage.py runserver
    ```