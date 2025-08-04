# 🔎 Decoder-Image-Generator

⭐ **Decoder Image Generator** is a simple [Streamlit](https://streamlit.io/) web app that allows you to create hidden-text *decoder images*. More specifically, these are special images where secret messages are embedded using a red-noise overlay and can only be revealed when viewed through red decoder glasses.


## 🛠️ Project Setup

This project uses **Poetry** for dependency management.

### 🚀 Steps to Set Up

1. 📦 **Install Poetry** (if not already installed):
   ```bash
    pip install poetry
   ```
   For more installation options, refer to [Poetry’s documentation](https://python-poetry.org/docs/).

2. 📥 **Install dependencies:** Navigate to the project directory and install the required packages:
    ```bash
   poetry install
   ```

3. 🪄 **Activate the environment:**
    ```bash
   poetry env activate
   ```

4. 🪝 **Set up pre-commit hooks:** This repository uses pre-commit hooks to ensure code quality. Install them by running:
    ```bash
   pre-commit install
   ```

## ▶️ Running the Web App

After completing the setup steps, you can start the Streamlit app with:

```bash
poetry run streamlit run app.py
```

## 📃 Repository Structure

- `.gitignore`: Specifies files and directories to be ignored by Git.
- `.pre-commit-config.yaml`: Configuration for pre-commit hooks to ensure code quality.
- `poetry.lock` and `pyproject.toml`: Poetry files for dependency management.
- `README.md`: Project documentation.
- `generator.py`: Contains functionality for generating decoder images.
- `app.py`: Contains simple Streamlit App.
