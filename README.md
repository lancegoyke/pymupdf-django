```shell
# Create virtual environment
python -m venv .venv

# Activate virtual environment
source .venv/bin/activate

# Install dependencies
python -m pip install -r requirements.txt

# Create database
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run server to check that install worked
python manage.py runserver

# Navigate to http://localhost:8000/ and check for landing page
curl http://localhost:8000/

# Copy .env.example to .env
cp .env.example .env
```

## AWS Configuration

You'll need an AWS account to use test the S3 storage backend.

### AWS IAM User

Sign in to the AWS console and create an IAM user at https://us-east-1.console.aws.amazon.com/iam/home?region=us-east-2#/users

In step 2 for setting permissions, you can click "Attach existing policies directly" and select "AmazonS3FullAccess".

### AWS IAM User Credentials

Once you've created the IAM user, you'll need to create an access key for the user.

[Select the user](https://us-east-1.console.aws.amazon.com/iam/home?region=us-east-2#/users) and click "Security credentials" in the left sidebar.

Click "Create access key" and save the access key ID and secret access key. You may need to select and accept the type of application. I used "Local code" and said I was okay not using an IDE to configure the credentials.

Add these keys to your .env file.

Then copy your User ARN before heading to the next step.

## AWS S3 Configuration

You'll need an AWS S3 bucket to store media files.

Sign in to the AWS console and create a bucket at https://us-east-2.console.aws.amazon.com/s3/bucket/create.

I turned off the "Block all public access" option and enabled ACLs.

You'll need to create a bucket policy to allow the IAM user to access the bucket.

[Select the bucket](https://us-east-2.console.aws.amazon.com/s3/buckets) and click "Edit bucket policy".

[`django-storages` recommends a bucket policy.](https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#iam-policy)

You'll need to place your User ARN in the policy, as well as the bucket name.
