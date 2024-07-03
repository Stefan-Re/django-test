import string
import random
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.mail import send_mail, EmailMessage
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.views.generic import CreateView
from djangoProject.settings import EMAIL_HOST_USER
from userextend.forms import UserForm
from userextend.models import UserHistory


class UserCreateView(CreateView):
    template_name = 'userextend/create_user.html'
    model = User
    form_class = UserForm
    success_url = reverse_lazy('login')


    # Metoda form_valid - este o metoda pt clase de view-uri (UpdateView,
    # CreateView, DeleteView) care este apelata atunci cand formularul este
    # trimis catre salvare iar programatorul poate sa suplimenteze cu actiuni noi

    def form_valid(self, form):
       if form.is_valid():
          new_user = form.save(commit=False) # commit= False,  datele din formular nu sunt salvate

          # Customizare first_name si last_name
          new_user.first_name = new_user.first_name.title()
          # atribui valoarea new_user.first_name.title() campului first_name al obiectului new_user
          new_user.last_name = new_user.last_name.title()

          rand_num = random.randint(100000, 999999)

          new_user.username = new_user.first_name[0].lower() + new_user.last_name.lower() + '_' + str(rand_num)

          new_user.save()

          # Trimitere mail fara template
          subject = "Confirmare cont nou!"
          message = f"Felicitari, {new_user.first_name} {new_user.last_name}! Contul a fost activat!"
          # send_mail(subject, message, EMAIL_HOST_USER, [new_user.email])

          details_user = {
              'full_name': f'{new_user.first_name} {new_user.last_name}',
              'username': new_user.username,
          }

          subject = 'Confirmare cont nou'
          message = get_template('mail.html').render(details_user)
          mail = EmailMessage(subject, message, EMAIL_HOST_USER, [new_user.email])
          mail.content_subtype = "html"
          #mail.send()


          # Istoric
          history_message = (f'User a fost adaugat cu success.First_name:{new_user.first_name}, last_name:{new_user.last_name},'
                             f'email:{new_user.email}, username:{new_user.username}')

          UserHistory.objects.create(message=history_message)


          return super(UserCreateView, self).form_valid(form)