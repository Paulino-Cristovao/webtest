### README.md
```markdown
# Embassy of Mozambique Website

This Django project implements a multi-language, media-rich website for the Embassy of Mozambique with:

- **Home page** with hero banner & navigation
- **Visa Service**, **Passport Service**, and **Consular Assistance** pages
- PDF downloads for forms
- AI-powered chatbot endpoint
- Tailwind CSS for styling

## Setup & Run (macOS)

1. **Install Homebrew & Python 3** (if needed):
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   brew install python
   ```
2. **Clone & enter project**:
   ```bash
   git clone git@github.com:your-user/moz-embassy.git
   cd moz-embassy
   ```
3. **Create & activate venv**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
5. **Run migrations & start dev server**:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```
6. **Open** `http://127.0.0.1:8000` in your browser.
```
