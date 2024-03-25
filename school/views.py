from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.contrib import messages
from school.models import Teacher, Activity, Schedule, Zanyatie, Enrollment
from .forms import ReservationForm
from django.shortcuts import get_object_or_404


class HomeListView(ListView):
    model = Activity
    template_name = 'school/index.html'
    ordering = ["-date_created"]
    paginate_by = 3
    context_object_name = 'activity'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        teacher = Teacher.objects.all()
        context['teacher'] = teacher          
        return context


class CoursesListView(ListView):
    model = Activity
    template_name = 'school/courses.html'
    ordering = ["-date_created"]
    paginate_by = 9
    context_object_name = 'activity'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        teacher = Teacher.objects.all()
        context['teacher'] = teacher          
        return context


class CourseDetailView(DetailView):
    model = Activity
    template_name = 'school/course_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ReservationForm()   

        # Получение расписания для текущего курса (Activity)
        activity = self.get_object()
        schedule = Schedule.objects.filter(activity=activity)
        context['schedule'] = schedule
        return context
    

def handle_reservation(request, pk):
    activity = get_object_or_404(Activity, pk=pk)
    teacher = activity.teacher  

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.activity = activity
            reservation.teacher = teacher  
            reservation.save()

            messages.success(request, 'Вы записались на это занятие, скоро свяжемся с Вами, спасибо!')
            return redirect('course_details', pk=activity.pk)
    return redirect('course_details', pk=activity.pk)



def trainers(request):
    teacher = Teacher.objects.all()
    context = {'teacher': teacher}
    return render(request, 'school/trainers.html',  context)


def about(request):
    return render(request, 'school/about.html')