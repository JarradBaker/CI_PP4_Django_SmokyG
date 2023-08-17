# Skate Shack
(Developer: Jarrad Baker)

![Mockup image](docs/responsive.png)

[Live webpage](https://jarradbaker.github.io/CI_PP1_SkateShack/)

## Table Of Contents

1. [Project Goals](#project-goals)
  1. [User Goals](#user-goals)
  2. [Website Owner Goals](#website-owner-goals)
2. [User Experience](#user-experience)
    1. [Target Audience](#target-audience)
    2. [User Requrements and Expectations](#user-requirements-and-expectations)
    3. [User Stories](#user-stories)
3. [Design](#design)
    1. [Design Choices](#design-choices)
    2. [Colour](#colour)
    3. [Fonts](#fonts)
    4. [Structure](#structure)
    5. [Wireframes](#wireframes)
4. [Technologies Used](#technologies-used)
    1. [Languages](#languages)
    2. [Frameworks and Tools](#frameworks-and-tools)
5. [Features](#features)
6. [Testing](#validation)
    1. [HTML Validation](#HTML-validation)
    2. [CSS Validation](#CSS-validation)
    3. [Accessibility](#accessibility)
    4. [Performance](#performance)
    5. [Device testing](#performing-tests-on-various-devices)
    6. [Browser compatibility](#browser-compatability)
    7. [Testing user stories](#testing-user-stories)
8. [Bugs](#Bugs)
9. [Deployment](#deployment)
10. [Credits](#credits)
11. [Acknowledgements](#acknowledgements)

## Project Goals

### User Goals
- Find good quality skateboards
- See examples of pricing for the products
- Learn more about skateboarding
- Find the location of the store
- Learn what makes this company different
- Learn how to use skateboards

### Website Owner Goals
- Reach the target audience
- Increase the traffic and sales
- Direct interaction with customers
- Show what makes this company different

## User Experience

### Target Audience
The website is designed with the following target audience in mind:
- Skateboarders looking to buy a new board
- People looking to get in to skateboarding
- Physical skating shops looking for stock
- Skateboarders looking to learn new tricks

### User Requirements and Expectations
- Simplistic user interface
- Smooth Navigation System
- Easy to find relevant information
- All social links direct to the correct website
- Presentation of content is clear
- Visually appealing design
- Accessibility
- Media and functions work as expected

### User Stories

#### First Time User
1. As a first time user, I want to understand the product
2. As a first time user, I want to learn about the company
3. As a first time user, I want to know how much the product costs
4. As a first time user, I want to learn more about skateboarding
5. As a first time user, I want to learn how to use the product
6. As a first time user, I want to ask questions about my order
7. As a first time user, I want to know why to choose this company
8. As a first time user, I want to be able to navigate the site easily

#### Returning User
9. As a returning user, I want to be able to contact the company
10. As a returning user, I want to learn more tricks
11. As a returning user, I want to learn where a physical store is
12. As a returning user, I want to look at products

#### Site Owner
13. As a site owner, I want users to find out about our products
14. As a site owner, I want users to have a good visual experience when using the website
15. As a site owner, I want users to be able to see a 404 page if anything goes wrong
16. As a site owner, I want to enrich our users' skateboarding experience

## Design

### Design Choices
The website was designed to give a "street" feel to the users, which is why a colder colour theme was used. The images of products and skateboarding were used to engage the users.

### Colour
Colour was a very important aspect for engaging with the audience, as anything too childish, or bright may put visitors off. For this reason, I chose to use a nice cold themed colour set for the website, providing a "street" feel. For accessibility reasons, the colours were tested on Webaim using their contrast checker, and the darkest and lightest colours got a contrast ratio of 12.78:1 meaning that they were a great fit.
![Colours image](docs/Colours.png)

### Fonts
The chosen font for the website was "Quicksand", with sans serif as a backup font. I originally also used "Lobster" for headings, but I found that "Quicksand" fitted in much better for my target audience and the feel of the site, so I used a higher weight for the headings to make it appear bolder.

### Structure
To keep the user interface as beginner friendly, and simple as possible, I went for a classic looking nav bar style. It is a simple layout with the logo to the left on desktops, and above on mobile. The theme remains the same throughout all four pages:
- Index page: Shows an image of a skateboarder and why you would choose the company. Also contains the history of the company.
- Tricks page: Gives explanations of how to perform various tricks, enriching the users skateboarding experience. Also has a video for each trick.
- Boards page: Allows the users to see the products that are available.
- Contact page: Gives users a chance to communicate with the company, and also shows a real map displaying where the physical store is.

### Wireframes
<details><summary>index</Summary>
<img src="docs/Validation/Performance/index.png">
</details>

<details><summary>blog</Summary>
<img src="docs/Validation/Performance/tricks.png">
</details>

<details><summary>post_detail</Summary>
<img src="docs/Validation/Performance/boards.png">
</details>

<details><summary>bookings</Summary>
<img src="docs/Validation/Performance/contact.png">
</details>

<details><summary>my_booking</Summary>
<img src="docs/Validation/Performance/404.png">
</details>

<details><summary>login</Summary>
<img src="docs/Validation/Performance/404.png">
</details>

<details><summary>register</Summary>
<img src="docs/Validation/Performance/404.png">
</details>

<details><summary>logout</Summary>
<img src="docs/Validation/Performance/404.png">
</details>

## Technologies Used

### Languages
The following languages were used to develop the website:
- HTML
- CSS
- Python3
- Django
- Javascript
- SQL

### Frameworks and Tools
The following frameworks and tools were used to develop the website:
- Git
- Github
- Gitpod
- Google Fonts
- Font Awesome
- Balsamiq
- Favicon.io

## Features
The website contains 5 pages including the 404 page, and a total of 13 features

### Header (logo and navigation)
- Shows on every page
- The nav links stack under the logo on smaller screens making it responsive
- Enables easy and smooth navigation
- The current page is highlighted in blue
- User Stories: 8, 14
<details><summary>Header</Summary>
<img src="docs/features/Header.png">  
</details>

### Footer
- Shows on every page like the header
- Like the header, the social links also stack underneath the copyright text on smaller screens
- User Stories: 2, 8, 14
<details><summary>Footer</Summary>
<img src="docs/features/Footer.png">  
</details>


## Validation

### HTML Validation

The Nu HTML Checker (W3C) is used to validate HTML documents. This ensures that all unintended mistakes are spotted before release, so that they can be corrected. All of my pages passed the check without any errors, including the 404 page.

<details><summary>index</Summary>
<img src="docs/Validation/Performance/index.png">
</details>

<details><summary>blog</Summary>
<img src="docs/Validation/Performance/tricks.png">
</details>

<details><summary>post_detail</Summary>
<img src="docs/Validation/Performance/boards.png">
</details>

<details><summary>bookings</Summary>
<img src="docs/Validation/Performance/contact.png">
</details>

<details><summary>my_booking</Summary>
<img src="docs/Validation/Performance/404.png">
</details>

<details><summary>login</Summary>
<img src="docs/Validation/Performance/404.png">
</details>

<details><summary>register</Summary>
<img src="docs/Validation/Performance/404.png">
</details>

<details><summary>logout</Summary>
<img src="docs/Validation/Performance/404.png">
</details>

### CSS Validation

The W3C Jigsaw CSS Validation Service is used in exactly the same way as the Nu HTML Validator, but for CSS. I ran both my actual style.css file, and an actual web page through it, and both passed without any errors.

<details><summary>Web Page</Summary>
<img src="docs/Validation/CSS/CSS.png">
</details>

<details><summary>Stylesheet</Summary>
<img src="docs/Validation/CSS/stylesheet.png">
</details>

### Accessibility

The WAVE web accessibility evaluation tool by WebAIM was used to ensure the webpages met accessibility standards. All 5 pages passed without any errors.

<details><summary>index</Summary>
<img src="docs/Validation/Performance/index.png">
</details>

<details><summary>blog</Summary>
<img src="docs/Validation/Performance/tricks.png">
</details>

<details><summary>post_detail</Summary>
<img src="docs/Validation/Performance/boards.png">
</details>

<details><summary>bookings</Summary>
<img src="docs/Validation/Performance/contact.png">
</details>

<details><summary>my_booking</Summary>
<img src="docs/Validation/Performance/404.png">
</details>

<details><summary>login</Summary>
<img src="docs/Validation/Performance/404.png">
</details>

<details><summary>register</Summary>
<img src="docs/Validation/Performance/404.png">
</details>

<details><summary>logout</Summary>
<img src="docs/Validation/Performance/404.png">
</details>

### Performance

The Google Lighthouse tool, within the Google Chrome Developer Tools was used to ensure that each page met a high performance rating. This shows that the website will load efficiently over various devices.

<details><summary>index</Summary>
<img src="docs/Validation/Performance/index.png">
</details>

<details><summary>blog</Summary>
<img src="docs/Validation/Performance/tricks.png">
</details>

<details><summary>post_detail</Summary>
<img src="docs/Validation/Performance/boards.png">
</details>

<details><summary>bookings</Summary>
<img src="docs/Validation/Performance/contact.png">
</details>

<details><summary>my_booking</Summary>
<img src="docs/Validation/Performance/404.png">
</details>

<details><summary>login</Summary>
<img src="docs/Validation/Performance/404.png">
</details>

<details><summary>register</Summary>
<img src="docs/Validation/Performance/404.png">
</details>

<details><summary>logout</Summary>
<img src="docs/Validation/Performance/404.png">
</details>

### Performance tests on various devices

Throughout development and testing, I used the following devices to ensure that the site was responsive, and worked as intended.

- Samsung Galaxy ZFold 5 (both ultra slim mode, and wide mode)
- Microsoft Surface Book 2 (Both as the laptop, and tablet)
- Macbook Pro
- Desktop PC with a 32" monitor

### Browser Compatibility

The website was tested on several web browsers to ensure consistency. The browsers used are as follows:

- Microsoft Edge
- Google Chrome
- Brave Browser (A Chrome based browser)
- Mozilla Firefox
- Opera GX

### Testing User Stories

1. As a first time user, I want to understand the product

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Tricks | Navigate to the Tricks page and find any Trick | See the tricks | Works as expected |
| Trick Videos | Navigate to the Tricks page and find any Trick Video | See the trick videos | Works as expected |
| Why Choose Us? | Navigate to the Home page and scoll down | See the Why Choose Us? section | Works as expected |
| Boards | Navigate to the Boards page | See the page containing all the products | Works as expected |
| Products | Navigate to the Boards page, and scroll down | See all of the products available | Works as expected |

<details><summary>Screenshots</Summary>
  <details><summary>Tricks</Summary>
    <img src="docs/Validation/UserStoryTests/TricksTest.png">
  </details>
  <details><summary>Tricks Videos</Summary>
    <img src="docs/Validation/UserStoryTests/TricksVideosTest.png">
  </details>
  <details><summary>Why Choose Us?</Summary>
    <img src="docs/Validation/UserStoryTests/WhyChooseUsTestStep1.png">
    <img src="docs/Validation/UserStoryTests/WhyChooseUsTestStep2.png">
  </details>
  <details><summary>Boards</Summary>
    <img src="docs/Validation/UserStoryTests/BoardsTest.png">
  </details>
  <details><summary>Products</Summary>
    <img src="docs/Validation/UserStoryTests/ProductsTest.png">
  </details>
</details>


## Bugs

| **Bug** | **Fix** |
|---------|---------|
| Blog posts not loading correctly | Changed the URL mapping, as the changes for loading the actual post_detail broke the originals |
| Model and Admin view for the blog posts | The admin view was very messy. Tidied by loading and arranging by certain columns |
| Comments not adding correctly | Accidentally referred to the blog variable instead of post |

## Deployment

The website was deployed through the use of GitHub Pages, a feature built in to GitHub. This can be done by following the steps below.
1. In the desired repository, click on "Settings" from the top menu.
2. From the side menu to your left, select "Pages" in the "Code and automation" section.
3. Make sure the "Source" option is set to "Deploy from a branch"
4. Select the desired "Branch" from the drop down below (main branch in most cases, making sure the director is set to /(root)).
5. Select "Save", and after it refreshes the page, you will see a box at the top of the page providing you with the URL of your now published site.

You can fork my, or any other repository by doing the following.
1. Go to the desired repository
2. Click "Fork" in the upper right corner
3. Select the owner, and set the repository name. A description can be added if desired
4. Choose whether to copy the default branch, or all branches
5. Click "Create Form"

You can clone a repository by following the steps below.
1. Go to the desired repository
2. Click the "Code" button at the top of the files section of the page
3. Select your desired method for cloning (HTTPS/SSH/GitHub CLI)
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory
6. Type "git clone", and then paste the URL you copied earlier. It will look like this, with your GitHub username instead of "YOUR-USERNAME": "$ git clone https://github.com/YOUR-USERNAME/DESIRED-REPOSITORY"
7. Press Enter. Your local clone will be created.

## Credits

### Media

#### Images

- The logo, hero image, and product images were all provided by the client "Smoky G".


### Code

- HTML: "i" tags with the icons and the social media link icons were all imported from FontAwesome.
- CSS: The font "Lobster" and "Lobster 2" were imported from Google Fonts.

## Acknowledgements

I would like to take this opportunity to acknowledge and thank the following people:
- My mentor Mo Shami for continuous guidance and support.
- My mother, who always encouraged me to strive for a career that I enjoy.
- My peers on the Code Institute Slack channels, for advice and feedback.
- My partener Kirsty, for her belief in me, supporting me, encouraging me, and giving me the invaluable time needed to develop my skills
