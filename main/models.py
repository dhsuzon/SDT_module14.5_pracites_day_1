from django.db import models

class MyModel(models.Model):
        auto_field = models.AutoField(primary_key=True)  # Keep AutoField
        # Remove big_auto_field
        binary_field = models.BinaryField()
        big_integer_field = models.BigIntegerField()
        boolean_field = models.BooleanField()
        char_field = models.CharField(max_length=255)
        date_field = models.DateField()
        date_time_field = models.DateTimeField()
        decimal_field = models.DecimalField(max_digits=5, decimal_places=2)
        email_field = models.EmailField()
        duration_field = models.DurationField()
        file_field = models.FileField(upload_to='files/')
        file_path_field = models.FilePathField(path='/path/to/files/')
        float_field = models.FloatField()
        generic_ip_address_field = models.GenericIPAddressField()
        image_field = models.ImageField(upload_to='images/')
        integer_field = models.IntegerField()
        positive_big_integer_field = models.PositiveBigIntegerField()
        positive_integer_field = models.PositiveIntegerField()
        positive_small_integer_field = models.PositiveSmallIntegerField()
        slug_field = models.SlugField()
        small_integer_field = models.SmallIntegerField()
        text_field = models.TextField()
        url_field = models.URLField()
        uuid_field = models.UUIDField()

