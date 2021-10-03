from django.shortcuts import render
from .models import Posts, Categories , SubCategories
from django.views.generic.list import ListView
from django.http import JsonResponse, HttpResponse, request
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404

class PostDetailView(DetailView):
    
    model = Categories
    template_name = './masonry/posts_detail.html'
    
    def get(self, request, *args, **kwargs):
        subid = kwargs['pk']
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        context['ResultPost'] = Posts.objects.filter(sub_category_id = subid).values()
        return self.render_to_response(context)

class PageView(ListView):
    model = Posts  

def subCategoriesData(request):
    if 'categoryid' in request.GET:
        Result = Categories.objects.filter(
            parent=request.GET['categoryid']).values()
        return JsonResponse({"sub_categories_data": list(Result)})
    else:
        return HttpResponse('')
    
    