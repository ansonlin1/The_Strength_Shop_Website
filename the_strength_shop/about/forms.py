from django.forms import ModelForm
from .models import EmailReachOuts

# Define the class of a form
class EmailReachOutsForm(ModelForm):
    class Meta:
        # Write the name of models for which the form is made
        model = EmailReachOuts
        # Custom fields
        fields = '__all__'

    # # Function will be used for the validation
    # def clean(self):
    #     # Data from the form is fetched using super function
    #     super(EmailReachOutsForm, self).clean()
    #
    #     # Extract field data
    #     first_name = self.cleaned_data.get('first_name')
    #
    #     # Conditions to be met
    #     if len(first_name) < 0:
    #         self._errors['first_name'] = self.error_class(['Required'])
    #
    #     # return any errors if found
    #     return self.cleaned_data
