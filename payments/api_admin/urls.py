from django.urls import path

from payments.api_admin.views import PaymentListAPIView, PaymentReportGeneratorAPIView

app_name = "admin-payments"

urlpatterns = [
    path("list/", PaymentListAPIView.as_view(), name="payment-list"),
    path(
        "report/generate/",
        PaymentReportGeneratorAPIView.as_view(),
        name="generator-payment",
    ),
]
