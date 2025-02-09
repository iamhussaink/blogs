from django.shortcuts import render, HttpResponse, redirect
from .models import Comment, Blogs , Contact_me
from .forms import CommentForm,ContactForm
from django.db.models import Q
from django.contrib import messages

# Create your views here.
def aboutme(request):
    return render(request, 'aboutme.html')

'''def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                contact = Contact_me(
                    email=form.cleaned_data['email'],
                    subject=form.cleaned_data['subject'],
                    message=form.cleaned_data['message']
                )
                contact.save()
                messages.success(request, 'Your message has been sent successfully!')
            except Exception as e:
                messages.error(request, f'An error occurred: {e}') # Helpful debugging
                return render(request, 'contact.html', {'form': form})  # Return HttpResponse here!
        else:
            messages.error(request, 'Please correct the errors below.')
            return render(request, 'contact.html', {'form': form}) # Return HttpResponse here!
    else:  # This is the GET request
        form = ContactForm()
        return render(request, 'contact.html', {'form': form}) # Return HttpResponse here!'''

def contact(request):
    if request.method == 'POST':
        print("Received POST request")
        form = ContactForm(request.POST)
        if form.is_valid():
            print("Form is valid!")
            try:
                contact = Contact_me(
                    email=form.cleaned_data['email'],
                    subject=form.cleaned_data['subject'],
                    message=form.cleaned_data['message']
                )
                contact.save()
                print("Contact saved!")
                return redirect('contact_success')
            except Exception as e:
                print(f"Error saving contact: {e}")
                return render(request, 'contact.html', {'form': form})
        else:
            print("Form is invalid!")
            print(form.errors)
            return render(request, 'contact.html', {'form': form})
    else:
        print("Received GET request")
        form = ContactForm()
        return render(request, 'contact.html', {'form': form})


def home(request):
    post = Blogs.objects.all().order_by('created_date')
    return render(request, 'home.html', {'post': post})

def blog_detail(request, pk):
    blog = Blogs.objects.get(pk=pk)  # Include the required argument
    comments = blog.comment_set.all()  # Fetch comments related to the blog

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)  # No need to set comment.blog
            comment.blog = blog  # Might still be redundant
            comment.save()  # Save the comment after associating it with the blog
            return redirect('blog_detail', pk=pk)
    else:
        form = CommentForm()
    return render(request, 'blog_detail.html', {'blog': blog, 'comments': comments, 'form': form})

def search(request):
    query = request.GET.get('query')
    blogs = Blogs.objects.filter(
        Q(title__icontains=query) | Q(content__icontains=query)
    )
    return render(request, 'search.html', {'blogs': blogs})

def contact_success(request):
    return render(request, 'contact_success.html')
