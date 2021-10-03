from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey("self", on_delete=models.CASCADE,blank=True, null=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class SubCategories(Categories):
    
    class Meta:
        proxy = True
        verbose_name = "Sub Category"
        verbose_name_plural = "Sub Categories"
        
class Posts(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    
    sub_category = models.ForeignKey(
        SubCategories, on_delete=models.CASCADE, related_name="Categories", blank=True, null=True)
    
    url = models.URLField(max_length=255)
    date = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
