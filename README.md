# Disaster Ready


This e-commerce project is focused on providing a user with learning material in the **Disaster Risk Reduction** field. It is an increasingly popular, multidisciplinary research area between natural and social sciences. Its multi-faceted results are implemented in everyday confrontations with natural hazards by numerous practitioners across the globe. The need to disseminate practical and theoretical knowledge about **DRR** grows with rapid changes in the natural and social environment. Hence, there are numerous potential users of this course. For practical reasons, this time, the project is limited to German-speaking countries, *Germany, Austria and Switzerland*, the three countries exposed to *floods*, *stormy weather conditions*, *forest fires*, and *heat weaves* as the four most relevant natural disasters in this part of Europe.

Considering that the website's main users will be municipality workers, this e-commerce platform is based on B2B principles.
When customers pay for specific services, they get an unlimited approach. In this stage of development, the option of offering a test to the user is indicated but not fully implemented. The same statement applies to the foreseen feature of booking consulting services from team members. It should be available on the *About* page.

### Types of commercial activities

Find out more about Disaster Ready E-Commerce Business Strategy here:  

- [1](docs/images/busines_strategy/0001.png);
- [2](docs/images/busines_strategy/0002.png);
- [3](docs/images/busines_strategy/0003.png);
- [4](docs/images/busines_strategy/0004.png);


## E-commerce Marketing Strategy

[Disaster Ready Germany SEO](https://drive.google.com/file/d/1z7MxM64oRXnc64d1jDV9fn02sncI2X6F/view?usp=drive_link "Disaster Ready Germany SEO")

### Facebook Business Page

- [Link 09.01.2025](https://www.facebook.com/profile.php?id=61571470064318 "Disaster Ready Germany Facebook Business Page")
- [Facebook Business Page Screenshot](docs/images/facebook%20busines%20page.png);

### Sites main structure
 - log in/log out - see more in the Authentication section below
 - navigation bar
 - footer
 - landing page
 - all courses view
 - content of individual courses
 - course content management as Admin - See section Superuser's features below
 - profile page
 - money transfer component
- About page

## Navigation

Here are documented some of the major **navigation possibilities** provided to the final user

- [Index Page](docs/images/navigation/navigation%20to%20index%20page.png);
- [All Courses 1](docs/images/navigation/navigation%20all%20courses%20view%20LG.png);
- [All Courses 2](docs/images/navigation/navigation%20all%20courses%20view%20LG%202.png);
- [All Courses - Bag View](docs/images/navigation/navigation%20all%20courses%20from%20shopping%20bag%20view%20LG%203.png);
- [All Courses - Individual Course](docs/images/navigation/navigation%20to%20all%20and%20individiual%20courses.png);
- [All Courses - Dropping Menu](docs/images/navigation/navigation%20to%20all%20courses%20from%20Navigate%20dropping%20menu%20in%20the%20navbar.png);
- [All Courses - Dropping Menu with a Refactored View](docs/images/individual%20category%20view%20refactored.png);
- [Individual Course - Structure](docs/images/navigation/navigation%20to%20individual%20course%20structure%20page.png);
- [Individual Course - Content](docs/images/navigation/);
- [**Navigate Drop-down Menu** in the Navbar with links to *Home*, *Courses*, *About Disaster Research* and *Subscribe* links](docs/images/subscribe%20link.png);


## Superuser's features

- The superuser can enter the **admin page**. It can monitor or adjust the 1. user's status, 2. course content, and 3. payment/ordering process. The CRUD operations are present.
- The Superuser has access to the **product form** to execute CRUD operations.

### Authentication
- django-allauth==0.54.0
- [testing allauth](docs/images/testing_allauth.png);
- [testing "My Account" section 1](docs/images/loginTesting-1.png);
- [testing "My Account" section 2](docs/images/loginTesting-2.png);
- [testing "My Account" section 3](docs/images/loginTesting-3.png);

## Authentication Visual indicators in the Navbar

- [Icon the User is **Blocked**](docs/images/my%20account%20locked%20navbar.png);
- [Icon the User is **Unblocked**](docs/images/my%20account%20unlocked%20navbar.png);

### Profile Page

This feature is by default [locked](docs/images/profile%20page%20locked.png), and it [opens](docs/images/profile%20page%20unlocked.png) only for logged users in the dropdown menu when clicking on the "my account" section in the Navbar. The [user's name](docs/images/users%20name%20on%20the%20profile%20page.png) is rendered in the welcome message to make navigation easier. The profile page has a [dual puprose](docs/images/profile%20design.png). On the user's left side is a form to enter the user's delivery data and to confirm the identity. This information can be changed/corrected/adjusted by clicking the **update information** button. The [message](docs/images/update%20profile.png) is present to indicate the changes in the profile's data. The right side provides the *Order History*. 


### Exploring and Selecting/Managing Courses

Being informed about the courses offered in this project is crucial. 

The *Seach Courses* Options in Navbar allow for querying the learning material based on the search words coming from:

 - [categories name 1](docs/images/search%20cat%201.png); [categories name 2](docs/images/search%20cat%202.png)
 - [short description 1](docs/images/search%20short%201.png); [short description 2](docs/images/search%20short%202.png)
 - [long descriptio 1](docs/images/search%20long%201.png); [long descriptio 2](docs/images/search%20long%202.png)
 - Functionality was tested in the [development](docs/images/search%20development.png) stage, too.

 The messages improve the UI by indicating that [no criteria have been entered](docs/images/search%20no%20criteria.png) in the search field or that [no categories found matching your search.](docs/images/seacht%20no%20match%20message.png).
 
Upon landing on the index page, users can click the *Explore Courses* button. There, it can learn more about the basic structure of the *individual courses*. The basic logos are shown in the head section so that the particular courses are visually different from others. The following values: *Difficulty Level*, *Credits*, *Number of Lectures*, *Short Description*, *Estimated Time*, *Starting date* and *Price* are displayed textually on this level.  The value *Test* is indicated with the appropriate [icons](docs/images/test%20exist.png) in specific colors to raise the user's attention on this feature (**note:** the same feature present on the [individual course view](docs/images/test exist individual category.png)). Logged superusers can edit or delete the content of individual courses [edit or delete](docs/images/edit%20and%20delete%20course%20categories.png). However, this option is exclusively available to [superusers](docs/images/resticted%20edit%20.png). By choosing the edit option, the [form page](docs/images/edit%20form.png) to edit the course's content opens. The functionality is tested: [step 1](docs/images/edit%20flood%201.png); [step 2](docs/images/edit%20flood%203.png). After the change has been submitted, the [popup message](docs/images/edit%20flood%202.png) informs the user about the consequences of his last activity.

To prevent unintentional deletion, a safety net in the form of a deletion modal has been introduced: [step 1](docs/images/test%20deletion%20modal.png); [step 2](docs/images/test%20deletion%20modal%201.png). 

The deletion of the part of a database is indicated by [message deleted](docs/images/message%20deleted.png) 
info in the popup field, too [Source code](https://getbootstrap.com/docs/4.1/components/modal/ "Bootstrap Modal Documentation").

**New feature:** Only authenticated users can access a page with the learning materials.

By clicking the **Explore Course button**, the page rendering the content of each course's *learning material* is visible. It is a combination of textual material and PDF and video material. In this stage of development, only the two latter are hidden from the user until the course fee is paid.  *Add this course to the bag"* is centrally located and activates the *Bag* view.

This page offers a tabular overview of selected courses, their quantity, price, and discount (if activated). By wish, the *remove* link allows the User to eliminate the undesired course from the bag. The logos of individual courses serve as links to individual categories view, too. This feature makes it easier to understand the connections between the course overview and its content. If the category logo is unavailable, the project's  [logo](docs/images/bag_project_logo_display.png) will be rendered. Finally, the *Keep Exploring* link invites users to learn more about other courses and eventually add them to the shopping basket. At the lower end of the page, a button is available to finalize the shopping activities.

The *Checkout page* consists of two major sections: 1: Order Summary, which provides the overview of the User's shopping selection, and 2: Checkout Form, which makes it possible for the User to enter personal data. They serve both the site administrator and the User as a confirmation that the digital learning service is provided to the desired customer. In cases where the User is a *Registered User*, most fields are prepopulated with the User's account data. The idea is to improve the UI. The same goal is achieved when the User selects *Save this delivery information* in the My Profile checkout field. The last feature is the self-explanatory outcome. Not less important is that even in this stage, the User has the *Adjust Bag* at its disposal. It will lead him to the bag page, where it is possible to delete the unwanted courses from the shopping bag. Additionally, if the categories logo is not availble, the projects  [logo](docs/images/project%20logo%20instead%20of%20category%20logo%20in%20checkout.png) will be rendered.

The essential part of the form field is the payment window dedicated to credit card data. Upon successful payment the [message](docs/images/email%20in%20production%201.png) will indicate the number of the order, as well as the [email](docs/images/email%20in%20production%202.png) ([Gmail View](docs/images/email%20in%20production%203.png)) where the order details are going to be sent ([test in development stage](docs/images/email%20in%20development.png)). 

The data about purchased courses is stored in profiles/models/PurchasedCourse model/database. This feature ensures that unlogged users do not lose access to purchased courses.

The icons **locked** or **unlocked** in appropriate colours of red or green are rendered on the [categories purchase status](docs/images/locked_unlocked.png) - [categories purchase status restyled](docs/images/locked_unlocked%20categories.png) and [individual_categor purchase status](docs/images/locked_unlocked%20ind%20category.png).

### Discount
If more than 1500 euros are spent, a 10% discount is offered on the index page, too. If this option is activated, the reduced price is visible in Navabar, while in the [Shopping Bag](docs/images/discount_bag.png) and [shopping confirmation details](docs/images/discount_checkout_success.png) the amount of saved money is indicated. The later is located on the *Profile page*.*

*About Page* begins with a centred heading **About Disaster Ready - Germany** and another call-to-action button for exploring online courses. The main content includes an introductory section describing the platform’s mission to enhance emergency preparedness through digital learning. Below this, a instructor profile cards present experts specializing in various disaster-related fields, including dummy links to instructor's profiles. As mentioned earlier in this text, this would be an ideal place to add *Make an Appoitment* feature in the further stages of the project's development. An additional section highlights recent public events related to disaster communication. At a very end, a promotional message offers a tempting discount on online courses.

## Mailchimp

- User subscription is located on the *Profile page*. The user who shared data to form the profile is presumed to continue with this activity and subscribe to our periodical letter.


#### Mailchimp Design and Responsivness

- [SM](docs/images/profile%20page%20SM.png); [MD](docs/images/profile%20page%20MD.png); [LG](docs/images/profile%20page%20LG.png);


## Footer
This feature is present on almost all pages. It contains the link to the [*Facebook Business Page*](docs/images/facebook%20busines%20page.png). Hover effect contributes to the interactivity UI experience. 

- [footer general view SM](docs/images/footer_sm.png);
- [footer general view LG](docs/images/footer_md.png);
- [footer general view LG](docs/images/footer_1.png);

### Error Page

- [Test](docs/images/error%20404%20documentation.png);

### Design Proces

#### Models

- [Category and Material models](docs/images/erd_category_material_models.png) in the **Products app**;
- [Checkout Order Model](docs/images/checkout_order_model.png) in the **Checkout app**;
- [Checkout OrderLineItem model](docs/images/checkout_OrderLineItem_model.png) in the **Checkout app**;
- [Checkout OrderLineItem model Refactoring](docs/images/checkout_OrderLineItem_model_refactoring.png) in the **Checkout app**;
- [User Profile Model](docs/images/UserProfile_model.png) in the **Profiles app**;
- [PurchasedCourse Profile Model](docs/images/model_purchased_course.png) in the **Profiles app**;

- External Code Sources: [Crispy Bootstrap5 Documentation](https://django-bootstrap-v5.readthedocs.io/en/latest/installation.html "django-bootstrap-v5");  [Stack Overflow](https://stackoverflow.com/questions/71641974/implementing-django-bootstrap-crispy-forms-into-default-signup-login-pages "Stack Overflow.com")

#### ERD
- [ERD Category](docs/images/ERD%20Category.png) in **Products app**; 
- [ERD Material](docs/images/ERD%20Material.png) in **Products app**; 
- [ERD UserProfile](docs/images/ERD%20UserProfile.png) in **Profiles app**;
- [ERD PurchasedCourse](docs/images/erd_purchased_course) in **Profiles app**;
- [ERD Order](docs/images/model_order.png) in **Checkout**;
- [ERD OrderLineItem](docs/images/model_order_line_item.png) in **Checkout**;

#### Mockups

Considering the EC-nature of the project, the basic philosophy applied in this project is to deliver a uniform, tabular structure of how the data for individual courses or learning material is presented.

- [SM](docs/images/mockup/mockup_SM-1.png);
- [MD](docs/images/mockup/mockup_MD-1.png);
- [LG](docs/images/mockup/mockup_LG-1.png);

## Technologies Used:
 - Python 3.2.0
 - Django 3.2.25
 - Bootstrap 5
 - MySQL in the developmnet stage and Postgress in the production stage
 - Stripe - for secure finacial transactions
 - Mailchimp - for User's subscriptions and mail services
 - Amazon AWS S3 - to store video data
 - Heroku - to deploy the project
 

### Software Resources Used

### Icon's Source 
- [Font Awsome](https://fontawesome.com "fontawesome.com")
- [Bootstrap](https://icons.getbootstrap.com/icons/currency-euro/ "Bootstrap")


## Software Resources Used

- Git Version control was managed using Git, with commits executed via the Gitpod terminal and pushes directed to GitHub.
- GitHub The project's code is stored on GitHub after being pushed from Git.
- "Projects", "Milestones" and "Issues" functions embedded in GitHub utilised to apply AGILE concepts
- [HEROKU](https://www.heroku.com/ "HEROKU cloud platform") is used to deploy and manage the applications.

## Deployment

- it was necessary to reestablish IDE (Gitpod) - [Django](docs/images/django_requirements_21_12_24.png); [Pillow](docs/images/pillow_requirements_21_12_24.png); [Allauth](docs/images/allauth_requirements_21_12_24.png);
- 28. 12. 2024. Gitpod IDE became unfunctional - unpushed changes were lost and reinstalling requirements and re-establishment of the settings parameters was necessary
- 05. 01. 2025. Gitpod IDE became unfunctional - a new workspace opened, which might affect some features because there was not enough time to test and document all the project's elements again.

## Dealing with Logo Images
 - The project's style in base.css is set to best suit the PNG image format. Hence, it is recommended that you use this format.

## Automated Testing

**Profiles App**
- [test_forms.py](docs/images/test%20profiles%20test_forms.png) - *test_form_is_valid* passed, because it was populated with correct arguments. The test *test_form_missing_required_fields* was deliberately designed to fail bacauese of the false assertion that profile_form.is_valid().

**Products App**
- [test profiles test_forms](docs/images/test_category_form_valid_data.png) - *passed*, because it was populated with correct arguments.
- [test_category_form_missing_required_fields](docs/images/test_category_form_missing_required_fields.png) - *passed*, because it was deliberately designed to fail bacauese of the false assertion that profile_form.is_valid().
- [Test products views (test_views for **category_detail**)](docs/images/test_product_views.png):
- test_render_individual_category_page_for_authenticated_user - *passed* becauese the user was authenticated; 
- test_render_individual_category_page_for_unauthenticated_user - *failed* authenticated user could access the rendered content;
- [Test products views (test_add_category_view for: **add_course**](docs/images/test_add_course_successful.png). Test passed because the post_data was field with the correct data (exception: course_logo was left out of the database)

## Manual Testing

 - User's Registration

### Development
- [Registration Form](docs/images/registration/sign_up_development.png); [Confirmation Email Sent](docs/images/registration/sign_up_development_1.png);
[Registration Email Confirmed](docs/images/registration/sign_up_development_3.png); [Registration Success](docs/images/registration/sign_up_development_4.png);

### Production

- [Registration Form](docs/images/registration/sign_up_production.png); [Confirmation Email Sent](docs/images/registration/sign_up_production_1.png); 
[Email Content](docs/images/registration/sign_up_production_2.png); [Registration Email Confirmed](docs/images/registration/sign_up_production_3.png); 
[Registration Success](docs/images/registration/sign_up_production_4.png); [Profile Page of the New User](docs/images/registration/sign_up_production_5.png); 
[User Account in the Admin Panel](docs/images/registration/sign_up_production_6.png); 

- [external source material - Django-AllAuth ACCOUNT_CONFIRM_EMAIL_ON_GET confusion](https://stackoverflow.com/questions/28248647/django-allauth-account-confirm-email-on-get-confusion)

### Testing Responsiveness

#### All Courses
 - testing ["Categories Page" XL and L](docs/images/testing_courses_lg.png);
 - testing ["Categories Page" M](docs/images/testing_courses_md.png);
 - testing ["Categories Page" SM](docs/images/testing_add_course_functionality_shopping_bag.png);
 - UI [unstyled](docs/images/categories%20unstyled.png); [styled](docs/images/categories%20styled.png);

 #### Individual Course
 - testing [ "Category Page" SM - 1](docs/images/responsivnes_individual_course_sm.png);
 - testing [ "Category Page" SM - 2](docs/images/responsivnes_individual_course_sm_1.png);
 - testing [ "Category Page" MD - 1](docs/images/responsivnes_individual_course_md_1.png);
 - testing [ "Category Page" MD - 2](docs/images/responsivnes_individual_course_md_2.png);
 - testing [ "Category Page" LG - Bug](docs/images/responsivnes_individual_course_lg_bug.png);

#### Bag
- testing ["Bag" XL and L](docs/images/testing_bag_big_size.png);
- testing ["Bag" XL and L rotated](docs/images/testing_bag_big_size_rotated.png);
- testing ["Bag" M](docs/images/testing_bag_medium_size.png);
- testing ["Bag" M rotated](docs/images/testing_bag_medium_size_rotated.png);
- testing ["Bag" SM with bug](docs/images/testing_bag_small_size_bug.png);
- testing ["Bag" Trashold functionality](docs/images/testing_trashold_functionality.png);
- testing ["Bag" Reverse functionality bug](docs/images/testing_reverse_functionality.png);
- testing ["Bag" Solving Reverse functionality bug 1](docs/images/solving_reverse_functionality_1.png);
- testing ["Bag" Solving Reverse functionality bug 2](docs/images/solving_reverse_functionality_2.png);
- testing ["Bag" Bag Icon not visible when bag is empty](docs/images/testing_bag_not_visible.png);
- testing ["Bag" Bag Icon visible when bag is not empty](docs/images/testing_bag_visible.png);

### Testing Add Courses Functionality

- [Initial Testing](docs/images/testing_add_course_functionality.png)
- [Multiple Items Testing](docs/images/testing_add_course_functionality_multiple_courses.png)
- [Multiple Items Testing](docs/images/testing_add_course_functionality_multiple_courses.png)


### Testing Toasts

- [Add Course Toast](docs/images/Toast_Success_Add.png); [Add Course Toast SM](docs/images/toast_success_sm.png)
- [Add Course Toast Bug](docs/images/Toast_Success_Add_Bug.png) Bad user experience noticed: add course message emerges multiple times.
- [Add Course Refactored Bug](docs/images/Toast_Warning_Twice.png) Good user experience requires informing the user that he cannot add the same product two times
- [Warning Course Toast SM](docs/images/toast_warning_sm.png)
- [Delete Course](docs/images/Toast_Warning_Delete.png); [Delete Course Toast SM](docs/images/toast_allert_sm.png)
- message.error in the delete view was not tested.
- [external source material - searching for the ID value in the Courses](https://stackoverflow.com/questions/59738782/check-if-id-in-string-exists-in-another-list)

### Testing Checkout Models and Admin Page
- [Checkout Admin](docs/images/admin_order_view.png)
- [Checkout Admin Add Courses](docs/images/admin_order_view_add_products.png)
- [Checkout Template Incomplete Rendering](docs/images/check_out_template_incomplete.png)
- [Checkout Template Complete Rendering](docs/images/check_out_template_complete.png)

### Checkout Responsiveness
- [Checkout SM 1](docs/images/check_out_template_SM_1.png); [Checkout SM 2](docs/images/check_out_template_SM_2.png)
- [Checkout MD 1](docs/images/check_out_template_MD_1.png); [Checkout MD 2](docs/images/check_out_template_MD_2.png)
- [Checkout LG](docs/images/check_out_template_LG.png)

### Checkout Card Input Form Initial Test

- [Checkout Inspect JS](docs/images/Card_Input_Form_JS.png)
- [Checkout Template](docs/images/Card_Input_Form_Template.png)
- [Checkout Wrong Bank Number](docs/images/Card_Input_Form_Wrong_Banknumber.png)
- [Checkout Dummy Bank Number](docs/images/Card_Input_Form_Dummy_Banknumber.png)
- [Checkout Style Bug](docs/images/Card_Input_Style_Bug.png)
- [Checkout Input Validation Error](docs/images/Card_Input_Validation_Error.png)

### Checkout Payment Intent
- [Terminal Report](docs/images/Payment%20Intent%20Terminal%20Report.png)
- [Terminal Report Status Field](docs/images/Payment%20Intent%20Terminal%20Report%20Status.png)
- [Payment Intent Succeeded Stripe Report](docs/images/Payment%20Intent%20Succeeded.png)

### Checkout Payment Form Data
- [testing Payment Form Data Template](docs/images/checkout_success.png)
- [testing Payment Form Data Stripe](docs/images/checkout_success_stripe_developers.png)
- [testing Payment Form Data Stripe Details](docs/images/checkout_success_stripe_developers_details.png)
- [testing Payment Form Data Terminal](docs/images/checkout_terminal.png)
- [testing Payment Form Data Admin](docs/images/checkout_admin.png)
- [testing Payment Form Data Admin Changed Order](docs/images/checkout_admin_changed_order.png)


### Checkout Page-overlay and Load-spinner

- [testing](docs/images/checkout_3d_security.png)

### Testing Checkout Success Template Responsiveness
- [SM 1](docs/images/Order%20Confirmation%20SM.png); [SM 2](docs/images/Order%20Confirmation%20SM%202.png); [SM 3](docs/images/Order%20Confirmation%20SM%203.png);
- [MD 1](docs/images/Order%20Confirmation%20MD.png); [MD 2](docs/images/Order%20Confirmation%20MD%202.png); [MD 3](docs/images/Order%20Confirmation%20MD%203.png);
- [LG 1](docs/images/Order%20Confirmation%20LG.png); [LG 2](docs/images/Order%20Confirmation%20LG%201.png);

### Testing Checkout Unlocking Paid Courses

- [Locked Course](docs/images/locked%20course.png); 
- [Unlocked Course](docs/images/unlocked%20course.png);
- [Unlocked Course Indicator](docs/images/unlocked%20course.png) - "Add this course to the bag" changes color and text to "Course Unlocked".


### Testing Form Data Cashing Template
[Terminal](docs/images/form_data_cashing_terminal.png); [Template](docs/images/form_data_cashing_template.png);

### Testing Web Hook Functionality

- [Stripe Form Template](docs/images/stripe_final_check_template.png); [Stripe Form Order Confirmation](docs/images/stripe_final_check_order_confirmation.png); 
- [Stripe Form Developers](docs/images/stripe_final_check_developers_1.png); [Stripe Form Status and Shipping](docs/images/stripe_final_check_developers_status_shipping.png); 
- [Stripe Form Billing](docs/images/stripe_final_check_developers_billing.png);  [Stripe Form Meta](docs/images/stripe_final_check_developers_meta.png); 
- [Stripe Form Receipt](docs/images/stripe_final_check_developers_receipt.png); 


### Checkout Logo Rendering Bug
- [Logo Rendering Bug](docs/images/checkout_organisation_logo_bug.png)

### Testing Profile App

- [Basic Profile Template](docs/images/Profile_Template.png); [User Account Data visible in Profile Template Test](docs/images/Profile_Template_Test.png);
- [rendering Form Profile Template](docs/images/Profile_Form_Template_Test.png);
- [Update Delivery Info User Profile 1](docs/images/Update_Profile_Form_Template_Test_Documentation.png);
- [Update Delivery Info User Profile SM](docs/images/Update_Profile_Form_Template_Test.png);
- [Update Delivery Info User Profile MD](docs/images/Update_Profile_Form_Template_Test_MD.png);
- [Update Delivery Info User Profile LG](docs/images/Update_Profile_Form_Template_Test_LG.png);

### Testing Order History

- [Order History Initial Stage](docs/images/order%20history%20good.png);
- [Order History after updating form](docs/images/order%20history%20010125.png);
- [Order Confirmation Updated](docs/images/order%20history%20010125.png);
- [Order Confirmation Whole Screen](docs/images/order%20confirmation%20whole%20screen.png);
- [Order Confirmation Bug](docs/images/order%20confirmation%20010125.png); It was not possible to change the profile data.


### Testing Save Profile Info Checked
- [Save Info Checked Terminal](docs/images/Save%20Info%20Checked%20Terminal.png);
- [Save Info Checked Template](docs/images/Save%20Info%20Checked%20Template.png);
- [Save Info Checked Order History 1](docs/images/Save%20Info%20Checked%20Order%20History%201.png);
- [Save Info Checked Order History 2](docs/images/Save%20Info%20Checked%20Order%20History%202.png);


### Products Form - Initial Development

#### ADD
- [Add products form - **Only category model values visible**](docs/images/products%20form/add%20products%20form%20only%20category%20model%20values.png);
- [Add products form - **Category and Material models values visible**](docs/images/products%20form/add%20products%20form%20category%20and%20material%20models%20values%20.png) the shortcoming: short description value present two times;
- [Add products form - **Category and Material models values visible**](docs/images/products%20form/add%20products%20material%20title.png) refactored code: short_description replaced with material_title value;
- [Add products form - **Category and Material models values visible - upper part**](docs/images/products%20form/add%20products%20form%20category%20and%20material%20models%20values%20upper%20part.png);
- [Add products form - **Category and Material models values visible - lower part**](docs/images/products%20form/add%20products%20form%20category%20and%20material%20models%20values%20lower%20part.png);
- [Add products form - **Responsiveness SM**](docs/images/products%20form/add%20products%20form%20SM.png);
- [Add products form - **Responsiveness MD**](docs/images/products%20form/add%20products%20form%20MD.png);
- [Add products form - **Responsiveness LG**](docs/images/products%20form/add%20products%20form%20LG.png);
- [Add products form - **success message**](docs/images/products%20form/add%20products%20success.png);
- [Add products form - **error message**](docs/images/products%20form/add%20products%20error.png);
- [Add products form - **rendering added course in categories template**](docs/images/products%20form/added%20course%20rendered%20in%20cagetories%20template.png);
- [Add products form - **rendering added course in materials template**](docs/images/products%20form/added%20course%20rendered%20in%20materials%20template.png);
- [Add products form - **Product management link in Navbar functional**](docs/images/products%20form/Product%20management%20link%20in%20navbar%20functional.png);

### Products Form - Code After Refactoring 

The initial view *add_product* didn't allow to add the learning material content to the newly formed course in one template [**image**](docs/images/products%20form/bug%20adding%20course%20and%20material%20simultaniously%20impossible.png) because the category was not created yet! 
The refactored code includes two templates: *add_products* and *add_material*:
- [Add courses form - success](docs/images/products%20form/successfull%20added%20online%20course.png);
- [Add learning material form - success](docs/images/products%20form/successfull%20added%20online%20material.png);

The templates stress that material can be added only after the category has been created.
- [Course](docs/images/add%20category%20info.png);
- [Material](docs/images/add%20material%20info.png);

- We couldn't make the forms fail. Hence, the 'error messages' have not been tested.


#### EDIT
- [Edit products form - **rendering edit courses and materials**](docs/images/products%20form/edit%20courses%20and%20materials.png);
- [Edit products form - **edit courses and materials - success 1**](docs/images/products%20form/edit%20courses%20and%20materials%20success.png);
- [Edit products form - **edit courses and materials - success 2**](docs/images/products%20form/edit%20courses%20and%20materials%20success%202.png);
- [Edit products form - **edit courses and materials - error**](docs/images/products%20form/edit%20courses%20and%20materials%20error.png);
- [Edit products form - **edit courses and materials - edit button 1**](docs/images/products%20form/test%20update%20course%20success%20button.png);
- [Edit products form - **edit courses and materials - edit button 2**](docs/images/products%20form/test%20update%20course%20success%20button%202.png);
- [Edit products form - **edit courses and materials - success**](docs/images/products%20form/test%20update%20course%20success%20button.png);

#### DELETE
- [delete products form - **delete courses and materials - delete success**](docs/images/products%20form/delete%20course%20success%20button.png);

- [delete products form - **delete courses and materials - delete success**](docs/images/products%20form/delete%20course%20success%20button.png);

###  Validation

#### W3C Markup Validation Service

- [base.html and home.html](docs/images/validation/validation%20base%20home.png);
- [categories.html](docs/images/validation/validation%20categories.png);
- [individual_category.html](docs/images/validation/validation%20individual%20category.png);
- [material.html](docs/images/add%20material%20info.png);
- [add_course.html](docs/images/validation/validation%20add%20course.png);
- [add_material.html](docs/images/validation/validation%20add%20material.png);
- [edit_products.html](docs/images/validation/validation%20edit.png);
- [bag.html](docs/images/validation/validation%20bag.png);
- [checkout.html](docs/images/validation/validation%20checkout%20address%20method.png);
- [checkout_success.html](docs/images/validation/validation%20checkout%20success.png);
- [validation profile error.html](docs/images/validation/validation%20profile%20error.png). This error is most probably caused by the fact that validator doesn't have access to the private data.
- [validation profile upload document method.html](docs/images/validation/validation%20profile%20file%20update.png). The errors in the report are caused by specificity of the Django syntax.
- [about.html](docs/images/validation/validation%20about.png);
- [error_404.html load file method](docs/images/validation/validation%20error%20page%20file%20upload.png); [error_404.html address method](docs/images/validation/validation%20error%20page%20file%20upload.png);
- [signup.html](docs/images/validation/validation%20signup.png);
- [login.html](docs/images/validation/validation%20login.png);
- [logout.html](docs/images/validation/validation%20logout.png);

#### W3C CSS Validation Service

- [project/static/base](docs/images/validation/css/validation%20css%20base.png);
- [products/static/products.css](docs/images/validation/css/validation%20css%20products%20file.png);
- [bag/static/bag.css](docs/images/validation/css/validation%20css%20bag%20file.png);
- [checkout/static/checkout.css](docs/images/validation/css/validation%20css%20checkout%20file.png);
- [profile/static/profile.css](docs/images/validation/css/validation%20css%20profile%20file.png);

 #### [Pythonium Linter Service](https://pythonium.net/linter)

 - **Project Level** [views](docs/images/pythonium/project_views.png); [URLs](docs/images/pythonium/project_URLs.png); [ASGI](docs/images/pythonium/project_ASGI.png); [WSGI](docs/images/pythonium/project_WSGI.png); [settings](docs/images/pythonium/project_settings.png);

 - **About App** [views](docs/images/pythonium/about_view.png); [URLs](docs/images/pythonium/about%20URLs.png);

 - **Bag App** [views](docs/images/pythonium/bag_views.png); [URLs](docs/images/pythonium/bag_URLs.png); [context](docs/images/pythonium/bag_context.png); 
 

 - **Checkout App** [views](docs/images/pythonium/checkout_views.png); [URLs](docs/images/pythonium/checkout_URLS.png); [webhooks](docs/images/pythonium/checkout_webhooks.png); 
 [WH](docs/images/pythonium/checkout_webhook%20handler%20OK.png); [WH error](docs/images/pythonium/checkout_webhook%20handler%20error.png); 
 [signals](docs/images/pythonium/checkout_signals.png); [model](docs/images/pythonium/checkout_models.png); [forms](docs/images/pythonium/checkout_forms.png); 

 - **Home App** [views](docs/images/pythonium/home_views.png); [URLs](docs/images/pythonium/home_URLs.png); 

 - **Products App** [views](docs/images/pythonium/products_views.png); [URLs](docs/images/pythonium/products_URLs.png); [widgets](docs/images/pythonium/products_widgets.png); 
 [models](docs/images/pythonium/products_models.png); [forms](docs/images/pythonium/products_forms.png); [admin](docs/images/pythonium/products_admin.png);

 - **Profile App** [views](docs/images/pythonium/profiles_view.png); [URLs](docs/images/pythonium/profiles_URLs.png); [models](docs/images/pythonium/profiles_models.png);
 [forms](docs/images/pythonium/profiles_forms.png); 


### Bugs
#### Resolved Bug Issues
1
- [Grand Total not visible in Navbar for the amounts > 1500](docs/images/bugs/bug_grand_total_navbar.png);
- [Grand Total not visible - resolved](docs/images/bugs/bug_grand_total_navbar_resolved.png);

2
- [default URLnoimage file rendered when custom image file not provided](docs/images/bugs/default%20URLnoimage%20file%20rendered%20when%20custom%20image%20file%20not%20provided.png);

3

- [all views failed](docs/images/bugs/all%20views%20retriving%20404%20eror.png);
EXTERNAL SOURCES:
    - [Stack Overflow](https://stackoverflow.com/questions/67215329/why-am-i-getting-error-404-in-my-django-project-when-everything-seems-correct "Stack Overflow.com");
    - [Stack Overflow](https://stackoverflow.com/questions/68050309/why-do-i-get-an-404-error-in-part-4-of-the-django-tutorial-writing-you-first-dj "Stack Overflow.com");

4 

- The organisation's Logo is visible in the Navbar

5 

- minor repositioning of the logo in the toast messages
[Original](docs/images/bugs/style%20images%20in%20the%20success%20messages.png);
[Refactored](docs/images/bugs/style%20images%20in%20the%20success%20messages%20refactored.png);

6 

- The missing logo in the flood category caused broken links. After introducing an if item.product.log statement in the bag.html, the problem was solved. 
Instead of the custom logo, the default logo has been rendered.

[Missin Flood Logo in the "Shopping Bag"](docs/images/bugs/missing%20flood%20logo.png);
[Missin Flood Logo in the "Checkout"](docs/images/bugs/missing%20flood%20logo%20checkout.png);

7

- The IDs for individual categories are created [dynamically](docs/images/bugs/dynamic%20creation%20of%20categories_id.png), preventing this [error](docs/images/bugs/404%20page%20not%20found%20floods.png).

8 
**registration of a new user** - please consult *registration section* above.


#### Unresolved Bug Issues

1

- [Bug Navbar links blocked when sign in open](docs/images/bugs/bug_navbar_links_blocked_when_signin_open.png);


### Image's Sources
 - [Flickr.com](https://www.flickr.com/photos/apfelauge/25528764266/in/photolist-ETTAd3-aruDcd-oybpY8-ars18K-ars1Sr-ars1qM-arrZ2e-arrZeB-arrZpV-ars1ye-aruDB3-arrYTK-aruD1A-2kypz9o-aruE9b-eHdPys-2kxmpUV-98weQw-9aL4ZS-98t6mT-2n6BFgN-2qhpUcR-9a6i7e-rGaTjQ-dFkWsU-ahaC5Z-eBNHfs-5sEf1V-6aFqEa-2nURaUe-7Qxk4N-2kxMii3-4NXPkq-4NXY91-4NXQMA-4NYfnC-4NXSyE-4NY3jU-4NU8rH-JkiUrD-QhphK4-4NY8um-4NY8Sh-4NY4iC-4NTA6K-4NTU7H-i8tXAS-4NXTYY-4NTTLr-4NXXk1/ "flickr.com").
 

## Important Note
 - [Shopping Bag](https://github.com/users/VladaAlek/projects/16/) **Project** is not visible in the project`s repo.


**Acknowledgements:** Oisin, Thomas, Rebecca, Sarah, Roman, Holly.
