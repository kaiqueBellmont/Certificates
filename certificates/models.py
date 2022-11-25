from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name


class Certificate(models.Model):
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    total_time = models.DecimalField(decimal_places=2, max_digits=4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    institution = models.CharField(max_length=65)
    cover = models.ImageField(
        upload_to='certificates/covers/%Y/%m/%d/', blank=True, default='')
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True,
        default=None,
    )

    def __str__(self):
        return self.title



