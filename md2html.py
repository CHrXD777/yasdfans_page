import markdown2
from datetime import datetime

def extract_metadata(markdown_content):
    metadata = {"title": "", "first_paragraph": "", "timestamp": "", "author": ""}

    # Split metadata and content
    sections = markdown_content.split("---", 2)
    if len(sections) > 2:
        metadata_section = sections[1].strip()
        content_section = sections[2].strip()

        # Extract metadata values
        for line in metadata_section.splitlines():
            key, value = map(str.strip, line.split(":", 1))
            metadata[key.lower()] = value

        # Extract first paragraph from content
        paragraphs = content_section.split("\n\n")
        if paragraphs:
            metadata["first_paragraph"] = paragraphs[0]

    return metadata

def generate_article_html(metadata, html_content):
    article_html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{metadata['title']}</title>
    </head>
    <body>

        <h1>{metadata['title']}</h1>
        <p>Published: {metadata['timestamp']}</p>
        <p>Author: {metadata['author']}</p>

        {html_content}

    </body>
    </html>
    """

    return article_html

def process_submission(markdown_file_path):
    # Read Markdown file content
    with open(markdown_file_path, 'r', encoding='utf-8') as markdown_file:
        markdown_content = markdown_file.read()

    # Extract metadata
    metadata = extract_metadata(markdown_content)

    # Convert Markdown to HTML
    html_content = markdown2.markdown(markdown_content)

    # Write metadata and HTML to article HTML file
    article_filename = f"article_{datetime.now().strftime('%Y%m%d%H%M%S')}.html"
    article_html = generate_article_html(metadata, html_content)

    with open(f'posts/{article_filename}', 'w', encoding='utf-8') as article_file:
        article_file.write(article_html)

    return article_filename, metadata

if __name__ == "__main__":
    submission_file = "test.md"
    article_filename, metadata = process_submission(submission_file)

    # Update main page with metadata
    with open('index.html', 'r', encoding='utf-8') as index_file:
        index_html = index_file.read()

    # Insert link to the new article
    #在此定义插入主页的内容
    link_to_article = f'<!-- INSERT_ARTICLE_LINK --><h1>{metadata["title"]}</h1><p>{metadata["first_paragraph"]}</p><p><span>作者：{metadata["author"]}</span> <span class="timestamp">发布时间：{metadata["timestamp"]}</span></p><a href="posts/{article_filename}"> 阅读-> </a>'
    updated_index_html = index_html.replace('<!-- INSERT_ARTICLE_LINK -->', link_to_article)

    # Update main page HTML file
    with open('index.html', 'w', encoding='utf-8') as updated_index_file:
        updated_index_file.write(updated_index_html)

    print(f"Article HTML file generated: {article_filename}")
    print(f"Main page updated with link to the new article")
