import re

with open('_portal_generators/it_sections_u6.py', 'r', encoding='utf-8') as f:
    txt = f.read()

articles = re.findall(r'<article[^>]*id="([^"]+)"[^>]*>.*?<h2[^>]*>(.*?)</h2>', txt, re.DOTALL)
print(f"Total articles in Unit 6: {len(articles)}")
for aid, atitle in articles:
    clean = re.sub(r'<[^>]+>', '', atitle).strip()
    print(f" - [{aid}] {clean}")

# Check for subheadings (h3) in Unit 6
h3s = re.findall(r'<h3[^>]*>(.*?)</h3>', txt)
print(f"\nSubheadings in Unit 6 ({len(h3s)}):")
for h in h3s:
    clean_h = re.sub(r'<[^>]+>', '', h).strip()
    print(f"   * {clean_h}")
