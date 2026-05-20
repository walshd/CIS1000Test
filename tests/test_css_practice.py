"""Tests for the Flexbox and Float Practice lesson."""
import os
import re

SCAFFOLDS = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'scaffolds')


def read(filename):
    with open(os.path.join(SCAFFOLDS, filename)) as f:
        return f.read()


def normalize(css):
    css = re.sub(r'/\*.*?\*/', '', css, flags=re.DOTALL)
    return re.sub(r'\s+', ' ', css).lower()


def block_for(css, selector):
    """Return concatenated content of all { } blocks whose selector contains `selector`."""
    norm = normalize(css)
    result = []
    pos = 0
    while True:
        idx = norm.find(selector, pos)
        if idx == -1:
            break
        brace = norm.find('{', idx)
        if brace == -1:
            break
        close = norm.find('}', brace)
        if close == -1:
            break
        result.append(norm[brace + 1:close])
        pos = close + 1
    return ' '.join(result)


# ── Task 1: nav flex container ────────────────────────────────────────────────

def test_nav_display_flex():
    block = block_for(read('practice-styles.css'), 'nav')
    assert re.search(r'display\s*:\s*flex', block), (
        "Add 'display: flex' to the nav rule in practice-styles.css"
    )


def test_nav_justify_content_space_around():
    block = block_for(read('practice-styles.css'), 'nav')
    assert re.search(r'justify-content\s*:\s*space-around', block), (
        "Add 'justify-content: space-around' to the nav rule"
    )


def test_nav_align_items_center():
    block = block_for(read('practice-styles.css'), 'nav')
    assert re.search(r'align-items\s*:\s*center', block), (
        "Add 'align-items: center' to the nav rule"
    )


def test_nav_has_height():
    block = block_for(read('practice-styles.css'), 'nav')
    assert 'height' in block, (
        "Add a height to the nav rule (e.g. height: 60px)"
    )


# ── Task 2: equal-width nav items ────────────────────────────────────────────

def test_nav_items_flex_1():
    css = read('practice-styles.css')
    # Accept nav > p or nav>p (with or without spaces around >)
    block = block_for(css, 'nav > p') + ' ' + block_for(css, 'nav>p')
    assert re.search(r'flex\s*:\s*1', block), (
        "Add 'flex: 1' to the nav > p rule so all nav items share equal width"
    )


# ── Task 3: two-column page layout ───────────────────────────────────────────

def test_page_layout_display_flex():
    block = block_for(read('practice-styles.css'), '.page-layout')
    assert re.search(r'display\s*:\s*flex', block), (
        "Add 'display: flex' to the .page-layout rule"
    )


def test_sidebar_has_flex_basis():
    block = block_for(read('practice-styles.css'), '.sidebar')
    assert 'flex-basis' in block, (
        "Add 'flex-basis' to the .sidebar rule to give it a fixed starting width"
    )


def test_sidebar_flex_shrink_0():
    block = block_for(read('practice-styles.css'), '.sidebar')
    assert re.search(r'flex-shrink\s*:\s*0', block), (
        "Add 'flex-shrink: 0' to the .sidebar rule so it keeps its width on small screens"
    )


def test_main_content_flex_1():
    block = block_for(read('practice-styles.css'), '.main-content')
    assert re.search(r'flex\s*:\s*1', block) or re.search(r'flex-grow\s*:\s*1', block), (
        "Add 'flex: 1' to the .main-content rule so it fills the remaining space"
    )


# ── Task 4: float the profile picture ────────────────────────────────────────

def test_profile_pic_float_left():
    block = block_for(read('practice-styles.css'), '.profile-pic')
    assert re.search(r'float\s*:\s*left', block), (
        "Add 'float: left' to the .profile-pic rule"
    )


def test_profile_pic_has_width():
    block = block_for(read('practice-styles.css'), '.profile-pic')
    assert 'width' in block, (
        "Add a width to the .profile-pic rule (e.g. width: 80px)"
    )


def test_profile_pic_has_margin_right():
    block = block_for(read('practice-styles.css'), '.profile-pic')
    assert 'margin-right' in block or re.search(r'margin\s*:', block), (
        "Add 'margin-right' to the .profile-pic rule to give it some space from the text"
    )
