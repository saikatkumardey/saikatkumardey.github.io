import os
import shutil
import markdown
from datetime import datetime
from template import POST_TEMPLATE

class BlogGenerator:
    def __init__(self, posts_dir="posts", output_dir="docs"):
        self.posts_dir = posts_dir
        self.output_dir = output_dir
        self.posts = []
        self.md = markdown.Markdown(extensions=['fenced_code', 'codehilite'])

    def generate_html(self, title, content, active_page):
        nav_items = {
            "Home": "index.html",
            "Blog": "blog.html",
            "Projects": "projects.html",
        }
        nav_html = []
        for page, url in nav_items.items():
            class_attr = ' class="active"' if page == active_page else ""
            nav_html.append(f'<a href="/{url}"{class_attr}>{page}</a>')
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
            "filename": os.path.splitext(os.path.basename(filename))[0] + ".html",
            "relative_path": os.path.relpath(os.path.dirname(filename), self.posts_dir),
        }

    def generate_post_list(self, posts):
        post_list = "<ul class='post-list'>"
        for post in posts:
            date_str = post["date"].strftime("%d %b, %Y").replace(" 0", " ") if post["date"] else ""
            post_path = os.path.join(post["relative_path"], post["filename"]).replace("\\", "/")
            post_list += f"""
            <li>
                <span class='post-date'>{date_str}</span>
                <a href='/{post_path}'>{post['title']}</a>
            </li>"""
        post_list += "</ul>"
        return post_list

    def process_posts(self):
        for root, _, files in os.walk(self.posts_dir):
            for filename in files:
                if filename.endswith(".md") and filename not in ["index.md", "projects.md"]:
                    file_path = os.path.join(root, filename)
                    post = self.parse_post(file_path)
                    self.posts.append(post)

                    content = f"""# {post['title']}\n\n{post["content"]}"""
                    post_content = self.md.convert(content)
                    post_html = self.generate_html(post["title"], post_content, "Blog")
                    
                    output_path = os.path.join(self.output_dir, post["relative_path"], post["filename"])
                    os.makedirs(os.path.dirname(output_path), exist_ok=True)
                    with open(output_path, "w") as f:
                        f.write(post_html)

        self.posts.sort(key=lambda x: x["date"] if x["date"] else datetime.min, reverse=True)

    def generate_blog_page(self):
        blog_content = "<h1>Blog Posts</h1>" + self.generate_post_list(self.posts)
        blog_html = self.generate_html("Blog - Saikat's Blog", blog_content, "Blog")
        with open(os.path.join(self.output_dir, "blog.html"), "w") as f:
            f.write(blog_html)

    def generate_home_page(self):
        home_page_path = os.path.join(self.posts_dir, "index.md")
        home_post = self.parse_post(home_page_path)

        home_content = self.md.convert(home_post["title"] + "\n\n" + home_post["content"])

        recent_posts = self.posts[:3]
        recent_posts_html = self.generate_post_list(recent_posts)
        home_content += f"<h2>Recent Posts</h2>{recent_posts_html}"

        index_html = self.generate_html("Saikat's Blog", home_content, "Home")

        with open(os.path.join(self.output_dir, "index.html"), "w") as f:
            f.write(index_html)

    def generate_projects_page(self):
        projects_post = self.parse_post(os.path.join(self.posts_dir, "projects.md"))
        content = f"""# {projects_post['title']}\n\n{projects_post["content"]}"""
        projects_content = self.md.convert(content)
        projects_html = self.generate_html("Projects - Saikat's Blog", projects_content, "Projects")
        with open(os.path.join(self.output_dir, "projects.html"), "w") as f:
            f.write(projects_html)

    def build(self):
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