
POST_TEMPLATE = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title}</title>
        <style>
            :root {{
                --primary-color: #3498db;
                --secondary-color: #2c3e50;
                --background-color: #f8f9fa;
                --text-color: #333;
                --link-color: #2980b9;
                --border-color: #e0e0e0;
            }}
            body {{
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
                line-height: 1.8;
                color: var(--text-color);
                background-color: var(--background-color);
                max-width: 800px;
                margin: 0 auto;
                padding: 20px;
                font-size: 18px;
            }}
            a {{ 
                color: var(--link-color); 
                text-decoration: none; 
                transition: color 0.3s ease;
            }}
            a:hover {{ 
                color: var(--primary-color);
                text-decoration: underline; 
            }}
            h1, h2 {{ 
                margin-top: 1.5em;
                color: var(--secondary-color);
            }}
            header {{
                background-color: black;
                color: white;
                padding: 20px;
                border-radius: 5px;
                margin-bottom: 30px;
                box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            }}
            header h1 {{
                margin: 0;
                font-size: 2.5em;
                color: white;
            }}
            nav {{ 
                margin-top: 20px; 
                display: flex;
                justify-content: center;
            }}
            nav a {{ 
                margin: 0 15px;
                color: white;
                font-weight: bold;
                text-transform: uppercase;
                letter-spacing: 1px;
                font-size: 0.9em;
                position: relative;
            }}
            nav a::after {{
                content: '';
                position: absolute;
                width: 0;
                height: 2px;
                bottom: -5px;
                left: 0;
                background-color: white;
                transition: width 0.3s ease;
            }}
            nav a:hover::after {{
                width: 100%;
            }}
            nav a.active {{ 
                font-weight: bold;
            }}
            nav a.active::after {{
                width: 100%;
            }}
            .post-list {{ 
                list-style-type: none; 
                padding: 0; 
            }}
            .post-list li {{ 
                margin-bottom: 20px;
                padding: 15px;
                background-color: white;
                border-radius: 5px;
                box-shadow: 0 2px 5px rgba(0,0,0,0.05);
                transition: transform 0.3s ease;
            }}
            .post-list li:hover {{
                transform: translateY(-3px);
            }}
            .post-date {{ 
                color: #6a737d; 
                margin-right: 10px;
                font-size: 0.9em;
            }}
            img {{ 
                max-width: 100%; 
                height: auto;
                border-radius: 5px;
                margin: 20px 0;
            }}
            pre {{ 
                overflow-x: auto;
                background-color: #f0f0f0;
                padding: 15px;
                border-radius: 5px;
            }}
            blockquote {{
                border-left: 4px solid var(--primary-color);
                padding-left: 20px;
                margin-left: 0;
                font-style: italic;
                color: #555;
            }}
            @media (max-width: 800px) {{
                body {{ 
                    font-size: 16px;
                    padding: 10px;
                }}
                header {{
                    padding: 15px;
                }}
                header h1 {{
                    font-size: 2em;
                }}
                h1 {{ font-size: 24px; }}
                h2 {{ font-size: 20px; }}
                nav {{ 
                    flex-direction: column;
                    align-items: center;
                }}
                nav a {{ 
                    margin: 5px 0;
                }}
                .post-list li {{ 
                    padding: 10px;
                }}
            }}
        </style>
    </head>
    <body>
        <header>
            <h1>✦ (^‿^) ✦ Saikat's blog</h1>
            <nav>{nav_html}</nav>
        </header>
        <main>
            {content}
        </main>
        <footer style="text-align: center; margin-top: 50px; color: #777; font-size: 0.9em;">
            © {current_year} Saikat's Blog. All rights reserved.
        </footer>
    </body>
    </html>
    """
