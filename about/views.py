from django.shortcuts import render
from .models import About

# Create your views here.


def about(request, about):
    """
    Display the about page.

    **Content**

    **Template:**

    :template:`about/about.html`
    """

    about = get_object_or_404(About, about=about)

    return render(
        request,
        "about/about.html",
        {"about": about}
    )
