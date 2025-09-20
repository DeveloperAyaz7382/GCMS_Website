from django.db import models
from django.utils import timezone
from django.utils.text import slugify


# ----------------------------- Department -----------------------------
from django.db import models
from django.utils.text import slugify

class Department(models.Model):
    DEGREE_CHOICES = [
        ('BS', 'Bachelor of Science'),
        ('MS', 'Master of Science'),
        ('BBA', 'Bachelor of Business Administration'),
        ('MBA', 'Master of Business Administration'),
        ('Diploma', 'Diploma'),
        ('PhD', 'Doctor of Philosophy'),
        ('Other', 'Other'),
    ]

    image = models.ImageField(upload_to='departments/', default='departments/default.png')
    name = models.CharField(max_length=100, default="Department Name")
    faculty = models.CharField(max_length=100, default="Faculty Member Name")
    head_of_department = models.CharField(max_length=100, default="HOD Name")  # ✅ Added this line
    hod_image = models.ImageField(upload_to='hods/', blank=True, null=True)
    description = models.TextField(default="Department description.")
    slug = models.SlugField(unique=True, blank=True)
    num_of_courses = models.IntegerField(default=0)
    num_of_students = models.IntegerField(default=0)
    degree_type = models.CharField(max_length=20, choices=DEGREE_CHOICES, default='BS')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name



# ----------------------------- Faculty Member -----------------------------

class FacultyMember(models.Model):
    DESIGNATION_CHOICES = [
        ('Professor', 'Professor'),
        ('Associate Professor', 'Associate Professor'),
        ('Assistant Professor', 'Assistant Professor'),
        ('Lecturer', 'Lecturer'),
        ('Instructor', 'Instructor'),
    ]

    department = models.ForeignKey(
        'Department',
        on_delete=models.CASCADE,
        related_name='faculty_members'
    )
    name = models.CharField(max_length=100)
    designation = models.CharField(
        max_length=50,
        choices=DESIGNATION_CHOICES,
        blank=True,
        null=True
    )
    subject = models.CharField(max_length=100)
    image = models.ImageField(
        upload_to='faculty/',
        default='faculty/default.jpg'
    )

    class Meta:
        ordering = ['name']
        verbose_name = "Faculty Member"
        verbose_name_plural = "Faculty Members"

    def __str__(self):
        return f"{self.name} ({self.designation})" if self.designation else self.name


# ----------------------------- Principal Message -----------------------------
class PrincipalMessage(models.Model):
    title = models.CharField(max_length=200, default="Message from the Principal")
    subtitle = models.CharField(max_length=200, default="Empowering parents. Nurturing futures.")
    message = models.TextField()
    image = models.ImageField(upload_to='principal_images/', default='principal_images/default.jpg')

    def __str__(self):
        return self.title


# ----------------------------- Event -----------------------------
class Event(models.Model):
    event_image = models.ImageField(upload_to='event/', default='event/default.png')
    title = models.CharField(max_length=200, default="Event Title")
    description = models.TextField(default="Event description.")
    date = models.DateTimeField()
    venue = models.CharField(max_length=200, default="Event Venue")

    def __str__(self):
        return self.title


# ----------------------------- Academic Excellence -----------------------------
class AcademicExcellence(models.Model):
    background_image = models.ImageField(upload_to='backgrounds/', default='backgrounds/default.jpg')
    heading = models.CharField(max_length=255, default="Academic Excellence At Our University")
    subheading = models.CharField(max_length=255, default="Shape Your Future Through World-Class Education")
    search_placeholder = models.CharField(max_length=255, default="Explore our academic programs...")
    students_enrolled = models.PositiveIntegerField(default=1500)
    academic_programs = models.PositiveIntegerField(default=120)
    employment_rate = models.PositiveIntegerField(default=95)

    def __str__(self):
        return self.heading


# ----------------------------- Testimonial -----------------------------
class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=150)
    message = models.TextField()
    image = models.ImageField(upload_to='testimonials/', default='testimonials/default.jpg')

    def __str__(self):
        return f"{self.name} - {self.role}"


# ----------------------------- News -----------------------------
class News(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(default="No description available")
    image = models.ImageField(upload_to='news/', default='news/default.jpg')
    author = models.CharField(max_length=100, default="GCMS Admin")
    date = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while News.objects.filter(slug=slug).exists():
                slug = f'{base_slug}-{counter}'
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title




# ----------------------------- Facility -----------------------------
class Facility(models.Model):
    LAB_CHOICES = [
        ('programming', 'Programming Lab'),
        ('multimedia', 'Multimedia Lab'),
        ('networking', 'Networking Lab'),
        ('research', 'Research Lab'),
    ]

    name = models.CharField(max_length=50, choices=LAB_CHOICES, default='programming', verbose_name='Lab Type')
    title = models.CharField(max_length=100, default='Programming Lab')
    description = models.TextField(default='This lab is equipped with modern tools and infrastructure.')
    image = models.ImageField(upload_to='facilities/', default='facilities/default.jpg')
    feature_1 = models.CharField(max_length=200, default='30 workstations with i7 processors', blank=True, null=True)
    feature_2 = models.CharField(max_length=200, default='Latest programming tools and IDEs', blank=True, null=True)
    feature_3 = models.CharField(max_length=200, default='Interactive learning systems', blank=True, null=True)

    def __str__(self):
        return f"{self.get_name_display()} - {self.title}"


# ----------------------------- Hostel Intro -----------------------------
class HostelIntro(models.Model):
    heading = models.CharField(max_length=200, default='Comfortable Living')
    description = models.TextField(default='Our hostel facilities provide a comfortable and secure environment.')
    image = models.ImageField(upload_to='hostel/', default='hostel/default.jpg')

    def __str__(self):
        return self.heading


# ----------------------------- Hostel Facility -----------------------------
class HostelFacility(models.Model):
    title = models.CharField(max_length=100, default='Facility Title')
    description = models.TextField(default='This is a default description for the hostel facility.')
    image = models.ImageField(upload_to='hostel/', default='hostel/default.jpg')
    feature_1 = models.CharField(max_length=200, default='Feature One')
    feature_2 = models.CharField(max_length=200, default='Feature Two')
    feature_3 = models.CharField(max_length=200, default='Feature Three')
    feature_4 = models.CharField(max_length=200, default='Feature Four')

    def __str__(self):
        return self.title


# ----------------------------- Visit Request -----------------------------
class VisitRequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    interest = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.interest}"


# ----------------------------- Library Book -----------------------------
class LibraryBook(models.Model):
    
    CATEGORY_CHOICES = [
        ('cs', 'Computer Science'),
        ('management', 'Management'),
        ('engineering', 'Engineering'),
        ('business', 'Business'),
        ('economics', 'Economics'),
        ('mathematics', 'Mathematics'),
        ('fiction', 'Fiction'),
        ('textbooks', 'Textbooks'),
        ('history', 'History'),
        ('biography', 'Biography'),
        ('science', 'Science'),
        ('arts', 'Arts & Humanities'),
        ('language', 'Languages & Literature'),
        ('reference', 'Reference'),
        ('philosophy', 'Philosophy'),
        ('religion', 'Religion'),
        ('ba_economics', 'Business Administration & Economics'),
        ('children', "Children's Books"),
        ('magazines', 'Magazines & Journals'),
    ]

    title = models.CharField(max_length=255, default="Untitled Book")
    author = models.CharField(max_length=255, default="Unknown Author")
    publisher = models.CharField(max_length=255, default="Unknown Publisher")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='cs')
    edition = models.CharField(max_length=50, blank=True, default="1st")
    published_year = models.CharField(max_length=4, blank=True, default="2024")
    description = models.TextField(default="No description provided.")
    image = models.ImageField(upload_to='library_books/', default='library_books/default.jpg')

    def __str__(self):
        return self.title


# ----------------------------- Admission Process -----------------------------
class AdmissionStep(models.Model):
    title = models.CharField(max_length=100, default='Admission Step')
    icon_class = models.CharField(max_length=50, default='fas fa-graduation-cap', help_text="FontAwesome class")
    description = models.TextField(default='Description of the step.')

    def __str__(self):
        return self.title


class FeeStructure(models.Model):
    DEPARTMENT_CHOICES = [
        ('engineering', 'Engineering'),
        ('business', 'Business'),
        ('computing', 'Computing'),
        ('management', 'Management'),
        ('arts', 'Arts & Humanities'),
    ]
    department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES, default='engineering')
    program = models.CharField(max_length=100, default='Program Name')
    fee_range = models.CharField(max_length=50, default='0 - 0')
    duration = models.CharField(max_length=20, default='4 Years')

    def __str__(self):
        return self.program


class ApplicationDownload(models.Model):
    intake_season = models.CharField(max_length=50, default='Fall 2025')
    description = models.TextField(default='Apply for admission by downloading the application form.')
    form_file = models.FileField(upload_to='admissions/forms/')

    def __str__(self):
        return f"{self.intake_season} Form"


class Admission(models.Model):
    department = models.CharField(max_length=200, default="Department Name")
    program = models.TextField(default="Program description.")
    annual_fees = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    duration = models.CharField(max_length=50, default="Duration")
    eligibility = models.TextField(default="Eligibility criteria.")

    def __str__(self):
        return f"{self.department} - {self.program}"


# ----------------------------- Examination -----------------------------
from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

class Exam(models.Model):
    title = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='exams', default=1)
    start_date = models.DateField()
    end_date = models.DateField()
    time = models.CharField(max_length=100)
    venue = models.CharField(max_length=200)
    instructions = models.TextField()
    status = models.CharField(max_length=100)
    schedule_file = models.FileField(upload_to='exam_schedules/', blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)  # ✅ Default current datetime

    def clean(self):
        # ✅ Validation: end date must not be earlier than start date
        if self.end_date < self.start_date:
            raise ValidationError("End date cannot be earlier than start date.")

    def __str__(self):
        return f"{self.title} ({self.department.name})"

from django.core.exceptions import ValidationError

class ExamResult(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default='Not Released')
    release_date = models.DateField()
    access_method = models.CharField(max_length=100, default='Online')
    required_info = models.CharField(max_length=100, default='Student ID')
    progress = models.PositiveIntegerField(default=0)
    result_file = models.FileField(upload_to='results/', blank=True, null=True)  # ✅ download field

    def __str__(self):
        return f"{self.exam.title} Results"

    def clean(self):
        if self.release_date and self.exam and self.release_date < self.exam.end_date:
            raise ValidationError("Release date cannot be before the exam's end date.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)




class Rule(models.Model):
    category = models.CharField(max_length=100, default='General')
    content = models.TextField()
    visible = models.BooleanField(default=True)  # ✅ Show/hide rule
    order = models.PositiveIntegerField(default=0)  # ✅ Custom ordering
    created_at = models.DateTimeField(default=timezone.now)  # ✅ Default current datetime
    class Meta:
        ordering = ['order', 'created_at']

    def __str__(self):
        return f"{self.category}"

# ----------------------------- Philosophy and Stats -----------------------------
class PhilosophyBlock(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.ImageField(upload_to='icons/')

    def __str__(self):
        return self.title


class Statistic(models.Model):
    title = models.CharField(max_length=100)
    count = models.PositiveIntegerField()
    color = models.CharField(max_length=20, default="primary")

    def __str__(self):
        return self.title

class HighlightSection(models.Model):
    heading = models.CharField(max_length=200)
    subheading = models.CharField(max_length=200)
    description = models.TextField()
    background_image = models.ImageField(upload_to='backgrounds/')
    button_text = models.CharField(max_length=100)
    button_url = models.URLField()

    def __str__(self):
        return self.heading
# ----------------------------- Contact -----------------------------
class ContactInformation(models.Model):
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    facebook_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)
    google_plus_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return "Contact Information"


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"


class GalleryImage(models.Model):
    image = models.ImageField(upload_to='gallery/')
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.caption if self.caption else "Gallery Image"
    

from django.db import models
from django.db import models

class OnlineApplication(models.Model):
    PROGRAM_CHOICES = [
        ('ICS', 'ICS (Computer Science)'),
        ('Computer Science', 'Computer Science'),
        ('I.Com', 'I.Com (Commerce)'),
        ('D.Com', 'D.Com (Diploma in Commerce)'),
        ('DIT', 'DIT (Diploma in IT)'),
        ('Business Admin', 'Business Administration'),
        ('FSc Pre-Engineering', 'FSc Pre-Engineering'),
        ('Commerce', 'Commerce'),
        ('Other', 'Other'),
    ]

    full_name = models.CharField("Full Name", max_length=100)
    email = models.EmailField("Email")
    phone = models.CharField("Phone Number", max_length=20)
    address = models.TextField("Address", default="Swat, Khyber Pakhtunkhwa")

    program = models.CharField(
        "Program Applying For", 
        max_length=50, 
        choices=PROGRAM_CHOICES, 
        default='ICS'  # Set default value here
    )
    previous_institute = models.CharField("Previous School/College", max_length=150, default="Government School Swat")

    year_completed = models.PositiveIntegerField("Year Completed", default=2024)
    created_at = models.DateTimeField(auto_now_add=True)  # No default needed — auto set


    def __str__(self):
        return f"{self.full_name} - {self.program}"

    class Meta:
        verbose_name = "Online Application"
        verbose_name_plural = "Online Applications"
        ordering = ['-created_at']


class Course(models.Model):
    title = models.CharField(max_length=100, default="Untitled Course")
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(default="No description available at the moment.")
    duration = models.CharField(max_length=50, default="Duration not specified")
    image = models.ImageField(upload_to='course_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Auto-generate slug from title if not provided
        if not self.slug:
            self.slug = slugify(self.title)
        super(Course, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
