from django.db import models
import re
import bcrypt 


class QuoteManager(models.Manager):
    def postValidator(self, postData):
        errors= {}
        if len(postData['content']) < 4:
            errors['content'] = "You must put more content"
        if len(postData['author']) == 0:
            errors['author'] = "You must put your name Author!"
        return errors

class UserManager(models.Manager):
    def loginValidator(self, postData):
        errors= {}
        usersWithemail = Users.objects.filter(email_address = postData['email'])
        print(usersWithemail)
        if len(postData['email']) == 0:
            errors['emailreq'] = "Email is required to login."
        elif len(usersWithemail) == 0:
            errors['emailnotfound'] = "Email is not found, please Register first."
        else:
            userToCheck = usersWithemail[0]
            print(usersWithemail[0])
            print(usersWithemail[0].password)
            if bcrypt.checkpw(postData['pw'].encode(), usersWithemail[0].password.encode()):
                print("password match")
            else:
                errors['pwmatch'] = "Password is incorrect"
        return errors
    def regValidator(self, postData):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        errors = {}
        if len(postData['fname']) == 0:
            errors['fnamereq'] = "First name is required"
        if len(postData['lname']) == 0:
            errors['lnamereq'] = "Last name is required"
        if len(postData['email']) == 0:
            errors['emailreq'] = "Email is required"
        elif not EMAIL_REGEX.match(postData['email']):
            errors['invalidemail'] = "a real Email is necessary"
        if len(postData['pw']) < 4:
            errors['pwreq'] = "Password must have atleast 4 characters"
        if postData['pw'] != postData['cpw']:
            errors['confirmpw'] = "Confirm password must match"
        return errors



# Create your models here.
class Users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Quotes(models.Model):
    content = models.TextField()
    uploader = models.ForeignKey(Users, related_name= "quotes_uploaded", on_delete = models.CASCADE, null=True)
    favorites = models.ManyToManyField(Users, related_name="quotes_liked")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = QuoteManager()