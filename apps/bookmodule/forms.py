from django import forms
from .models import Book, student1,student2,address1,address2,register1

class BookForm(forms.ModelForm):
    
    title = forms.CharField(
        max_length=50,
        label="Title",
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter book title',
            'class': 'form-control'
        })
    )
    author = forms.CharField(
        max_length=50,
        label="Author",
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter author name',
            'class': 'form-control'
        })
    )
    price = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        label="Price",
        widget=forms.NumberInput(attrs={
            'placeholder': 'Enter price',
            'class': 'form-control'
        })
    )
    edition = forms.IntegerField(
        label="Edition",
        widget=forms.NumberInput(attrs={
            'placeholder': 'Enter edition',
            'class': 'form-control'
        })
    )

    class Meta:
        model = Book
        fields = ['title', 'author', 'price', 'edition']
        

# class AddressForm1(forms.ModelForm):
#     class Meta:
#         model = address1
#         fields = ['city']

# class AddressForm2(forms.ModelForm):
#     class Meta:
#         model = address2
#         fields = ['city']


class StudentForm1(forms.ModelForm):
    class Meta:
        model = student1
        fields = ['name', 'address']  # Include address here
    

class StudentForm2(forms.ModelForm):
    class Meta:
        model = student2
        fields = ['name', 'address']
        widgets = {
              'address' : forms.CheckboxSelectMultiple(),
        }

class registration1(forms.ModelForm):
    class Meta:
        model = register1
        fields = ['name', 'age','picture']
        
# class DocumentForm(forms.ModelForm):
#     class Meta:
#         model  = Document
#         fields = ['title', 'file']
        
        
    
        
        