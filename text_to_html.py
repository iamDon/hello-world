#!/usr/bin/env python3
"""
Simple Python script that takes text input and generates an HTML file.
"""

def create_html_file(text_content, output_filename="output.html"):
    """
    Creates an HTML file with the provided text content.

    Args:
        text_content: The text to include in the HTML file
        output_filename: Name of the output HTML file (default: output.html)
    """
    html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Generated HTML</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
            background-color: #f5f5f5;
        }}
        .content-box {{
            background-color: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        h1 {{
            color: #333;
            border-bottom: 2px solid #007bff;
            padding-bottom: 10px;
        }}
        .text-content {{
            line-height: 1.6;
            color: #555;
            white-space: pre-wrap;
        }}
    </style>
</head>
<body>
    <div class="content-box">
        <h1>Your Text Content</h1>
        <div class="text-content">
{text_content}
        </div>
    </div>
</body>
</html>"""

    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write(html_template)

    print(f"\nHTML file created successfully: {output_filename}")
    print(f"You can open it in your web browser to view the content.")


def main():
    """Main function to run the script."""
    print("=" * 50)
    print("Text to HTML Converter")
    print("=" * 50)
    print("\nEnter your text below (press Enter, then Ctrl+D on Unix/Linux/Mac")
    print("or Ctrl+Z on Windows when finished):\n")

    try:
        # Read multiple lines of input
        lines = []
        while True:
            try:
                line = input()
                lines.append(line)
            except EOFError:
                break

        text_content = '\n'.join(lines)

        if not text_content.strip():
            print("\nNo text entered. Exiting.")
            return

        # Ask for filename
        print("\n" + "=" * 50)
        filename = input("Enter output filename (default: output.html): ").strip()
        if not filename:
            filename = "output.html"
        elif not filename.endswith('.html'):
            filename += '.html'

        # Create the HTML file
        create_html_file(text_content, filename)

    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user.")


if __name__ == "__main__":
    main()
