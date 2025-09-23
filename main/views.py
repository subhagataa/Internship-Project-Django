from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.contrib import messages
from django.db.models import Avg, Count
import csv
from datetime import datetime
from .forms import SurveyForm
from .models import SurveyResponse

def home(request):
    form = SurveyForm()
    responses = SurveyResponse.objects.all().order_by('-created_at')[:4]
    
    # Calculate statistics
    total_responses = SurveyResponse.objects.count()
    avg_satisfaction = SurveyResponse.objects.aggregate(Avg('satisfaction_score'))['satisfaction_score__avg'] or 0
    avg_recommend = SurveyResponse.objects.aggregate(Avg('would_recommend'))['would_recommend__avg'] or 0
    
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your feedback! Your response has been recorded.')
            return redirect('home')
    
    return render(request, 'main/home.html', {
        'form': form,
        'responses': responses,
        'total_responses': total_responses,
        'avg_satisfaction': avg_satisfaction,
        'avg_recommend': avg_recommend,
    })

def analytics_dashboard(request):
    # Calculate comprehensive analytics
    total_responses = SurveyResponse.objects.count()
    avg_satisfaction = SurveyResponse.objects.aggregate(Avg('satisfaction_score'))['satisfaction_score__avg'] or 0
    avg_recommend = SurveyResponse.objects.aggregate(Avg('would_recommend'))['would_recommend__avg'] or 0
    avg_quality = SurveyResponse.objects.aggregate(Avg('quality_rating'))['quality_rating__avg'] or 0
    avg_price = SurveyResponse.objects.aggregate(Avg('price_rating'))['price_rating__avg'] or 0
    avg_support = SurveyResponse.objects.aggregate(Avg('support_rating'))['support_rating__avg'] or 0
    
    # Calculate completion rate (simplified)
    completion_rate = min(95, total_responses * 10)  # Placeholder calculation
    
    # Get usage frequency distribution
    usage_distribution = SurveyResponse.objects.values('product_usage').annotate(count=Count('id'))
    
    # Get recent feedback for sidebar
    recent_feedback = SurveyResponse.objects.all().order_by('-created_at')[:4]
    
    # Satisfaction score distribution
    satisfaction_distribution = []
    for i in range(1, 6):
        count = SurveyResponse.objects.filter(satisfaction_score=i).count()
        percentage = (count / total_responses * 100) if total_responses > 0 else 0
        satisfaction_distribution.append({
            'score': i,
            'count': count,
            'percentage': percentage
        })
    
    return render(request, 'main/analytics.html', {
        'total_responses': total_responses,
        'avg_satisfaction': avg_satisfaction,
        'avg_recommend': avg_recommend,
        'avg_quality': avg_quality,
        'avg_price': avg_price,
        'avg_support': avg_support,
        'completion_rate': completion_rate,
        'recent_feedback': recent_feedback,
        'satisfaction_distribution': satisfaction_distribution,
        'usage_distribution': usage_distribution,
    })

def api_responses(request):
    responses = SurveyResponse.objects.all().values()
    return JsonResponse(list(responses), safe=False)

def export_csv(request):
    import io
    import csv
    
    # Create a string buffer
    output = io.StringIO()
    writer = csv.writer(output)
    
    # Write headers
    writer.writerow([
        'ID', 'Name', 'Email', 'Satisfaction Score', 'Would Recommend',
        'Quality Rating', 'Price Rating', 'Support Rating', 'Product Usage',
        'Favorite Feature', 'Improvement Suggestions', 'Created At'
    ])
    
    # Write data rows
    responses = SurveyResponse.objects.all().order_by('-created_at')
    for survey_response in responses:
        writer.writerow([
            survey_response.id,
            survey_response.name or '',
            survey_response.email or '',
            survey_response.satisfaction_score,
            survey_response.would_recommend,
            survey_response.quality_rating,
            survey_response.price_rating,
            survey_response.support_rating,
            survey_response.get_product_usage_display() if survey_response.product_usage else '',
            survey_response.favorite_feature or '',
            survey_response.improvement_suggestions or '',
            survey_response.created_at.strftime('%Y-%m-%d %H:%M:%S')
        ])
    
    # Prepare response
    response = HttpResponse(output.getvalue(), content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="survey_responses_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv"'
    
    return response