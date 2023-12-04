from django.db import models

# создание продукта и наследование класса models.Model
# создание колонок в таблице базы данных
class Product(models.Model):
    name = models.CharField(max_length=40, blank=False)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=200)

# создание функции для представления чего-то понятного написанного в таблице базы данных
def __str__(self):
    return f'{self.name}-{self.price}'

class ProductComment(models.Model):
   user_name = models.CharField(max_length=200)
   comment = models.TextField()
   product = models.ForeignKey(Product, on_delete=models.CASCADE)


def __str__(self):
    return f'{self.user_name}-{self.comment}'



#class BookReview(models.Model):
#   full_name = models.CharField(max_length=200, verbose_name='ФИО')
 #  email = models.EmailField(max_length=200, verbose_name='Email')
 #  review_text = models.TextField(verbose_name='Текст отзыва')
 #  checked = models.BooleanField(default=False, verbose_name='Проверено')


class BookReview(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    review_text = models.TextField()
    checked = models.BooleanField(default=False)


def __str__(self):
    return f'{self.full_name}-{self.email}'



