from django.contrib import admin
from django.db.models.base import Model
from .models import Categories, Posts, SubCategories

class CategoriesAdmin(admin.ModelAdmin):
    Model = Categories
    list_display = ['name']
    exclude = ['parent']

class PostsAdmin(admin.ModelAdmin):
    class Media:
        js = ('js/mymodel.js', 'js/jquery-3.6.0.min.js')
        
    def render_change_form(self, request, context, *args, **kwargs):
        context['adminform'].form.fields['category'].queryset = Categories.objects.filter(
            parent__isnull=True)
        return super(PostsAdmin, self).render_change_form(request, context, *args, **kwargs)
    
    Model = Posts
    list_display = ['sub_category', 'url', 'date']

class SubCategoriesAdmin(admin.ModelAdmin):
    def render_change_form(self, request, context, *args, **kwargs):
        context['adminform'].form.fields['parent'].queryset = SubCategories.objects.filter(
            parent__isnull=True)
        return super(SubCategoriesAdmin, self).render_change_form(request, context, *args, **kwargs)
    
    list_display = ['name', 'parent']
    fields = ('parent', 'name')
    
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Posts, PostsAdmin)
admin.site.register(SubCategories, SubCategoriesAdmin)
