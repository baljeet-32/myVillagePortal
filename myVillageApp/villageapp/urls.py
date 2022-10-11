from django.urls import path
from villageapp import views

from .views import NotificationDeleteView, NotificationListView, NotificationDetailView, NotificationCreateView, NotificationUpdateView, ComplaintsListView, ComplaintsDetailView, ComplaintsCreateView, ComplaintsUpdateView, ComplaintsDeleteView, SolvedComplaintsListView, UnSolvedComplaintsListView, UserComplaintsListView, JobsListView, JobsDetailView, JobsCreateView, JobsUpdateView, JobsDeleteView, UserJobsListView, listenNotification


urlpatterns = [
    path('', views.home, name="village-home"),
    path('about/', views.about, name="village-about"),
    path('notification/', NotificationListView.as_view(),
         name="village-notification"),

    path('notification/<int:pk>',
         NotificationDetailView.as_view(), name="notif_detail"),
    path('notification/new/',
         NotificationCreateView.as_view(), name="notif_new_add"),
    path('notification/<int:pk>/update',
         NotificationUpdateView.as_view(), name="notif_update"),
    path('notification/<int:pk>/delete',
         NotificationDeleteView.as_view(), name="notif_delete"),


    path('jobs/', JobsListView.as_view(), name="village-jobs"),
    path('jobs/<int:pk>',
         JobsDetailView.as_view(), name="job_detail"),

    path('jobs/new/',
         JobsCreateView.as_view(), name="job_new_add"),

    path('jobs/<int:pk>/update',
         JobsUpdateView.as_view(), name="job_update"),
    path('jobs/<int:pk>/delete',
         JobsDeleteView.as_view(), name="job_delete"),

    path('job/user/<str:username>/',
         UserJobsListView.as_view(), name="user_job"),




    path('complaints/', ComplaintsListView.as_view(),
         name="village-complaints"),
    path('complaints/solved', SolvedComplaintsListView.as_view(),
         name="solved_complaints"),
    path('complaints/unsolved', UnSolvedComplaintsListView.as_view(),
         name="unsolved_complaints"),

    path('complaints/<int:pk>',
         ComplaintsDetailView.as_view(), name="comp_detail"),
    path('complaints/new/',
         ComplaintsCreateView.as_view(), name="comp_new_add"),
    path('complaints/<int:pk>/update',
         ComplaintsUpdateView.as_view(), name="comp_update"),
    path('complaints/<int:pk>/delete',
         ComplaintsDeleteView.as_view(), name="comp_delete"),
    path('complaints/user/<str:username>/',
         UserComplaintsListView.as_view(), name="user_comp"),




    path('deletequery/<int:id>', views.delete_query, name='deletequery'),
    path('notification/listen',
         listenNotification, name="notif_listen"),


]
