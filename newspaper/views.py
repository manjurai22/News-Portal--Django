from django.shortcuts import render 
from django.views.generic import TemplateView, DetailView, ListView
from django.utils import timezone
from datetime import timedelta
from .models import Post,Advertisement,Category

class SideBarMixin:
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)

        context["popular_posts"] = Post.objects.filter(
            published_at__isnull=False,
            status="active"
        ).order_by("-published_at")[:5]

        context['advertisement'] = (
            Advertisement.objects.all().order_by("-created_at").first()
        )

        return context


class HomeView(SideBarMixin, TemplateView):
    template_name ="newsportal/home.html"
#template ma data pathaunu cha bhaney use get_context_data
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)

        context["breaking_news"] = Post.objects.filter(
            published_at__isnull = False, status="active", is_breaking_news= True
            ).order_by("-published_at")[:3]
        
        context["featured_post"] = (
            Post.objects.filter(published_at__isnull=False,status="active")
            .order_by("-published_at","-views_count")
            .first()
        )

        context["trending_news"]= Post.objects.filter(
            published_at__isnull=False, status="active"
        ).order_by("-published_at")[:4]
        
        one_week_ago = timezone.now() - timedelta(days=7)
        context["weekly_top_posts"] = Post.objects.filter(
            published_at__isnull=False, status="active",published_at__gte=one_week_ago
        ).order_by("-published_at","-views_count")[:5]
        return context
        
class PostListView(SideBarMixin, ListView):
    model = Post
    template_name = "newsportal/list/list.html"
    context_object_name = "posts"
    paginate_by = 1

    def get_queryset(self):
        return Post.objects.filter(
            published_at__isnull=False,
            status="active"
        ).order_by("-published_at")
 
class PostDetailView(SideBarMixin , DetailView):
    model =Post
    template_name = "newsportal/detail/detail.html"
    context_object_name = "post"

    def get_queryset(self):
        query = super().get_queryset()
        query = query.filter(published_at__isnull=False, status="active")
        return query
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        #increase the viewcount of currently viewed post
        current_post = self.get_object()
        current_post.views_count += 1
        current_post.save()

        context ["related_articles"] = (
            Post.objects.filter(
                published_at__isnull=False,
                category=self.object.category,
                status="active"
            )
            .exclude(id=self.object.id)
            .order_by("-published_at","-views_count")[:2]
        )
        return context
    
class PostByCategoryView(SideBarMixin,ListView):
    model = Post
    template_name = "newsportal/list/list.html"
    context_object_name = "posts"
    paginate_by = 1

    def get_queryset(self):
        query = super().get_queryset()
        query = query.filter(
            published_at__isnull=False,
            status = "active",
            category__id=self.kwargs["category_id"],
        ).order_by("-published_at")
        return query
    

class CategoryListView(ListView):
    model = Category
    template_name = "newsportal/categories.html"
    context_object_name = "categories"