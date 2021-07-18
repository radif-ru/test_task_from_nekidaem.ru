from django import forms

from personalblogapp.models import ReadPost


class FormControlMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ReadPostForm(FormControlMixin, forms.ModelForm):
    class Meta:
        model = ReadPost
        # exclude = ('user',)
        fields = '__all__'
