from django.db import models

class SurveyResponse(models.Model):
    # Personal Information
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField(default=25)  # Added default
    gender = models.CharField(max_length=10, choices=[
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
        ('prefer_not', 'Prefer not to say')
    ], default='prefer_not')  # Added default
    country = models.CharField(max_length=50, default='India')
    
    # Survey Questions
    satisfaction_score = models.IntegerField(choices=[(i, f'{i} - {["Very Poor", "Poor", "Average", "Good", "Excellent"][i-1]}') for i in range(1, 6)], default=3)  # Added default
    would_recommend = models.IntegerField(choices=[(i, f'{i} - {["Very Unlikely", "Unlikely", "Neutral", "Likely", "Very Likely"][i-1]}') for i in range(1, 6)], default=3)  # Added default
    
    # Product/Service Specific
    product_usage = models.CharField(max_length=20, choices=[
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
        ('rarely', 'Rarely'),
        ('first_time', 'First Time')
    ], default='monthly')  # Added default
    
    # Rating Categories
    quality_rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=3)  # Added default
    price_rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=3)  # Added default
    support_rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=3)  # Added default
    
    # Additional Feedback
    favorite_feature = models.CharField(max_length=100, blank=True, verbose_name="What's your favorite feature?")
    improvement_suggestions = models.TextField(blank=True, verbose_name="Suggestions for improvement")
    feedback = models.TextField(blank=True, verbose_name="Additional comments")
    
    # Timestamp
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - Satisfaction: {self.satisfaction_score}/5"