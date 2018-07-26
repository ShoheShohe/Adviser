from django import forms
from .models import Attitude


class AttitudeForm(forms.ModelForm):
    class Meta:
        model = Attitude
        fields = (
            'declaration',
            'situation',
            'wrong_action',
            'reason',
            'logic',
            'draft_logic',
        )
        widgets = {
            'declaration': forms.TextInput(attrs={'placeholder': 'Be simple'}),
            'situation': forms.Textarea(attrs={'rows': 4}),
            'wrong_action': forms.Textarea(attrs={'rows': 4}),
            'reason': forms.Textarea(attrs={'rows': 2}),
            'logic': forms.Textarea(attrs={'rows': 6}),
            'draft_logic': forms.Textarea(attrs={'rows': 20}),
        }
