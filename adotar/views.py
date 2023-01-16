from django.shortcuts import render, redirect
from divulgar.models import Pet, Raca
from django.contrib import messages
from datetime import datetime
from .models import PedidoAdocao


def listar_pets(request):
    if request.method == "GET":
        pets = Pet.objects.filter(status="P")
        racas = Raca.objects.all()
        cidade = request.GET.get('cidade')
        raca_filter = request.GET.get('raca')

        if cidade:
            pets = pets.filter(cidade__icontains=cidade)

        if raca_filter:
            pets = pets.filter(raca__id=raca_filter)

        return render(request, 'listar_pets.html',
                      {'pets': pets,
                       'racas': racas,
                       'cidade': cidade,
                       'raca_filter': raca_filter})


def pedido_adocao(request, id_pet):
    pet = Pet.objects.filter(id=id_pet).filter(status="P")
    if not pet.exists():
        messages.error(request, 'Esse pet já foi adotado :)')
        return redirect('/adotar')
    pedido = PedidoAdocao(pet=pet.first(),
                          usuario=request.user,
                          data=datetime.now())

    pedido.save()

    messages.sucess(
        request, 'Pedido de adoção realizado, você receberá um e-mail caso ele seja aprovado.')
    return redirect('/adotar')


def ver_pedido_adocao(request):
    if request.method == "GET":
        pedidos = PedidoAdocao.objects.filter(
            usuario=request.user).filter(status="AG")
        return render(request, 'ver_pedido_adocao.html', {'pedidos': pedidos})