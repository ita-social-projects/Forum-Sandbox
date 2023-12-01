from django.http import JsonResponse
from django.views import View
from profiles.models import Profile
from authentication.models import CustomUser

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

        partners_data = CustomUser.objects.all()[:3].values('surname')
        response_data = {
            'Clients': clients_json,
            'Partners': [{'surname': partner['surname']} for partner in partners_data]
        }

        return JsonResponse(response_data, safe=False, json_dumps_params={'indent': 2})

