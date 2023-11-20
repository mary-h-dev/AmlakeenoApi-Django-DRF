
from django.contrib import admin
from django.urls import path, include

# listings
from listings.api import views as listings_api_views

# profile
from users.api import views as users_api_views

# posts
from posts.api import views as posts_api_views

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = (
    [
        path("admin/", admin.site.urls),
        path("api/listings/", listings_api_views.ListingList.as_view()),
        path("api/listings/create/", listings_api_views.ListingCreate.as_view()),
        path("api/listings/<int:pk>/", listings_api_views.ListingDetail.as_view()),
        path(
            "api/listings/<int:pk>/delete/", listings_api_views.ListingDelete.as_view()
        ),
        path(
            "api/listings/<int:pk>/update/", listings_api_views.ListingUpdate.as_view()
        ),
        path("api/posts/", posts_api_views.PostList.as_view()),
        path("api/posts/<int:pk>/", posts_api_views.PostDetail.as_view()),

        path("api/comments/", posts_api_views.CommentList.as_view()),
        path("api/comments/create/", posts_api_views.CommentCreate.as_view()),

        path("api/posts/like",posts_api_views.LikeDislikeList.as_view()),
        path("api/posts/<int:pk>/like_dislike/",posts_api_views.LikeDislikeCreate.as_view()),
   

        path("api/profiles/", users_api_views.ProfileList.as_view()),
        path("api/profiles/<int:seller>/", users_api_views.ProfileDetail.as_view()),
        path(
            "api/profiles/<int:seller>/update/", users_api_views.ProfileUpdate.as_view()
        ),


        path("api-auth-djoser/", include("djoser.urls")),
        path("api-auth-djoser/", include("djoser.urls.authtoken")),
    ]
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)


