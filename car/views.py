from django.shortcuts import render, redirect
from . import forms
from . import models
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
# Create your views here.

def add_car(request):
    if request.method == 'POST':
        car_form = forms.CarForm(request.POST)
        if car_form.is_valid():
            car_form.save()
            return redirect('add_car')
    else:
        car_form = forms.CarForm()
    return render(request, 'add_car.html', {'form': car_form})

class DetailCarView(DetailView):
    model = models.Car
    pk_url_kwarg = 'id'
    template_name = 'car_details.html'

    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data=self.request.POST)
        post = self.get_object()
        car = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        if car.quantity > 0 and request.user not in car.purchased_by.all():
            # Purchase the car
            car.quantity -= 1
            car.purchased_by.add(request.user)
            car.save()

            
        return self.get(request, *args, **kwargs)
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        comments = post.comments.all()
        
        comment_form = forms.CommentForm()
        
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context
    # def post(self, request, *args, **kwargs):
    #     car = self.get_object()
    #     if car.quantity > 0 and request.user not in car.purchased_by.all():
    #         # Purchase the car
    #         car.quantity -= 1
    #         car.purchased_by.add(request.user)
    #         car.save()

    #     return redirect('car_details', id=car.id)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     car = self.object
    #     comments = car.comments.all()
    #     comment_form = forms.CommentForm()

    #     context['comments'] = comments
    #     context['comment_form'] = comment_form
    #     return context

