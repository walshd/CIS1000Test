---
id: css-03-flexbox-nav
title: Flexbox Navigation Bar
language: css
releaseDate: "2026-01-01"
prerequisites: [css-02-flexbox-basics]
---

# Flexbox Navigation Bar

Time to put this new knowledge into practice using an example of an actual page component that you are likely to create many times, a navigation bar.

The flexbox-nav.html and Flexbox-nav-styles.css have been pre-coded to give you a basic three-item navigation bar (See Figure 7). As it stands, all the items are styled as we would expect, with three block-level elements stacked on top of each other and taking up the full width of the browser space.

![A basic three-item navigation bar.](https://teaching.computing.edgehill.ac.uk/wte/parts/9969/files/name/assets/start-nav.png)

**Figure 7**: A basic three-item navigation bar.

For the rest of this tutorial, we will work on this example, and it will be enough to teach you all about Flexbox.

## Declare the flex container (parent element)

As discussed in the last example, each flex component has a parent container element that holds all child flex items.

Declaring this parent should always be your first action when creating a flex component. This is because it provides all of those default styles that we saw in the last example. Not applying this first could mean that you either create too much code that is creating what would be applied anyway, or you will be creating confusing code that is hard to then track down.

Looking at the HTML code for our navigation bar in the flexbox-nav.html file, you can see that we have a body that holds the nav and the nav, in turn, contains all of the p tags. This means that the nav is the parent of the p tags, and the body is the parent of the nav. We do not, however, want to create the body as the flex-container as this would mean that all items in the page would then be flex-items, and this would not really be ideal as the point of flexbox it to create components of the page that are flexible, not to create full pages that are (although this is possible, it is just not good practice).

So with this in mind it is clear that the **nav** should be made into our flex container. To do this we add the `display:flex` to the flexbox-nav-styles.css file just under the `border: 5px solid #000000;` rule:

```css
nav{
 border: 5px solid #000000;
 display:flex;
}
```

After applying the `display:flex` to the parent container, all of the nav items should now arrange themselves into a horizontal bar (this means the flex-direction is automatically set to row) instead of how they were originally stacked (See Figure 8). This shows us that the default styles of Flexbox make all items line up left to right and also makes each item have a width based on its contents.

![All items in horizontal structure.](https://teaching.computing.edgehill.ac.uk/wte/parts/10022/files/name/assets/display-flex-nav.png)

**Figure 8**: All items in horizontal structure.

## Flexbox - axis

In our last exercise, we discussed the flexbox axis and saw the results of applying the `flex-direction: column` rule. In this example, applying this is not required as we are building a top navigation bar, but if we wanted to create a side nav navigation bar, then we would apply this. Whilst that would then make the component look like it was when all items were in the default HTML flow, it would actually create a flexible component, and so I would still create the side nav as a flex component (See Figure 9).

![Flex-direction set to column.](https://teaching.computing.edgehill.ac.uk/wte/parts/10022/files/name/assets/start-nav.png)

**Figure 9**: Flex-direction set to column.

**Make sure you are set to flex-direction of row or do not have this set at all before moving on!**

## Justifying content

At the moment, all are flex-items (nav buttons) are crammed to the left of the nav component. For many navigation bars, this may be enough, but as this is a tutorial on Flexbox, we are going to experiment and learn about how to position the items.

The first way to control some of the items is to use `justify-content:`. The default setting when creating the flex component is that all children are given a justification of left. The flex code for this would be `justify-content:flex-start;` which means start placing the items on the left. Meaning that there is no visual difference from when the display:flex setting was set (See Figure 10).

```css
nav{
 border: 5px solid #000000;
 display:flex;
 justify-content:flex-start;
}
```

![All items in horizontal structure with left justified content.](https://teaching.computing.edgehill.ac.uk/wte/parts/10022/files/name/assets/display-flex-nav.png)

**Figure 10**: All items in horizontal structure with left justified content.

As with almost all things, where you can set it to the left, you can also set it to the right (See Figure 11). In flex using justify-content we do this by setting the value to flex-end like: `justify-content:flex-end;`.

```css
nav{
 border: 5px solid #000000;
 display:flex;
 justify-content:flex-end;
}
```

![All items in horizontal structure with justified content set to "end".](https://teaching.computing.edgehill.ac.uk/wte/parts/10022/files/name/assets/justify-content-flex-end-nav.png)

**Figure 11**: All items in horizontal structure with justified content set to "end".

If we assign center to the justify-content (`justify-content:center;`) property, then all items are placed in the centre (See Figure 12).

```css
nav{
 border: 5px solid #000000;
 display:flex;
 justify-content:center;
}
```

![All items in horizontal structure with justified content set to "center".](https://teaching.computing.edgehill.ac.uk/wte/parts/10022/files/name/assets/justify-content-center-nav.png)

**Figure 12**: All items in horizontal structure with justified content set to "center".

As well as these three basic justification styles, we have some more powerful options, such as spacing the items out the full width of the parent element. To do this, we can set the justify-content to space-between (`justify-content:space-between;`) (See Figure 13).

```css
nav{
 border: 5px solid #000000;
 display:flex;
 justify-content:space-between;
}
```

![All items in horizontal structure with justified content set to "space between".](https://teaching.computing.edgehill.ac.uk/wte/parts/10022/files/name/assets/justify-content-space-between-nav.png)

**Figure 13**: All items in horizontal structure with justified content set to "space between".

Another option is to space the items evenly across the parent element but add space at the start and the end. This uses the value of space-around (`justify-content:space-around;`) (See Figure 14).

```css
nav{
 border: 5px solid #000000;
 display:flex;
 justify-content:space-around;
}
```

![All items in horizontal structure with justified content set to "space around".](https://teaching.computing.edgehill.ac.uk/wte/parts/10022/files/name/assets/justify-content-space-around-nav.png)

**Figure 14**: All items in horizontal structure with justified content set to "space around".

## The *Flex* property

*"Moving the items around is great, but how do we get the items to be spread across the parent using equal sizes"* I hear you ask.. well, for this, we can use the flex property. The flex property makes the flex-items become responsive inside of the parent flexbox container. To make the items take up the full space evenly, we set the flex property to a value of 1 (`flex:1;`) (See Figure 15).

```css
nav{
 border: 5px solid #000000;
 display:flex;
}

nav>p {
flex:1;
}
```

![All items in horizontal structure with flex property set to 1.](https://teaching.computing.edgehill.ac.uk/wte/parts/10022/files/name/assets/flex-1-nav.png)

**Figure 15**: All items in horizontal structure with flex property set to 1.

The power in this property means that we can cause different items to have different values. Let's make our contact button to be twice as wide as the others as in Figure 16:

```css
nav{
 border: 5px solid #000000;
 display:flex;
}

nav>p {
flex:1;
}

nav>p:nth-child(3) {
flex:2;
}
```

![All items in horizontal structure with flex property set to 1 for all p tags but nth child 3 (contact) set to flex of 2.](https://teaching.computing.edgehill.ac.uk/wte/parts/10022/files/name/assets/flex-contact-2-nav.png)

**Figure 16**: All items in horizontal structure with flex property set to 1 for all p tags but nth child 3 (contact) set to flex of 2.

*We will discuss nth-child in a later tutorial when we look at CSS in detail, but for now, all you need to know is that **nth-child(2)** is the second item, e.g. the about button and **nth-child(3)** is the third item, e.g. the contact button.*

If you take off the `flex:1;` rule from the `nav>p` style then you will see that the Contact button takes up all of the space available after the Home and about buttons take up only their content spacing.

## Positioning items using margin

Controlling all of the items together is excellent and will in a lot of use cases, be what you need. But there are often times when you want something a little different where not all items are doing the same or spaced the same.

What if we wanted to have our Contact button on the right but the other two on the left? Well, we can do this using the margin-left property (See Figure 17).

```css
nav{
 border: 5px solid #000000;
 display:flex;
}

nav>p:nth-child(3) {
margin-left:auto;
}
```

![Margin left set to auto on 3rd child element (contact).](https://teaching.computing.edgehill.ac.uk/wte/parts/10022/files/name/assets/margin-left-auto-nav.png)

**Figure 17**: Margin left set to auto on 3rd child element (contact).

The margin-left is calculating all of the space (width) left in the parent element, subtracting its own width from this and then applying the remainder as the value to the margin-left property. If you were to want the button to sit in the center of the space after the about button, then we could use the `margin:auto` which will take the width from the end of the about button to the end of the parent and then subtract its own width and then split the remainder between the left and right margins.

Now should we want to move both About and Contact over we can do this by only applying margin-left to the About. To do this you need to move your margin-left rule from your nav>p:nth-child(3) to nav>p:nth-child(2). Both the About and Contact move now because the Contact is after the About and so just gets drawn on screen after the About (See Figure 18).

```css
nav{
 border: 5px solid #000000;
 display:flex;
}

nav>p:nth-child(2) {
margin-left:auto; /* moved up from nth-child(3) */
}

nav>p:nth-child(3) {
}
```

![Margin left set to auto on 2nd child element (About).](https://teaching.computing.edgehill.ac.uk/wte/parts/10022/files/name/assets/margin-left-auto-about-nav.png)

**Figure 18**: Margin left set to auto on 2nd child element (About).

## Align items property

Align-items is not the same as justify-items. When flex-direction is set to row, justify-items controls the placement of items horizontally across the row, and align-items controls the vertical placement. However, should the flex-direction be set to column, the justify-items would control the vertical and align-items controls the horizontal.

Let us explore this a little bit. We will stick with our current nav, which uses the flex-direction set to row. To demonstrate this better, we need to give our parent flex-container a bit of height. Add a height of 300px to the nav flex-container (See Figure 19).

```css
nav{
 border: 5px solid #000000;
 display:flex;
 height: 300px;
}
```

![Height of 300 pixels added to elements.](https://teaching.computing.edgehill.ac.uk/wte/parts/10022/files/name/assets/add-height-nav.png)

**Figure 19**: Height of 300 pixels added to elements.

You will notice that the flex-items (the buttons) automatically fill the height of the parent container. There is some padding on each of the p tags; that is why there is white space at the top and bottom.

We can use align-items to control where the buttons sit. If we want them to sit at the top, then we would use the `align-items: flex-start;` rule (See Figure 20).

```css
nav{
 border: 5px solid #000000;
 display:flex;
 height: 300px;
 align-items: flex-start;
}
```

![align-items: flex-start.](https://teaching.computing.edgehill.ac.uk/wte/parts/10022/files/name/assets/align-items-flex-start-nav.png)

**Figure 20**: align-items: flex-start.

To align then to the center of the parent, we would use the value of center (See figure 21):

```css
nav{
 border: 5px solid #000000;
 display:flex;
 height: 300px;
 align-items: center;
}
```

![align-items: centre.](https://teaching.computing.edgehill.ac.uk/wte/parts/10022/files/name/assets/align-items-center-nav.png)

**Figure 21**: align-items: centre.

And to the bottom, we would use the value of flex-end (See Figure 22):

```css
nav{
 border: 5px solid #000000;
 display:flex;
 height: 300px;
 align-items: flex-end;
}
```

![align-items: flex-end.](https://teaching.computing.edgehill.ac.uk/wte/parts/10022/files/name/assets/align-items-flex-end-nav.png)

**Figure 22**: align-items: flex-end.

## Using align-items and justify-items together

The real power with these flexbox rules is that when used together, they allow you to achieve one of the things web developers have wanted to do since the creation of CSS but have not been able to, till Flexbox came out; perfectly centre an item in the parent. Perfect centring means both in width and height (See Figure 23).

With flex this is simply a case of applying `align-items: center;` and `justify-content: center;`.

```css
nav{
 border: 5px solid #000000;
 display:flex;
 height: 300px;
 align-items: center;
 justify-content: center;
}
```

![Perfectly centred nav using justify-content " centre" and align-items "centre".](https://teaching.computing.edgehill.ac.uk/wte/parts/10022/files/name/assets/perfect-centering-nav.png)

**Figure 23**: Perfectly centred nav using justify-content " centre" and align-items "centre".

## Align single flex-items

We can align single items on their own using the align-self property (See Figure 24):

```css
nav{
 border: 5px solid #000000;
 display:flex;
 align-items: center;
}

nav>p:nth-child(2) {
 align-self: flex-start
}
```

![Resetting align-items for seconf child only to "flex-start".](https://teaching.computing.edgehill.ac.uk/wte/parts/10022/files/name/assets/align-self-flex-start-nav.png)

**Figure 24**: Resetting align-items for second child only to "flex-start".

Here you can see that the align-self rule overrules the align-items rule of the parent.

**Have a go at trying to move the contact button to the bottom!**

## Flex-wrap

In float layouts, all items wrap onto the next row if the widths of the items do not fit on the row. In Flexbox, this is not true by default. By default, flexbox is set to no-wrap. This means that even though the widths are set to beyond the width of the parent's width, the items will be equally split between the items. Set the width of the p tags to something that is way beyond the width of the screen, say 500px (See Figure 25).

```css
nav{
 border: 5px solid #000000;
 display:flex;
}

nav>p {
width: 500px;
}
```

![Large widths set but still all show on one line.](https://teaching.computing.edgehill.ac.uk/wte/parts/10022/files/name/assets/500px-nav.png)

**Figure 25**: Large widths set but still all show on one line.

You should see that the items are equally split into the space.

Now, if we change the wrap of the flex container to allow wrapping, you will see that each item folds onto its own row because the 500px is larger than the row (See Figure 26).

```css
nav{
 border: 5px solid #000000;
 display:flex;
 flex-wrap: wrap;
}

nav>p {
width: 500px;
}
```

![Large width set but flex-wrap set to "wrap".](https://teaching.computing.edgehill.ac.uk/wte/parts/10022/files/name/assets/flex-wrap-500px-nav.png)

**Figure 26**: Large width set but flex-wrap set to "wrap".

Let's reduce the width of the items to something that allows multiple items to sit on a row but not all of them, let us say 360 pixels (See Figure 27).

```css
nav{
 border: 5px solid #000000;
 display:flex;
 flex-wrap: wrap;
}

nav>p {
width: 360px;
}
```

![Flex-wrap set to "wrap" and width of items set to 360 pixels allows two items to fit on a line, but the third wraps.](https://teaching.computing.edgehill.ac.uk/wte/parts/10022/files/name/assets/360px-nav.png)

**Figure 27**: Flex-wrap set to "wrap" and width of items set to 360 pixels allows two items to fit on a line, but the third wraps.

Here you can see that the third item gets folded onto the next row and leaves a gap at the end of the first row.

## Flex grow, shrink and basis

Earlier, we used the flex property to make all the flex-items responsive. This flex property is actually shorthand notation for using three properties: **flex-grow, flex-shrink, and flex-basis**.

Earlier we set the flex value to 1:

```css
nav>p {
    flex:1;
}
```

The equivalent long hand versions would be:

```css
nav>p {
    flex:1 1 0;
}
```

or

```css
nav>p {
    flex-grow: 1;
    flex-shrink: 1;
    flex-basis: 0;
}
```

Let's examine these three properties. The **flex-basis** property sets the initial main size of the flex-item.

The **flex-grow** property sets the dynamic grow amount of the flex-item. Basically, it determines how much of the available space in the flex container is given to this flex-item. Earlier, when we set this to 1 for all of the flex-items, it told the browser to divide the space in the flex-container equally between all of the flex-items.

The **flex-shrink** property sets the dynamic shrink factor of the flex-items. When a flex-item has a width or height set that is bigger than the size of the flex-container, the flex-shrink property controls how the item will shrink to fill the space in the flex-container.

Right, it is time to test this out. Remove the Contact p tag from your flexbox-nav.html, which would now look like:

```html
<body>
    <nav>
        <p>Home</p>
        <p>About</p>
    </nav>
</body>
```

In your flexbox-nav-styles.css file, ensure your nav container has a display of flex set, your home p tag has a flex-basis set to 200px, and your about p tag also has a flex-basis set to 200px. This will mean that both have a fixed size set and should take up only a fraction of your nav container (See Figure 28).

```css
nav {
    display: flex;
}

nav>p:nth-child(1) {
    flex-basis: 200px;
}

nav>p:nth-child(2) {
    flex-basis: 200px;
}
```

![Flex-basis set to 200 pixels.](https://teaching.computing.edgehill.ac.uk/wte/parts/10022/files/name/assets/flex-basis-200px-nav.png)

**Figure 28**: Flex-basis set to 200 pixels.

Having flex-basis set to 200px for each item means that both buttons will initially be set to 200px each, but if the container is smaller, then they will shrink to fit proportionately as can be seen in the Figure 29.

![Flex-basis set to 200 pixels and items shrinking to fit (animated  gif).](https://teaching.computing.edgehill.ac.uk/wte/parts/10022/files/name/assets/flex-basis-200px-nav.gif)

**Figure 29**: Flex-basis set to 200 pixels and items shrinking to fit (Animated gif).

If we now add flex-grow to the items, the result will be that it starts to act more like just setting flex, and all items will grow equally as the container expands (See Animated gif in Figure 30).

```css
nav {
    display: flex;
}

nav>p:nth-child(1) {
    flex-basis: 200px;
    flex-grow: 1;
}

nav>p:nth-child(2) {
    flex-basis: 200px;
    flex-grow: 1;
}
```

![Flex-basis set to 200 pixels and items shrinking to fit and with flex-grow set to 1 they expand fill the space (Animated gif).](https://teaching.computing.edgehill.ac.uk/wte/parts/10022/files/name/assets/flex-basis-200px-flex-grow-nav.gif)

**Figure 30**: Flex-basis set to 200 pixels and items shrinking to fit and with flex-grow set to 1 they expand fill the space (Animated gif).

If you just want one item to grow, then you can set flex-grow to 1 on the item that you want to expand and set flex-grow to 0 on the item you do not wish to expand (See Figure 31).

```css
nav {
    display: flex;
}

nav>p:nth-child(1) {
    flex-basis: 200px;
    flex-grow: 0;
}

nav>p:nth-child(2) {
    flex-basis: 200px;
    flex-grow: 1;
}
```

![Only one items set to expand.](https://teaching.computing.edgehill.ac.uk/wte/parts/10022/files/name/assets/flex-basis-200px-flex-grow-0-1-nav.gif)

**Figure 31**: Only one items set to expand.

As you can see above, the home button shrinks and expands but stops when it hits the flex-basis size of 200px where the about button now shrinks and expands.

Okay, so we have now looked at flex-basis and flex-grow, so let us examine flex-shrink.

Flex-shrink controls if you want the item to be allowed to shrink smaller than the set flex-basis size or not. From all of the above animations, you can see that both of the buttons shrink their width to a lot smaller than the 200px set on the flex-basis. To stop this, we can set the flex-shrink value to 0 (See the result in Figure 32).

```css
nav {
    display: flex;
}

nav>p:nth-child(1) {
    flex-basis: 200px;
    flex-grow: 0;
    flex-shrink: 1;
}

nav>p:nth-child(2) {
    flex-basis: 200px;
    flex-grow: 0;
    flex-shrink: 1;
}
```

![Items will not shrink past set width.](https://teaching.computing.edgehill.ac.uk/wte/parts/10022/files/name/assets/flex-basis-200px-flex-shrink-nav.gif)

**Figure 32**: Items will not shrink past set width.

In this example, we have set both items to not have any flex-grow and have set the home button to allow flex shrinking and the contact button to not. You should notice that when the container gets too small, the about button starts to go outside of the bounds of the container. When the container gets really small, the button even goes off the page. So this is something to be used only after some serious consideration and design, though.

## Order

Flexbox has a feature that allows you to re-order items visually. This means that the HTML is untouched. Add the extra p tag for the Contact button back into your HTML file.

```html
<body>
    <nav>
        <p>Home</p>
        <p>About</p>
        <p>Contact</p>
    </nav>
</body>
```

So you know the natural order (flow) of the HTML items is that they will appear from left to right as Home> About > Contact. But using the **order** property, we can change this, so let's change it to Home> Contact > About.

To make this change, we add the order property to the About button and set the value to 1. I have removed all of the long hand grow and shrink settings and reverted back to adding the flex shorthand property back on all p elements. For your code, you can simply add in the order if you like (See Figure 33).

```css
nav {
    display: flex;
}

nav>p {
    flex: 1;
}

nav>p:nth-child(2) {
    order: 1;
}
```

![Changing the order of items using the order property.](https://teaching.computing.edgehill.ac.uk/wte/parts/10022/files/name/assets/flex-order-nav.png)

**Figure 33**: Changing the order of items using the order property.

Order works based on the value of the number. In the above example, both Home and Contact have a default order value of 0, and we gave About an order value of 1, which is higher, and so the about button appears last.

To demonstrate this again and maybe a little more clearly, let's give the Home button an order value of 50; The About button an order value of 10 and the Contact button an order value of 30 (See Figure 34 for result).

```css
nav {
    display: flex;
}

nav>p {
    flex: 1;
}

nav>p:nth-child(1) {
    order: 50;
}

nav>p:nth-child(2) {
    order: 10;
}

nav>p:nth-child(3) {
    order: 30;
}
```

![Changing the order of items using the order property on multiple items.](https://teaching.computing.edgehill.ac.uk/wte/parts/10022/files/name/assets/flex-order-all-nav.png)

**Figure 34**: Changing the order of items using the order property on multiple items.

As you can see above in figure 34, the lowest order value of 10 for the about button starts the nav followed by the Contact that has an order value of 30 and lastly, there is the Home button that has the highest order value of 50.

This is quite a powerful tool and one that should be remembered.

## Nesting

Flexboxes can be placed inside of other flexboxes! So this means that a flex-item can be both the child of its parent but also be a parent to its children flex-items.

Just as an example, we can add a div inside of our Nav flex-container and then inside of the div add two p tags (See Figure 35).

```html
<body>
    <nav>
        <p>Home</p>
        <p>About</p>
        <p>Contact</p>
        <div>
            <p>Nested 1</p>
            <p>Nested 2</p>
        </div>
    </nav>
</body>
```

![Nesting items.](https://teaching.computing.edgehill.ac.uk/wte/parts/10022/files/name/assets/flex-nested1-nav.png)

**Figure 35**: Nesting items.

There are currently no styles set for our Div p elements, and so they use the default Flow and are stacked on top of each other. If we turn the div into a flex container using the `display: flex;` then the child p elements of the div will line up next to each other and be flex-items (See Figure 36). This means that they can be controlled exactly as you have just learnt but that these items are independent of the nav children.

![Nesting items controlled by flex.](https://teaching.computing.edgehill.ac.uk/wte/parts/10022/files/name/assets/flex-nested2-nav.png)

**Figure 36**: Nesting items controlled by flex.

Please have a play with the code on these and see how it works.

## Flex Nav Challenge

Can you get the nested items to be stacked on top of each other (but still be flex-items) with 'nested 2' on the top and both being the first items in the nav as in Figure 37 (without changing any HTML code)?

![Flex Navigation Challenge.](https://teaching.computing.edgehill.ac.uk/wte/parts/10022/files/name/assets/flex-nav-challenge.png)

**Figure 37**: Flex Navigation Challenge.

## Conclusion

So as you can see, Flexbox overall is very useful and, with certain properties, quite powerful. It has been abused and used for complete layouts in the past (before css-grid was released), but ideally, it should be used for creating and controlling components of a page, such as a navbar, and image gallery or product gallery.

## Next

Now please move on to the tutorial for Week 4 part 2 which will teach you about CSS-Grid. For your further learning the next page will highlight some more flexbox content you can engage with outside of class.
