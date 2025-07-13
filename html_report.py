# modules/html_report.py

import datetime

def generate_html_report(title, findings, output_file='report.html'):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    html_content = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            padding: 20px;
        }}
        h1 {{
            color: #333;
        }}
        .timestamp {{
            font-size: 0.9em;
            color: #777;
        }}
        ul {{
            background: #fff;
            padding: 15px;
            border-radius: 8px;
            box-shadow: 0 0 5px rgba(0,0,0,0.1);
        }}
        li {{
            margin-bottom: 10px;
        }}
    </style>
</head>
<body>
    <h1>{title}</h1>
    <p class="timestamp">Generated on: {timestamp}</p>
    <ul>
"""

    for finding in findings:
        html_content += f"        <li>{finding}</li>\n"

    html_content += """    </ul>
</body>
</html>"""

    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        print(f"[+] Report saved to {output_file}")
    except Exception as e:
        print(f"[!] Failed to write report: {e}")
