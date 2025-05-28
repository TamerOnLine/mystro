# logic/formatter.py

def format_text_to_html(text: str, mode='paragraph'):
    lines = [line.strip() for line in text.strip().splitlines() if line.strip()]

    if mode == 'paragraph':
        return ''.join(f"<p>{line}</p>" for line in lines)
    elif mode == 'list':
        return "<ul>" + ''.join(f"<li>{line}</li>" for line in lines) + "</ul>"
    
    return text
