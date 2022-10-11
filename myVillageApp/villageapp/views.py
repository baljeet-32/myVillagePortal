import os
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from villageapp.models import Userquery
from villageapp.models import Notification, Complaints, Jobs, Review

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.contrib.auth.models import User

from .form import AddNotification, AddComplaints, AddJob, UserQuery


def home(req):
    if req.method == 'POST':
        fm = UserQuery(req.POST)
        if fm.is_valid():
            fm.save()
            fm = UserQuery()
            messages.success(
                req, f'Sent Successfully !')
            return redirect('village-home')
    else:
        fm = UserQuery()
    return render(req, 'villageapp/index.html', {'form': fm})

### HANDLING NOTIFICATION PART ######


class NotificationListView(ListView):
    model = Notification
    template_name = 'villageapp/notification.html'
    context_object_name = 'data'
    ordering = ['date_posted']
    paginate_by = 5

    fm = UserQuery()

    def get_context_data(self, **kwargs):
        context = super(NotificationListView, self).get_context_data(**kwargs)
        context.update({'form': self.fm})
        return context


class NotificationDetailView(DetailView):
    model = Notification
    template_name = 'villageapp/notif_detail.html'
    context_object_name = 'item'


class NotificationCreateView(LoginRequiredMixin, CreateView):
    model = Notification
    # fields = ['title', 'content']
    form_class = AddNotification
    template_name = 'villageapp/add_new_notify.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class NotificationUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Notification
    # fields = ['title', 'content']
    form_class = AddNotification
    template_name = 'villageapp/add_new_notify.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class NotificationDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Notification
    template_name = 'villageapp/notify_confirm_delete.html'
    success_url = "/notification/"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


### HANDLING Complaints PART ######


class ComplaintsListView(ListView):
    model = Complaints
    template_name = 'villageapp/complaints.html'
    context_object_name = 'data'
    ordering = ['date_posted']
    paginate_by = 5
    fm = UserQuery()

    def get_context_data(self, **kwargs):
        context = super(ComplaintsListView, self).get_context_data(**kwargs)
        context.update({'form': self.fm})
        return context


class SolvedComplaintsListView(ListView):
    model = Complaints
    template_name = 'villageapp/solved_complaints.html'
    context_object_name = 'data'
    ordering = ['date_posted']
    fm = UserQuery()

    def get_context_data(self, **kwargs):
        context = super(SolvedComplaintsListView,
                        self).get_context_data(**kwargs)
        context.update({'form': self.fm})
        return context


class UnSolvedComplaintsListView(ListView):
    model = Complaints
    template_name = 'villageapp/unsolved_complaints.html'
    context_object_name = 'data'
    ordering = ['date_posted']
    fm = UserQuery()

    def get_context_data(self, **kwargs):
        context = super(UnSolvedComplaintsListView,
                        self).get_context_data(**kwargs)
        context.update({'form': self.fm})
        return context

    # paginate_by = 1


class UserComplaintsListView(ListView):
    model = Complaints
    template_name = 'villageapp/user_complaints.html'
    context_object_name = 'data'
    ordering = ['date_posted']
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Complaints.objects.filter(author=user).order_by('-date_posted')

    fm = UserQuery()

    def get_context_data(self, **kwargs):
        context = super(UserComplaintsListView,
                        self).get_context_data(**kwargs)
        context.update({'form': self.fm})
        return context


class ComplaintsDetailView(DetailView):
    model = Complaints
    template_name = 'villageapp/comp_detail.html'
    context_object_name = 'item'


class ComplaintsCreateView(LoginRequiredMixin, CreateView):
    model = Complaints
    # fields = ['title', 'category', 'descritrion', 'image']
    form_class = AddComplaints
    template_name = 'villageapp/add_new_comp.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ComplaintsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Complaints
    # fields = ['title', 'category', 'descritrion', 'image']
    form_class = AddComplaints
    template_name = 'villageapp/add_new_comp.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class ComplaintsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Complaints
    template_name = 'villageapp/comp_confirm_delete.html'
    success_url = "/complaints/"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


# JOBS

# 1.ListView

class JobsListView(ListView):
    model = Jobs
    template_name = 'villageapp/jobs.html'
    context_object_name = 'data'
    ordering = ['-date_posted']
    paginate_by = 5

# 2.Detailed View


class JobsDetailView(DetailView):
    model = Jobs
    template_name = 'villageapp/job_detail.html'
    context_object_name = 'item'


# 3. Add new job

class JobsCreateView(LoginRequiredMixin, CreateView):
    model = Jobs
    # fields = ['title', 'descritrion', 'no_of_opening',  'salary_desc', 'location', 'contact_details', 'status']
    form_class = AddJob
    template_name = 'villageapp/add_new_job.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# 4. Update Existing


class JobsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Jobs
    # fields = ['title', 'descritrion', 'no_of_opening',
    #           'salary_desc', 'location', 'contact_details', 'status']
    form_class = AddJob
    template_name = 'villageapp/add_new_job.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


# 4. Delete Job
class JobsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Jobs
    template_name = 'villageapp/job_confirm_delete.html'
    success_url = "/jobs/"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

# 5.Jobs by user filter


class UserJobsListView(ListView):
    model = Jobs
    template_name = 'villageapp/user_jobs.html'
    context_object_name = 'data'
    ordering = ['-date_posted']
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Jobs.objects.filter(author=user).order_by('-date_posted')


# Reviews Functionality


# 1. Show Review
# class ReviewListView(ListView):
#     model = Review
#     template_name = 'villageapp/base.html'
#     context_object_name = 'data'
#     ordering = ['-date_posted']
#     paginate_by = 5

#################################


def about(req):
    fm = UserQuery()
    return render(req, 'villageapp/about.html', {'form': fm})


def delete_query(req, id):
    if req.method == 'POST':
        pi = Userquery.objects.get(pk=id)
        pi.delete()
        messages.success(
            req, f'Query deleted successfully')
    return redirect('user-profile')


def listenNotification(req):

    mytext = 'Welcome to geeksforgeeks! hii hello hello'

    # Language in which you want to convert
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("welcome.mp3")
    os.system("mpg321 welcome.mp3")
    return redirect('village-notification')
