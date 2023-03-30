from django.db import models

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Maqola nomi')
    content = models.TextField(blank=True, verbose_name = 'Asosiy qism')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Maqola joylashtrilgan vaqt')
    updated_at = models.DateTimeField(auto_now=True, verbose_name = 'Taxrirlangan vaqti')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name = 'Rasm')
    is_published = models.BooleanField(default=True, verbose_name = 'Nashr qilingan')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name="bo'limlar")

    def __str__(self) -> str:
        return str(self.title)

    class Meta:
        verbose_name = 'Yangliklar'
        verbose_name_plural = 'Yanglik'

class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name="Bo'limlar nomi")

    def __str__(self) -> str:
        return str(self.title)
    
    class Meta:
        verbose_name = "Yo'nalishlar"
        verbose_name_plural = "Yo'nalishlar"
        ordering = ['title']
        