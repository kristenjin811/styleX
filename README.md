# STYLEX
## An Online Shopping Platform
Built fully-featured Python Django eCommerce website with advanced custom functionalities and RDS Postgres. The application is formed by four app directories and one project directory.


### Initializing all the services
To initialize all the services on a local development environment, simply activate the virtual environment and runserver in terminal with codes below.
```
source ./.venv/bin/activate
python manage.py runserver
```
### Application overview
<img src="static/images/readme/signin.png" alt="Alt text" title="checkout">
<img src="static/images/readme/homepage.png" alt="Alt text" title="checkout">
<img src="static/images/readme/homepage2.png" alt="Alt text" title="checkout">
<img src="static/images/readme/store.png" alt="Alt text" title="checkout">
<img src="static/images/readme/productdetail.png" alt="Alt text" title="checkout">
<img src="static/images/readme/shoppingcart.png" alt="Alt text" title="checkout">
<img src="static/images/readme/checkout.png" alt="Alt text" title="checkout">


## All API Endpoints runs on port 8000
### The accounts app
URLS to access the accounts app:


### The accounts app
URLS to access the accounts app:
- http://localhost:8000/api/accounts/
- http://localhost:8000/api/accounts/register/
- http://localhost:8000/api/accounts/login/
- http://localhost:8000/api/accounts/logout/
- http://localhost:8000/api/accounts/dashboard/
- http://localhost:8000/api/accounts/forgotPassword/
- http://localhost:8000/api/accounts/activate/<uidb64>/<token>/
- http://localhost:8000/api/resetPassword_validate/<uidb64>/<token>/
- http://localhost:8000/api/resetPassword/


### The carts app
URLS to access the carts app:
- http://localhost:8000/api/cart/
- http://localhost:8000/api/cart/add_cart/<int:product_id>/
- http://localhost:8000/api/cart/remove_cart/<int:product_id>/<int:cart_item_id>/
- http://localhost:8000/api/cart/remove_cart_item/<int:product_id>/<int:cart_item_id>/
- http://localhost:8000/api/cart/checkout/


### The store app
URLS to access the store app:
- http://localhost:8000/api/store/
- http://localhost:8000/api/store/category/<slug:category_slug>/
- http://localhost:8000/api/store/category/<slug:category_slug>/<slug:product_slug>/
- http://localhost:8000/api/store/search/