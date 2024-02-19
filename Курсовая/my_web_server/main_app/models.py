from django.db import models

class Tasks(models.Model):
    title = models.CharField('Title', max_length =25, null=False, blank=False)
    task = models.TextField('Task', max_length=225, null=False, blank=False)



    def __str__(self):
        return f'{self.title}{self.task}'

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'



# class Provider(models.Model):
#     name = models.CharField(max_length = 200, null=False, blank=False,unique = True)
#     def __str__(self):
#         return self.name
# class Country_Provider(models.Model):
#     name = models.CharField(max_length = 200, null=False, blank=False,unique = True)
#     def __str__(self):
#         return self.name
#
# class Tag(models.Model):
#     name = models.CharField(max_length = 200, null=False, blank=False,unique = True)
#     def __str__(self):
#         return self.name
#
#
# class Furniture(models.Model):
#     name = models.CharField(max_length = 200, null=False, blank=False)
#     price = models.FloatField(max_length = 200, null=False, blank=False)
#     provider = models.ForeignKey(Provider,null = False,blank = False,on_delete = models.PROTECT)
#     country_provider = models.ForeignKey(Country_Provider,null = False,blank = False,on_delete = models.PROTECT)
#     def __str__(self):
#         return f'{self.name} {self.price} {self.provider} {self.country_provider} '