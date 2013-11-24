storefront
==========

**CMS External Requirements**
This app is built using the Python (v2.7) framework Django (v1.3.1) using a PostgreSQL database and Apache/mod_wsgi (v3.3) deployment. It also makes use of the following Python modules:
* PIL: http://www.pythonware.com/products/pil/
* sorl-thumbnail: http://thumbnail.sorl.net/
* Django-MPTT: https://github.com/django-mptt/django-mptt
* Django Template Utils: https://bitbucket.org/ubernostrum/django-template-utils/
* Django Contact Form: https://bitbucket.org/ubernostrum/django-contact-form/
* Akismet: http://www.voidspace.org.uk/python/akismet_python.html
* Markdown: http://www.freewisdom.org/projects/python-markdown/

**The front-end development of the website makes use of the following:**
* Reset CSS: http://meyerweb.com/eric/tools/css/reset/
* jQuery 1.7.0: http://jquery.com/
* jQuery UI 1.8.16: http://jqueryui.com/
* Google Oswald font: http://www.google.com/webfonts/specimen/Oswald
* Infinite Carousel jQuery plugin: http://code.google.com/p/jquery-infinite-carousel/
* Modernizr: http://www.modernizr.com/
* Fancybox jQuery plugin: http://fancybox.net/

**Application Structure**
The CMS application is composed of the following applications, all located within the “storefront” project/directory:
* Apparel: Controls products and attributes such as features, colors and sizes
* Categories: Controls parent and child level categorization of products
* Media: Controls photos and photosets for relating images to products
* Auth: Controls users and groups (users w/varying permissions) within the CMS
* Flatpages: Controls one-off pages such as FAQ and About
* Redirects: Controls any redirect made within the starlightapparel.com domain (excludes subdomains)
* Sites: Not used outside initial deployment (don’t modify current values)
* Testimonials: Controls any testimonial used for display on the homepage
* Contact_form: Allows for logging messages sent using the contact form
