from django import forms
from macros import informations

class ProfileForm(forms.Form):
    name = forms.CharField(max_length=30)

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        for item, fields in informations:
            self.fields[item] = forms.BooleanField(required=False, label=item)
            for field in fields:
                self.fields[field + '_' + item] = forms.BooleanField(required=False, label=field)

        phone_number = forms.CharField(required=True, label='Phone Number', max_length=10)
        self.phone_list = [phone_number]
        self.update_phoneNumbers()

    def update_phoneNumbers(self):
        for i in range(0, len(self.phone_list)):
            self.fields['Phone_' + str(i)] = self.phone_list[i]


    def add_phoneNumber(self, howmany=1):
        for i in range(0, howmany):
            phone_number = forms.CharField(required=False, label='Phone Number', max_length=10)
            self.phone_list.append(phone_number)
        self.update_phoneNumbers()

    def __unicode__(self):
        return "Profile Form"

