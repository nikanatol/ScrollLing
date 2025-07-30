# ScrollLing

**ScrollLing** is an interactive PWA designed to make learning foreign languages engaging and fun through a dynamic, scroll-based interface.

## About The Project

The core idea behind ScrollLing is to transform the routine task of memorizing vocabulary into a fast-paced, addictive game. Instead of static flashcards, users interact with a dynamic feed or a "wheel of fortune," scrolling through words, discovering associations, and building phrases.

### Key Features

*   **Interactive Word Feed:** An endless stream of words with translations and visual cues.
*   **Part-of-Speech Spinner:** Swap words within a sentence with synonyms or other words of the same type (nouns, verbs, etc.) and see the result instantly.
*   **Image Associations:** Each word is paired with an image to enhance memory retention.
*   **Adaptive PWA:** A fully responsive app that works on any device and can be installed on the home screen.

## Built With

*   **Backend:** Python, Flask, uWSGI
*   **Frontend:** HTML, CSS, JavaScript, Bootstrap 5
*   **Architecture:** Progressive Web App (PWA)

## Getting Started

To get a local copy up and running, follow these simple steps.

1.  **Clone the repo:**
    ```
    git clone https://github.com/your_username/scrollling-app.git
    cd scrollling-app
    ```
2.  **Create and activate a virtual environment:**
    ```
    python3 -m venv venv
    source venv/bin/activate
    ```
3.  **Install dependencies:**
    ```
    pip install -r requirements.txt
    ```
4.  **Run the app with uWSGI:**
    ```
    uwsgi --ini uwsgi.ini
    ```
    The application will be available at `http://localhost:1234`.

## Roadmap

1.  ✅ **Stage 1:** Basic uWSGI + PWA Bootstrap boilerplate.
2.  ▶️ **Stage 2:** Add image-based translations for words.
3.  🔲 **Stage 3:** Implement the "word spinner" logic with JavaScript.
4.  🔲 **Future Ideas:** Multi-language support, user profiles, learning statistics.

## License

Distributed under the MIT License. See `LICENSE` for more information.
