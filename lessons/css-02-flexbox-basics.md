---
id: css-02-flexbox-basics
title: Flexbox Basics
language: css
releaseDate: "2026-01-01"
prerequisites: [css-01-float-position]
---

# Flexbox Basics

The first thing to do is clear out some of the code we set for the last few coding exercises.

Make your html divs look like:

```html
<div>1</div>
<div>2</div>
<div>3</div>
```

Now make your css file look like:

```css
div, p{
   border: 1px solid red;
}
div {
    margin: 5px;
    width: 50px;
    height: 200px;

}
```

Your output window should now look like it did at the start of today's tutorial, with all the elements stacked on top of one another.

## Flexbox

### Flexbox - display

When starting to code out flexbox, we need to tell the browser which elements we want to use flexbox on. We do this by setting a special value of **display** on the parent element. In our case, this is the section tag that holds all of the other elements. It is rare that you would want all of your page elements to be controlled by flex, but in this example, the three divs and one p tag are all we have.

To use flexbox, we want to set the **display** value to **flex** for flexbox. Add the following CSS command to the bottom of your CSS file.

> **NOTE:** You may see a little yellow warning sign appear on the side of the code window on the CSS when you code flex elements. Please ignore these it is not anything wrong with your code; it is just the code authenticator for the WTE is awaiting a release update to check the newer HTML and CSS code elements.

```css
section {
  display: flex;
}
```

This is quite a powerful command all on its own, as you can probably see from your output panel or Figure 6 below. All of the content has automatically come into one line, with each element only taking the width of its content.

What has happened is that the `disply:flex` command causes the `<section>` element to become a flex container, and its children to become flex items.

![Flex Display:flex.](https://teaching.computing.edgehill.ac.uk/wte/parts/10021/files/name/assets/flex-display-flex.png)

**Figure 6**: Flex Display:flex.

### Flexbox - flex-direction

The default direction of flexbox is in the "row", but we can also easily turn this into a "column" should we wish by adding the `flex-direction: column;` command to the section CSS styles. In our case, this would only give us the same representation as we had in the default flow, so we will not add it. But by all means, try it and see what it does but **please remove it after that**.
