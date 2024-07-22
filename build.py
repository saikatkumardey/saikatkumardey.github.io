import os
import shutil
import markdown
from datetime import datetime

class BlogGenerator:
    def __init__(self, posts_dir='posts', output_dir='docs'):
        self.posts_dir = posts_dir
        self.output_dir = output_dir
        self.posts = []

    def generate_html(self, title, content, active_page):
        nav_items = {
            "Home": "index.html",
            "Blog": "blog.html"
        }
        nav_html = []
        for page, url in nav_items.items():
            class_attr = ' class="active"' if page == active_page else ''
            nav_html.append(f'<a href="{url}"{class_attr}>{page}</a>')
        nav_html = ''.join(nav_html)
        
        return f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; line-height: 1.6; color: #333; max-width: 800px; margin: 0 auto; padding: 20px; }}
        a {{ color: #0366d6; text-decoration: none; }}
        h1, h2 {{ margin-top: 1.5em; }}
        nav {{ margin-bottom: 20px; }}
        nav a {{ margin-right: 15px; }}
        nav a.active {{ font-weight: bold; }}
        .post-list {{ list-style-type: none; padding: 0; }}
        .post-list li {{ margin-bottom: 10px; }}
        .post-date {{ color: #6a737d; margin-right: 10px; }}
    </style>
</head>
<body>
    <header>
        <h1>✦ (^‿^) ✦ Saikat's blog</h1>
        <nav>{nav_html}</nav>
    </header>
    <main>
        <h2>{title}</h2>
        {content}
    </main>
</body>
</html>
"""

    def parse_post(self, filename):
        try:
            date = datetime.strptime(os.path.basename(filename)[:10], '%Y-%m-%d')
        except ValueError:
            date = datetime.fromtimestamp(os.path.getmtime(filename))

        with open(filename, 'r') as f:
            content = f.read().split('\n', 2)
        
        title = content[0].strip('# ')
        return {
            'date': date,
            'title': title,
            'content': '\n'.join(content[1:]),
            'filename': os.path.splitext(os.path.basename(filename))[0] + '.html'
        }

    def generate_post_list(self, posts):
        post_list = "<ul class='post-list'>"
        for post in posts:
            date_str = post['date'].strftime('%d %b, %Y').replace(' 0', ' ')  # Remove leading zero from day
            post_list += f"""
            <li>
                <span class='post-date'>{date_str}</span>
                <a href='{post['filename']}'>{post['title']}</a>
            </li>"""
        post_list += "</ul>"
        return post_list

    def process_posts(self):
        for filename in os.listdir(self.posts_dir):
            if filename.endswith('.md') and filename != 'index.md':
                post = self.parse_post(os.path.join(self.posts_dir, filename))
                self.posts.append(post)
                
                post_content = markdown.markdown(post["content"])
                post_html = self.generate_html(post['title'], post_content, "Blog")
                with open(os.path.join(self.output_dir, post['filename']), 'w') as f:
                    f.write(post_html)

        self.posts.sort(key=lambda x: x['date'], reverse=True)

    def generate_blog_page(self):
        blog_content = self.generate_post_list(self.posts)
        blog_html = self.generate_html("Blog - Saikat's Blog", blog_content, "Blog")
        with open(os.path.join(self.output_dir, 'blog.html'), 'w') as f:
            f.write(blog_html)

    def generate_home_page(self):
        with open('index.md', 'r') as f:
            home_content = f.read()
        
        # Convert markdown to HTML
        home_content = markdown.markdown(home_content)
        
        # Add the list of recent posts
        popular_posts = self.posts[:3]  # Assuming the first 5 are the most popular
        popular_posts_html = self.generate_post_list(popular_posts)
        home_content += f"<h3>My latest posts</h3>{popular_posts_html}"

        index_html = self.generate_html("Saikat's Blog", home_content, "Home")
        with open(os.path.join(self.output_dir, 'index.html'), 'w') as f:
            f.write(index_html)

    def build(self):
        # Clean the output directory
        if os.path.exists(self.output_dir):
            shutil.rmtree(self.output_dir)
        os.makedirs(self.output_dir)

        self.process_posts()
        self.generate_blog_page()
        self.generate_home_page()
        print("Site built successfully!")

if __name__ == "__main__":
    generator = BlogGenerator()
    generator.build()