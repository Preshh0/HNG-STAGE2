from django.shortcuts import redirect, render
from .forms import ContactForm

def contact_view(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        
        if form.is_valid():
            form.save()
            return render(request, 'app/success.html')
            
    context = {'form': form}
    return render(request, 'app/index.html', context)
