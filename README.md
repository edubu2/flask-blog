# Learning Flask by Creating a Blog

Big thank you to **Corey Schafer** for his YouTube Flask Tutorial ([link](https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH&ab_channel=CoreySchafer)), which gave me an outline for this project. I customized the site material with my information instead of his, but none of this is really my creation.

NOTE: The final application (served with Nginx) can be found here: [ewilens.com](https://www.ewilens.com)

## The code is broken up into two main branches: web-server and local-state
- web-server: Contains the production code running on the Linode VM
- local-state: Contains development application to test locally

## Tools Implemented
- Python3
- Flask for application framework
- Bootstrap for HTML, CSS & JS
- SQLAlchemy Database
- BCrypt Password Hashing
- Web serving with Nginx and Gunicorn on a virtual machine (Linode Cloud)
