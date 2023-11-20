
# Management Portal

## Introduction
The Management portal is a portal where we can manage teachers in a university. This portal also sends mail updates to teachers when any action (Addition/Updation/Deletion) is done on their data. I am planning to add the student Management also in this same software.

## Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Testing](#testing)
- [Installation](#installation)
- [Contributing](#contributing)
- [License](#license)

## Features

The Software has the following components

### Teachers
- Adding New Teachers
- Updating Teachers
- Deleting Teachers
- Searching Teachers
- Filtering Teachers Based on Age and Classes 
- Show All Teachers

### Students
- Adding New Students
- Updating Students
- Deleting Students
- Searching Students
- Show All Students

The Student Module is still under development

## Tech Stack

- Django: A powerful web framework for building scalable and secure applications
- Python: The programming language used for implementing the backend logic
- CockroachDB: A robust and reliable relational database management system for storing and retrieving data, distributed database with standard SQL for cloud applications.
- HTML: The markup language used for structuring the webpages
- Bootstrap 5: A powerful Library on CDN, feature-packed frontend toolkit.
- App Engine (GCP): Google App Engine is a cloud computing platform as a service for developing and hosting web applications in Google-managed data centers. Applications are sandboxed and run across multiple servers.
## Testing

Visit this URL to Test the Live Hosted Application: [Visit Site](https://rashw.in)

Email: admin
Password: admin

## Installation

To run the Management Portal Locally, Follow these steps:

1. Clone the repository to your local machine.
2. Install Python and the required dependencies by running 
```
pip install -r requirements.txt
```
3. Change the Line 84 in settings.py inside the management folder to the below code
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```
5. If you have SMTP Credentials Change enter the Credentials in line 131 and 132 in settings.py inside the management folder
```
EMAIL_HOST_USER = os.environ['EMAIL_USERNAME']
EMAIL_HOST_PASSWORD = os.environ['EMAIL_PASSWORD']
```
6. If you don't have SMTP Credentials Comment Line 5 to 11 inside the functions file inside utilities folder
```
def send_email(subject, body, email):
    #send_mail(
    #    subject,
    #    body,
    #    settings.EMAIL_HOST_USER,
    #    [email],
    #    fail_silently=True,
    #)
    
    return True
```
7. Migrate the models to MySQL by running the following commands:
```
python manage.py makemigrations
python manage.py migrate
```

8. Create a superuser account by running 
```
python manage.py createsuperuser
```

9. Run the server using
```
python manage.py runserver
```
10. Access the SIP Portal in your web browser at
```
http://localhost:8000
```

## Contributing

Contributions to the Management Portal are welcome. If you encounter any issues or have suggestions for improvements, please open an issue on the GitHub repository.

## License

The Management Portal is open-source software licensed under the [MIT License](LICENSE).


