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
## Step 2: Install Python and Dependencies

Install Python 3 and pip:

bash
Copy code
sudo apt install python3 python3-pip
Install additional dependencies:

bash
Copy code
sudo apt install python3-venv

   
