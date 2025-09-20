from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.utils import timezone
from django.core.paginator import Paginator
from django.utils.text import slugify

# Import all necessary models
from .models import (
    AcademicExcellence, Event, Department, News, PrincipalMessage,
    Facility, LibraryBook, Testimonial, HostelIntro, HostelFacility,
    AdmissionStep, FeeStructure, ApplicationDownload,
    Exam, ExamResult, Rule, PhilosophyBlock, Statistic, HighlightSection,
    ContactInformation, ContactMessage, GalleryImage,Course,
)

# ============================ Home Page ============================

def index(request):
    """Render the homepage with dynamic content."""
    context = {
        'principal_message': PrincipalMessage.objects.first(),
        'testimonials': Testimonial.objects.all(),
        'academic_excellence': AcademicExcellence.objects.first(),
        'departments': Department.objects.all(),
        'facilities': Facility.objects.all(),
        'contact_info': ContactInformation.objects.first(),
        'events': Event.objects.all(),
        'news': News.objects.order_by('-date')[:6],
        'latest_events': Event.objects.order_by('-date')[:3],
        'images': GalleryImage.objects.all(),
        'courses' : Course.objects.all(),
        
       
        
    }
    return render(request, 'gcms_sitehub/index.html', context)

# ============================ Department Views ============================

def department_list(request):
    """Display list of all departments."""
    images = GalleryImage.objects.all()
    departments = Department.objects.all()
    return render(request, 'gcms_sitehub/department.html', {'images': images, 'departments': departments})

def department_detail(request, slug):
    """Display detailed view of a specific department."""
    department = get_object_or_404(Department, slug=slug)
    images = GalleryImage.objects.all()
    return render(request, 'gcms_sitehub/department_detail.html', {
        'images': images,
        'department': department,
        'faculty_members': department.faculty_members.all()
    })

# ============================ Event Views ============================

def event_list(request):
    """List all events with category (happening, upcoming, expired)."""
    today = timezone.now().date()
    images = GalleryImage.objects.all()
    events = Event.objects.all().order_by('-date')

    for event in events:
        event_date = event.date.date() if hasattr(event.date, 'date') else event.date
        if event_date == today:
            event.category = 'happening'
        elif event_date > today:
            event.category = 'upcoming'
        else:
            event.category = 'expired'

    return render(request, 'gcms_sitehub/event.html', {'images': images, 'events': events})

def event_detail(request, id):
    """Display details of a specific event."""
    event = get_object_or_404(Event, id=id)
    images = GalleryImage.objects.all()
    return render(request, 'gcms_sitehub/event_detail.html', {'images': images, 'event': event})

# ============================ Facilities View ============================

def facilities_view(request):
    """Display lab and hostel facility information."""
    labs = Facility.objects.all().order_by('name')
    hostel_intro = HostelIntro.objects.first()
    hostel_facilities = HostelFacility.objects.all()
    return render(request, 'gcms_sitehub/facilities.html', {
        'labs': labs,
        'hostel_intro': hostel_intro,
        'hostel_facilities': hostel_facilities
    })

# ============================ Library Views ============================

def library_home(request):
    """Library homepage with book filters and pagination."""
    search_query = request.GET.get('search', '')
    books = LibraryBook.objects.filter(title__icontains=search_query)
    images = GalleryImage.objects.all()

    paginator = Paginator(books, 9)
    books_page = paginator.get_page(request.GET.get('page'))

    categories = set(book.category for book in books if book.category)
    filters = [{'name': cat, 'slug': slugify(cat)} for cat in categories]

    return render(request, 'gcms_sitehub/library.html', {
        'books': books_page,
        'filters': filters,
        'images': images,
    })

def book_detail(request, pk):
    """Detail view of a specific book."""
    book = get_object_or_404(LibraryBook, pk=pk)
    images = GalleryImage.objects.all()
    return render(request, 'gcms_sitehub/book_detail.html', {'images': images, 'book': book})

# ============================ Admission Views ============================

def admission_view(request):
    """Display admission steps, fees, and downloadable application."""
    context = {
        'steps': AdmissionStep.objects.all(),
        'fees': FeeStructure.objects.all(),
        'application': ApplicationDownload.objects.last(),
        'images': GalleryImage.objects.all(),
    }
    return render(request, 'gcms_sitehub/admission.html', context)

from .forms import OnlineApplicationForm

def apply_online(request):
    """Handle the online application form."""
    if request.method == 'POST':
        form = OnlineApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('https://admission.hed.gkp.pk/')  # External redirect to HED
    else:
        form = OnlineApplicationForm()

    return render(request, 'gcms_sitehub/admission.html', {'form': form})


# ============================ Examination Info View ============================

def examination_info(request):
    """Display upcoming exams, results, and rules."""
    context = {
        'departments': Department.objects.prefetch_related('exams').all(),
        'results': ExamResult.objects.select_related('exam').all(),
        'rules': Rule.objects.filter(visible=True),
        'images': GalleryImage.objects.all()
    }
    return render(request, 'gcms_sitehub/exam.html', context)

# ============================ About Page ============================

def about_page(request):
    """Render the About page with principal message and stats."""
    context = {
        'principal': PrincipalMessage.objects.first(),
        'philosophy': PhilosophyBlock.objects.all(),
        'stats': Statistic.objects.all(),
        'highlight': HighlightSection.objects.first(),
        'testimonials': Testimonial.objects.all(),
        'images': GalleryImage.objects.all(),
    }
    return render(request, 'gcms_sitehub/about.html', context)

# ============================ Contact Views ============================

def contact_page(request):
    """Render the contact page with contact information."""
    contact_info = ContactInformation.objects.first()
    images = GalleryImage.objects.all()
    return render(request, 'gcms_sitehub/contact.html', {'contact_info': contact_info, 'images': images})

def submit_contact_message(request):
    """Handle contact form submission."""
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Save message to the database
        ContactMessage.objects.create(
            name=name,
            email=email,
            phone=phone,
            subject=subject,
            message=message
        )

        messages.success(request, "Thank you! Your message has been sent successfully.")
        return redirect('contact_page')
    return redirect('contact_page')

# ============================ News Views ============================

def news_list(request):
    """Display list of news articles."""
    images = GalleryImage.objects.all()
    news = News.objects.all().order_by('-date')
    return render(request, 'gcms_sitehub/news.html', {'news': news, 'images': images})

def news_detail(request, slug):
    """Display detail of a specific news item."""
    news_item = get_object_or_404(News, slug=slug)
    images = GalleryImage.objects.all()
    return render(request, 'gcms_sitehub/news_detail.html', {'news_item': news_item, 'images': images})

# ============================ Gallery View ============================

def gallery_view(request):
    """Render gallery page with all images."""
    images = GalleryImage.objects.all()
    return render(request, 'gcms_sitehub/gallery.html', {'images': images})

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'gcms_sitehub/course_list.html', {'courses': courses})

def course_detail(request, slug):
    course = get_object_or_404(Course, slug=slug)
    return render(request, 'gcms_sitehub/course_detail.html', {'course': course})

