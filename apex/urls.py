from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from fcm_django.api.rest_framework import FCMDeviceAuthorizedViewSet
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

from accounts.api.views import CustomLoginView, CustomLogoutView, get_refresh_view
from meetings.api_admin.urls import subject_urlpatterns

router = DefaultRouter()
router.register(r"devices", FCMDeviceAuthorizedViewSet)


schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version="v1",
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    re_path(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    re_path(
        r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
    ),
]

api_urls = [
    path("accounts/", include("accounts.api.urls")),
    path("auth/login/", CustomLoginView.as_view(), name="auth_login"),
    path("auth/logout/", CustomLogoutView.as_view(), name="auth_logout"),
    path("auth/token/refresh/", get_refresh_view().as_view(), name="auth_refresh"),
    path("auth/", include("dj_rest_auth.urls")),
    path("courses/", include("courses.api.urls")),
    path("notes/", include("notes.api.urls")),
    path("exams/", include("exams.api.urls")),
    path("enrollments/", include("enrollments.api.urls")),
    path("physical-book/", include("physicalbook.api.urls")),
    path("attendance/", include("attendance.api.urls")),
    path("meetings/", include("meetings.api.urls")),
    path("payments/", include("payments.api.urls")),
    path("infocenter/", include("infocenter.api.urls")),
    path("bannerad/", include("bannerad.api.urls")),
    path("notifications/", include("notifications.api.urls")),
    path("dashboard/", include("dashboard.api.urls")),
    path("discussion/", include("discussion.api.urls")),
]

api_admin_urls = [
    path("exams/", include("exams.api_admin.urls")),
    path("courses/", include("courses.api_admin.urls")),
    path("notes/", include("notes.api_admin.urls")),
    path("enrollments/", include("enrollments.api_admin.urls")),
    path("accounts/", include("accounts.api_admin.urls")),
    path("meetings/", include("meetings.api_admin.urls")),
    path("subjects/", include(subject_urlpatterns)),
    path("infocenter/", include("infocenter.api_admin.urls")),
    path("notifications/", include("notifications.api_admin.urls")),
    path("payments/", include("payments.api_admin.urls")),
    path("report/", include("report.api_admin.urls")),
    path("banner/", include("bannerad.api_admin.urls")),
    path("dashboard/", include("dashboard.api_admin.urls")),
    path("counseling/", include("counseling.api_admin.urls")),
    path("attendance/", include("attendance.api_admin.urls")),
    path("physicalbook/", include("physicalbook.api_admin.urls")),
    path("stafftracking/", include("stafftracking.api_admin.urls")),
    path("discussion/", include("discussion.api_admin.urls")),

]

fcm_urls = [
    path("", include(router.urls)),
]

urlpatterns += [
    path("admin/", admin.site.urls),
    path("api/", include(api_urls)),
    path("api/admin/", include(api_admin_urls)),
    path("api/fcm/", include(fcm_urls)),
    # path("student_urls/", include("student.api.urls")),
    # path("teacher_urls/", include("teacher.api.urls")),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Path for silky django profiler
if settings.DEBUG:
    urlpatterns += [
        path("silk/", include("silk.urls", namespace="silk")),
        path("__debug__/", include("debug_toolbar.urls")),
    ]
