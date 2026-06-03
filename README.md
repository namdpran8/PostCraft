# PostCraft

Lightweight Streamlit app for generating social media posts (LinkedIn, etc.) using prompt templates and simple AI integration.

## Features
- Streamlit UI for entering inputs and generating posts
- Prompt-building helpers in `prompt_builder.py`
- Sample LinkedIn prompt in `LINKDIN_POST_ai.txt`

## Requirements
Install dependencies from `requirements.txt` (recommended inside a virtual environment).

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1   # PowerShell (Windows)
pip install -r requirements.txt
```

## Run
Start the Streamlit app:

```bash
streamlit run app.py
```

## Deploy on Streamlit Cloud
1. Push this repository to GitHub.
2. Create a new app in Streamlit Community Cloud and select this repo.
3. Set the main file path to `app.py`.
4. Add a secret named `GEMINI_API_KEY` in the app settings.
5. Deploy.

The app reads the Gemini key from Streamlit secrets first, then falls back to a local `.env` file for development.

## Development notes
- Main entry: `app.py`
- Helper modules: `prompt_builder.py`, `components.py`, `user_inputs.py`
- Ignore sensitive files: see `.gitignore`

## Contributing
Open an issue or submit a PR. Keep changes small and focused.

