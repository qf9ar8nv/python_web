from django.contrib import admin
from django.urls import path, include
import board.views
import reply.views
import user.views
from django.conf.urls.static import static
from config import settings

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('board/create/', board.views.create),

    path('board/list/', board.views.list),
    path('board/read/<int:bid>', board.views.read),
    path('board/delete/<int:bid>', board.views.delete),
    path('board/update/<int:bid>', board.views.update),

    path('user/signup/', user.views.signup),
    path('user/login/', user.views.user_login),
    path('user/logout/', user.views.user_logout),

    path('reply/create/<int:bid>', reply.views.create),

    path('oauth/redirect/', user.views.getCode)
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
