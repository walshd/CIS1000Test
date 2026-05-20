---
id: css-05-flexbox-practice
title: Practice — Portfolio Page Layout
language: css
releaseDate: "2026-01-01"
prerequisites: [css-04-flexbox-further]
---

# Practice — Portfolio Page Layout

Time to put everything together. In this exercise you will style a simple portfolio page from scratch using the float and flexbox skills you have built up across this week's tutorials.

The HTML has already been written for you in `practice-index.html` — open it and read through the structure before you start. You will see a navigation bar, a two-column layout with a sidebar and a main content area, and a profile picture placeholder inside the sidebar.

All of your CSS goes into `practice-styles.css`. Some base styles are already there; add your rules below the comments in each section.

## Task 1 — Navigation bar

Make the `nav` element a horizontal navigation bar using flexbox.

Your nav should:

- Use `display: flex` to make it a flex container
- Space the items evenly across the bar using `justify-content: space-around`
- Centre the items vertically using `align-items: center`
- Have a fixed height (for example, `height: 60px`)

```css
nav {
    background: #333;
    color: white;
    display: flex;
    justify-content: space-around;
    align-items: center;
    height: 60px;
}
```

::: task id=practice-nav kind=scaffold marking=auto
**Style the `nav` element as a horizontal flexbox navigation bar with items spaced evenly and centred vertically.**

scaffold: scaffolds/practice-styles.css
validator: python3 -m pytest tests/test_css_practice.py::test_nav_display_flex tests/test_css_practice.py::test_nav_justify_content_space_around tests/test_css_practice.py::test_nav_align_items_center tests/test_css_practice.py::test_nav_has_height -v
:::

## Task 2 — Equal-width nav items

Right now the nav items are only as wide as their text. Make each `nav > p` item fill an equal share of the nav bar by adding `flex: 1`.

```css
nav > p {
    flex: 1;
}
```

::: task id=practice-nav-items kind=scaffold marking=auto
**Add `flex: 1` to the `nav > p` rule so all four nav items share equal width.**

scaffold: scaffolds/practice-styles.css
validator: python3 -m pytest tests/test_css_practice.py::test_nav_items_flex_1 -v
:::

## Task 3 — Two-column page layout

The `.page-layout` div holds the sidebar and the main content area. Use flexbox to place them side by side.

- Make `.page-layout` a flex container
- Give `.sidebar` a fixed starting width using `flex-basis` (250px works well) and set `flex-shrink: 0` so it does not shrink on smaller screens
- Give `.main-content` a value of `flex: 1` so it fills all the remaining space

```css
.page-layout {
    display: flex;
}

.sidebar {
    flex-basis: 250px;
    flex-shrink: 0;
}

.main-content {
    flex: 1;
}
```

::: task id=practice-layout kind=scaffold marking=auto
**Create a two-column layout using flexbox — fixed-width sidebar on the left, flexible main content on the right.**

scaffold: scaffolds/practice-styles.css
validator: python3 -m pytest tests/test_css_practice.py::test_page_layout_display_flex tests/test_css_practice.py::test_sidebar_has_flex_basis tests/test_css_practice.py::test_sidebar_flex_shrink_0 tests/test_css_practice.py::test_main_content_flex_1 -v
:::

## Task 4 — Float the profile picture

Inside the sidebar there is a `.profile-pic` placeholder div. Use the float skills from the first tutorial to float it to the left of the bio text.

- Float it to the left using `float: left`
- Give it a width (for example, `width: 80px`)
- Add some space between the picture and the text using `margin-right`

```css
.profile-pic {
    float: left;
    width: 80px;
    margin-right: 1rem;
}
```

::: task id=practice-float kind=scaffold marking=auto
**Float the `.profile-pic` element to the left with a set width and a right margin.**

scaffold: scaffolds/practice-styles.css
validator: python3 -m pytest tests/test_css_practice.py::test_profile_pic_float_left tests/test_css_practice.py::test_profile_pic_has_width tests/test_css_practice.py::test_profile_pic_has_margin_right -v
:::

## Task 5 — Challenge: make the layout wrap on small screens

This task gives you no example code. Use what you have learned in the tutorial to work it out.

At the moment, if the browser window gets very narrow the sidebar and main content are squeezed together because flex does not wrap by default. Add a single CSS property to `.page-layout` to allow the columns to wrap onto separate rows when there is not enough horizontal space.

> **Hint:** The property name was covered in the flex-wrap section of the Flexbox Navigation Bar tutorial.

::: task id=practice-wrap kind=scaffold marking=auto
**Add flex wrapping to `.page-layout` so the columns stack vertically on narrow screens — no example code given.**

scaffold: scaffolds/practice-styles.css
validator: python3 -m pytest tests/test_css_practice.py::test_layout_flex_wrap tests/test_css_practice.py::test_css_syntax_braces_balanced tests/test_css_practice.py::test_css_declarations_have_colons -v
:::

## What you have practised

- `display: flex` to create horizontal layouts
- `justify-content` and `align-items` to position flex items
- `flex: 1` to share available space equally
- `flex-basis` and `flex-shrink` to create a fixed-width sidebar
- `float: left` to wrap text around an element

Once all four tasks are green, your portfolio page should have a dark horizontal nav bar, a two-column layout with a sidebar and main area side by side, and a floated profile picture with the bio text wrapping around it.
