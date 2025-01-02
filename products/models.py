from django.db import models


class Meta:
        verbose_name_plural = 'Categories'

class Category(models.Model):
    name = models.CharField(max_length=50)
    friendly_name = models.CharField(max_length=100)
    difficulty_level = models.CharField(max_length=50)
    credits = models.IntegerField()
    number_of_lectures = models.IntegerField()
    est_time = models.IntegerField()
    short_description = models.TextField(max_length=255)
    long_description = models.TextField(max_length=1000)
    test = models.BooleanField(default=False)
    logo = models.ImageField(upload_to='logos/', null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    starting_date = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Material(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    material_title = models.TextField(max_length=255)
    full_content = models.TextField()
    pdf_file = models.FileField(upload_to='pdfs/', null=True, blank=True)
    video_url = models.URLField(max_length=200, null=True, blank=True)
    video_name = models.CharField(max_length=255, null=True, blank=True)
    pdf_name = models.CharField(max_length=255, null=True, blank=True) 
 

    def __str__(self):
        return f"{self.category.name} Material"

    def get_category_name(self):
        return self.category.name

    def get_category_logo(self):
        return self.category.logo

    def get_video_name(self):
        return self.video_name or "No Video"

    def get_pdf_name(self):
        return self.pdf_name or "No PDF"
