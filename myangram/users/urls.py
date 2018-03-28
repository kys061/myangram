from django.conf.urls import url

from . import views

urlpatterns = [
    # url(
    #     regex=r'^$',
    #     view=views.UserListView.as_view(),
    #     name='list'
    # ),
    # url(
    #     regex=r'^~redirect/$',
    #     view=views.UserRedirectView.as_view(),
    #     name='redirect'
    # ),
    # url(
    #     regex=r'^(?P<username>[\w.@+-]+)/$',
    #     view=views.UserDetailView.as_view(),
    #     name='detail'
    # ),
    # url(
    #     regex=r'^~update/$',
    #     view=views.UserUpdateView.as_view(),
    #     name='update'
    # ),
    # GET
    url(
        regex=r'explore/$',
        view=views.Explore.as_view(),
        name='explore'
    ),
    url(
        regex=r'(?P<user_id>\d+)/follow/$',
        view=views.FollowUser.as_view(),
        name='follow_user'
    ),
    url(
        regex=r'(?P<user_id>\d+)/unfollow/$',
        view=views.UnFollowUser.as_view(),
        name='unfollow'
    ),
]
