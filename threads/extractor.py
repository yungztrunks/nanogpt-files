import json
import codecs

data = json.load(codecs.open("threads_and_replies.json", "r", "utf-8"))

def extract_titles(data):
    titles = []
    for entry in data.get("text_post_app_text_posts", []):
        for media_item in entry.get("media", []):
            title = media_item.get("title", "").strip()
            if title:
                titles.append(title)
    
    return titles

# Example usage:
titles = extract_titles(data)
print(titles)

# save to file
with open("titles.txt", "w", encoding="utf-8") as f:
    for title in titles:
        f.write(title + "\n")
