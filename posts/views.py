from django.db.models import Count, Q
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.exceptions import ValidationError
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView

from django.http import HttpResponseRedirect

from .forms import CommentForm, PostForm
from .models import Post, Profile, PostView, Comment
from reporter.models import Incidences
from account.forms import EmailSignupForm
from account.models import Signup

form_email = EmailSignupForm()

def get_profile(user):
    qs = Profile.objects.filter(user=user)
    if qs.exists():
        return qs[0]
    return None


class SearchView(ListView):
    form_email = EmailSignupForm()
    model = Post
    template_name = 'search_results.html'
    context_object_name = 'queryset'
    ordering = ['-created']
    paginate_by = 4

    def get(self, request, *args, **kwargs):
        queryset = Post.objects.all()
        query = request.GET.get('q')
        category_count = get_category_count()
        most_recent = Post.objects.order_by('-created')[:3]
        
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) |
                Q(overview__icontains=query)
            ).distinct()
        context = {
            'queryset': queryset,
            'most_recent' : most_recent,
            'page_request_var' : "page",
            'category_count' : category_count,
            'form_email' : self.form_email
        }
        return render(request, 'search_results.html', context)


class SearchCategorieView(ListView):
    form_email = EmailSignupForm()
    model = Post
    template_name = 'search_results.html'
    context_object_name = 'queryset'
    ordering = ['-created']
    paginate_by = 4

    def get(self, request, *args, **kwargs):
        queryset = Post.objects.all()
        query = request.GET.get('q')
        category_count = get_category_count()
        most_recent = Post.objects.order_by('-created')[:3]
        
        if query:
            queryset = queryset.filter(
                Q(categories__title=query))
        context = {
            'queryset': queryset,
            'most_recent' : most_recent,
            'page_request_var' : "page",
            'category_count' : category_count,
            'form_email' : self.form_email
        }
        return render(request, 'search_results.html', context)


def get_category_count():
    queryset = Post \
        .objects \
        .values('categories__title') \
        .annotate(Count('categories__title'))
    return queryset


class IndexView(View):
    form_email = EmailSignupForm()

    def get(self, request, *args, **kwargs):
        latest = Post.objects.order_by('-created')[0:3]
        context = {
            'latest': latest,
            'form_email': self.form_email
        }
        return render(request, 'index.html', context)

    def post(self, request, *args, **kwargs):
        email = request.POST.get("email")
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()
        messages.info(request, "Berhasil Berlangganan")
        return redirect("post-list")


class PostListView(ListView):
    form_email = EmailSignupForm()
    model = Post
    template_name = 'blog.html'
    context_object_name = 'queryset'
    ordering = ['-created']
    paginate_by = 4

    def get_context_data(self, **kwargs):
        category_count = get_category_count()
        most_recent = Post.objects.order_by('-created')[:3]
        context = super().get_context_data(**kwargs)
        context['most_recent'] = most_recent
        context['page_request_var'] = "page"
        context['category_count'] = category_count
        context['form_email'] = self.form_email
        return context

    def post(self, request, *args, **kwargs):
        email = request.POST.get("email")
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()
        messages.info(request, "Berhasil Berlangganan")
        return redirect("post-list")


class PostDetailView(DetailView):
    form_email = EmailSignupForm()
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'
    form_com = CommentForm()

    def get_object(self):
        obj = super().get_object()
        if self.request.user.is_authenticated:
            PostView.objects.get_or_create(
                user=self.request.user,
                post=obj
            )
        return obj

    def get_context_data(self, **kwargs):
        category_count = get_category_count()
        most_recent = Post.objects.order_by('-created')[:3]
        context = super().get_context_data(**kwargs)
        context['most_recent'] = most_recent
        context['page_request_var'] = "page"
        context['category_count'] = category_count
        context['form_com'] = self.form_com
        context['form_email'] = self.form_email
        return context

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            post = self.get_object()
            form.instance.user = request.user
            form.instance.post = post
            form.save()
            return redirect(reverse("post-detail", kwargs={
                'pk': post.pk
            }))
        form_email = EmailSignupForm(request.POST)
        if form_email.is_valid():
            email = request.POST.get("email")
            new_signup = Signup()
            new_signup.email = email
            new_signup.save()
            messages.info(request, "Berhasil Berlangganan")
            return HttpResponseRedirect(request.path_info)


class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'comment_confirm_delete.html'

    def get_success_url(self):
        # Assuming there is a ForeignKey from Comment to Post in your model
        comment = self.get_object() 
        return reverse( 'post-detail', kwargs={
            'pk': comment.post.id
            })

    def get_context_data(self, **kwargs):
        category_count = get_category_count()
        most_recent = Post.objects.order_by('-created')[:3]
        context = super().get_context_data(**kwargs)
        context['most_recent'] = most_recent
        context['page_request_var'] = "page"
        context['category_count'] = category_count
        return context


def point_post(request, pk):
    queryset = Post.objects.filter(point=pk)
    context = {
        'queryset' : queryset,
    }
    return render(request, 'search_results.html', context)


def district_post(request, pk):
    queryset = Post.objects.filter(district=pk)
    context = {
        'queryset' : queryset,
    }
    return render(request, 'search_results.html', context)