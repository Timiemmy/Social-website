from django import forms
from .models import Image
from django.core.files.base import ContentFile  # Imported this for using requests
from django.utils.text import slugify
import requests


class ImageCreateForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'url', 'description']
        widgets = {
            # This widget will be used because we don't want the url to be visible to users.
            'url': forms.HiddenInput,
        }

    def clean_url(self):
        url = self.cleaned_data['url']
        # This is the valid filename ends allowed
        valid_extensions = ['jpg', 'jpeg', 'png']
        # This will split the filename to check if the filenaeme has a valid extension.
        extension = url.rsplit('.', 1)[1].lower()
        if extension not in valid_extensions:  # If not, it will raise this extension.
            raise forms.ValidationError('The given URL does not '
                                        'match valid image extensions.')
        return url

    # Overriding the save method to retrieve the image by the given url.
    def save(self, force_insert=False,
             force_update=False,
             commit=True):  # The new image instance is created by calling save method.
        image = super().save(commit=False)
        # The url is retrieved from cleaned data dic of the form.
        image_url = self.cleaned_data['url']
        name = slugify(image.title)  # This will generate slug from title.
        extension = image_url.rsplit('.', 1)[1].lower()
        image_name = f'{name}.{extension}'
        # download image from the given URL with request library
        response = requests.get(image_url)
        image.image.save(image_name,
                         # This will save image to media dir
                         ContentFile(response.content),
                         save=False)  # This will prevent it from saving to db.
        if commit:  # The image will be saved to db if commit parameter is true.
            image.save()
        return
