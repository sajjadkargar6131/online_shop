from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from PIL import Image

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    cover = models.ImageField(upload_to='covers/products/',blank=True)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.title 
    
    def get_absolute_url(self):
        return reverse("product", kwargs={"pk": self.pk})
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # ابتدا تصویر ذخیره می‌شود
        if self.cover and self.cover.name :
            img_path = self.cover.path  # مسیر تصویر ذخیره‌شده
            img = Image.open(img_path)

            max_size = (400, 400)  # حداکثر عرض و ارتفاع

            # تغییر سایز تصویر (حفظ نسبت‌ها)
            img.thumbnail(max_size)

            # ذخیره مجدد تصویر با کیفیت بهینه
            img.save(img_path, format='JPEG', quality=80)  # کاهش کیفیت برای کاهش حجم
        
class Comment(models.Model):
    PRODUCT_STARS = [
        ('1', 'Very Bad'),
        ('2', 'Bad'),
        ('3', 'Normal'),
        ('4', 'Good'),
        ('5', 'Very Good')
    ]
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    star = models.CharField(max_length=9, choices=PRODUCT_STARS)
    active = models.BooleanField(default=True)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f'{self.author} say: {self.body}'