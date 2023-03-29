from django.urls import path, include
from rest_framework.routers import DefaultRouter
from snippets import viewset

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r"snippets", viewset.SnippetViewSet, basename="snippet")
router.register(r"users", viewset.UserViewSet, basename="user")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path("", include(router.urls)),
]


# urlpatterns = [
#     path("snippets/", views.SnippetList.as_view(), name="snippet-list"),
#     path("snippets/<int:pk>/", views.SnippetDetail.as_view(), name="snippet-detail"),
#     path("users/", views.UserList.as_view(), name="user-list"),
#     path("users/<int:pk>/", views.UserDetail.as_view(), name="user-detail"),
#     path("", views.api_root),
#     path(
#         "snippets/<int:pk>/highlight/",
#         views.SnippetHighlight.as_view(),
#         name="snippet-highlight",
#     ),
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)
