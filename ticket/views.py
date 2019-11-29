from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, TemplateView
from ticket import models
from django.urls import reverse_lazy
from.models import Ticket, Comment
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseForbidden
from .forms import EditTicketForms, CommentForm
from django.contrib import messages

class OwnerProtectMixin(object):
    def dispatch(self, request, *args, **kwargs):
        objectUser = self.get_object()
        if objectUser.user != self.request.user:
            return HttpResponseForbidden()
        return super(OwnerProtectMixin, self).dispatch(request, *args, **kwargs)

class dashView(ListView):
    model = models.Ticket
    template_name = 'dashboard.html'


class createTicketView(LoginRequiredMixin, CreateView):
    model = Ticket
    template_name = 'createTicket.html'
    fields = ('ticketName', 'ticketDescription', 'priority', 'role')
    success_url = reverse_lazy('dashboard')


class EditTicketView(UpdateView, LoginRequiredMixin):
        model = Ticket
        post_form_class = EditTicketForms
        comment_form_class = CommentForm
        template_name = 'editTicket.html'
        fields = ['ticketName', 'ticketDescription', 'condition', 'priority', 'role']
        success_url = reverse_lazy('dashboard')
    #else:
        #model = Ticket
        #template_name = 'dashboard.html'
        #fields = ['ticketName', 'ticketDescription', 'condition', 'priority', 'role']


def CreateCommentView(request, pk):
    post = get_object_or_404(Ticket, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            Comment = form.save(commit=False)
            Comment.ticketId = post
            #form.cleaned_data('description')
            Comment.save()
            return redirect('viewComment', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'Createcomment.html', {'form': form})

class viewComments(ListView):
    model = Comment
    template_name = 'editTicket.html'

'''
class CommentCreateView(CreateView):
	model = Comment
	fields = ['description', 'userId', 'timestamp']

	def form_valid(self, form):
		_ticket = get_object_or_404(Ticket, id=self.kwargs['pk'])
		form.instance.user = self.request.user
		form.instance.forum = _ticket
		return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class CommentUpdateView(OwnerProtectMixin, UpdateView):
	model = Comment
	fields = ['description']
	template_name = 'editTicket.html'

@method_decorator(login_required, name='dispatch')
class CommentDeleteView(OwnerProtectMixin, DeleteView):
	model = Comment
	success_url = 'editTicket'''''