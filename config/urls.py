from django.contrib import admin
from django.urls import path, include
import board.views
import reply.views
import user.views
from django.conf.urls.static import static
from config import settings
import accounts.views

urlpatterns = [
    path('', user.views.mainPage),
    path('accounts/', include('allauth.urls')),
    path('accounts/profile/', accounts.views.profile),

    path('admin/', admin.site.urls),

    path('board/list/', board.views.list),
    path('board/create/', board.views.create),
    path('board/read/<int:bid>', board.views.read),
    path('board/delete/<int:bid>', board.views.delete),
    path('board/update/<int:bid>', board.views.update),

    path('like/<int:bid>', board.views.like),

    path('user/signup/', user.views.signup),
    path('user/login/', user.views.user_login),
    path('user/logout/', user.views.user_logout),
    path('user/withdrawal', user.views.withdrawal),
    path('user/update', user.views.update),

    path('reply/create/<int:bid>', reply.views.create),
    path('reply/update/<int:bid>/<int:bid2>', reply.views.update),
    path('reply/delete/<int:bid>/<int:bid2>', reply.views.delete),
    path('reply/like/<int:bid>', reply.views.like),

    path('oauth/redirect/', user.views.getCode)

]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
