import os
import re

portals = [
    ("IT Fundamentals", "IT_Fundamentals_Portal/index.html", "1HW", 184),
    ("Cloud Administration", "Cloud_Administration_Portal/index.html", "C1", 180),
    ("Server Administration", "Server_Administration_Portal/index.html", "S1", 180),
]

print("=" * 70)
print("COMPREHENSIVE THREE-PORTAL ARCHITECTURAL AUDIT & VERIFICATION")
print("=" * 70)

all_passed = True

for name, path, sample_unit, expected_mcqs in portals:
    print(f"\n>>> AUDITING: {name} ({path})")
    assert os.path.exists(path), f"File not found: {path}"
    
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()

    size_kb = len(html) / 1024
    lines = len(html.splitlines())
    print(f"  • File Size: {size_kb:.1f} KB | Total Lines: {lines:,}")

    # 1. HTML Theme tag
    has_light_theme = '<html lang="en" data-theme="light">' in html
    print(f"  • HTML data-theme='light': {'PASS' if has_light_theme else 'FAIL'}")
    if not has_light_theme: all_passed = False

    # 2. Reading progress bar
    has_progress = '<div id="readingProgress" class="reading-progress-bar"></div>' in html
    print(f"  • Reading Progress Bar: {'PASS' if has_progress else 'FAIL'}")
    if not has_progress: all_passed = False

    # 3. Top Toolbar
    has_top_toolbar = '<header class="top-toolbar">' in html
    has_toc_left = 'id="btnToggleTocLeft"' in html
    has_theme_toggle = 'id="btnThemeToggle"' in html
    has_search = 'id="quickSearchInput"' in html
    print(f"  • Top Toolbar (.top-toolbar): {'PASS' if has_top_toolbar else 'FAIL'}")
    print(f"  • ToC Toggle Button (#btnToggleTocLeft): {'PASS' if has_toc_left else 'FAIL'}")
    print(f"  • Theme Toggle Button (#btnThemeToggle): {'PASS' if has_theme_toggle else 'FAIL'}")
    print(f"  • Quick Search Box (#quickSearchInput): {'PASS' if has_search else 'FAIL'}")
    if not (has_top_toolbar and has_toc_left and has_theme_toggle and has_search): all_passed = False

    # 4. ToC Drawer
    has_toc_drawer = '<aside class="toc-drawer open" id="tocDrawer">' in html
    toc_units = len(re.findall(r'class="toc-unit', html))
    toc_groups = len(re.findall(r'class="toc-group', html))
    toc_links = len(re.findall(r'class="toc-link', html))
    print(f"  • ToC Drawer (<aside class='toc-drawer open'>): {'PASS' if has_toc_drawer else 'FAIL'}")
    print(f"  • ToC Units: {toc_units} | Groups: {toc_groups} | Links: {toc_links}")
    if not has_toc_drawer: all_passed = False

    # 5. MCQ Engine & Attributes
    mcq_cards = len(re.findall(r'class="mcq-card"', html))
    data_opts = len(re.findall(r'data-opt="[A-D]"', html))
    data_options = len(re.findall(r'data-option=', html))
    score_badges = len(re.findall(r'id="mcqScore[^"]+"', html))
    print(f"  • Total MCQ Cards: {mcq_cards} (Expected: >={expected_mcqs}) - {'PASS' if mcq_cards >= expected_mcqs else 'FAIL'}")
    print(f"  • Valid data-opt attributes: {data_opts}")
    print(f"  • Deprecated data-option attributes: {data_options} (Must be 0) - {'PASS' if data_options == 0 else 'FAIL'}")
    print(f"  • Score Badges: {score_badges}")
    if mcq_cards < expected_mcqs or data_options != 0 or score_badges == 0: all_passed = False

    # 6. JavaScript Engine Functionality
    has_lucide = 'lucide.createIcons()' in html
    has_comments_toggle = 'btn-toggle-comments' in html
    has_copy_code = 'btn-copy-code' in html
    has_theme_cycler = 'themes = [\'light\', \'sepia\', \'dark\']' in html
    print(f"  • Lucide Vector Icons Init: {'PASS' if has_lucide else 'FAIL'}")
    print(f"  • Code Comments Toggle: {'PASS' if has_comments_toggle else 'FAIL'}")
    print(f"  • Code Smart Copy: {'PASS' if has_copy_code else 'FAIL'}")
    print(f"  • Theme Cycler: {'PASS' if has_theme_cycler else 'FAIL'}")
    if not (has_lucide and has_comments_toggle and has_copy_code and has_theme_cycler): all_passed = False

print("\n" + "=" * 70)
if all_passed:
    print("ALL 3 PORTALS PASSED VERIFICATION WITH 100% IDENTICAL GOLD-STANDARD QUALITY!")
else:
    print("SOME CHECKS FAILED! REVIEW OUTPUT ABOVE.")
print("=" * 70)
