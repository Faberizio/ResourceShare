from django import forms

class PostResourceForm(forms.Form):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "title-input",
                "placeholder": "Enter a title",
            }
        )
    )  # type='text'
    link = forms.URLField()  # type='url'
    description = forms.CharField(widget=forms.Textarea)  # type='textarea'
    
    CATEGORY_CHOICES = [
        ('category1', 'Programming Languages'),
        ('category2', 'Databases'),
    ]
    category = forms.ChoiceField(
        choices=CATEGORY_CHOICES,
        widget=forms.RadioSelect
    )

    TAG_CHOICES = [
        ('tag1', 'Python'),
        ('tag2', 'Django'),
        ('tag3', 'Paid'),
        ('tag4', 'Free'),
    ]
    tags = forms.MultipleChoiceField(
        choices=TAG_CHOICES,
        widget=forms.SelectMultiple
    )

    
    