from django.db import models

#TimeStampModel -> inheritance ko lagi banako so that duplicate code lekhna naparos
class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
     
    class Meta:
       abstract = True #don't care about the table in DB

class Category(TimeStampModel):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=100, null= True ,blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["name"] #Category.objects.all()
        verbose_name="category"
        verbose_name_plural ="Categories"

class Tag(TimeStampModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
#Post -Category
#1 Category cna have M post =>M
#1 Post is associated to only 1 category => 1

#User - Post
#1 user can add M posts => M
#1 post is associated to 1 user =>1

#Post - Tag
#1 Post cna have M tags =>M
#1 Tag can be added to M post -> M

class Post(TimeStampModel):
    STATUS_CHOICES = [
        ("active","Active"), #database/django
        ("in_active","Inactive"),
    ]
    title = models.CharField(max_length=200)
    content = models.TextField()
    featured_image = models.ImageField(upload_to="post_images/%Y/%m/%d",blank=False)
    author = models.ForeignKey("auth.User",on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="active")
    views_count =models.PositiveBigIntegerField(default=0)
    is_breaking_news = models.BooleanField(default=False)
    published_at = models.DateTimeField(null=True,blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title