from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = (
	("Draft", "Draft"), 
	("Published", "Published")
)


# Create your models here.
class Category(models.Model):
	category_name = models.CharField(max_length=50, unique=True)
	created_on = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name_plural = 'Categories'

	def __str__(self):
		return self.category_name


class Blog(models.Model):
	title = models.CharField(max_length=200, unique=True)
	slug = models.SlugField(max_length=200, unique=True, blank=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	author = models.ForeignKey(
		User, on_delete=models.CASCADE, related_name="blog_posts")
	created_on = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	featured_image = CloudinaryField('image', default='placeholder')
	# excerpt same as short_description
	excerpt = models.TextField(max_length=500, blank=True)
	body = models.TextField()
	status = models.CharField(max_length=10, choices=STATUS, default="Draft")
	is_featured = models.BooleanField(default=False)
	likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)

	class Meta:
		ordering = ['-created_on']

	def __str__(self):
		return self.title

	def number_of_likes(self):
		return self.likes.count()


class Comment(models.Model):
	blog = models.ForeignKey(
		Blog, on_delete=models.CASCADE, related_name='comments')
	name = models.CharField(max_length=80)
	email = models.EmailField()
	body = models.TextField()
	created_on = models.DateTimeField(auto_now_add=True)
	approved = models.BooleanField(default=False)

	class Meta:
		ordering = ['created_on']

	def __str__(self):
		return f"Comment {self.body} by {self.name}"


class Product(models.Model):
	name = models.CharField(max_length=80)
	price = models.DecimalField(max_digits=6, decimal_places=2)
	featured_image = CloudinaryField('image', default='placeholder')

	def __str__(self):
		return self.name


class Booking(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	date = models.DateField()
	start_time = models.TimeField()
	end_time = models.TimeField()

	def __str__(self):
		return f"{self.user.username} - {self.date} {self.start_time} - {self.end_time}"
