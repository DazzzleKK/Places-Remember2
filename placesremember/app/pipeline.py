from .models import Profile


def get_info(backend, response, user=None, *args, **kwargs):

    url = None
    name = None

    if backend.name == "vk-oauth2":
        url = response.get("photo", "")
        name = response.get("first_name")

    if url and name:
        Profile.objects.update_or_create(user=user, name=name, avatar=url)
