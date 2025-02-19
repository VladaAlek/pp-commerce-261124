# Disaster Ready


This e-commerce project is focused on providing a user with learning material in the **Disaster Risk Reduction** field. It is an increasingly popular, multidisciplinary research area between natural and social sciences. Its multi-faceted results are implemented in everyday confrontations with natural hazards by numerous practitioners across the globe. The need to disseminate practical and theoretical knowledge about **DRR** grows with rapid changes in the natural and social environment. Hence, there are numerous potential users of this course. For practical reasons, this time, the project is limited to German-speaking countries *German, Austria and Switzerland*, the three countries that are exposed to *floods*, *stormy weather conditions*, *forest fires*, and *heat weaves* as the four most relevant natural disasters in this part of Europe.

Considering that the main users of the website's services will be municipality workers, this e-commerce platform is based on B2B principles.
When customers pay for specific services, they get an unlimited approach. In this stage of development, the option of offering a test to the user is indicated but not fully implemented. The same statement applies to the foreseen feature of booking consulting services from team members. 
Find out more about Disaster Ready E-Commerce Business Strategy here:  

- [1](docs/images/busines_strategy/0001.png);
- [2](docs/images/busines_strategy/0002.png);
- [3](docs/images/busines_strategy/0003.png);
- [4](docs/images/busines_strategy/0004.png);

### Type of commercial activity

## E-commerce Marketing Strategy

[Disaster Ready Germany SEO](https://drive.google.com/file/d/1z7MxM64oRXnc64d1jDV9fn02sncI2X6F/view?usp=drive_link "Disaster Ready Germany SEO")

### Facebook Busines Page

- [Link 09.01.2025](https://www.facebook.com/profile.php?id=61571470064318 "Disaster Ready Germany Facebook Busines Page")
- [Facebook Busines Page Screenshot](docs/images/facebook%20busines%20page.png);

### Sites main structure
 - log in/log out - see more in the Authentication section below
 - navigation bar
 - footer
 - landing page
 - all courses view
 - content of individual courses
 - - course content management as Admin - See section Superuser's features below
 - profile page
 - money transfer component

## Navigation

here are documented some of the major **navigation possibilities** provided to the final user

- [Index Page](docs/images/navigation/navigation%20to%20index%20page.png);
- [All Courses 1](docs/images/navigation/navigation%20all%20courses%20view%20LG.png);
- [All Courses 2](docs/images/navigation/navigation%20all%20courses%20view%20LG%202.png);
- [All Courses - Bag View](docs/images/navigation/navigation%20all%20courses%20from%20shopping%20bag%20view%20LG%203.png);
- [All Courses - Individual Course](docs/images/navigation/navigation%20to%20all%20and%20individiual%20courses.png);
- [All Courses - Dropping Menu](docs/images/navigation/navigation%20to%20all%20courses%20from%20Navigate%20dropping%20menu%20in%20the%20navbar.png);
- [Individual Course - Structure](docs/images/navigation/navigation%20to%20individual%20course%20structure%20page.png);
- [Individual Course - Content](docs/images/navigation/);


## Superuser's features

- Superuser can enter the **admin page**. There, it can monitor or adjust the 1. user's status, 2. content of the courses, 3. payment/ordering proccess. The CRUD operations are present.
- Superuser has access to the **product form** in which it can execute CRUD operations

### Authentication
- django-allauth==0.54.0
- [testing allauth](docs/images/testing_allauth.png);
- [testing "My Account" section 1](docs/images/loginTesting-1.png);
- [testing "My Account" section 2](docs/images/loginTesting-2.png);
- [testing "My Account" section 3](docs/images/loginTesting-3.png);

**new feature:** Only authenticated users are allowed to have access to a page with the learning materials

### Exploring and Selecting/Managing Courses

Being informed about the courses offered in this project is crucial. Upon landing on the index page, users can click the Explore Courses button. There, it can learn more about the basic structure of the *individual courses*. The basic logos are shown in the head section so that the particular courses are visually different from others. The following values *Difficulty Level*, *Credits*, *Number of Lectures*, *Short Description*, *Estimated Time*, *Starting date* and *Price* are displayed textually on this level.  The value *Test* is indicated with the appropriate [icons](docs/images/test%20exist.png). Logged superusers can edit or delete the content of individual courses [edit or delete](docs/images/edit%20and%20delete%20course%20categories.png). However, this option is exclusively available to [superusers](docs/images/resticted%20edit%20.png). By choosing the edit option, the [form page](docs/images/edit%20form.png) to edit the course's content opens. The functionality is tested: [step 1](docs/images/edit%20flood%201.png); [step 2](docs/images/edit%20flood%203.png). After the change have been submitted, the [popup message](docs/images/edit%20flood%202.png) informs the user about the consequences of his last activity.

This type of changes in the database is indicated by [message deleted](docs/images/message%20deleted.png) info in the popup field, too.

By clicking the Explore Course button, the page rendering the content of each course's *learning material* is visible. It is a combination of textual material and PDF and video material. In this stage of development, only the two latter are hidden from the user until the course fee is paid.  *Add this course to the bag" is centrally located and activates the *Bag* view.

This page offers a tabular overview of selected courses, their quantity, price, and discount (if activated). By wish, the *remove* link allows the User to eliminate the undesired course from the bag. The logos of individual courses serve as links, too. If categories logo is not availble, the projects  [logo](docs/images/bag_project_logo_display.png) will be rendered. Finally, the *Keep Exploring* link invites users to learn more about other courses and eventually add them to the shopping basket. button is available to finalize the shopping activities.

The *Checkout page* consists of two major sections: 1: Order Summary, which provides the overview of the User's shopping selection, and 2: Checkout Form, which makes it possible for the User to enter personal data. They serve both the site administrator and the User as a confirmation that the digital learning service is provided to the desired customer. In cases where the User is a *Registered User*, most fields are prepopulated with the User's account data. The idea is to improve the UI. The same goal is achieved when the User selects the *Save this delivery information to my profile* checkout field. Not less important is that even in this stage, the User has the *Adjust Bag* at its disposal. The last feature is the self-explanatory outcome. The essential part of the form field is the payment window dedicated to credit card data. Additionally, if categories logo is not availble, the projects  [logo](docs/images/project%20logo%20instead%20of%20category%20logo%20in%20checkout.png) will be rendered.


### *Seach Products Options in Navbar*  this task is not realised as it is a secondary project's feature

### Discount
If more than 1500 euros are spent, a 10% discount is offered on the index page. If this option is activated, the reduced price is visible in Navabar, in the Shopping Bag and Checkout templates, shopping confirmation details.


The Footer is present on minority pages, with the exception of the Checkout and Form Page. In the latter, significant additional styling is required, which was impossible shortly before the website's release.
This feature contains the link to the *Facebook Business Page* and subscription *Mailchimp*
- Remark: The Footer requires intensive additional styling

- [footer general view LG](docs/images/footer%20general%20view%20LG.png)
- [footer general view SM](docs/images/footer%20general%20view%20SM.png)

- [Mailchimp Success](docs/images/mailchimp%20success.png)
- [Mailchimp All Emails](docs/images/mailchimp%20success%20audience.png)



### Design Proces

#### Models

- [Category and Material models](docs/images/erd_category_material_models.png) in products app

- [Checkout Order Model](docs/images/checkout_order_model.png) in checkout app;
- [Checkout OrderLineItem_model Model](docs/images/checkout_OrderLineItem_model.png) in checkout app;
- [Checkout OrderLineItem_model Model Refactoring](docs/images/checkout_OrderLineItem_model_refactoring.png) in **Checkout app**;
- [User Profile Model](docs/images/UserProfile_model.png) in **Profiles app**;

- External Code Sources: [Crispy Bootstrap5 Documentation](https://django-bootstrap-v5.readthedocs.io/en/latest/installation.html "django-bootstrap-v5");  [Stack Overflow](https://stackoverflow.com/questions/71641974/implementing-django-bootstrap-crispy-forms-into-default-signup-login-pages "Stack Overflow.com")

#### Mockups

Considering the EC-nature of the project, the basic philosophy applied in this project is to deliver a uniform, tabular structure of how the data for individual courses or learning material is presented.

- [SM](docs/images/mockup/mockup_SM-1.png);
- [MD](docs/images/mockup/mockup_MD-1.png);
- [LG](docs/images/mockup/mockup_LG-1.png);

## Technologies Used:
 - Python 3.2.0
 - Django 3.2.25
 - Bootstrap 5
 - Stripe - for secure finacial transactions
 - Mailchimp - for User's subscriptions and mails services
 - Amazon AWS S3 - to storage video data
 - Heroku - to deploy the project

### Software Resources Used

### Icon's Source 
- [Font Awsome](https://fontawesome.com "fontawesome.com")
- [Bootstrap](https://icons.getbootstrap.com/icons/currency-euro/ "Bootstrap")


## Software Resources Used

- Git Version control was managed using Git, with commits executed via the Gitpod terminal and pushes directed to GitHub.
- GitHub The project's code is stored on GitHub after being pushed from Git.
- "Projects", "Milestones" and "Issues" functions embedded in GitHub utilised to apply AGILE concepts
- [HEROKU](https://www.heroku.com/ "HEROKU cloud platform") used to deploy and manage the applications.

## Deployment

- it was necessary to reestablish IDE (Gitpod) - [Django](docs/images/django_requirements_21_12_24.png); [Pillow](docs/images/pillow_requirements_21_12_24.png); [Allauth](docs/images/allauth_requirements_21_12_24.png);
- 28. 12. 2024. Gitpod IDE became unfunctional - unpushed changes were lost and reinstalling requirements and re-establishment of the settings parameters was necessary
- 05. 01. 2025. Gitpod IDE became unfunctional - a new workspace opened, which might affect some features because there was not enough time to test and document all project's elements again

## Dealing with Logo Images
 - The project's style in base.css is set to best suit the PNG image format. Hence, it is recommended that you use this format.

## Manual Testing - User's Registration

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
 - testing [ "Categories Page" M](docs/images/testing_courses_md.png);
 - testing [ "Categories Page" SM](docs/images/testing_add_course_functionality_shopping_bag.png);

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
- [Add Course Toast Bug](docs/images/Toast_Success_Add_Bug.png) Bad user experience noticed: add course message emerges multiple times
- [Add Course Refactored Bug](docs/images/Toast_Warning_Twice.png) Good user experience requires informing the user that he cannot add the same product two times
- [Warning Course Toast SM](docs/images/toast_warning_sm.png)
- [Delete Course](docs/images/Toast_Warning_Delete.png); [Delete Course Toast SM](docs/images/toast_allert_sm.png)
- message.error in the delete view was not tested
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
- [testing Payment Form Data Stripe Deteils](docs/images/checkout_success_stripe_developers_details.png)
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
- [Unlocked Course Indicator](docs/images/unlocked%20course.png) - "Add this course to the bag" changes color and text to "Course Unlocked"


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
- [Add products form - **Product management link in navbar functional**](docs/images/products%20form/Product%20management%20link%20in%20navbar%20functional.png);

### Products Form - Code After Refactoring 

The initial view *add_product* didnt allow to add the learning material content to the newly formed course in one template [**image**](docs/images/products%20form/bug%20adding%20course%20and%20material%20simultaniously%20impossible.png) because it was not created yet!
The refactored code includes two templates: *add_products* and *add_material*:
- [Add courses form - success](docs/images/products%20form/successfull%20added%20online%20course.png);
- [Add learning material form - success](docs/images/products%20form/successfull%20added%20online%20material.png);
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


### About page

- [Test](docs/images/error%20404%20documentation.png);

### Error Page

- [delete products form - **delete courses and materials - delete success**](docs/images/products%20form/delete%20course%20success%20button.png);


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

minor repositioning of the logo in the toast messages
[Original](docs/images/bugs/style%20images%20in%20the%20success%20messages.png);
[Refactored](docs/images/bugs/style%20images%20in%20the%20success%20messages%20refactored.png);

6 

The missing logo in the flood category caused broken links. After introducing an if item.product.log statement in the bag.html, the problem was solved. 
Instead of the custom logo, the default logo has been rendered.

[Missin Flood Logo in the "Shopping Bag"](docs/images/bugs/missing%20flood%20logo.png);
[Missin Flood Logo in the "Checkout"](docs/images/bugs/missing%20flood%20logo%20checkout.png);

7

The ids for individual categories are created [dynamicaly](docs/images/bugs/dynamic%20creation%20of%20categories_id.png), preventing this [error](docs/images/bugs/404%20page%20not%20found%20floods.png).

8 
**registration of a new user** - please, consult *registration section* above



During manual testing, a strange situation was noticed. Namely, all emails have the primary status, which should not be the case. However, they don't have access to the management panel.
Additionally, the regular registration flow was interrupted by this template: [conf itsector email bug](docs/images/confirmation_mails/conf%20itsector%20email%20bug.png). On the backend side, the accounts were formed only partially successfully because the action in the admin panel was necessary. Besides, the registration process was not visible on the frontend side. 


#### Unresolved Bug Issues

1

- [Added courses not rendering corectly](docs/images/bugs/bug_added%20courses%20not%20rendering%20corectly.png);

2 

- [Bug navbar links blocked when sign in open](docs/images/bugs/bug_navbar_links_blocked_when_signin_open.png);




### Image's Sources
 - [Flickr.com](https://www.flickr.com/photos/apfelauge/25528764266/in/photolist-ETTAd3-aruDcd-oybpY8-ars18K-ars1Sr-ars1qM-arrZ2e-arrZeB-arrZpV-ars1ye-aruDB3-arrYTK-aruD1A-2kypz9o-aruE9b-eHdPys-2kxmpUV-98weQw-9aL4ZS-98t6mT-2n6BFgN-2qhpUcR-9a6i7e-rGaTjQ-dFkWsU-ahaC5Z-eBNHfs-5sEf1V-6aFqEa-2nURaUe-7Qxk4N-2kxMii3-4NXPkq-4NXY91-4NXQMA-4NYfnC-4NXSyE-4NY3jU-4NU8rH-JkiUrD-QhphK4-4NY8um-4NY8Sh-4NY4iC-4NTA6K-4NTU7H-i8tXAS-4NXTYY-4NTTLr-4NXXk1/ "flickr.com")
 

Keep this as a template
[Next Only](docs/images/testing_allauth.png); [Prev Next](docs/images/testing_allauth.png); 

## Important Note
 - [Shopping Bag](https://github.com/users/VladaAlek/projects/16/) **Project** not visible in the project`s repo


**Acknowledgements:** Oisin, Thomas, Rebecca, Sarah, Roman, Holly.
