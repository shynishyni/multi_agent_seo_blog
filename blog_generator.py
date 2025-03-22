

import json
import re
import random
import textwrap

# ========== RESEARCH MODULE ==========
def fetch_trending_topics():
    topics = [
        "AI in HR and Recruitment",
        "Remote Work Policies",
        "Employee Well-being & Mental Health",
        "Diversity & Inclusion Strategies",
        "HR Automation Tools",
        "The Future of Hybrid Work"
    ]
    return random.choice(topics) 

# ========== CONTENT PLANNING MODULE ==========
def generate_blog_outline(topic):
    return {
        "title": topic,
        "sections": [
            {
                "heading": "Introduction",
                "content": [
                    "Briefly introduce the topic and its relevance in HR.",
                    "Explain why this topic is trending."
                ]
            },
            {
                "heading": "Understanding the Topic",
                "subsections": [
                    {
                        "subheading": f"What is {topic}?",
                        "content": ["Define the topic and its importance in HR."]
                    },
                    {
                        "subheading": "Why is this topic important?",
                        "content": ["Discuss benefits and challenges."]
                    }
                ]
            },
            {
                "heading": "Key Strategies and Best Practices",
                "subsections": [
                    {
                        "subheading": "Implementation Strategies",
                        "content": ["Steps to integrate this in HR workflows."]
                    },
                    {
                        "subheading": "Common Mistakes to Avoid",
                        "content": ["Highlight pitfalls and solutions."]
                    }
                ]
            },
            {
                "heading": "Future Trends and Predictions",
                "content": ["Discuss future possibilities and trends."]
            },
            {
                "heading": "Conclusion",
                "content": ["Summarize key takeaways."]
            }
        ]
    }

# ========== CONTENT GENERATION MODULE ==========
def generate_blog_content(outline):
    blog_content = f"# {outline['title']}\n\n"
    
    for section in outline["sections"]:
        blog_content += f"## {section['heading']}\n"
        
        if "content" in section:
            for point in section["content"]:
                blog_content += f"- {point}\n"

        if "subsections" in section:
            for sub in section["subsections"]:
                blog_content += f"### {sub['subheading']}\n"
                for point in sub["content"]:
                    blog_content += f"- {point}\n"
                    
        blog_content += "\n"
    
    return blog_content.strip()

# ========== SEO OPTIMIZATION MODULE ==========
def optimize_for_seo(blog_content, topic):

    
    seo_content = f""
    
    seo_content += blog_content + "\n\n"

    
    return seo_content

# ========== REVIEW & FORMATTING MODULE ==========
def perform_grammar_check(text):
    text = re.sub(r"\bteh\b", "the", text) 
    return text

def save_to_file(content, filename, format_type="txt"):
    if format_type == "txt":
        with open(filename, "w", encoding="utf-8") as file:
            file.write(content)
    elif format_type == "md":
        with open(filename.replace(".txt", ".md"), "w", encoding="utf-8") as file:
            file.write(content)
    elif format_type == "html":
        html_content = f"<html><body><pre>{content}</pre></body></html>"
        with open(filename.replace(".txt", ".html"), "w", encoding="utf-8") as file:
            file.write(html_content)
    
    print(f"\n✅ Blog saved as {filename}")

# ========== MAIN EXECUTION ==========
if __name__ == "__main__":
    topic = fetch_trending_topics()
    print(f"🔍 Selected Topic: {topic}\n")
    
    outline = generate_blog_outline(topic)
    blog_content = generate_blog_content(outline)
    
    seo_optimized_content = optimize_for_seo(blog_content, topic)
    final_content = perform_grammar_check(seo_optimized_content)
    
    save_to_file(final_content, "HR_blog_post.txt", format_type="md")
