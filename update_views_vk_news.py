from .models import Vk

#...


# def...

def hidden_post(request, pk):
    Vk.hidden(pk)
    return redirect('vk:vk')                                                               


def delete_post(request):
    Vk.objects.all().delete()
    return redirect('vk:vk')
