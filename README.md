# Host Django Project on Amazon EC2

This guide will walk you through the steps to host a Django project on an Amazon EC2 instance.

## Prerequisites

- An active AWS account
- Basic knowledge of AWS EC2 and Django
- Your Django project ready to be deployed

## Step 1: Set Up EC2 Instance

1. Launch an EC2 instance with your preferred operating system.
2. Connect to your EC2 instance using SSH.
3. Update the package repository:
   
   ```bash
   sudo apt update
   ```

## Step 2: Install Python and Dependencies

Install Python 3 and pip:

```bash
sudo apt install python3 python3-pip
```

Install additional dependencies:

## Step 3: Prepare Your Django Project
Navigate to the desired directory and create a folder for your Django project:

```bash
sudo mkdir djangoproject
```

cd djangoproject/

Set appropriate permissions:

```bash
sudo chown -R ubuntu:ubuntu djangoproject
```

Clone your Django project or copy your project files into the djangoproject directory.

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install project dependencies:

```bash
pip install -r requirements.txt
```

Run database migrations:

```bash
python manage.py migrate
```

## Step 4: Run the Django Server
Start the Django development server:

``` bash
python manage.py runserver 0.0.0.0:8000
```

(Optional) Run the server in the background using nohup:

```
bash
nohup python manage.py runserver 0.0.0.0:8000 &
```

Access your Django application using your EC2 instance's public IP address and port 8000 (e.g., http://<your-ec2-ip>:8000).

Notes
Make sure to configure security groups to allow inbound traffic on port 8000.
For production use, consider using a production-ready WSGI server like Gunicorn or uWSGI and a web server like Nginx or Apache.

```
bash

sudo apt install python3-venv
```

   
