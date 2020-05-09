from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import UserMedico
from .forms import UserMedicoForm, UserMedicoEditForm
from django.urls import reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse
from functools import reduce
from django.http import JsonResponse, HttpResponse
import operator
from django.db.models import Q


# Create your views here.

class UserCreate(generic.CreateView):
    # Vista del formulario para agregar un usuario 
    model = UserMedico
    template_name = "users/user_form.html"
    form_class = UserMedicoForm
    success_url = reverse_lazy('Cestock:PaginaPrincipal')

    def form_valid(self, form):
        return super().form_valid(form)


def user_update(request, pk):
    # Vista para el formulario de creación del modelo usuario
    user_editado = None
    user_editado = get_object_or_404(UserMedico, pk=pk)
    print(user_editado)
    if request.method == 'POST':

        form = UserMedicoEditForm(request.POST, request.FILES, instance=user_editado)
        print(request.POST)
        if form.is_valid():
            user_editado = form.save()
            user_editado.save()
            return redirect(reverse('users:lista_users'))
        else:
            print(form.errors)
    else:
        form = UserMedicoEditForm(instance=user_editado)
    data = {
        'form': form,
        'user_editado': user_editado
    }

    return render(request, 'users/user_form.html', data)


# Vista listado de usuarios(doctores)
def lista_users(request):
    context = {
    }
    print("user_list")
    return render(request, 'users/lista_users.html', context)


# Vista busqueda en listado de usuarios(doctores)
def usuario_lista_database(request):
    start = int(request.POST["start"])
    per_page = int(request.POST["length"])
    search = request.POST["search[value]"].strip()
    order_column = int(request.POST["order[0][column]"])
    order_dir = request.POST["order[0][dir]"]

    page = (start / per_page) + 1

    user_list = UserMedico.objects.all()
    print(user_list)
    if search != "":
        keywords = search.split()

        id_qs = reduce(operator.or_, (Q(id__icontains=keyword.strip()) for keyword in keywords))
        username_qs = reduce(operator.or_, (Q(username__icontains=keyword.strip()) for keyword in keywords))
        rut_medico_qs = reduce(operator.or_, (Q(rut_medico__icontains=keyword.strip()) for keyword in keywords))
        email_qs = reduce(operator.or_, (Q(email__icontains=keyword.strip()) for keyword in keywords))

        if len(keywords) > 0:
            user_list = user_list.filter(Q(id_qs) | Q(username_qs) | Q(rut_medico_qs) | Q(email_qs))

    user_list = user_list.order_by('-date_joined')

    total = user_list.count()

    paginator = Paginator(user_list, per_page)  # Show per_page

    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        users = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        users = paginator.page(paginator.num_pages)

    dataArray = []
    for user in users:
        try:

            url_edit = reverse('users:editar_doctor', kwargs={'pk': user.id})
            edit_button = '<a href="' + url_edit + '" class="btn btn-link"><i class="fas fa-pen"></i></a>'
            delete_button = '<button class="btn btn-link" onclick="delete_user(' + str(user.id) + ')"  ><i class="fas fa-trash"></i></button>'

            if user.is_staff:
                actions = edit_button 
            else:
                actions = edit_button + delete_button

            dataArray.append([
                user.id,
                user.username,
                user.rut_medico,
                user.email,
                actions,
            ])

        except Exception as e:
            print(e)

    if order_dir == 'asc':
        dataArray = sorted(dataArray, key=lambda x: x[order_column])
    else:
        dataArray = sorted(dataArray, key=lambda x: x[order_column], reverse=True)

    output = {
        "recordsTotal": total,
        "recordsFiltered": total,
        "data": dataArray
    }
    return JsonResponse(output)


def eliminar_doctor(request):
    if request.POST:
        user = UserMedico.objects.filter(id=request.POST['id'])
        user.delete()
        return JsonResponse({"status": 1})
    else:
        return JsonResponse({"status": 0})