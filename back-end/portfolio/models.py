from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager

# Create your models here.
class User(AbstractBaseUser):
  username = models.CharField(max_length=500, unique=True)
  password = models.CharField(max_length=500)
  email = models.EmailField()
  is_active = models.BooleanField()
  is_staff = models.BooleanField()
  is_superuser = models.BooleanField()
  last_login = models.DateTimeField()

  USERNAME_FIELD = 'username'
  EMAIL_FIELD = 'email'
  REQUIRED_FIELDS = ['email']

  def __str__(self):
    return self.username

class Post(models.Model):
  author = models.ForeignKey(
    User,
    related_name='posts',
    many=True
  )
  title = models.CharField(max_length=100)
  topic = models.CharField(max_length=100)

  def __str__(self):
    return self.title

class PostSection(models.Model):
  post = models.ForeignKey(
    Post,
    related_name='sections',
    many=True
  )
  
  def __str__(self):
    return f'{self.post.title} | {self.id}'

class PostSectionContent(models.Model):
  post_section = models.ForiegnKey(
    PostSection,
    related_name='contents',
    many=True
  )
  ContentTypes = models.TextChoices('ContentTypes', 'PARAGRAPH', 'IMAGE')
  type = models.CharField(choices=ContentTypes.choices, max_length=10)
  content = models.TextField(max_length=2000)

  def __str__(self):
    return f'{self.post_section.id} | {self.content[0:10]}'

class Comment(models.Model):
  author = models.ForeignKey(
    User,
    related_name='comments',
    many=True
  )
  replies = models.ForeignKey(
    'self',
    many=True,
    null=True
  )
  text = models.TextField(max_length=2000)

class UserCommentVotes(models.Model):
  user = models.ForeignKey(
    User,
    related_name='votes',
    many=True
  )
  comment = models.ForeignKey(
    Comment,
    related_name='votes',
    many=True
  )
  vote = models.IntegerField()

  def __str__(self):
    return f'{self.user.username} | {self.vote}'