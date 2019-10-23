from django.shortcuts import render
from .models import Contact
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required()
def contact_detail(request, uuid):
    contact = Contact.objects.get(uuid=uuid)
    return render(request,
                'contacts/contact_detail.html',
                {'contact': contact}
    )
