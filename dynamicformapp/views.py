

# dynamicformapp/views.py
from django.shortcuts import render, redirect
from .forms import DynamicFormDataForm, DynamicFormDataFormSet
from .models import DynamicFormData

def dynamic_form_view(request):
    if request.method == 'POST':
        formset = DynamicFormDataFormSet(request.POST, queryset=DynamicFormData.objects.none())
        if formset.is_valid():
            instances = []
            for form in formset:
                if form.is_valid():
                    instance = form.save(commit=False)
                    instances.append(instance)
                    print(f"Form data: {form.cleaned_data}")
                    print(f"Instance before save: {instance}")
                    instance.save()
                    print(f"Instance after save: {instance}")
                else:
                    print(f"Form errors: {form.errors}")
            return redirect('success_view')  # Use the correct URL name here
        else:
            print(f"Formset errors: {formset.errors}")
    else:
        formset = DynamicFormDataFormSet(queryset=DynamicFormData.objects.none())

    return render(request, 'dynamicformapp/dynamic_form.html', {'formset': formset})

def success_view(request):
    return render(request, 'dynamicformapp/success.html')

























































#dynamicformapp/views.py
# from django.shortcuts import render, redirect
# from .forms import DynamicForm
# from .models import DynamicFormData

# def dynamic_form_view(request):
#     # Retrieve the list of form data from the session
#     form_data_list = request.session.get('form_data_list', [])

#     if request.method == 'POST':
#         form = DynamicForm(request.POST)
#         if form.is_valid():
#             # Save the current form data
#             current_data = form.cleaned_data
#             form_data_list.append(current_data)

#             # Update the session variable
#             request.session['form_data_list'] = form_data_list

#             # Check if the submit button is clicked
#             if 'submit' in request.POST:
#                 # Save data from all form data in the correct order
#                 for data in form_data_list:
#                     DynamicFormData.objects.create(
#                         name=data['name'],
#                         password=data['password'],
#                         data=data['data']
#                     )

#                 # Clear the session variable
#                 request.session.pop('form_data_list', None)

#                 # Redirect to a success page or another URL
#                 return redirect('success_url_name')
#             else:
#                 # Redirect to the same page or another URL
#                 return redirect('success_url_name')

#     else:
#         form = DynamicForm()

#     return render(request, 'dynamicformapp/dynamic_form.html', {'form': form, 'form_data_list': form_data_list})

# dynamicformapp/views.py
# from django.shortcuts import render, redirect
# from .forms import DynamicForm
# from .models import DynamicFormData

# def dynamic_form_view(request):
#     # Retrieve the list of form data from the session
#     form_data_list = request.session.get('form_data_list', [])

#     if request.method == 'POST':
#         form = DynamicForm(request.POST)
#         if form.is_valid():
#             # Save the current form data
#             current_data = form.cleaned_data
#             form_data_list.append(current_data)

#             # Update the session variable
#             request.session['form_data_list'] = form_data_list

#             # Check if the submit button is clicked
#             if 'submit' in request.POST:
#                 # Save data from all form data in the correct order
#                 for data in form_data_list:
#                     DynamicFormData.objects.create(
#                         name=data['name'],
#                         password=data['password'],
#                         data=data['data']
#                     )

#                 # Clear the session variable
#                 request.session.pop('form_data_list', None)

#                 # Redirect to a success page or another URL
#                 return redirect('success_url_name')

#     else:
#         form = DynamicForm()

#     # Redirect to the same page when the form is not submitted
#     return render(request, 'dynamicformapp/dynamic_form.html', {'form': form, 'form_data_list': form_data_list})

# dynamicformapp/views.py
# from django.shortcuts import render, redirect
# from .forms import DynamicForm
# from .models import DynamicFormData

# def dynamic_form_view(request):
#     if request.method == 'POST':
#         form = DynamicForm(request.POST)
#         if form.is_valid():
#             # Save the current form data to the database
#             current_data = form.cleaned_data
#             DynamicFormData.objects.create(
#                 name=current_data['name'],
#                 password=current_data['password'],
#                 data=current_data['data']
#             )

#             # Redirect to a success page or another URL
#             return redirect('success_url_name')
#     else:
#         form = DynamicForm()

#     return render(request, 'dynamicformapp/dynamic_form.html', {'form': form})

# dynamicformapp/views.py
# from django.shortcuts import render, redirect
# from django.forms import formset_factory
# from .forms import DynamicForm
# from .models import DynamicFormData

# def dynamic_form_view(request):
#     DynamicFormSet = formset_factory(DynamicForm, extra=1)
    
#     if request.method == 'POST':
#         formset = DynamicFormSet(request.POST)
#         if formset.is_valid():
#             for form in formset:
#                 # Save the current form data to the database
#                 current_data = form.cleaned_data
#                 DynamicFormData.objects.create(
#                     name=current_data['name'],
#                     password=current_data['password'],
#                     data=current_data['data']
#                 )

#             # Redirect to a success page or another URL
#             return redirect('success_url_name')

#     else:
#         formset = DynamicFormSet()

#     return render(request, 'dynamicformapp/dynamic_form.html', {'formset': formset})
