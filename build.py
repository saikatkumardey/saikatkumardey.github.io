import os
import shutil
import markdown
from datetime import datetime

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
            @media (max-width: 600px) {{
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


class BlogGenerator:
    def __init__(self, posts_dir="posts", output_dir="docs"):
        self.posts_dir = posts_dir
        self.output_dir = output_dir
        self.posts = []

    def generate_html(self, title, content, active_page):
        nav_items = {
            "Home": "index.html",
            "Blog": "blog.html",
            "Projects": "projects.html",
        }
        nav_html = []
        for page, url in nav_items.items():
            class_attr = ' class="active"' if page == active_page else ""
            nav_html.append(f'<a href="{url}"{class_attr}>{page}</a>')
        nav_html = "".join(nav_html)
        return POST_TEMPLATE.format(
            title=title, content=content, nav_html=nav_html, current_year=datetime.now().year
        )

    def parse_post(self, filename):
        try:
            date = datetime.strptime(
                os.path.basename(filename)[:10], "%Y-%m-%d"
            )
        except ValueError:
            date = None

        with open(filename, "r") as f:
            content = f.read().split("\n", 2)

        title = content[0].strip("# ")
        return {
            "date": date,
            "title": title,
            "content": "\n".join(content[1:]),
            "filename": os.path.splitext(os.path.basename(filename))[0]
            + ".html",
        }

    def generate_post_list(self, posts):
        post_list = "<ul class='post-list'>"
        for post in posts:
            date_str = (
                post["date"].strftime("%d %b, %Y").replace(" 0", " ")
            )  # Remove leading zero from day
            post_list += f"""
            <li>
                <span class='post-date'>{date_str}</span>
                <a href='{post['filename']}'>{post['title']}</a>
            </li>"""
        post_list += "</ul>"
        return post_list

    def process_posts(self):
        for filename in os.listdir(self.posts_dir):
            if filename.endswith(".md") and filename not in [
                "index.md",
                "projects.md",
            ]:
                post = self.parse_post(os.path.join(self.posts_dir, filename))
                self.posts.append(post)

                content = f"""# {post['title']}\n\n{post["content"]}"""
                post_content = markdown.markdown(content)
                post_html = self.generate_html(
                    post["title"], post_content, "Blog"
                )
                with open(
                    os.path.join(self.output_dir, post["filename"]), "w"
                ) as f:
                    f.write(post_html)

        self.posts.sort(key=lambda x: x["date"], reverse=True)

    def generate_blog_page(self):
        blog_content = "<h1>Blog Posts</h1>" + self.generate_post_list(self.posts)
        blog_html = self.generate_html(
            "Blog - Saikat's Blog", blog_content, "Blog"
        )
        with open(os.path.join(self.output_dir, "blog.html"), "w") as f:
            f.write(blog_html)

    def generate_home_page(self):
        home_page_path = os.path.join(self.posts_dir, "index.md")
        home_post = self.parse_post(home_page_path)

        # Convert markdown to HTML
        home_content = markdown.markdown(
            home_post["title"] + "\n\n" + home_post["content"]
        )

        # Add the list of recent posts
        recent_posts = self.posts[:3]  # Get the 3 most recent posts
        recent_posts_html = self.generate_post_list(recent_posts)
        home_content += f"<h2>Recent Posts</h2>{recent_posts_html}"

        index_html = self.generate_html("Saikat's Blog", home_content, "Home")

        with open(os.path.join(self.output_dir, "index.html"), "w") as f:
            f.write(index_html)

    def generate_projects_page(self):
        projects_post = self.parse_post(
            os.path.join(self.posts_dir, "projects.md")
        )
        content = f"""# {projects_post['title']}\n\n{projects_post["content"]}"""
        projects_content = markdown.markdown(content)
        projects_html = self.generate_html(
            "Projects - Saikat's Blog", projects_content, "Projects"
        )
        with open(os.path.join(self.output_dir, "projects.html"), "w") as f:
            f.write(projects_html)

    def build(self):
        # Clean the output directory
        if os.path.exists(self.output_dir):
            shutil.rmtree(self.output_dir)
        os.makedirs(self.output_dir)

        self.process_posts()
        self.generate_blog_page()
        self.generate_home_page()
        self.generate_projects_page()
        print("Site built successfully!")


if __name__ == "__main__":
    generator = BlogGenerator()
    generator.build()