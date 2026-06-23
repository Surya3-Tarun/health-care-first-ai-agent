from pathlib import Path
import re

SECRET_PATTERNS = [
   r"GROQ_API_KEY=YOUR_API_KEY"
]
REPLACEMENT = "GROQ_API_KEY=your_key_here"

root = Path('.')
for env_file in [".env", ".env.local", ".env.production", ".env.development"]:
    path = root / env_file
    if path.exists():
        path.unlink()

for file_name in [".env.example", "DEBUG_FIXES.md"]:
    path = root / file_name
    if path.exists():
        text = path.read_text(encoding='utf-8')
        new_text = text
        for pattern in SECRET_PATTERNS:
            new_text = re.sub(re.escape(pattern), REPLACEMENT, new_text)
        if new_text != text:
            path.write_text(new_text, encoding='utf-8')
