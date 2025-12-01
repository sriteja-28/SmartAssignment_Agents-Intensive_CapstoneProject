# smart-assignment-helper

## 1. Create and activate virtual environment

Open VS Code terminal in your project folder (E:\smart-assignment-helper) and run:

## create virtual environment
python -m venv studenthelper_ai

## activate venv
studenthelper_ai\Scripts\activate


Your prompt should now show (studenthelper_ai)

This isolates packages for this project.

## 2. Create requirements.txt

Save this file in the project root:

openai>=1.0.0
faiss-cpu
numpy
scipy
PyPDF2
tqdm


Add any other libraries your project uses.

## 3. Install dependencies
pip install --upgrade pip
pip install -r requirements.txt


This installs all libraries in your virtual environment.

## 4. Set OpenAI API key (optional)

Windows PowerShell:

<!-- $env:OPENAI_API_KEY="sk-your_api_key_here" -->


Make sure no newline or extra space at the end.

To make permanent, add as User Environment Variable in Windows settings.

## 5. Run the CLI demo
python -m app.main --demo


Upload a PDF

Ask questions

Memory storage works

If no API key or quota exceeded → simulated answers.

## 6. Test memory and indexing

You can run multiple PDFs to check FAISS indexing.

Use store fact prompts to verify SQLite memory bank.

## 7. Initialize Git & push to GitHub
## initialize git repo
git init

## add files
git add .

## commit
git commit -m "Initial commit - Smart Assignment Helper"

## create a repo on GitHub (e.g., smart-assignment-helper)
# copy HTTPS URL from GitHub

## add remote
git remote add origin https://github.com/<your-username>/smart-assignment-helper.git

## push
git branch -M main
git push -u origin main