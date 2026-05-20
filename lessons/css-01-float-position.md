---
id: css-01-float-position
title: CSS Float and Position
language: css
releaseDate: "2026-01-01"
prerequisites: []
---

# CSS Float and Position

**Please ignore the flexbox-nav HTML and CSS for now.**

Before we have a go at Flexbox, understanding how Float and Position work is required.

On the index.html page on the right, you will see you have three div tags, each with a number in them. Then there is a p tag containing some Lorem ipsum text (Lorem Ipsum is a non-sense language used as a placeholder in designs that will be replaced later with actual textual content).

Right now, you can see that the elements are all stacked on top of each other. This is the normal flow as both the DIV and paragraph tags are both Block-level elements. (you can discover all of the block-level elements at: [https://developer.mozilla.org/en-US/docs/Web/HTML/Block-level_elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Block-level_elements))

To play about with the Float, we will now add in some basic CSS which I will not explain right now, as we will cover CSS in a later tutorial, but it is helpful to use in this tutorial as a demonstration of Float and Position.

In the styles.css tab type in the following code:

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

Once the CSS has saved (the red styles.css tab has changed from red to green), then you will see that the output has changed and now all of your elements now have a set width and height and a border, but they are all still stacked on top of each other, even though they are restricted to a width of 50px (See Figure 1). This is because they are still block-level elements and are following the default Flow.

![Divs with border stacked after float.](https://teaching.computing.edgehill.ac.uk/wte/parts/10020/files/name/assets/float-before.png)

**Figure 1**: Divs with border stacked after float.

Alter the opening div tags in your HTML code to look like the following (you are only adding CSS classes to the HTML elements):

```html
<div class="left">1</div>
<div class="left">2</div>
<div class="right">3</div>
```

Now add the following CSS to the end of your CSS code:

```css
.left{
    float: left;
}

.right{
    float: right;
}
```

You should see now that the elements are no longer stacked on top of each other, but instead, the paragraph is still in the normal flow and seems to start just before div's 1 and 2, and then div 3 is on the right.

We can sort this ordering issue by telling the parent section tag to float.

Add the following rule to the end of your CSS file:

```css
section{
    float: left;
    width: 100%;
}
```

You should now see that the p tag is just below the start of the divs (See Figure 2).

![P Tag floating.](https://teaching.computing.edgehill.ac.uk/wte/parts/10020/files/name/assets/float-after.png)

**Figure 2**: P Tag floating.

Have a play around with changing the class assignments in the HTML file. Make them all "left", then add "right to the first div", etc.

Once you have finished, set it back to what it was before you started playing around.

## Clear

When using Float, there is always a time you do not want an element to continue flowing the Float. For this, we use a command called **CLEAR**. Depending on which Float we want to stop depends upon the value you add to it. The value could be Left, Right, Both or None.

In our code example, we can force the p tag to be at the bottom of the divs. Add the following code to the bottom of your CSS file:

```css
p{
   clear: left;
}
```

The result should be that the left and right floats on the divs have continued to work, but the p tag has been removed from the Float and now sits at the bottom (See Figure 3).

![Float cleared.](https://teaching.computing.edgehill.ac.uk/wte/parts/10020/files/name/assets/clear-float.png)

**Figure 3**: Float cleared.

Have a go at trying to clear the Float from div 2.

## Position

Now you have a good basic grasp of how to float elements to the left or right of the screen and how to bring them back into the normal flow, it is time to look at position. Position accepts values of top, right, bottom, and left. Not all are always required, but there should always be at least one vertical (top or bottom) and one horizontal (left or right) value provided.

We will use position to control our paragraph of text.

### Relative

The first value we will explore is that of position:relative.

Relative positions the element according to the normal flow of the document and then offsets it relative to itself based on the values provided.

In your css file change your current p tag style to:

```css
p{
position: relative;
top: 40px;
left: 40px;
}
```

![Position relative.](https://teaching.computing.edgehill.ac.uk/wte/parts/10020/files/name/assets/position-relative.png)

**Figure 4**: Position relative.

As you can see in Figure 4, the p tag is kept in the flow and then moved 40px down from the top and pushed 40px to the right by adding the 40px to the left-hand side. Notice how this keeps the content the same distance inside of the p tag as it was when the p tag was just part of the normal flow (you can look at either of the earlier images).

### Absolute

As we said earlier, Position absolute removes the element from the flow altogether and positions the element on the page based upon the values provided.

Make your p tag css code look like:

```css
p{
position: absolute;
top: 40px;
left: 40px;
}
```

So all we really did in the above code was to change the word relative to absolute, but the result is quite substantial.

![Position absolute.](https://teaching.computing.edgehill.ac.uk/wte/parts/10020/files/name/assets/position-absolute.png)

**Figure 5**: Position absolute.

In Figure 5 you can see the content (text) of the p tag no longer keeps that left margin that the normal flow forced. Instead, the text now overlaps the div tags.

**WARNING** position: absolute can be very dangerous to use and should be used very rarely because you do not really know what screen size your user will have, and you are basically forcing the element into that position on whatever screen it is shown on. With it removing the elements from the normal flow, this means that it will probably never look the same on a users screen as it does on your screen when developing it.

Right, now you know the basics of how block and inline elements are controlled in the layout by flow and float and position, so it is time to move onto Flexbox.
