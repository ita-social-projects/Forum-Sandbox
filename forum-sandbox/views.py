from django.http import JsonResponse
from django.views import View
from profiles.models import Profile, ProfilesImage
from authentication.models import CustomUser
from django.shortcuts import render

class MainPageView(View):
    def get(self, request, *args, **kwargs):
        
        clients_data = Profile.objects.order_by('id')[:6].values(
            'common_info', 'official_name', 'address', 'service_info', 'product_info'
        )

        clients_json = []
        for client in clients_data:
            client_json = {
                'common_info': client['common_info'],
                'official_name': client['official_name'],
                'address': client['address'],
                'service_info': client['service_info'],
                'product_info': client['product_info'],
            }
            clients_json.append(client_json)

        
        partners_data = ProfilesImage.objects.order_by('id')[:6].values('name', 'path')
        partners_json = [{'name': partner['name'], 'path': "/media/"+partner['path']} for partner in partners_data]
        context = {
            'clients': clients_json,
            'partners': partners_json
        }

        return render(request, 'main_page/index.html', context)

