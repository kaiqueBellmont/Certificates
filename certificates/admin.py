from django.contrib import admin
from .models import Certificate, Category
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    ...


admin.site.register(Category, CategoryAdmin)
