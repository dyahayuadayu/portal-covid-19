from django.conf import settings
from django.conf.urls import handler404, handler500, handler403
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib.auth import views as auth_views
from account import views as user_views
from posts import views
from posts.views import (
    IndexView,
    SearchView,
    SearchCategorieView,
    PostListView,
    PostDetailView,
    CommentDeleteView,
    point_post,
    district_post,
)
from . views import (
    county_datasets,
    point_datasets,
    )

urlpatterns = [
    path('', PostListView.as_view(), name = 'home'),
    path('point-post/<pk>/', views.point_post, name="point-post"),
    path('district-post/<pk>/', views.district_post, name="district-post"),
    path('county_data/', county_datasets, name = 'county'),
    path('incidence_data/', point_datasets, name = 'incidences'),
    path('blog/', PostListView.as_view(), name='post-list'),
    path('search/', SearchView.as_view(), name='search'),
    path('search-categorie/', SearchCategorieView.as_view(), name='search-categorie'),
    path('post/<pk>/', PostDetailView.as_view(), name='post-detail'),
    path('comment/<pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='accounts/password_reset.html'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='accounts/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='accounts/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='accounts/password_reset_complete.html'
         ),
         name='password_reset_complete'),

    path('tinymce/', include('tinymce.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

handler404 = user_views.error_404
handler500 = user_views.error_500
handler403 = user_views.error_403