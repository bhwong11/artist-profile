**===Project: Ransom Bergen Artist Profile===**

This is an Artist Profile and Art Showcase for writer and graphic design Ransom Bergen with the goal of people to buy his artwork. This will be a server rendered application using the Django Stack with a Postgres Database.

**===Main features:===**

Users will be able to view these 6 main pages:
home page showcasing a featured art piece and navigation to other pages

Artwork Showcase Page where all artwork that the artist will want featured is displayed and categorized but medium(painting, drawing, writing, graphic art)

Commissions page where users can request artwork via sending emails

Buy Artwork Page where users can buy premade art or prints(these would be links to product pages redbubble, a site for art buying)

Each product will have it’s own show page where full details will be display and users can also leave reviews

A contact page containing and email and social media platforms

A blog page containing updates and post from the artist

The Artist will be able to post art/products/blogs, and remove art/products/blogs and edit them as well.
External users will be able to create an account and create/edit/delete reviews for products

Each artwork, product, and blog can have tags added on to them to categorize them.

**===User Stories:===**

**User: potential customer**

Once the user enters the website( either from link or directly typing url into browser) the user will see a home page featuring the artist name and 3 featured artworks. By the later 2 featured artworks there will be text with a link to the “Buy Artwork” page and the “Commission's” page There will be a navigation bar to the “home page”, “artwork page”, “Commision”, “Buy Artwork”, “blog” and “contact” page.

When a user enters the artwork page(either from navigation link or directly typing in) the user will see images of artwork divided into categories of medium. Each image will have a title and tags attached below it as well. Users will also see a drop down menu where they can select a tag and see all artworks containing that tag. This page will also contain the navigation bar from the home page.
When a user enters the commission page(either from navigation link or directly typing in) the user will see on the right side of the page commission examples and on the left side rules, guidelines for permissions and an email contact to request a submission. This page will also contain the navigation bar from the home page.

When a user enters the Buy Artwork page the user will be able to see a series of product images with a title and a link to a show page for that artwork. These images will be categorized by art medium. This page will also contain the navigation bar from the home page.

Show pages will display an image of the product with the price of the product, a description of the product, reviews of the product that users can leave along with the reviewer name, and a button that will display a form to leave a review themselves. This page will also contain the navigation bar from the home page.

Users can leave a review by clicking the leave a review button.

If the user has a registered review creation account and is logged in a form will be displayed below the button and the user can leave a review by filling out the form containing a text box and clicking the submit button on the form. From submission the page will be reloaded with the new comment.

If a user is not logged in or does not have an account, when clicking the make comment button a form will appear where they can log in and once logged in they can click the button to create a review. If they do not have an account, there will be a link to another form where they can register for an account and be redirected to the login form.
Once logged in a logout button will appear next to the leave a review button, where if clicked will reload the page and set the leave a review button to the logged out state.

Once a review is made a user will be able to edit that review and any other reviews they made by clicking a edit or delete button on the review. If the edit button is clicked they will be able to see a form prefilled with the current review and be able to edit it. Once edited the page will reload and the new review will be seen. If the delete button is clicked a modal will show up asking for confirmation if this is an appropriate action. The page will be reloaded and the deleted review will not appear on the page.

All account registration and login forms will appear on the product show page

When a user enters the blog page they will see the most recent blog and as they scroll down they will see older blogs. Each blog will have a title displayed and text body as well as creation date. This page will also contain the navigation bar from the home page.

When the user enters the contact page they will see an email listed on the center of the page as well as icons linking to instagram and twitter. This page will also contain the navigation bar from the home page.

If a user tries to type in the url of a non-existent page, the website will display a page with “404 Error” displayed with the navigation bar from other pages.

If the user experiences a 500 server error, a web page will appear with the error displayed with the navigation bar from other pages.

**User: The Client**

This User will be able to view everything a potential customer user can but with these additions:

The Client User will be able to log in via a route ‘/loginadmin’ and the user which once logged in will be able to redirected to login

On the artwork page the user will be able to see a form that will allow them to add new artwork on the top of the page. The form will have an image input(choose file input), a title, and a drop down input of tags. The user will also be able to see 2 links on the bottom of each artwork image. One that will send them to a form to edit that artwork and one that will delete the artwork. If the delete button is selected a modal will appear asking for confirmation of deletion. Once an artwork has been made, edited, or deleted, the user will be redirected to the artwork page.

On the blog page the user will be able to see a form on top of the page that will have a title and text area input to add a new blog. Each existing blog will have 2 links on the bottom of each blog. One that will send them to a form to edit that blog and one that will delete the blog. If the delete button is selected a modal will appear asking for confirmation of deletion. Once a new blog has created, or existing blog has been edited or deleted the user will be redirect the the blogs page
On the product page the user will be able to see a form on top of the page that will have a title, text area input, buy link,image(choose file input), and price input to create a new product. Each existing product will have 2 links on the bottom of each product. One that will send them to a form to edit that product and one that will delete the product. If the delete button is selected a modal will appear asking for confirmation of deletion. Once a product has created, edited, or deleted the user will be redirect the the products page

On the contact page the user will be able to see two links at the bottom of the page. One that will send the user to an edit contact form where they can change contact information on social media or email. This form will have pre-filled values of the current contact information with social media appearing as links.

**===Wireframes:===**

Home page:
![Home Page](https://i.imgur.com/xmc3NCl.png)

Blogs:
![Blog Page](https://i.imgur.com/PREPGKQ.png)

Commissions:
![Comissions Page](https://i.imgur.com/OeY6srK.png)

Artwork
![Artwork Page](https://i.imgur.com/GYQACyA.png)

Products:
![Products Page](https://i.imgur.com/2ha7E9s.png)

Product Show Page:
![Products Show Page](https://i.imgur.com/R4DYjWq.png)

Product Show Page scroll down to reviews signed in:
![Review Signed in](https://i.imgur.com/3viOYlX.png)

Product Show Page scroll down to reviews signed out:
![Reviews Signed Out](https://i.imgur.com/eDXIFDe.png)

Register Button Modal(appears on button click of Register)
![Reviews Register](https://i.imgur.com/eCa0rtF.png)

Login Button Modal(appears on button click of Login)
![Review Login Button](https://i.imgur.com/NvAqRiJ.png)

Edit Review Page
![Review Edit Page](https://i.imgur.com/nhJQgg0.png)

Delete Review
![Delete Review](https://i.imgur.com/8vCiRxM.png)

Contact Page
![Contact Page](https://i.imgur.com/ByM4lGN.png)

Client User Login
![Client Login Page](https://i.imgur.com/S8AOQIO.png)

Client Product Page for Edit/Create/Delete
![Client Product Page](https://i.imgur.com/dRFv4Nx.png)

Artwork Page for Edit/Create/Delete
![Artwork Page](https://i.imgur.com/MBFSTW0.png)

Product/Artwork Create Page
![Product/Artwork Create Page](https://i.imgur.com/hM516ms.png)

Product/Artwork Edit Page
![Product/Artwork Edit Page](https://i.imgur.com/qD5qhYR.png)

Product/Artwork Delete Modal:
![Product/Artwork Delete](https://i.imgur.com/FpMdRdi.png)

**===Data Models ERD:===**
![ERD](https://i.imgur.com/ONIh3si.png)

**===Milestones:===**

Application is able to send back html response for 6 main pagers (home, blogs, commissions, artwork, buy, and contact) containing information from postgres database, as well as a show page for specific products (seed data for now) - 9/8

Client user is able to create, edit and delete Products, and only the client user will be able to do this - 9/9

Potential customer user is able to register, sign in, create reviews, edit reviews, and delete reviews - 9/10

Client user is able to create, edit and delete Artwork, and only the client user will be able to do this - 9/11

Client user is able to create, edit and delete Blogs, and only the client user will be able to do this - 9/12

All forms will have error handling and display an error if incorrect information is added in displaying an issue and refusing to admit data into database if incorrect - 9/14

Client user is not only able to add product/image artwork via image address but is able to upload on the site with image storage in s3 bucket -9/15

Entire website is styled - 9/16

Potential customer user is able to sort artwork by tags - 9/16(if time allows)

Potential customer user is able to search by artwork title - 9/16(if time allows)
