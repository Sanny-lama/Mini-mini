from django import forms
from .models import Post


class PostForm(forms.ModelForm):

    caption = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            "class": "field-control",
            "rows": 4,
            "placeholder": "What's on your mind? Share your moment…",
        }),
    )

    location = forms.CharField(
        required=False,
        max_length=150,
        widget=forms.TextInput(attrs={
            "class": "field-control",
            "placeholder": "Add a location…",
        }),
    )

    image = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={
            "accept": "image/*",
        }),
    )

    class Meta:
        model  = Post
        fields = ["caption", "location", "image"]

    def clean(self):
        cleaned = super().clean()
        caption = cleaned.get("caption", "").strip()
        image   = cleaned.get("image")
        if not caption and not image:
            if not (self.instance.pk and self.instance.has_image()):
                raise forms.ValidationError(
                    "A post must have at least a caption or a photo."
                )
        return cleaned
