from django.urls import path
from . import views

urlpatterns = [
    # Home Page
    path('', views.index, name='index'),

    # Departments Section
    path('departments/', views.department_list, name='department_list'),                     # List all departments
    path('departments/<slug:slug>/', views.department_detail, name='department_detail'),      # Detail view of a specific department

    # Events Section
    path('events/', views.event_list, name='event_list'),                                     # List all events
    path('events/<int:id>/', views.event_detail, name='event_detail'),                        # Detail view of a specific event

    # Facilities Page
    path('facilities/', views.facilities_view, name='facilities'),                            # Overview of college facilities

    # Library Section
    path('library/', views.library_home, name='library_home'),                                # Library home and book gallery
    path('library/book/<int:pk>/', views.book_detail, name='book_detail'),                    # Detail view of a specific book

    # Admission Section
    path('admission/', views.admission_view, name='admission'),                              # Admission info: process, requirements, etc.
    path('apply-online/', views.apply_online, name='apply_online'),                           # Online application form   

    # Examination Information Center
    path('examination-info/', views.examination_info, name='examination_info'),               # Exams schedule, results, and rules

    # About Us Page
    path('about/', views.about_page, name='about_page'),                                      # Institution background, principal message, etc.

    # Contact Us Section
    path('contact/', views.contact_page, name='contact_page'),                                # Contact page view
    path('contact/submit/', views.submit_contact_message, name='contact_message'),            # Handle contact form submissions

    # News Section
    path('news/', views.news_list, name='news_list'),                                         # List of news articles
    path('news/<slug:slug>/', views.news_detail, name='news_detail'),                         # Detail view of a specific news item

    # Gallery Page
    path('gallery/', views.gallery_view, name='gallery'),                                     # Image and media gallery

    path('courses/', views.course_list, name='course_list'),
    path('courses/<slug:slug>/', views.course_detail, name='course_detail'),
 
                          
]
