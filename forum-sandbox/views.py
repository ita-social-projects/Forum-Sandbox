from django.http import JsonResponse
from django.views import View
from profiles.models import Profile, ProfilesImage, SavedCompany
from authentication.models import CustomUser
from django.shortcuts import render



class MainPageView(View):
    def get(self, request, *args, **kwargs):
        latest_saved_companies = SavedCompany.objects.order_by('-added_at')[:6]

        clients_json = []
        for saved_company in latest_saved_companies:
            profile = saved_company.company
            image_data = ProfilesImage.objects.filter(profile_id=profile.id).order_by('-id').first()

            client_json = {
                'common_info': profile.common_info,
                'official_name': profile.official_name,
                'address': profile.address,
                'service_info': profile.service_info,
                'product_info': profile.product_info,
                'image_path': "/media/" + image_data.path if image_data else None,
            }
            clients_json.append(client_json)

        partners_data = ProfilesImage.objects.order_by('id')[:6].values('name', 'path')
        partners_json = [{'name': partner['name'], 'path': "/media/"+partner['path']} for partner in partners_data]

        context = {
            'clients': clients_json,
            'partners': partners_json
        }

        return render(request, 'main_page/index.html', context)


