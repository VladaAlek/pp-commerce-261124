# Disaster Ready


This e-commerce project is focused on providing a user with learning material in the **Disaster Risk Reduction**field. It is an increasingly popular, multidisciplinary research area between natural and social sciences. Its multi-faceted results are implemented in everyday confrontations with natural hazards by numerous practitioners across the globe. The need to disseminate practical and theoretical knowledge about **DRR** grows with rapid changes in the natural and social environment. Hence, there are numerous potential users of this course. For practical reasons, this time the project is limited to German-speaking countries *German, Austria and Switzerland*, the three countries that are exposed to *floods*, *stormy weather conditions*, *forest fires*, and *heat weaves* as the four most relevant natural disasters in this part of Europe.

### Sites main structure
 - log in/log out - on this topic more in the Authentication section below
 - navigation bar
 - landing page
 - all courses view
 - content of individual courses
 - profile page
 - money transfer component

### Design Proces

- [Category and Material models](docs/images/erd_category_material_models.png) in products app

- [Checkout Order Model](docs/images/checkout_order_model.png) in checkout app;
- [Checkout OrderLineItem_model Model](docs/images/checkout_OrderLineItem_model.png) in checkout app;
- [Checkout OrderLineItem_model Model Refactoring](docs/images/checkout_OrderLineItem_model_refactoring.png) in checkout app;

- External Code Sources: [Crispy Bootstrap5 Documentation](https://django-bootstrap-v5.readthedocs.io/en/latest/installation.html "django-bootstrap-v5");  [Stack Overflow](https://stackoverflow.com/questions/71641974/implementing-django-bootstrap-crispy-forms-into-default-signup-login-pages "Stack Overflow.com")

## Technologies Used:
 - Python 3.2.0
 - Django 3.2.25
 - Bootstrap 5

### Authentication
- django-allauth==0.54.0
- [testing allauth](docs/images/testing_allauth.png);
- [testing "My Account" section 1](docs/images/loginTesting-1.png);
- [testing "My Account" section 2](docs/images/loginTesting-2.png);
- [testing "My Account" section 3](docs/images/loginTesting-3.png);


### Software Resources Used

### Icon's Source 
- [Font Awsome](https://fontawesome.com "fontawesome.com")
- [Bootstrap](https://icons.getbootstrap.com/icons/currency-euro/ "Bootstrap")


## Software Resources Used

- Git Version control was managed using Git, with commits executed via the Gitpod terminal and pushes directed to GitHub.
- GitHub The project's code is stored on GitHub after being pushed from Git.
- "Projects", "Milestones" and "Issues" functions inbeded in GitHub utilized to apply AGILE concepts
- [HEROKU](https://www.heroku.com/ "HEROKU cloud platform") used to deploy and manage the applications.

## Deployment

- it was necessary to reestablish IDE (Gitpod) - [Django](docs/images/django_requirements_21_12_24.png); [Pillow](docs/images/pillow_requirements_21_12_24.png); [Allauth](docs/images/allauth_requirements_21_12_24.png);
### Testing Responsivness
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
- [Add Course Toast Bug](docs/images/Toast_Success_Add_Bug.png) Bad user experiance noticed: add course messege emerges multiple times
- [Add Course Refactored Bug](docs/images/Toast_Warning_Twice.png) Good user experince requires to inform the user that he cannot add the same product two times
- [Warning Course Toast SM](docs/images/toast_warning_sm.png)
- [Delete Course](docs/images/Toast_Warning_Delete.png); [Delete Course Toast SM](docs/images/toast_allert_sm.png)
- message.error in the delete view was not tested
- [external source material -seaching for the ID value in the Courses](https://stackoverflow.com/questions/59738782/check-if-id-in-string-exists-in-another-list)

### Testing Checkout Models and Admin Page
- [Checkout Admin](docs/images/admin_order_view.png)
- [Checkout Admin Add Courses](docs/images/admin_order_view_add_products.png)
- [Checkout Template Incomplete Rendering](docs/images/check_out_template_incomplete.png)
- [Checkout Template Complete Rendering](docs/images/check_out_template_complete.png)

### Checkout Responsivnes
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


### Checkout Logo Rendering Bug
- [Logo Rendering Bug](docs/images/checkout_organisation_logo_bug.png)



### Image Source
 - [Flickr.com](https://www.flickr.com/photos/apfelauge/25528764266/in/photolist-ETTAd3-aruDcd-oybpY8-ars18K-ars1Sr-ars1qM-arrZ2e-arrZeB-arrZpV-ars1ye-aruDB3-arrYTK-aruD1A-2kypz9o-aruE9b-eHdPys-2kxmpUV-98weQw-9aL4ZS-98t6mT-2n6BFgN-2qhpUcR-9a6i7e-rGaTjQ-dFkWsU-ahaC5Z-eBNHfs-5sEf1V-6aFqEa-2nURaUe-7Qxk4N-2kxMii3-4NXPkq-4NXY91-4NXQMA-4NYfnC-4NXSyE-4NY3jU-4NU8rH-JkiUrD-QhphK4-4NY8um-4NY8Sh-4NY4iC-4NTA6K-4NTU7H-i8tXAS-4NXTYY-4NTTLr-4NXXk1/ "flickr.com")
 

Keep this as a template
[Next Only](docs/images/testing_allauth.png); [Prev Next](docs/images/testing_allauth.png); 

## Important Note
 - [Shopping Bag](https://github.com/users/VladaAlek/projects/16/) project not visible in the project`s repo