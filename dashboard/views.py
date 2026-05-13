from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import CouresDay
from recommendations.models import YogaPose
from ml_model.src.predict import predict


def index_view(request):
    return render(request, 'dashboard/index.html')

@login_required
def home(request):
    course_days = CouresDay.objects.all().order_by('day')
    return render(request, 'dashboard/home.html', {
        'course_days': course_days
    })
@login_required
def search_view(request):
    if request.method == 'POST':
        description = request.POST.get('description')
        duration = request.POST.get('duration')

        # convert duration safely
        try:
            duration = int(duration)
        except:
            duration = 0

        body_part, pain_level = predict(description, duration)

        poses = YogaPose.objects.filter(
            body_part=body_part,
            pain_level=pain_level
        )
        return render(request, 'recommendations/results.html', {
            'poses': poses,
            'body_part': body_part,
            'pain_level': pain_level
        })

def about_us(request):
    return render(request, 'dashboard/aboutus.html')
