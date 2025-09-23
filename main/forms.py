from django import forms
from .models import SurveyResponse

class SurveyForm(forms.ModelForm):
    class Meta:
        model = SurveyResponse
        fields = [
            'name', 'email', 'age', 'gender', 'country',
            'satisfaction_score', 'would_recommend', 'product_usage',
            'quality_rating', 'price_rating', 'support_rating',
            'favorite_feature', 'improvement_suggestions', 'feedback'
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter your full name',
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter your email address',
                'required': True
            }),
            'age': forms.NumberInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Your age',
                'min': 18,
                'max': 100
            }),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Your country',
                'value': 'India'
            }),
            'satisfaction_score': forms.Select(attrs={'class': 'form-control'}),
            'would_recommend': forms.Select(attrs={'class': 'form-control'}),
            'product_usage': forms.Select(attrs={'class': 'form-control'}),
            'quality_rating': forms.Select(attrs={'class': 'form-control'}),
            'price_rating': forms.Select(attrs={'class': 'form-control'}),
            'support_rating': forms.Select(attrs={'class': 'form-control'}),
            'favorite_feature': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'What do you like most about our service?'
            }),
            'improvement_suggestions': forms.Textarea(attrs={
                'class': 'form-control', 
                'placeholder': 'What can we do better?',
                'rows': 3
            }),
            'feedback': forms.Textarea(attrs={
                'class': 'form-control', 
                'placeholder': 'Any other comments or feedback...',
                'rows': 3
            }),
        }
        
    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age and (age < 18 or age > 100):
            raise forms.ValidationError("Age must be between 18 and 100")
        return age