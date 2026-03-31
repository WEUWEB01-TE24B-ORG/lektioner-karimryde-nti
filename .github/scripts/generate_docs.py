import os
import subprocess
import json
import datetime
from google import genai

# Konfigurera Gemini
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    print("Inget GEMINI_API_KEY hittades. Avbryter.")
    exit(1)

# Vi använder -preview eftersom modellen ofta kräver det i mars 2026
DEFAULT_MODEL = "gemini-3.1-flash-preview"
MODEL = os.getenv("GEMINI_MODEL", DEFAULT_MODEL)

client = genai.Client(api_key=GEMINI_API_KEY)

def get_git_info():
    """Hämtar information om senaste ändringar med felhantering."""
    try:
        commit_msg = subprocess.check_output(['git', 'log', '-1', '--pretty=%B']).decode('utf-8').strip()
        # Hämtar diff mellan de två senaste commitarna
        diff = subprocess.check_output(['git', 'diff', 'HEAD~1', 'HEAD']).decode('utf-8', errors='ignore')
        files_changed = subprocess.check_output(['git', 'diff', '--name-only', 'HEAD~1', 'HEAD']).decode('utf-8').splitlines()
        
        folders = set()
        for f in files_changed:
            if '/' in f and not f.startswith('.github'):
                folders.add(os.path.dirname(f))
                
        return commit_msg, diff, list(folders)
    except subprocess.CalledProcessError as e:
        print(f"Kunde inte hämta git-info (kanske första committen?): {e}")
        return "Initial commit", "", []

def read_file(path):
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    return ""

def write_file(path, content):
    os.makedirs(os.path.dirname(path) if os.path.dirname(path) else '.', exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    commit_msg, diff, folders = get_git_info()
    
    if not diff and not folders:
        print("Inga relevanta ändringar upptäcktes.")
        return

    history_content = read_file('history.md')
    today = datetime.datetime.now().strftime("%Y-%m-%d")

    prompt = f"""
    Du är en pedagogisk assistent för en gymnasielärare i webbutveckling.
    Skapa dokumentation baserat på dessa ändringar.
    
    Datum: {today}
    Commit: {commit_msg}
    Diff: {diff}
    Nuvarande historik: {history_content}

    Returnera ett JSON-objekt med:
    1. "dagbok_updates": Array med {{"folder": "namn", "content": "markdown-text"}}.
    2. "history_update": Sträng med hela den nya versionen av history.md.
    """

    print(f"Anropar {MODEL} med JSON-mode...")
    
    # JSON-mode aktiveras här via config
    response = client.models.generate_content(
        model=MODEL,
        contents=prompt,
        config={
            'response_mime_type': 'application/json',
            'temperature': 0.2, # Lägre temperatur för stabilare JSON
        }
    )

    try:
        # Tack vare JSON-mode kan vi ladda response.text direkt
        data = json.loads(response.text)
        
        # Spara dagböcker
        for update in data.get("dagbok_updates", []):
            folder = update.get("folder")
            dagbok_path = os.path.join(folder, 'dagbok.md')
            write_file(dagbok_path, update.get("content"))
            print(f"✅ Uppdaterade {dagbok_path}")

        # Spara history.md
        if data.get("history_update"):
            write_file("history.md", data.get("history_update"))
            print("✅ Uppdaterade history.md")

    except json.JSONDecodeError:
        print("❌ Fel: Gemini returnerade ogiltig JSON.")
        print("Svar:", response.text)

if __name__ == "__main__":
    main()
