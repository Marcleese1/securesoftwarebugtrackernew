from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from ticket import models
from django.urls import reverse_lazy
from.models import Ticket, Comment
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseForbidden
'''
class OwnerProtectMixin(object):
    def dispatch(self, request, *args, **kwargs):
        objectUser = self.get_object()
        if objectUser.user != self.request.user:
            return HttpResponseForbidden()
        return super(OwnerProtectMixin, self).dispatch(request, *args, **kwargs)'''

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
        template_name = 'editTicket.html'
        fields = ['ticketName', 'ticketDescription', 'condition', 'priority', 'role']
        success_url = reverse_lazy('dashboard')
    #else:
        #model = Ticket
        #template_name = 'dashboard.html'
        #fields = ['ticketName', 'ticketDescription', 'condition', 'priority', 'role']


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
	template_name = ''

@method_decorator(login_required, name='dispatch')
class CommentDeleteView(OwnerProtectMixin, DeleteView):
	model = Comment
	success_url = 'editTicket'''''