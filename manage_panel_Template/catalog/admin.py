from django.contrib import admin
from .models import Product, ProductComment, BookReview

# Добавление раздела Product в каталоге
admin.site.register(Product)
admin.site.register(ProductComment)
admin.site.register(BookReview)