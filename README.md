# Django CMS 4 example app to demonstrate the use of app_hook and having a model with editable cms elements through render_placeholder.

Current status: Working with help of fsbraun, thank you so much! 

An example for a template generated django CMS 4 installation with a installed demonstrator django "shop" app with a very basic product model linked with an app_hook to django CMS.

To run:

1. Create virtual environment and activate it
   ```
   python3 -m venv .venv
   . .venv/bin/activate
   ```
2. Install Django, django CMS and other required packages
   ```
   pip install -r requirements.txt
   ```
3. Sqlite database is included and contains example data

4. Start Django server
   ```
   python3 manage.py runserver 0:8000
   ```
5. Login as admin to CMS backend
   ```
   http://localhost:8000/admin
   Login: django
   Password: django
   ```
6. Open shop page containing render_placeholder
   ```
   http://localhost:8000/shop/1st_product/
   ```

7. Press the 'edit' button in the cms toolbar to edit the product description
